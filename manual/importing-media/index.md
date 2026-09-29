---
layout: manual
title: "Importing Media — MediaFlowSwift Manual"
description: "Pick a card, drive or folder, choose the files and the camera that shot them, and copy them into your project."
permalink: /manual/importing-media/
generated: tools/import-guide.sh
---
# Importing Media

## Importing from a Card, Drive or Folder

*Pick a card, drive or folder, choose the files and the camera that shot them, and copy them into your project.*

An import copies media from a card, a drive or a folder into your project’s working folder on this Mac and adds the clips to the project. The original files are not changed.

1. Choose File → Import…
2. Pick a source at the top of the sheet: Cards & drives lists the SD cards and USB drives MediaFlow has detected; Folder lets you browse to any directory
3. For a card, choose it from the Choose Card… menu (a single connected card is picked for you; Rescan looks again). For a folder, click Choose Folder…
4. MediaFlow scans the source, including subfolders, for supported video, image and audio files
5. Review the file list and check or uncheck the items to include
6. Set the Camera picker to the camera that shot the footage; click New camera… to add one that is not listed
7. Optionally tick “Ask a model to suggest categories” — see below
8. Click Import Selected

Once the copy starts, the bottom of the sheet shows “Importing to:” with the folder the files are going to.

### Previewing a File

Click a file in the list to see it in the Preview on the right, with details such as its size, length and date. Press Space to play or pause a video there, whatever you clicked last in the sheet. While a video is showing, Space never ticks a checkbox or presses a button. A photo shows as a still picture; with a photo or nothing showing, Space does what it does elsewhere on your Mac (with Keyboard navigation on, it presses the button you moved to with Tab).

### Duplicates

Files that are already in the project are marked Duplicate in the list. A line at the bottom of the sheet says how many duplicates were detected, and they are skipped when you import.

### Disk Space

The working folder’s disk needs room for the selected files plus 10 GB of headroom. If it has less, the import does not start and MediaFlow tells you there is not enough free space.

### Cancelling

To close the sheet without importing anything, click Cancel at the top or press Esc.

To stop a long import, click Cancel on the progress window. The copy stops between files, the partly written file is discarded, and every file already copied is added to the project and kept in the working folder.

### New camera…

The Camera picker lists the project’s cameras (Camera A, Drone, Phone, …). New camera… adds a name to that list, saves it with the project, and selects it for this import. Typing a name that already exists selects the existing entry rather than adding a duplicate.

### Sorting the List

Click a column header to sort the list by Filename, Date, Type, Length or Size; click it again to reverse. Filename keeps a GoPro recording’s chapters together, as the clip table does. The choice is remembered for the next import, whichever source you use. Until a video’s length has been read, it sorts as the shortest.

### Ask a Model to Suggest Categories

This checkbox asks an AI model to look at each imported video clip and propose one of your project’s categories. It is off every time the sheet opens and applies to this import only, so no import uses a model unless you tick the box for it. The model runs in the background after the copy finishes. Its answers arrive as proposals: nothing is applied to a clip until you confirm it.

- With a model that runs on this Mac, nothing leaves the Mac and it costs nothing. It is slow — about a minute a clip
- With a paid provider (Claude, ChatGPT or Gemini), MediaFlow sends three small frames from each clip to that provider, together with your category list, the clip’s camera, duration and place name, the opening words of its transcript when it has one, and your recent category corrections. The provider bills you for each clip
- The line under the checkbox names the model and, for a paid one, says “costs money”

The checkbox appears only after you turn on “Use a model to suggest categories” and finish setting up a model in Settings › Analysis. It is dimmed when “Propose category, camera and scene after an import” is off in the same tab, because the model refines that proposal.

> **Warning:** A paid provider charges for every clip it looks at, and frames from your footage leave this Mac. Set “Stop after … a day” in Settings › Analysis to cap the spend; MediaFlow checks the limit before each clip and stops when it is reached.

### Ejecting or Clearing a Card

When the source is an SD card or USB drive, an Eject button appears next to the Camera picker, and again on the completion card after the import. The same command is available from File → Eject Removable Media. MediaFlow asks you to confirm, shows an “Ejecting…” step while the card is unmounted (do not pull the card yet), and then tells you it is safe to remove. If the eject fails because files on the card are still open, close any app or Finder window using them and click Retry.

A Clear Card… button appears beside Eject. It closes the Import sheet and opens the Clear Card sheet, which deletes only clips that are already organized and verified at the destination.

