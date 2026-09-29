---
layout: manual
title: "Reports — MediaFlowSwift Manual"
description: "Write a summary of the open project as a PDF, web page or spreadsheet, or as a hand-off file for an editor."
permalink: /manual/reports/
generated: tools/import-guide.sh
---
# Reports

## Generating Reports

*Write a summary of the open project as a PDF, web page or spreadsheet, or as a hand-off file for an editor.*

A report lists what is in the open project: totals, a breakdown, and a line for every clip. The project must contain at least one clip.

1. Choose Workflow → Plan & Deliver → Report
2. In the Export / Generate Report dialog, choose a format and click Generate
3. Choose the folder to save into

You do not type a filename. MediaFlow names the file after the project file, as name_report plus the format’s extension. If a file with that name is already there, it adds the date and time to the name rather than replace it.

### Formats

- PDF — A document for printing or sharing
- HTML — A web page that opens in any browser
- CSV — Rows and columns for a spreadsheet
- FCPXML (Final Cut Pro) — A file Final Cut Pro can import
- EDL CSV (Resolve / Premiere) — A spreadsheet-style clip list that includes rating and select status

### What the PDF and HTML Reports Contain

- Project summary: total files, total duration and total size
- Categories: how many clips are in each
- Devices: how many clips came from each camera (the report prints the heading “Devices”)
- A line for each clip with its filename, technical details, camera and notes
- A thumbnail for each clip

> **Tip:** For more control over what an editor receives, use NLE Template Export instead of the two hand-off formats here.

