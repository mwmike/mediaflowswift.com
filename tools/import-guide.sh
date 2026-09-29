#!/bin/sh
# Copy the app's generated user guide into the site as the online manual.
#
#   tools/import-guide.sh [path/to/user-guide.md]
#
# The guide is generated from the app's Help (MEDIAFLOW_WRITE_USER_GUIDE=1
# swift test --filter UserGuideMarkdownTests in the app repository), so the
# manual always says what the app says. Run this after each release, then
# commit manual/ and sitemap.xml together.
#
# tools/import-guide.py does the work: one page per chapter at
# manual/<chapter>/index.md, the contents page at manual/index.md (which also
# sends old /manual/#heading links to their chapter), and the manual's entries
# in sitemap.xml. It checks everything first and writes nothing if a link in
# the guide leads nowhere. GitHub Pages renders the pages through
# _layouts/manual.html. Afterwards tools/check-links.py checks every link on
# the site.
#
# Angle brackets in the guide are placeholders (<name>, <drive-1>), not HTML,
# so they are escaped; the guide contains no real HTML.
set -e
SRC="${1:-../VideoProductionManager/docs/guides/user-guide.md}"
DIR="$(cd "$(dirname "$0")/.." && pwd)"
[ -f "$SRC" ] || { echo "user guide not found at $SRC" >&2; exit 1; }
python3 "$DIR/tools/import-guide.py" "$SRC" "$DIR"
python3 "$DIR/tools/check-links.py" "$DIR"