Importing is part of the Studio plan; see Plans and Pricing.

See also: [Importing from iPhone or Camera](#importing-from-iphone-or-camera), [The Import Sheet and Completion Card](#the-import-sheet-and-completion-card), [Clear Card](/manual/organizing-media/#clear-card), [Clip Classifier, Second Pass (Tier 1)](/manual/organizing-media/#clip-classifier-second-pass-tier-1)

## Importing from iPhone or Camera

*Import photos and videos from an iPhone or camera connected over USB, and what to do when clips are missing.*

The iPhone segment of the Import sheet copies photos and videos straight from a phone or camera connected by USB into your project’s working folder.

1. Connect your iPhone or camera via USB. Unlock the iPhone and tap Trust if it asks
2. Choose File → Import… and select the iPhone segment at the top of the sheet
3. Select your device from the Device picker
4. Check the items to import in the list. Items already in the project are marked Duplicate and are skipped
5. Click Import Selected

Click an item to preview it on the right; MediaFlow copies it to this Mac to show it. Press Space to play or pause a video, as for a card or folder.

MediaFlow uses Apple’s Image Capture framework to talk to the device. While an iPhone is locked, the sheet asks you to unlock it and tap Trust.

### If Clips Are Missing

Only media stored on the phone itself appears in the list. Photos and videos that iCloud Photos has moved to the cloud are invisible until they are downloaded to the iPhone:

1. On the iPhone, open Settings → Photos and choose Download and Keep Originals
2. Keep the iPhone unlocked, on Wi-Fi and on power until the download finishes
3. Click Refresh in the Import sheet

### Disk Space

The import does not start unless the working folder’s disk has at least 10 GB free.

> **Tip:** If the device does not appear, disconnect and reconnect the USB cable, then click Refresh to scan again.

The “Ask a model to suggest categories” checkbox is available here too. See Importing from a Card, Drive or Folder for what it sends and what it costs.

See also: [Importing from a Card, Drive or Folder](#importing-from-a-card-drive-or-folder), [The Import Sheet and Completion Card](#the-import-sheet-and-completion-card), [Import Not Detecting Files](/manual/troubleshooting/#import-not-detecting-files)

## The Import Sheet and Completion Card

*One Import sheet for every source, its per-import options, and the card that appears when the import finishes.*

File → Import… opens a single Import sheet. The segment at the top chooses the source: Cards & drives (detected SD cards and USB drives), iPhone (phones and cameras over USB), or Folder (any directory). The banner that appears when a card or phone is plugged in opens the sheet on Cards & drives.

### Ask a Model to Suggest Categories

When a model is set up in Settings › Analysis, the bottom of the sheet offers the checkbox “Ask a model to suggest categories”. It is unticked every time the sheet opens and applies to this import only. A model on this Mac is free and sends nothing off the Mac. A paid provider receives frames from each clip and charges for each one. See Importing from a Card, Drive or Folder for the details.

### Completion Card

When an import finishes, the file list is replaced by a card that reads, for example, “Imported 24 clips (8.1 GB) from Camera A”. It offers these actions:

- Eject &lt;card> — shown only when the source was a removable card or drive; runs the same confirm → ejecting → safe-to-remove flow as File → Eject Removable Media
- Categorize now — closes the sheet and opens category suggestions for the clips just imported, so earlier uncategorized clips are not mixed in. It is dimmed when nothing new was imported
- Done — closes the sheet

You can also categorize later: choose Workflow → Analyze… and run Categories.

### Naming a New Camera

When the import includes clips from a camera MediaFlow could identify only by its make, the card lists each such camera with a name field. Type the name you use for that camera and click Save. MediaFlow remembers the camera and re-labels the clips from this import. If you leave the fields alone, you can name the cameras later in Settings › Cameras.

> **Tip:** Categorize now is the quickest way to get a fresh card into the right categories while you still remember what you shot.

See also: [Importing from a Card, Drive or Folder](#importing-from-a-card-drive-or-folder), [Importing from iPhone or Camera](#importing-from-iphone-or-camera), [Auto-Suggest Categories](/manual/tags-categories/#auto-suggest-categories), [The Analyze Hub](/manual/getting-started/#the-analyze-hub)

<div class="chapter-nav" role="navigation" aria-label="Chapters">
<a rel="prev" href="/manual/setup-network/">&larr; Setup &amp; Network</a>
<a href="/manual/">All chapters</a>
<a rel="next" href="/manual/managing-assets/">Managing Assets &rarr;</a>
</div>