See also: [NLE Template Export](#nle-template-export), [Dailies Report](#dailies-report), [Day Summary](#day-summary)

## NLE Template Export

*Hand your categories, scenes, ratings and notes to Final Cut Pro, Premiere Pro or DaVinci Resolve as an import file.*

The NLE Template Export creates a structured project file that you can import into your editing application. It transfers your MediaFlow organization — categories, cameras, scenes, tags, ratings, and notes — so your clips arrive pre-organized and annotated in your NLE.

### How to Export

1. Open a project with imported media
2. Choose Workflow → Plan & Deliver → NLE Template Export
3. Select your target NLE: Final Cut Pro, DaVinci Resolve, or CSV
4. Set the organization, clip filter and metadata options
5. Click Preview to see the file MediaFlow would write, if you like
6. Click Export… and choose where to save

### Final Cut Pro (FCPXML)

The FCP export generates an FCPXML v1.11 file that maps your MediaFlow metadata to FCP’s organizational structure:

- Library — Named after your MediaFlow project (editable). This becomes the top-level .fcpbundle container in FCP.
- Events — Choose which MediaFlow field becomes FCP Events: Category (for example A-roll, B-roll, Interview), Scene, Camera, Camera angle, Shooting Day, Tags, or Location.
- Keyword Collections — Choose a secondary field for sub-grouping within each Event: for example Camera within Category events, so your A-roll event has keyword collections for iPhone, Drone, GoPro, etc. Location can be used at either level.
- Empty Timeline — Optionally creates an “Edits” event with an empty FCP Project ready for editing.

Metadata mapping: notes become FCP comments, camera names become Reel metadata, star ratings become keywords, clips rated 4 or 5 stars or marked Hero become FCP favorites, the select status (Hero, Maybe or Reject) is added as a keyword, scene/shot/take data become markers at clip start, tags become keywords, and GPS coordinates are embedded as FCP scene/shot metadata with the reverse-geocoded location name as a keyword.

Rejected clips are not marked as rejected in Final Cut Pro. They arrive with the keyword for their select status, so you can filter on it there.

### Location-Based Organization

When your clips have GPS coordinates (common with phone and drone footage), MediaFlow reverse-geocodes them into readable place names. You can use Location as an Event or Keyword Collection field to automatically group clips by where they were shot — for example, an event per shooting location like “Malibu Beach” or “Downtown LA”. Clips without GPS data are grouped under “Unknown Location.”

> **Tip:** Combine Location events with Camera keyword collections to see exactly which cameras shot at each location, or use Category events with Location keywords to see where your A-roll vs B-roll was captured.

> **Tip:** A live preview at the bottom of the FCP section shows exactly how your Library → Events → Keywords tree will appear in FCP’s browser, using real data from your project.

### Adobe Premiere Pro

Premiere Pro can import FCPXML files natively via File → Import. Select the Final Cut Pro target in MediaFlow, configure your organization, and export the .fcpxml file. Then in Premiere Pro, use File → Import and select the .fcpxml file. Premiere will create bins from Events and preserve keywords, markers, and clip metadata.

> **Tip:** Premiere Pro’s FCPXML import handles Events, keywords, and markers well. This is the recommended workflow for Premiere users — there is no need for a separate Premiere-specific format.

### DaVinci Resolve (EDL)

The Resolve export generates an Edit Decision List with bin comments, clip names, timecodes, scene/shot metadata, notes, and ratings. Import the .edl file via File → Import → Timeline in DaVinci Resolve.

### Bins for Resolve and CSV

For the DaVinci Resolve and CSV targets, the Organization picker decides how clips are grouped: By Category, By Scene, By Camera, By Shooting Day, By Place, or Flat (No Bins).

### CSV (Universal)

The CSV export creates a spreadsheet-compatible file with all clip metadata organized into columns. Use this as a reference alongside manual import, or for custom workflows with other tools.

### Clip Filtering

- All Clips — Export every clip in the project
- Rated Only — Export only clips that have been rated
- Favorites Only — Export only clips with the Favorite mark. Hero alone does not count
- Selected Only — Export only the currently selected clips in the media list

### Metadata Options

Choose what travels with each clip: Notes, Scene/Shot, Ratings, Audio Flags and Tags. Turn off anything you do not want in your NLE.

Workflow → Plan & Deliver → Export FCPXML… is a separate, simpler command. It writes only your scene, shot and take data as Final Cut Pro markers.

See also: [Generating Reports](#generating-reports), [Format Conformance Checker](/manual/organizing-media/#format-conformance-checker)

## Dailies Report

*Generate a structured dailies report organized by shooting day, scene, and camera.*

The Dailies Generator creates a report of your footage organized by shooting date, with optional grouping by scene and camera. It highlights circle takes and includes ratings, timecodes, and notes. Output is available in HTML, CSV, or plain text format.

### How to Use

1. Open a project with media clips
2. Choose Workflow → Plan & Deliver → Generate Dailies
3. Configure grouping options and content to include
4. Select the output format (HTML, CSV, or Plain Text)
5. Click Generate Dailies and choose a save location

### Configuration Options

- Group by Scene — Organize clips under their assigned scene names
- Group by Camera — Sub-group clips by camera label or source device
- Circle Takes — Highlight the best takes at the top of each day
- Ratings — Show star ratings for each clip
- Timecodes — Include the time of day each clip was recorded
- Notes — Include any notes attached to clips

### Output Formats

- HTML — Dark-themed web page with styled tables, ideal for sharing with a director or editor
- CSV — Spreadsheet-compatible format for data analysis
- Plain Text — Simple text report suitable for email or printing

> **Tip:** For the most useful dailies report, make sure clips have scene assignments, camera labels, and ratings before generating.

See also: [Smart Selects](/manual/organizing-media/#smart-selects), [NLE Template Export](#nle-template-export)

## Day Summary

*A one-screen wrap-up of everything imported on a shooting day, ready to paste into a message.*

The Day Summary is a wrap-up you can send at the end of a shooting day. Choose Workflow → Plan & Deliver → Day Summary… and pick a date in the header. It covers every clip imported on that date, by import date rather than capture date.

### What It Shows

- Clips, total Duration, and total Size
- Cameras — Clip count per camera
- Categories — Clip count per category
- Highlights — How many clips are favorited and how many are marked Hero
- Issues — Clips flagged Clipping, Low or Silent by the Audio pass, and clips whose files are Missing

Click the Copy button to place a plain-text summary on the clipboard for a text message, e-mail, or production log. For a printable per-scene breakdown use Generate Dailies instead.

See also: [Dailies Report](#dailies-report), [Audio Levels](/manual/organizing-media/#audio-levels), [Generating Reports](#generating-reports)

<div class="chapter-nav" role="navigation" aria-label="Chapters">
<a rel="prev" href="/manual/storage-maintenance/">&larr; Storage Maintenance</a>
<a href="/manual/">All chapters</a>
<a rel="next" href="/manual/publishing/">Publishing &rarr;</a>
</div>
