---
layout: manual
title: "Storage Maintenance — MediaFlowSwift Manual"
description: "Point missing clips at their files again, one at a time or by scanning a folder for matching names."
permalink: /manual/storage-maintenance/
generated: tools/import-guide.sh
---
# Storage Maintenance

## Relinking Missing Media

*Point missing clips at their files again, one at a time or by scanning a folder for matching names.*

When a file is moved or renamed outside MediaFlow, its clip shows as Missing (a red X in the Where column). Relinking tells MediaFlow where the file is now.

### Single Clip Relink

Right-click a missing clip and choose Relink…, then pick the file. Relink… appears only when one clip is selected, and that clip is missing or reads On another Mac or Not on this Mac. Whenever the selection includes a missing clip, the same menu offers Relink Missing Media…, which scans a folder for the selected clips.

A clip that reads On another Mac or Not on this Mac is not missing: its file is in another account’s home folder, or somewhere this Mac has never had it, usually on the Mac that imported it. Relink Missing Media never scans for it. If you have a copy of it on this Mac, you can still point the clip at it with Relink…. The other Mac then sees the clip where you pointed it.

### Batch Auto-Relink

1. Choose Workflow → Repair → Relink Missing Media
2. Select a folder to scan for matching files
3. MediaFlow matches by filename and uses file size to choose between files with the same name
4. A progress dialog shows scanning, matching, and checking status
5. Results report how many clips were relinked, and name any that were found but not relinked

### Organized clips are checked, not just matched

When MediaFlow organizes a clip it records a checksum of the file. Clear Card later relies on that checksum to decide that a card can safely be erased. A file with the right name and size is not necessarily the same file, so when you relink a clip that has a recorded checksum, MediaFlow reads the file you chose (or the one it matched) in full and relinks only if its contents are identical.

- “Not the same file” means the contents differ from what was organized. The clip is left as it was. If you have deliberately replaced the clip with a new version, remove the old clip from the project and import the new file
- “Could not be read” means the file was found but reading it failed, for example because of permissions or a dropped network connection. Nothing is known about its contents; fix the problem and relink again
- Clips that were never organized have no checksum and are relinked by name and size as before

Reading a large file takes time, especially over a network, so relinking organized clips is slower than it used to be.

The progress window has a Cancel button, for a single clip as well as a folder scan. Cancelling stops the work, including part-way through reading a large file; a clip whose check was stopped is not relinked. Clips that were already matched and checked stay relinked and are saved with the project, and the window reports how many were reconnected before you stopped it. Run the command again to pick up the rest.

> **Tip:** Run Workflow → Repair → Re-check files after relinking to update every Where badge.

See also: [Re-check files](/manual/organizing-media/#re-check-files), [Clips Showing as Missing](/manual/troubleshooting/#clips-showing-as-missing)

## Storage Forecast

*Project when the destination drive will fill up from your recent import rate.*

The Storage Forecast tells you when the destination drive will fill up, so you can make room before a shoot. Choose Workflow → Plan & Deliver → Storage Forecast…. MediaFlow looks at the volume that holds the project destination and at how much you imported over the last seven days, then projects the day the drive will be full.

### What It Shows

- Used, Available, and Total capacity with a usage ring
- Import Rate — Bytes per day and clips per day over the last seven days
- Projection — Days until full and the projected date (or “No growth detected” if nothing was imported recently)
- Level — Safe (7 days or more), Caution (under 7 days), Warning (under 3 days), Critical (under 1 day)

### What-If Calculator

Drag the Additional shoot days (1–30) and GB per day (5–200) sliders to see how many days of headroom remain after the next shoot; the result turns red at three days or fewer, or reads “Over capacity!”.

If no destination is set, or its volume is not mounted, the sheet reports “No destination volume detected”. The Storage Warning smart notification opens this sheet when the destination passes 85% full. For storage history across all projects, use Database → Storage Dashboard.

See also: [Storage Dashboard](/manual/shared-database/#storage-dashboard), [Smart Notifications](/manual/settings-preferences/#smart-notifications), [Organizing Media to Storage](/manual/organizing-media/#organizing-media-to-storage)

<div class="chapter-nav" role="navigation" aria-label="Chapters">
<a rel="prev" href="/manual/shared-database/">&larr; Shared Database</a>
<a href="/manual/">All chapters</a>
<a rel="next" href="/manual/reports/">Reports &rarr;</a>
</div>
