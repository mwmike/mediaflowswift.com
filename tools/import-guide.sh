#!/bin/sh
# Copy the app's generated user guide into the site as the online manual.
#
#   tools/import-guide.sh [path/to/user-guide.md]
#
# The guide is generated from the app's Help (MEDIAFLOW_WRITE_USER_GUIDE=1
# swift test --filter UserGuideMarkdownTests in the app repository), so the
# manual always says what the app says. Run this after each release, then
# commit; GitHub Pages renders manual/index.md through _layouts/manual.html.
#
# Angle brackets in the guide are placeholders (<name>, <drive-1>), not HTML,
# so they are escaped; the guide contains no real HTML.
set -e
SRC="${1:-../VideoProductionManager/docs/guides/user-guide.md}"
DIR="$(cd "$(dirname "$0")/.." && pwd)"
[ -f "$SRC" ] || { echo "user guide not found at $SRC" >&2; exit 1; }
mkdir -p "$DIR/manual"
{
  printf -- '---\nlayout: manual\ntitle: Manual\ndescription: The MediaFlowSwift user guide, generated from the Help inside the app.\n---\n'
  sed -e 's/</\&lt;/g' -e 's/^# MediaFlow User Guide$/# MediaFlowSwift Manual/' "$SRC"
} > "$DIR/manual/index.md"
echo "manual/index.md written from $SRC ($(wc -l < "$SRC" | tr -d ' ') lines)"
