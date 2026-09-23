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
- `manual/index.md` — the online manual, GENERATED: run `tools/import-guide.sh` after each release (it copies the app's `docs/guides/user-guide.md`); GitHub Pages renders it through `_layouts/manual.html`
- `CNAME` — the custom domain

Static files plus one Jekyll-rendered page (the manual); GitHub Pages builds it. Edit, commit to `main`, and Pages publishes within a minute.

The privacy page must say the same as Settings › Privacy in the app (`Sources/Services/PrivacySettings.swift` in the app repository). When that file changes, change this page.

## Paddle (plans and checkout)

Paddle.js is loaded from Paddle's CDN on the home page only. The site runs against **live** unless the URL carries `?sandbox=1`, which switches token, price ids and licence-service URL to the sandbox block in `paddle-config.js` and carries through to `thanks.html`. An environment with blank ids shows a notice instead of prices; nothing falls back silently.

To test: `python3 -m http.server 8765` in this folder, open `http://localhost:8765/?sandbox=1#plans`, and pay with Paddle's test card 4242 4242 4242 4242 (any future expiry, any CVC). Sandbox approves localhost automatically; the live account needs mediaflowswift.com approved under Checkout › Website approval and a default payment link set under Checkout › Checkout settings.
