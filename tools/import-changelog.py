#!/usr/bin/env python3
"""Turn the app's change log into the What's New page, /changes/ (changes/index.html).

    python3 tools/import-changelog.py <CHANGELOG.md> <site folder> [--newest <version>]

tools/publish-release.sh runs it at every release, from the same CHANGELOG.md it copies to downloads/, before it
publishes anything; --newest makes sure the version being released is the newest in the log. The change log
itself is only read, never changed: the app's update window reads downloads/CHANGELOG.md.

The page lists the versions exactly as the app reads them (ReleaseNotes.sections in the app repository):
"## <version> · <date>", a line that is entirely bold as the headline, then "- **Title.** text" bullets.
"Coming next" is not a version and is left out. On top of that the log must be well formed, or nothing is
written: every version heading in that form with a real date, no version twice, newest first, a headline before
the bullets, at least one bullet, and no other line inside a version (the app would skip it silently).

Each version is a <details> row with the id v<version with dots as hyphens>, e.g. /changes/#v1-10-33. Those ids
are a public, stable format: the app may link to them.
"""
import datetime
import html
import os
import re
import sys
import unicodedata

SITE = "https://mediaflowswift.com"
PAGE = "changes/index.html"
TEMPLATE = "tools/changes-template.html"
SITEMAP_LINE = re.compile(r"^  <url><loc>https://mediaflowswift\.com/changes/</loc><lastmod>[0-9-]+</lastmod></url>$", re.M)
MANUAL_BLOCK = ("<!-- manual: written by tools/import-guide.sh, do not edit by hand -->", "<!-- end of manual -->")
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]

# Two versions written before the change log had its present form. The app's update window shows only the
# headline and the bullets, so it shows neither of these; the page shows them as the change log always has.
# Every other version must be in the form the app reads.
LEGACY_PARAGRAPH = {"1.5.1"}  # no headline or bullets, one "**Lead.** text" paragraph: lead as headline, text below
LEGACY_NOTE = {"1.10.1"}      # an italic "*...*" paragraph after the bullets, shown under them


def fail(problems):
    for p in problems:
        print("import-changelog: " + p, file=sys.stderr)
    print("import-changelog: nothing was written.", file=sys.stderr)
    sys.exit(1)


def trim(s):
    """Swift's trimmingCharacters(in: .whitespaces): tabs and Unicode space separators, not line breaks."""
    def space(c):
        return c == "\t" or unicodedata.category(c) == "Zs"
    i, j = 0, len(s)
    while i < j and space(s[i]):
        i += 1
    while j > i and space(s[j - 1]):
        j -= 1
    return s[i:j]


def read(log):
    """ReleaseNotes.sections, line for line, plus a note of every line inside a version that it skips."""
    sections, current, skipped, headings = [], None, [], []
    for number, raw in enumerate(log.split("\n"), 1):
        line = trim(raw)
        if line.startswith("## "):
            if current:
                sections.append(current)
            current = None
            title = trim(line[3:])
            parts = title.split(" · ")
            first = parts[0]
            headings.append((number, title, bool(first) and first[0].isnumeric()))
            if not first or not first[0].isnumeric():
                continue  # "Coming next" and the like
            current = {"version": first, "date": " · ".join(parts[1:]), "headline": "", "items": [],
                       "line": number, "parts": len(parts), "headline_after_items": False, "extra": []}
        elif current is not None and line.startswith("**") and line.endswith("**") and len(line) > 4 and not current["headline"]:
            current["headline"] = line[2:-2]
            current["headline_after_items"] = bool(current["items"])
        elif current is not None and line.startswith("- **") and line.find("**", 4) != -1:
            end = line.find("**", 4)
            current["items"].append((line[4:end], trim(line[end + 2:]), number))
        elif current is not None and line:
            current["extra"].append((number, line))
    if current:
        sections.append(current)
    return sections, headings


def components(version):
    return [int(p) if p.isdigit() else 0 for p in version.split(".")]


