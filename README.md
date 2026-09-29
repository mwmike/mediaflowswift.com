# mediaflowswift.com

The public website for MediaFlowSwift, served by GitHub Pages from the `main` branch.

- `index.html` — overview, how it works, plans
- `support.html`, `privacy.html`, `terms.html`
- `site.css` — the one stylesheet (light and dark)
- `paddle-config.js` — the plans, price ids and client-side tokens for sandbox and live; edit prices here and nowhere else
- `pricing.js` — the Plans section: local prices from Paddle, monthly/yearly toggle, Buy buttons opening Paddle's overlay checkout
- `thanks.html` — where Paddle sends a buyer; shows the licence key from the licence service
- `key.html` — Lost your key: the key again from the transaction number on a Paddle receipt
- `download.html` — the current version from `downloads/latest.json`, requirements, installing
- `downloads/` — `latest.json`, `CHANGELOG.md` and the newest zip, written by `tools/publish-release.sh` with each release
- `manual/` — the online manual, GENERATED from the app's `docs/guides/user-guide.md`: run `tools/import-guide.sh <release worktree>/docs/guides/user-guide.md` after each release, then commit `manual/` and `sitemap.xml` together. Each chapter of the guide becomes `manual/<chapter>/index.md` (served at `/manual/<chapter>/`, with its own title, description and previous/next links); `manual/index.md` is the contents page at `/manual/`, and its small script sends an old one-page link such as `/manual/#clear-card` to the chapter that heading is on now. The tool (`tools/import-guide.py`) checks every link in the guide before writing anything, rewrites the manual's block of `sitemap.xml` (a page keeps its `<lastmod>` unless it changed), removes the page of a chapter the guide no longer has, and then runs `tools/check-links.py`. GitHub Pages renders the pages through `_layouts/manual.html`. Never edit these files by hand
- `CNAME` — the custom domain
- `404.html` — what GitHub Pages shows for an address that does not exist; absolute links, since it is served at any depth
- `robots.txt`, `sitemap.xml` — for search engines. The sitemap is written by hand, except the manual's block between its two marker comments, which `tools/import-guide.sh` writes: add a page there when you add one to the site, and move its `<lastmod>` when its content changes. Pages that are `noindex` (`key.html`, `thanks.html`, `404.html`) stay out of it
- `tools/check-links.py` — checks that every link on the site leads to a page, file or heading, that each manual page has one H1, and that the sitemap lists every manual page and nothing marked `noindex`. Run `python3 tools/check-links.py` before committing a change to the pages
- `llms.txt` — a plain-text summary of the product for AI assistants; it states only what the pages already say, so change it when they change
- `images/og-image.png` — the picture shown when a page is shared, drawn by `swift tools/make_og_image.swift images/og-image.png`

Every page carries a canonical link, Open Graph and Twitter card tags (the two layouts build theirs from `site.url` and `page.url`), and the home page has JSON-LD for the app and the company. A new page needs the same `<head>` block.

Static files plus the Jekyll-rendered Markdown pages (the manual and the terms); GitHub Pages builds them. Edit, commit to `main`, and Pages publishes within a minute.

The privacy page must say the same as Settings › Privacy in the app (`Sources/Services/PrivacySettings.swift` in the app repository). When that file changes, change this page.

## Paddle (plans and checkout)

Paddle.js is loaded from Paddle's CDN on the home page only. The site runs against **live** unless the URL carries `?sandbox=1`, which switches token, price ids and licence-service URL to the sandbox block in `paddle-config.js` and carries through to `thanks.html`. An environment with blank ids shows a notice instead of prices; nothing falls back silently.

To test: `python3 -m http.server 8765` in this folder, open `http://localhost:8765/?sandbox=1#plans`, and pay with Paddle's test card 4242 4242 4242 4242 (any future expiry, any CVC). Sandbox approves localhost automatically; the live account needs mediaflowswift.com approved under Checkout › Website approval and a default payment link set under Checkout › Checkout settings.
