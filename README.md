# mediaflowswift.com

The public website for MediaFlowSwift, served by GitHub Pages from the `main` branch.

- `index.html` — overview, how it works, plans
- `support.html`, `privacy.html`, `terms.html`
- `site.css` — the one stylesheet (light and dark)
- `manual/index.md` — the online manual, GENERATED: run `tools/import-guide.sh` after each release (it copies the app's `docs/guides/user-guide.md`); GitHub Pages renders it through `_layouts/manual.html`
- `CNAME` — the custom domain

Static files plus one Jekyll-rendered page (the manual); GitHub Pages builds it. Edit, commit to `main`, and Pages publishes within a minute.

The privacy page must say the same as Settings › Privacy in the app (`Sources/Services/PrivacySettings.swift` in the app repository). When that file changes, change this page.