def check(sections, headings):
    problems, seen, dates = [], set(), {}
    first_version_line = min((s["line"] for s in sections), default=None)
    for number, title, is_version in headings:
        if not is_version and not (title == "Coming next" and (first_version_line is None or number < first_version_line)):
            problems.append(f"line {number}: '## {title}' is neither a version (## <version> · <Month D, YYYY>) "
                            "nor 'Coming next' above the versions")
    for s in sections:
        v, at = s["version"], f"line {s['line']} ({s['version']})"
        if not re.fullmatch(r"[0-9]+(\.[0-9]+){0,3}", v):
            problems.append(f"{at}: the version is not digits and dots")
        if s["parts"] != 2:
            problems.append(f"{at}: the heading needs exactly one ' · ' between the version and the date")
        m = re.fullmatch(r"([A-Z][a-z]+) ([0-9]{1,2}), ([0-9]{4})", s["date"])
        try:
            dates[v] = datetime.date(int(m.group(3)), MONTHS.index(m.group(1)) + 1, int(m.group(2)))
        except (AttributeError, ValueError):
            problems.append(f"{at}: '{s['date']}' is not a date like September 29, 2026")
        if v in seen:
            problems.append(f"{at}: {v} is in the log twice")
        seen.add(v)
        legacy_paragraph = (v in LEGACY_PARAGRAPH and not s["headline"] and not s["items"] and len(s["extra"]) == 1
                            and re.fullmatch(r"\*\*[^*]+\*\* \S.*", s["extra"][0][1]))
        if legacy_paragraph:
            continue
        if not s["headline"]:
            problems.append(f"{at}: no headline (a line that is entirely bold, before the bullets)")
        if s["headline_after_items"]:
            problems.append(f"{at}: the headline comes after the bullets")
        if not s["items"]:
            problems.append(f"{at}: no bullets (- **Title.** text)")
        for title, text, number in s["items"]:
            if not title.strip() or not text:
                problems.append(f"line {number}: a bullet needs a bold title and text after it")
        for number, line in s["extra"]:
            after_items = bool(s["items"]) and number > s["items"][-1][2]
            if v in LEGACY_NOTE and after_items and re.fullmatch(r"\*[^*].*[^*]\*", line):
                continue
            problems.append(f"line {number}: the app's update window would skip this line: {line[:70]}")
    ordered = [s["version"] for s in sections]
    for a, b in zip(ordered, ordered[1:]):
        if components(a) <= components(b):
            problems.append(f"{a} is listed above {b}; newest must come first")
        elif a in dates and b in dates and dates[a] < dates[b]:
            problems.append(f"{a} is dated before {b}, which it is listed above")
    if not sections:
        problems.append("the log has no versions")
    return problems, dates


# --- Inline Markdown: bold, italics, code and links; everything else is escaped ---------------------------------
INLINE = re.compile(
    r"`(?P<code>[^`]+)`"
    r"|\[(?P<label>[^\]]+)\]\((?P<href>[^)\s]+)\)"
    r"|\*\*(?P<bold>.+?)\*\*"
    r"|(?<![\w*])\*(?P<em>[^\s*](?:.*?[^\s*])?)\*(?![\w*])"
    r"|(?<![\w_])_(?P<em2>[^\s_](?:.*?[^\s_])?)_(?![\w_])"
)


def inline(text):
    out, at = [], 0
    for m in INLINE.finditer(text):
        out.append(html.escape(text[at:m.start()], quote=False))
        if m.group("code") is not None:
            out.append(f"<code>{html.escape(m.group('code'), quote=False)}</code>")
        elif m.group("label") is not None:
            href = m.group("href")
            if re.match(r"^(https?://|mailto:|/|#)", href):
                out.append(f'<a href="{html.escape(href, quote=True)}">{inline(m.group("label"))}</a>')
            else:
                out.append(html.escape(m.group(0), quote=False))
        elif m.group("bold") is not None:
            out.append(f"<strong>{inline(m.group('bold'))}</strong>")
        else:
            out.append(f"<em>{inline(m.group('em') or m.group('em2'))}</em>")
        at = m.end()
    out.append(html.escape(text[at:], quote=False))
    return "".join(out)


def anchor(version):
    return "v" + version.replace(".", "-")


