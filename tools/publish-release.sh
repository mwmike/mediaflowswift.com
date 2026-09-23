#!/bin/bash
# Publish a MediaFlowSwift release for the app's web updater (VideoProductionManager #560).
#
#   tools/publish-release.sh <notarized-and-stapled MediaFlowswift.app> <CHANGELOG.md>
#
# Zips the app the way the updater expects (ditto, parent kept), makes a GitHub Release
# v<version> on this repo with the zip attached, writes downloads/latest.json and
# downloads/CHANGELOG.md, commits and pushes. Run it AFTER stapling: the zip must carry the ticket.
# One step per command; nothing is chained past a failure.
set -u
APP="${1:?the stapled .app}"
LOG="${2:?CHANGELOG.md}"
SITE="$(cd "$(dirname "$0")/.." && pwd)"
REPO="mwmike/mediaflowswift.com"

PLIST="$APP/Contents/Info.plist"
VERSION=$(/usr/libexec/PlistBuddy -c "Print :CFBundleShortVersionString" "$PLIST") || { echo "no version in $PLIST"; exit 1; }
BUILD=$(/usr/libexec/PlistBuddy -c "Print :CFBundleVersion" "$PLIST") || { echo "no build in $PLIST"; exit 1; }
xcrun stapler validate "$APP" >/dev/null 2>&1 || { echo "$APP is not stapled; staple before publishing"; exit 1; }

WORK=$(mktemp -d)
ZIP="$WORK/MediaFlowswift-$VERSION.zip"
ditto -c -k --keepParent "$APP" "$ZIP" || { echo "zip failed"; exit 1; }
SIZE=$(stat -f %z "$ZIP")
SHA=$(shasum -a 256 "$ZIP" | awk '{print $1}')
TAG="v$VERSION"
URL="https://github.com/$REPO/releases/download/$TAG/MediaFlowswift-$VERSION.zip"

if gh release view "$TAG" --repo "$REPO" >/dev/null 2>&1; then
  echo "release $TAG already exists; not overwriting"; exit 1
fi
gh release create "$TAG" "$ZIP" --repo "$REPO" --title "MediaFlowSwift $VERSION" --notes "Build $BUILD. Notarized. What is new is in the change log at https://mediaflowswift.com/downloads/CHANGELOG.md" || { echo "release failed"; exit 1; }

mkdir -p "$SITE/downloads"
cat > "$SITE/downloads/latest.json" <<EOF
{"version":"$VERSION","build":$BUILD,"url":"$URL","size":$SIZE,"sha256":"$SHA","notesURL":"https://mediaflowswift.com/downloads/CHANGELOG.md","published":"$(date -u +%Y-%m-%d)"}
EOF
cp "$LOG" "$SITE/downloads/CHANGELOG.md" || { echo "change log copy failed"; exit 1; }
python3 - "$SITE/downloads/latest.json" <<'PY' || exit 1
import json, sys
m = json.load(open(sys.argv[1]))
assert m["build"] > 0 and len(m["sha256"]) == 64 and m["url"].startswith("https://"), m
print("manifest ok:", m["version"], m["build"], m["size"], "bytes")
PY
cd "$SITE" || exit 1
git add downloads/latest.json downloads/CHANGELOG.md || exit 1
git commit -q -m "release: MediaFlowSwift $VERSION (build $BUILD)" || { echo "nothing to commit"; exit 1; }
git push -q || { echo "push failed"; exit 1; }
echo "published $VERSION ($BUILD): $URL"
rm -rf "$WORK"