def row(s, date, newest):
    v = s["version"]
    if not s["headline"]:  # the legacy one-paragraph form
        lead, text = re.fullmatch(r"\*\*([^*]+)\*\* (\S.*)", s["extra"][0][1]).groups()
        headline, body, count = inline(lead), f'        <p class="release-text">{inline(text)}</p>\n', ""
    else:
        headline = inline(s["headline"])
        items = "".join(f"          <li><strong>{inline(t)}</strong> {inline(x)}</li>\n" for t, x, _ in s["items"])
        body = f'        <ul class="release-changes">\n{items}        </ul>\n'
        body += "".join(f'        <p class="release-note">{inline(line)}</p>\n' for _, line in s["extra"])
        n = len(s["items"])
        count = f'<span class="release-count">{n} change{"" if n == 1 else "s"}</span>'
    return (
        f'    <details class="release" id="{anchor(v)}"{" open" if newest else ""}>\n'
        # Spaces between the parts: the grid does not show them, but text read without the stylesheet (a
        # crawler, a screen reader's name for the row) would otherwise run "1.10.33September 29, 2026…" together.
        f'      <summary><span class="release-row">'
        f'<span class="release-version">{html.escape(v)}</span> '
        f'<time class="release-date" datetime="{date.isoformat()}">{html.escape(s["date"])}</time> '
        f'<span class="release-headline">{headline}</span> '
        f'{count + " " if count else ""}'
        f'<span class="release-icon" aria-hidden="true"></span>'
        f'</span></summary>\n'
        f'      <div class="release-body">\n{body}      </div>\n'
        f'    </details>\n'
    )


def lede(log):
    """The change log's own introduction: its first plain paragraph above the versions."""
    for block in log.split("\n## ", 1)[0].split("\n\n"):
        block = " ".join(trim(line) for line in block.strip().split("\n"))
        if block and not block.startswith(("#", "*", "-", ">")):
            return f'<p class="lead">{inline(block)}</p>'
    return ""


def main():
    args = sys.argv[1:]
    newest = None
    if "--newest" in args:
        i = args.index("--newest")
        newest = args[i + 1] if i + 1 < len(args) else ""
        del args[i:i + 2]
    if len(args) != 2:
        fail(["usage: import-changelog.py <CHANGELOG.md> <site folder> [--newest <version>]"])
    source, root = args[0], os.path.realpath(args[1])
    template_path, sitemap_path = os.path.join(root, TEMPLATE), os.path.join(root, "sitemap.xml")
    if not os.path.isfile(template_path):
        fail([f"{root} is not the site folder (no {TEMPLATE})"])
    with open(source, encoding="utf-8") as f:
        log = f.read()

    sections, headings = read(log)
    problems, dates = check(sections, headings)
    if newest is not None and sections and sections[0]["version"] != newest:
        problems.append(f"the newest version in the log is {sections[0]['version']}, not {newest}")
    if problems:
        fail(problems)

    template = open(template_path, encoding="utf-8").read()
    for marker in ("%%LEDE%%", "%%RELEASES%%"):
        if template.count(marker) != 1:
            fail([f"{TEMPLATE} needs {marker} exactly once"])
    releases = "".join(row(s, dates[s["version"]], i == 0) for i, s in enumerate(sections))
    page = template.replace("%%LEDE%%", lede(log)).replace("%%RELEASES%%", releases.rstrip("\n"))
    if "%%" in page:
        fail(["a %%placeholder%% is left in the page"])

    # The page's sitemap line, dated by the newest version. It sits outside the manual's block, which is left alone.
    sitemap = open(sitemap_path, encoding="utf-8").read()
    lines = SITEMAP_LINE.findall(sitemap)
    if len(lines) != 1:
        fail([f"sitemap.xml needs exactly one line for {SITE}/changes/ (found {len(lines)})"])
    start, end = sitemap.find(MANUAL_BLOCK[0]), sitemap.find(MANUAL_BLOCK[1])
    at = SITEMAP_LINE.search(sitemap).start()
    if start != -1 and start < at < end:
        fail(["the /changes/ line in sitemap.xml is inside the manual's block"])
    lastmod = dates[sections[0]["version"]].isoformat()
    sitemap = SITEMAP_LINE.sub(f"  <url><loc>{SITE}/changes/</loc><lastmod>{lastmod}</lastmod></url>", sitemap)

    os.makedirs(os.path.join(root, os.path.dirname(PAGE)), exist_ok=True)
    with open(os.path.join(root, PAGE), "w", encoding="utf-8") as f:
        f.write(page)
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap)
    total = sum(len(s["items"]) for s in sections)
    print(f"{PAGE} written from {source}: {len(sections)} versions, {total} changes, newest {sections[0]['version']}")


if __name__ == "__main__":
    main()
