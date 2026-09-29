---
layout: manual
title: Manual
description: The MediaFlowSwift user guide, generated from the Help inside the app.
---
# MediaFlowSwift Manual

For video creators. This guide is generated from the app’s own Help (Help → MediaFlow Help), so the two always say the same thing. To change a sentence here, change it in Help and regenerate.

## Contents

- [Getting Started](#getting-started)
  - [What Is MediaFlow?](#what-is-mediaflow)
  - [Creating a New Project](#creating-a-new-project)
  - [Opening an Existing Project](#opening-an-existing-project)
  - [Understanding the Interface](#understanding-the-interface)
  - [Understanding the Pipeline Strip](#understanding-the-pipeline-strip)
  - [What Things Are Called Now](#what-things-are-called-now)
  - [The Analyze Hub](#the-analyze-hub)
  - [Progress and Messages](#progress-and-messages)
  - [Terms of Use](#terms-of-use)
  - [About MediaFlowSwift](#about-mediaflowswift)

- [Setup & Network](#setup--network)
  - [Setting Up MediaFlow](#setting-up-mediaflow)
  - [Choosing and Connecting Your Network Share](#choosing-and-connecting-your-network-share)
  - [Saved Setup: A Copy of Your Settings](#saved-setup-a-copy-of-your-settings)
  - [Updating MediaFlow](#updating-mediaflow)
  - [The Settings Window, Tab by Tab](#the-settings-window-tab-by-tab)
  - [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac)

- [Importing Media](#importing-media)
  - [Importing from a Card, Drive or Folder](#importing-from-a-card-drive-or-folder)
  - [Importing from iPhone or Camera](#importing-from-iphone-or-camera)
  - [The Import Sheet and Completion Card](#the-import-sheet-and-completion-card)

- [Managing Assets](#managing-assets)
  - [Table and Grid Views](#table-and-grid-views)
  - [Selecting Clips](#selecting-clips)
  - [Context Menu Actions](#context-menu-actions)
  - [Filtering and Searching](#filtering-and-searching)
  - [Editing Clip Metadata](#editing-clip-metadata)
  - [Star Ratings & Selects](#star-ratings--selects)
  - [Undo and Redo](#undo-and-redo)

- [Organizing Media](#organizing-media)
  - [Organizing Media to Storage](#organizing-media-to-storage)
  - [Change destination folder](#change-destination-folder)
  - [Re-check files](#re-check-files)
  - [Freeing Up Space](#freeing-up-space)
  - [Clear Card](#clear-card)
  - [Proposals: What Import Analysis Suggests](#proposals-what-import-analysis-suggests)
  - [Using a Model to Suggest Categories](#using-a-model-to-suggest-categories)
  - [Running a Model on This Mac](#running-a-model-on-this-mac)
  - [How MediaFlow Verifies Copies](#how-mediaflow-verifies-copies)
  - [Format Conformance Checker](#format-conformance-checker)
  - [Workflow Templates](#workflow-templates)
  - [GPS Scene Detection](#gps-scene-detection)
  - [Sun Position & Shadow Continuity](#sun-position--shadow-continuity)
  - [Interactive Shoot Map](#interactive-shoot-map)
  - [Historical Weather Lookup](#historical-weather-lookup)
  - [Vision (AI Scene Analysis)](#vision-ai-scene-analysis)
  - [Speech Transcription](#speech-transcription)
  - [Smart Selects](#smart-selects)
  - [Audio Waveform Sync](#audio-waveform-sync)
  - [Shot List](#shot-list)
  - [Storyboard](#storyboard)
  - [Import Field Notes](#import-field-notes)
  - [Clip Classifier, Second Pass (Tier 1)](#clip-classifier-second-pass-tier-1)
  - [Audio Levels](#audio-levels)
  - [Exposure](#exposure)
  - [Transcode](#transcode)
  - [Continuity](#continuity)
  - [Logging Scene, Shot and Take](#logging-scene-shot-and-take)

- [Video Preview & Playback](#video-preview--playback)
  - [Video Playback Controls](#video-playback-controls)
  - [Pop-Out Video Window](#pop-out-video-window)
  - [Extracting Thumbnails and Subclips](#extracting-thumbnails-and-subclips)
  - [Reviewing Clips with the Keyboard](#reviewing-clips-with-the-keyboard)

- [Batch Operations](#batch-operations)
  - [Using the Proxy Queue](#using-the-proxy-queue)
  - [Processing the Proxy Queue](#processing-the-proxy-queue)

- [Tags & Categories](#tags--categories)
  - [Working with Categories](#working-with-categories)
  - [Working with Tags](#working-with-tags)
  - [Adding, Renaming, Retiring and Removing Categories](#adding-renaming-retiring-and-removing-categories)
  - [What Happens to Files When You Change a Category](#what-happens-to-files-when-you-change-a-category)
  - [Auto-Suggest Categories](#auto-suggest-categories)

- [Shared Database](#shared-database)
  - [Shared Database Overview](#shared-database-overview)
  - [Who Else Has a Project Open](#who-else-has-a-project-open)
  - [Searching All Projects](#searching-all-projects)
  - [Finding Duplicate Files](#finding-duplicate-files)
  - [Migrating Projects to the Database](#migrating-projects-to-the-database)
  - [Storage Dashboard](#storage-dashboard)
  - [Database File or Database Server?](#database-file-or-database-server)
  - [Connecting to a Database Server](#connecting-to-a-database-server)
  - [Copying Records Between the File and the Server](#copying-records-between-the-file-and-the-server)
  - [Working Offline and Syncing Later](#working-offline-and-syncing-later)
  - [One Mac at a Time on a Database File](#one-mac-at-a-time-on-a-database-file)

- [Storage Maintenance](#storage-maintenance)
  - [Relinking Missing Media](#relinking-missing-media)
  - [Storage Forecast](#storage-forecast)

- [Reports](#reports)
  - [Generating Reports](#generating-reports)
  - [NLE Template Export](#nle-template-export)
  - [Dailies Report](#dailies-report)
  - [Day Summary](#day-summary)

- [Publishing](#publishing)
  - [Preparing a Video for YouTube](#preparing-a-video-for-youtube)
  - [The SEO Agent](#the-seo-agent)
  - [The Publishing Checklist](#the-publishing-checklist)
  - [Making a Thumbnail](#making-a-thumbnail)
  - [Uploading to YouTube](#uploading-to-youtube)
  - [Setting Up Your Google Client](#setting-up-your-google-client)
  - [How Your Videos Are Doing](#how-your-videos-are-doing)

- [Project Management](#project-management)
  - [Saving Projects](#saving-projects)
  - [Renaming a Project](#renaming-a-project)
  - [Moving a Project](#moving-a-project)
  - [Editing on an Editing Drive](#editing-on-an-editing-drive)
  - [After Moving Your Library to a New Drive](#after-moving-your-library-to-a-new-drive)
  - [Deleting a Project](#deleting-a-project)
  - [Moving Clips Between Projects](#moving-clips-between-projects)
  - [Duplicating a Project](#duplicating-a-project)
  - [Archiving a Project to USB](#archiving-a-project-to-usb)
  - [Restoring an Archived Project](#restoring-an-archived-project)
  - [Managing Archive Volumes](#managing-archive-volumes)

- [Settings & Preferences](#settings--preferences)
  - [Plans and Pricing](#plans-and-pricing)
  - [The Settings Window](#the-settings-window)
  - [Smart Notifications](#smart-notifications)

- [Keyboard Shortcuts](#keyboard-shortcuts)
  - [Keyboard Shortcuts Reference](#keyboard-shortcuts-reference)

- [Troubleshooting](#troubleshooting)
  - [Clips Showing as Missing](#clips-showing-as-missing)
  - [Reporting a Problem](#reporting-a-problem)
  - [Contacting Support](#contacting-support)
  - [Database Connection Issues](#database-connection-issues)
  - [Searching All Projects Finds Nothing](#searching-all-projects-finds-nothing)
  - [Network Share 'Resource Busy' Errors](#network-share-resource-busy-errors)
  - [Import Not Detecting Files](#import-not-detecting-files)
  - [Understanding the Where Column](#understanding-the-where-column)

---

# Getting Started

## What Is MediaFlow?

*What MediaFlow does for a video creator, the basic workflow from card to archive, and where to find help.*

MediaFlow keeps track of the footage from a shoot. You import clips from cards, phones and folders, sort them into categories, review them, and copy them into a tidy folder structure at the project’s destination folder, ready for editing and archiving.

### System Requirements

Requires macOS 14 Sonoma or later on a Mac with Apple silicon (M1 or newer). MediaFlowSwift does not run on Intel-based Macs. About MediaFlowSwift, in the MediaFlowSwift menu, says the same.

### Key Capabilities

- Import media from SD cards, USB drives, folders, iPhones and cameras connected over USB
- Organize clips into category folders at the project’s destination folder — a network share, an external drive, or a folder on this Mac
- Preview video with frame-by-frame playback controls
- Add categories, tags, notes and star ratings to your clips
- Generate PDF, HTML, and CSV reports for your projects
- Search across projects and find duplicates with an optional shared database — a single file, or a database server several Macs can use

### Basic Workflow

1. Create or open a project
2. Import media from your cards, phones and folders
3. Categorize and review your clips
4. Organize the clips to the project’s destination folder
5. Generate a report for your editor, then archive the project

The pipeline strip under the toolbar follows these steps and always offers the next one.

### First-Run Setup

The first time you open MediaFlow, a short tour explains the app. A Setup Wizard follows it. It first asks where your footage goes: this Mac, an external drive, or a network share. Then it asks where organized media goes. Only for a network share does it ask more: which share, and whether to use a database every Mac shares. You can skip any question. To answer them later, choose Settings › General › Run Setup Again…

### Where to Get Help

- Help → MediaFlow Help (Cmd+/) opens this searchable help window
- Help → User Guide opens a printable version of every topic in your web browser
- Help → Keyboard Shortcuts jumps straight to the shortcut reference
- Help → Getting Started Guide re-opens the welcome tour shown the first time MediaFlowSwift opens. It opens by itself once only; to have it open every time, tick “Show this welcome when MediaFlowSwift opens” on the tour, or the same switch in Settings › General
- MediaFlowSwift keeps its own copy of your setup, including what you have already seen, the size and place of its windows and your view choices, and puts it back at launch if macOS has lost them

See also: [Setting Up MediaFlow](#setting-up-mediaflow), [Creating a New Project](#creating-a-new-project), [Opening an Existing Project](#opening-an-existing-project), [Understanding the Pipeline Strip](#understanding-the-pipeline-strip), [Keyboard Shortcuts Reference](#keyboard-shortcuts-reference), [About MediaFlowSwift](#about-mediaflowswift)

## Creating a New Project

*Create a new empty project, or build one from a folder of media you already have without copying anything.*

A project is a .vpm file that records your clips and everything you know about them. Start an empty project for a new shoot, or build one from a folder that already holds media.

### New Empty Project

1. Choose File → New Project (Cmd+N)
2. Enter a descriptive project name
3. Check Project location — the folder the new project folder is created in. It starts at the last location you used, or your Documents folder; click Choose… to pick another
4. Check “Organized media goes to” — the destination Organize Media copies clips to. It starts as the new project folder; click Change… to pick another folder, or Use project folder to go back
5. Click Create

MediaFlow creates a folder named after the project and saves the .vpm project file inside it.

When the destination is on this Mac’s own drive, a plain note under it says so; keeping everything on your Mac is a fine way to work. The note turns into an orange warning only when your setup points somewhere else: when your default destination in Settings › Storage is on another drive or a share, or, with no default destination set, when you use a network share. Then a folder on this Mac usually means that drive or share was not connected when the project was made. When the default destination in Settings › Storage is on this Mac, this Mac is your choice and there is no warning, even if a network share is also set up, for a shared database say. If this Mac is where you want the organized media, you can ignore the warning.

With a shared database set up (a database server, or a database file on a network share), other Macs share your projects, and they can only organize into a folder they reach. When the destination is on this Mac, or on a drive connected to it, New Project warns that other Macs sharing the project won’t be able to organize into it, and offers Choose a Folder on a Network Share…. It is a warning: Create still works. The Mac that creates a project owns its destination, and another Mac never quietly organizes the project somewhere else; see When This Mac Can’t Reach the Destination in Organizing Media to Storage.

### Create from Existing Folder

1. Choose File → Create Project From Folder (Cmd+Shift+N)
2. Select a folder that already contains media files
3. Choose where to save the project file. The suggested name is the folder’s name
4. MediaFlow scans the folder, including its subfolders, and adds every supported media file to the project

The files stay where they are — nothing is copied or moved. The project takes the folder’s name, and its destination is set to the folder you saved the project file in. You can change the destination later from the sidebar.

> **Tip:** Use Create Project From Folder when your media is already laid out the way you want and you only need MediaFlow to catalog it.

See also: [Opening an Existing Project](#opening-an-existing-project), [Saving Projects](#saving-projects), [Change destination folder](#change-destination-folder)

## Opening an Existing Project

*Open a saved project from its file, from the Open Recent menu, or from the Project Browser.*

### Open from File

1. Choose File → Open (Cmd+O)
2. Navigate to the .vpm project file
3. Click Open

### Open Recent

The File → Open Recent submenu lists your recently opened projects for quick access. Choose Clear Menu at the bottom of the submenu to empty the list.

### Project Browser

The Project Browser shows all known projects, including those registered in the shared database. It is in the main window: there whenever no project is open, and shown in place of the open project by Projects → Browse Projects… (Cmd+Shift+P). Back to, followed by the project’s name, returns to that project just as you left it. Opening another project from the list asks about unsaved changes first, as opening always does.

- Double-click a project to open it. Or select it and click Open Selected at the top right, or press Return
- Right-click anywhere on a project’s row for options: Open, Delete Project…, Remove from List, Show in Finder
- Type in the Filter projects by name field above the list to narrow it by project name. The count under Projects is of the projects listed, for example 3 of 12 projects
- The search field in the toolbar searches the clips of every project in the shared database, in the list’s place, under a line that says so; Clear brings the list back. See Searching All Projects
- Click a column header to sort the list; MediaFlow remembers your choice the next time you open it

See also: [Creating a New Project](#creating-a-new-project), [Deleting a Project](#deleting-a-project)

## Understanding the Interface

*A tour of the main window: pipeline strip, sidebar, media list, preview panel and metadata panel.*

The main window is divided into five areas:

### Pipeline Strip (Top)

- One row under the toolbar with the seven steps of a shoot: Import, Categorize, Review, Organize, Free up space, Archive, Eject
- See Understanding the Pipeline Strip for what each segment counts and what its button does

### Sidebar (Left)

- Shows the project name, the organize destination with a Change… link, and the active filters as chips
- Library section: All Media, Favorites, Proxy queue
- Smart Groups section: Not at destination (clips whose file is not at the destination yet), Missing, Uncategorized, Unrated, Unreviewed, Reject candidates
- Cameras section: the project’s camera list. Click a camera to see only its clips
- Places section: the places your clips were shot, grouped from their GPS data. It appears only when clips have GPS data

### Media List (Center)

- Displays your clips in either Table or Grid view
- Use the toolbar picker to switch between views
- In Table view, click the Filename, Date or Where header to sort
- Cmd+Click adds clips to the selection; in Table view Shift+Click selects a range
- When clips are selected, a bar at the bottom of the list offers Organize Media, Set Category, Toggle Favorite, Rate, Select, Remove from Project and Deselect All

### Preview Panel

- Shows a video player or image preview for the selected clip
- Video controls: play/pause, frame step, seek slider, pop-out

### Metadata Panel

- Six tabs: Workflow Tools, Edit, Full Metadata, Metadata, Scene Log and Transcript. When the panel is too narrow to show them all, scroll the row of tabs sideways. The tab you last used is remembered
- Drag the divider between the preview and this panel to give either more room; the panel can be as narrow as the tabs’ contents allow and much wider than before
- Workflow Tools — Extract a thumbnail, mark in and out points, create a subclip, and manage and process the Proxy queue
- Edit — Change the category, favorite flag, tags and notes of the selected clips
- Full Metadata — Everything read from the file, in sections you can open and close: file details; video (resolution, frame rate, codec, bit rate); color and HDR; audio; camera and lens; and, when the clip has them, GPS, weather, drone, GoPro and iPhone data
- Metadata — A short summary: filename, type, size, date created, duration, category, Camera and Where, and the clip’s thumbnail and proxy files
- Scene Log — Scene, shot type, take, Camera angle and Circle Take for the selected clip
- Transcript — Read, search, correct and export the clip’s transcript, or transcribe it if it has none

### Rearranging Panels

- The media list starts on top, full width, with the preview and metadata panels below it. If you have already moved it, your saved choice is kept
- View → Move Media to Top / Move Media to Bottom (Cmd+Opt+T) swaps the media and preview positions; the menu title shows the direction it will move
- View → Move Preview to Left / Move Preview to Right (Cmd+Opt+P) swaps the preview and metadata positions
- View → Reset to Default Layout restores the standard arrangement (enabled only after a swap)
- Drag the dividers between panels to resize them

See also: [What Is MediaFlow?](#what-is-mediaflow), [Understanding the Pipeline Strip](#understanding-the-pipeline-strip), [Table and Grid Views](#table-and-grid-views), [Filtering and Searching](#filtering-and-searching)

## Understanding the Pipeline Strip

*The row under the toolbar that shows how far the project has come and offers the one next action.*

The pipeline strip shows the seven steps of a shoot and how much work each one still has. It runs across the top of the window whenever a project is open. Every segment is a button.

### The Seven Segments

- Import — clips in the project. Button: Import…, the same sheet as File → Import…
- Categorize — clips with no category (a blank category counts). Button: Auto-suggest
- Review — clips with no star rating. Button: Rapid Review…, the same as Workflow → Review (Cmd+Opt+R)
- Organize — clips whose file is not at the destination folder. Button: Organize N clips. A clip that is at the destination with a size mismatch counts as organized here; the Where column still shows the mismatch
- Free up space — the space the working-directory copies of organized clips still take on this Mac. A copy Free Up Space has moved to Cleanup or deleted no longer counts, and one Restore from Cleanup puts back counts again. Button: Free Up Space…, which checks each file and shows exactly what it will reclaim
- Archive — Pending, or the volume the project was archived to (“USB #0007”) with the date. Button: Archive…
- Eject — removable cards and drives still mounted. Button: Eject &lt;name>, or an Eject menu when more than one is connected

### Clicking a Segment

Clicking a segment filters the media list to that step’s remaining work and reveals its one primary button on the right. Import shows all media, Categorize shows the uncategorized clips, Review shows the unrated ones and Organize shows the Not at destination smart group. Free up space, Archive and Eject leave the current filter alone because their work is not a subset of the list.

Until you click one, the strip follows the first step that still has work to do. A finished step shows a green check instead of its icon.

The Organize count turns orange once 10 or more clips are still waiting and the project has a destination.

See also: [Understanding the Interface](#understanding-the-interface), [Organizing Media to Storage](#organizing-media-to-storage), [Freeing Up Space](#freeing-up-space), [Smart Notifications](#smart-notifications)

## What Things Are Called Now

*One word per concept: the names that changed this release, and the old names they answer to.*

The same thing used to have several names and the same name used to mean several things. This release settles on one word per concept. Nothing stored in your projects changed — a .vpm file written before this release loads unchanged, and one written after it still opens in an older build. Only the words on screen moved.

### The Table

- Organize Media keeps its name, and the pipeline strip now says Organize too, instead of naming a device — the menu item, the toolbar button, the right-click action, the strip and the confirmation sheet all read the same. With clips selected it copies the selection; with nothing selected it copies the whole project, and the sheet says which
- Device is now Camera wherever it means the camera that shot the clip — the table column, the sidebar section, the Import sheet’s picker and the Set Camera menu. “Device” now means an import source: a card, a drive, an iPhone.
- The Scene Log’s Camera field is now Camera angle — A, B, C, the angle a take was shot from, not the camera body
- The Location column is now Where, and the sidebar’s Locations section is now Places. Where is about the file; Places is about the world
- Sync Folder Layout (Entire Project) is now Re-file folders by category, under Workflow → Repair
- Reconnect Destination is now Change destination folder, under Workflow → Repair
- Refresh Storage Locations is now Re-check files, under Workflow → Repair
- Do Not Copy now reads Skip (don’t copy). It is still stored as “Do Not Copy”
- The Dashboard and the Project Checklist are gone. The pipeline strip across the top of the window shows where the project stands
- Batch Queue is now Proxy queue — the queue for thumbnails and proxies
- Remove Selected Assets is now Remove from Project
- Kill is now Reject. It is still stored as “Kill”
- Favorite and Circle Take fold into Hero. A favorite becomes a Hero when the project loads; a circle take becomes a Hero rated five stars. Both flags stay in the file so an older build still reads it

### Where the Workflow Menu Went

- Organize Media…, Review, Free Up Space…, Archive to USB… — the things you do to footage once it is in, at the top level. Restore from Cleanup sits under Free Up Space…. Import… is in the File menu
- Analyze… — one sheet holding every optional analysis pass. See The Analyze Hub
- Plan & Deliver — Shot List, Storyboard, Shoot Map, Day Summary, Storage Forecast, Import Field Notes, Generate Dailies, NLE Template Export, Export FCPXML, Report and Prepare for YouTube
- Repair — Re-check files, Relink Missing Media, Change destination folder, Re-file folders by category. Library Moved is here too: it points every project at a library you have copied to a new drive
- Run Workflow Template… (Cmd+Shift+R) — at the bottom of the menu

> **Tip:** Searching this help for an old name still works. Type Organize Media, Sync Folder Layout, Reconnect Destination, Refresh Storage Locations, Batch Queue, Rapid Review, Kill or Circle Take and you will land on the topic that replaced it.

See also: [The Analyze Hub](#the-analyze-hub), [Organizing Media to Storage](#organizing-media-to-storage), [Star Ratings & Selects](#star-ratings--selects)

## The Analyze Hub

*Workflow → Analyze… lists every optional analysis pass with why you would run it, what it needs and when it last ran.*

The Analyze hub is one sheet that holds every optional analysis pass, so you can see what each one is for and whether this project has what it needs. Open it with Workflow → Analyze… The passes were separate Workflow menu items in earlier versions.

Each row gives the tool, one line on what running it buys you, a prerequisite counted from the project you have open — for example “needs GPS — 38 of 212 clips have it” — and the date it last ran. Click Run on a row to start that pass; its results open in the pass’s own review sheet.

### The Passes

- Categories — proposes a category for uncategorized clips (was Auto-Suggest Categories)
- GPS Scenes — groups clips into scenes by GPS proximity and time gaps (was GPS Scene Detection)
- Place names — turns coordinates into readable place names (was Geocode Locations)
- Sun — sun angle and shadow continuity (was Sun Position Analysis)
- Weather — historical weather per clip with GPS data (was Weather Lookup)
- Vision — shot type, faces and scene content on-device (was AI Scene Analysis)
- Smart Selects — quality scores and proposed star ratings (was AI Smart Selects)
- Audio — clipping, low level and silence (was Analyze Audio Levels)
- Transcribe — on-device speech transcription (was Transcribe All Clips)
- Format — mixed frame rates, resolutions and codecs (was Check Format Conformance)
- Exposure — exposure and color consistency (was Exposure & Color Check)
- Transcode — what your target NLE will struggle with (was Transcode Recommendations)
- Continuity — multi-camera coverage gaps per scene (was Continuity Checker)
- Audio Sync — lines up multi-camera clips by audio (was Audio Waveform Sync)

> **Tip:** The last-run date is per project and per pass, and is recorded when you press Run. It is a preference, not project data — it never touches the .vpm file or the database.

See also: [What Things Are Called Now](#what-things-are-called-now), [GPS Scene Detection](#gps-scene-detection), [Auto-Suggest Categories](#auto-suggest-categories)

## Progress and Messages

*The panel in the bottom-right corner where every long operation and every outcome appears.*

Anything that takes more than a moment — an import, an organize, a relink, a project move, and every analysis pass — opens a row in the progress panel at the bottom-right of the window. The row names the operation, shows a progress bar when the work can be counted, and disappears when the work is done.

### Outcomes Stay Put

The result of an operation waits for you instead of fading away. “Ejected CARD_A”, “Relinked 12 of 14 files” and “Audio analysis complete” stay in the progress panel until you click the × on them, and some carry the obvious next step as a button — Import Next Card after an eject, Review Ratings after Smart Selects.

### What Each Kind Looks Like

- Progress — a spinner or a bar with a percentage while the work runs
- Success (green check) — a finished operation; stays until dismissed
- Warning (orange triangle) — nothing to do, or something skipped; stays until dismissed
- Notice (grey) — a passing status; clears itself after a few seconds
- Error — an alert with an OK button, not a row in the panel

### Long Messages

A long message shows its first four lines with Show More under them. Click Show More to read the rest in place, and Show Less to fold it again; the panel remembers which messages you opened. A very long message scrolls inside its row once opened, and when several messages are open the panel never grows taller than the window: its messages scroll inside it, the newest at the bottom. So the × and any button that comes with a message, such as Show in Finder or Save As…, are always inside the window, where you can reach them. A passing notice stays longer the longer it is, about a second for every line past the second, up to about ten seconds. It never clears itself while the pointer is over it, and when you move the pointer away it waits at least two more seconds. A passing notice you open with Show More stays until you dismiss it. Hold the pointer over a message to see all of it at once, and VoiceOver reads every word. The reason under a failed operation, and a smart notification at the top of the window, open the same way.

### Failed Operations

An operation that fails keeps its row, tinted red, with the reason in place of the progress bar. It stays until you dismiss it, so a failure that happened while you were away is still there when you come back.

### While a Sheet Is Open

Messages raised inside a sheet — the Import sheet’s “No card selected”, a folder scan that failed — appear inside that sheet, next to the button that caused them, instead of behind the sheet, where you could not read them.

> **Tip:** When no project is open the same status appears in the centre of the window instead, where there is nothing else to look at.

See also: [Understanding the Interface](#understanding-the-interface), [Understanding the Pipeline Strip](#understanding-the-pipeline-strip), [Smart Notifications](#smart-notifications)

## Terms of Use

*MediaFlowSwift is sold by Long Road Software LLC under terms of use you agree to once, before you first use the app, and again only when they change.*

The first time MediaFlowSwift opens, it shows the terms of use before anything else: four points in plain words, and the full terms below them. Click Agree to start using the app. Quit closes it without changing anything, and it asks again the next time it opens.

Until you agree, the window shows only the terms and nothing else starts: MediaFlowSwift opens no project, connects to no database or share, and does not check for updates. Every menu is unavailable except Help, where you can still read Help, the user guide and the terms. On a new copy, the free trial’s 14 days start when you agree, not when you first open the app.

### What agreeing records

MediaFlowSwift keeps the version of the terms you agreed to and the date, on this Mac only: in your Keychain, and in a small file in MediaFlow’s folder under Library › Application Support. Two places, because some Macs do not keep an app’s preferences. Nothing is sent anywhere. If neither can be saved, the app opens anyway and asks again next time.

### When the terms change

An update that changes the terms shows them again, with a short list of what changed, and the app goes on once you agree to the new version. An update that does not change them asks nothing.

### Reading them again

Choose Help → Terms of Use to read the terms at any time. The window also says when you agreed to them on this Mac. The same terms are on the website at mediaflowswift.com/terms.html, with the refund policy beside them.

See also: [Setting Up MediaFlow](#setting-up-mediaflow), [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [What Is MediaFlow?](#what-is-mediaflow), [About MediaFlowSwift](#about-mediaflowswift)

## About MediaFlowSwift

*The version you are running, who makes MediaFlowSwift, what it needs to run, links to the website, and the open-source acknowledgements.*

Choose MediaFlowSwift → About MediaFlowSwift. The window shows the version and build you are running and © 2026 Long Road Software LLC, the maker and seller of MediaFlowSwift. Its links open the website, the support page, the terms of use and the privacy page in your web browser; nothing is opened until you click. Settings › General › About shows the same.

### System Requirements

Requires macOS 14 Sonoma or later on a Mac with Apple silicon (M1 or newer). MediaFlowSwift does not run on Intel-based Macs. The app is built for Apple silicon only, so on an Intel-based Mac macOS will not open it. Check the Apple menu → About This Mac: a Mac with Apple silicon names its chip there, such as Apple M1 or Apple M3.

### Acknowledgements

MediaFlowSwift is built with open-source packages, among them PostgresNIO and Apple’s SwiftNIO, Swift Log and Swift Crypto, and the BoringSSL code SwiftNIO SSL carries. Acknowledgements…, in About and in Settings › General, lists each package with its version and licence, then the full text of each licence and the notices the packages ask to be passed on, including BoringSSL’s OpenSSL, SSLeay and ISC licences. Copy All copies all of it as plain text.

See also: [What Is MediaFlow?](#what-is-mediaflow), [Terms of Use](#terms-of-use), [Contacting Support](#contacting-support), [The Settings Window](#the-settings-window)

---

# Setup & Network

## Setting Up MediaFlow

*The welcome tour explains the app; the Setup Wizard then asks where your footage goes and only what follows from that, and you can skip any of it.*

A new copy of MediaFlow knows nothing about your equipment: no network share, no shared database, no destination. Three things greet you on first launch. First come the terms of use, which you agree to once (see Terms of Use). The welcome tour then explains the app, and the Setup Wizard asks where your storage is.

You do not have to answer anything. MediaFlow works on a single Mac, with or without an external drive, and needs neither a network share nor a database; every answer can be changed later in Settings.

### The welcome tour

Four pages: Welcome, the workflow, your workspace, and a closing page of tips. Use Next to move on, Skip to leave, and Get Started on the last page. Help → Getting Started Guide opens it again at any time.

### The Setup Wizard

The wizard opens when the tour closes, if nothing is set up yet. It does not open when your saved setup was put back at launch. Its first answer decides which steps follow: two for this Mac or an external drive, four for a network share. A step you leave behind by changing that answer changes nothing: a server typed on the database step, for instance, is put back as it was, password included.

1. Where your footage goes — This Mac, An external drive, or A network share. Nothing is set by this answer alone; it chooses the steps that follow and where the folder picker opens
2. Your network share (a network share only) — shares that are connected now are listed with a Use this button. Look for servers searches the network, and Connect to… opens a server in Finder so you can sign in and mount a share. Use this takes effect as soon as you click it
3. Shared database (a network share only, or when a database is already set up) — choose None, Database file (a single file, one Mac at a time) or Database server (several Macs at once). For a database file, click New Database File… to choose where it will live (MediaFlow makes it at once, and connects when you click Done), or Use an Existing Database File… to use one another Mac made. For a server, fill in the connection fields
4. Where organized media goes — click Choose… to pick the default destination for new projects. It opens in your Movies folder for this Mac, among your drives for an external drive, and on the share for a network share. If the folder you pick is not where your first answer said, the step says so; a project can always use a different one

### Skipping

- To pass over one step, click Next without answering it
- Skip (Skip setup on the first page) closes the wizard and keeps the answers you have given so far
- A step you leave unanswered changes nothing, including a setting that was already in place

### Running it again

Choose Settings › General › Run Setup Again…. The wizard opens showing your current settings, not an empty form: the first answer reads A network share when one is chosen in Settings › Network, and otherwise follows your default destination. Choosing None on the database step turns the shared database off. Answering This Mac or An external drive does not forget a network share you chose before; Forget in Settings › Network does that.

See also: [Terms of Use](#terms-of-use), [Choosing and Connecting Your Network Share](#choosing-and-connecting-your-network-share), [Database File or Database Server?](#database-file-or-database-server), [Saved Setup: A Copy of Your Settings](#saved-setup-a-copy-of-your-settings), [The Settings Window, Tab by Tab](#the-settings-window-tab-by-tab), [What Is MediaFlow?](#what-is-mediaflow)

## Choosing and Connecting Your Network Share

*Settings › Network is where you tell MediaFlow which network share holds your projects and media.*

MediaFlow has no built-in network share. Until you choose one, Settings › Network reads “No network share chosen yet” and nothing is assumed. A share is optional: you can organize to any folder, including a drive attached to this Mac.

When you do choose a share, MediaFlow uses it as the starting point for file pickers, as the suggested place for the shared database file, and as the host offered for a database server. It also connects the share when it is needed: see below.

### Choose a share

1. Open Settings › Network
2. If the share is already connected, it appears in the list. Click Use this beside it. The button reads In use for the share you have chosen
3. If it is not listed, click Look for servers, then pick the server from the Connect to… menu. The server opens in Finder, which asks for the password and shows its shares
4. Mount the share you want in Finder, return to Settings, and click Use this

Picking a mounted share fills in both the share name and its address, so there is nothing to type. If you prefer, open “Type the address instead” and enter an smb:// address. A name ending in .local keeps working when the server gets a new network address.

### Connected when it is needed

Once a share is chosen, MediaFlowSwift connects it by itself whenever something needs it and it is not mounted: a couple of seconds after launch, a few seconds after the Mac wakes, and before opening a project whose file lives on it. The status area reads “Connecting to ‘share’…” meanwhile. The launch and wake attempts are made once, so a share that cannot be reached raises at most one password prompt; opening a project tries again, because you are there to answer. If the share still cannot be connected, the project is not opened and a message says so, rather than opening it from the database with every clip called missing. A project on some other drive that is unplugged gets the same treatment: the message names the drive.

If the share is dropped while MediaFlowSwift is open, because the network blinked or the server stopped answering for a minute and macOS removed it, MediaFlowSwift reconnects it. It waits 10 seconds before the first try, then 30 seconds, one minute and two minutes between tries, then five minutes, until the share is back. A strip at the top of the window says so, with Try Now and Stop. These tries never ask for a password; if macOS has not saved it, use Connect now. A share you eject in Finder is left alone, and nothing is tried while the Mac sleeps. Finder may still list the server under Network while the share itself is gone: seeing the server does not mean the share is connected.

While a drive is not connected, the clips on it read Volume not connected in the Where column, in grey, and Re-check files leaves their last known state alone. Nothing is called Missing because its drive is away.

### Passwords

macOS asks for the share’s password, not MediaFlow. MediaFlow never sees or stores it. If you let macOS remember the password, macOS keeps it in your Keychain and uses it to reconnect.

### Connect now and Forget

- The status line reads Connected with the mount path, Looking for the share…, or Not connected
- Connect now tries the stored address, then searches the network, then mounts the share. It is available only while the share is not connected
- Forget stops using this share. Settings that follow it go back to unset. The path to your database file is kept

### No servers found

Check that the server is switched on and on the same network. Also check that MediaFlow is allowed to use the local network: System Settings › Privacy & Security › Local Network.

See also: [Setting Up MediaFlow](#setting-up-mediaflow), [Updating MediaFlow](#updating-mediaflow), [Database File or Database Server?](#database-file-or-database-server), [Database Connection Issues](#database-connection-issues), [Network Share 'Resource Busy' Errors](#network-share-resource-busy-errors)

## Saved Setup: A Copy of Your Settings

*MediaFlow keeps a copy of your settings outside macOS preferences and puts it back if the settings are ever lost.*

The saved setup is a small file that holds your MediaFlow settings. It lives apart from the macOS preferences file, so a lost or reset preferences file does not take your setup with it. You do not need to do anything: it is written every time you quit, when you finish the Setup Wizard, and before an update installs.

Passwords and API keys are never in it. They stay in your Keychain.

### What it holds

- Your network share and its address
- The shared database settings: on or off, the store, the file path, and the server host, port, database and user
- The default destination, recent destinations and the verification setting
- Whether to check for new versions automatically
- Import analysis and model settings, including the daily spending limit
- The category and camera lists that new projects start with

### What it never holds

API keys and the database password. They stay in your Keychain. The saved setup is a plain file, and a secret copied into it would be readable by anyone who opened it. After a restore on a Mac with an empty Keychain, enter those again.

### When it is restored automatically

Only at launch, and only into a copy of MediaFlow that has nothing configured: no network share, no database file, no server and no default destination. It never overwrites settings you are already using.

### Doing it by hand

- Settings › General › Save Setup Now writes the file immediately. The line above the buttons shows when it was last saved
- Restore Saved Setup puts every saved setting back

> **Warning:** Restore Saved Setup overwrites the settings on this Mac with the saved ones. It asks you to confirm first. The saved copy is normally the one written when you last quit.

See also: [Setting Up MediaFlow](#setting-up-mediaflow), [Updating MediaFlow](#updating-mediaflow), [The Settings Window, Tab by Tab](#the-settings-window-tab-by-tab), [Connecting to a Database Server](#connecting-to-a-database-server)

## Updating MediaFlow

*MediaFlow updates itself from the MediaFlow website and keeps your settings.*

MediaFlow looks for a newer version of itself, tells you when there is one, and installs it when you say so. Your settings and projects are not touched by an update.

### Where new versions come from

New versions come from the MediaFlow website. MediaFlow reads one small file from mediaflowswift.com that names the newest version, and nothing about you or your Mac goes with the request. Every copy of MediaFlow updates this way; earlier versions could also update from a copy of the app on a share, and that choice is gone.

### Who may sign an update

An update is installed only if it was signed by the maker of the copy you are running, or by MediaFlowSwift’s Apple Developer ID. Nothing else can be handed to you as an update, whatever the website says. From MediaFlowSwift 1.10.18 the app is moving to the Developer ID: after the first update signed with it, macOS treats the app as one it knows, so your Keychain asks once more and then not again. The Local Network switch is another matter: on some versions of macOS the new build is still treated as a stranger, and the switch needs turning off and on once after an update. MediaFlowSwift now tells Launch Services about the new copy before reopening, which is meant to stop that; if it does not, the app says so and offers the switch.

### Automatic checks

With “Check for new versions automatically” on, MediaFlow looks shortly after launch, when the Mac wakes, and then every few hours; while the website cannot be reached it tries again every half hour. Checking reads one small file.

### When a new version is found

A window opens over the main window saying which version is available and which one you have, with the new version’s headline and what is new in it. It never opens while an import, organize, copy, archive, export, upload to YouTube or other work is running, while another sheet or dialog is open, Settings included, while you are typing, or while another MediaFlow window such as Help is the one you are using, and not while a card you have just connected is being offered for import: it waits until nothing is going on for a few seconds, then asks. If you are working in another app, MediaFlow does not take the screen from it; the window waits over MediaFlow’s main window, and the Dock icon bounces once.

- Install Now (Return) installs the new version straight away, with the same checks as the Software Update window: never while something is running, and your work is saved first. The window then shows the install as it goes
- Later (Esc) closes the window. MediaFlow asks again the next time it opens, or after about a day if it stays open
- Skip This Version closes the window and does not ask about that version again. A newer version is asked about as usual
- Install Now and Skip This Version work only once the keyboard has been still for a moment: while keys keep coming, even a Return held down, Return and Space do nothing there, and neither does a click on either button. The same moment passes after the window opens and after you come back to MediaFlow from another app, so a key you were pressing for something else cannot install or skip a version. Tab and Shift-Tab between the window’s own buttons do not count, so with Full Keyboard Access you can Tab to a button and press Space straight away. Later (Esc) always works

Whatever you answered, Check for Updates… in the app menu always offers the newest version, even one you skipped or put off, and you can install it from there at once. Later in the Software Update window means the same as Later in the question. A version you skipped is shown in Settings › General under Updates, with Offer It Again to be asked about it once more.

### Installing

1. Choose Check for Updates… in the app menu, or click Install Now when a new version asks
2. From Check for Updates…, click Install Update. The button is unavailable while a background operation, such as an import or an upload to YouTube, is running; wait for it to finish
3. MediaFlow downloads the new version and checks that it is exactly the file, and the version, the website promised, checks that it is genuine and from the same maker as the one you are running, closes, puts it in place of the old one and reopens. It reopens only once the old copy has fully closed, which can take some seconds while the shared database is saved. Do not quit or reopen it yourself while it works

The update window lists what is new in the version on offer: every version newer than yours, its headline and its points, taken from the change log the website publishes beside the version file. Notes are read before anything is installed and are not signed, so treat the list as a preview; the copy itself is checked for its maker’s signature when it is installed. When the website has no change log to offer, the list is simply absent.

Your settings are written to disk and to the saved setup before the app restarts.

MediaFlow looks for a new version a few seconds after launch, again every half hour until it can reach the website, and then every few hours, as well as after the Mac wakes. If anything about the new version does not check out, nothing is changed and the version you had reopens. The version you updated from is kept whole for Revert, in MediaFlow’s own folder under Library › Application Support, not beside the app: two copies of MediaFlow in Applications made macOS judge the wrong one when the app asked for your local network after an update. A copy an earlier version left beside the app is moved there the first time this version opens. Every version is the same signed app to macOS, and before the new one reopens the installer tells Launch Services about it, so that permissions you have given MediaFlow carry over from one update to the next; the Keychain’s do. Reaching your local network is the one macOS has sometimes made the new version ask for again; see It Stopped Connecting After an Update. What the installer did is written to Library/Logs/MediaFlow/update.log in your home folder.

### Going back

After an update, the Software Update window shows Revert to Previous Version (or Revert to a named version). It puts the version you had before back in place and relaunches.

See also: [Choosing and Connecting Your Network Share](#choosing-and-connecting-your-network-share), [Saved Setup: A Copy of Your Settings](#saved-setup-a-copy-of-your-settings), [The Settings Window, Tab by Tab](#the-settings-window-tab-by-tab)

## The Settings Window, Tab by Tab

*A map of the eight Settings tabs, so you know which one holds the setting you are looking for.*

Settings has eight tabs. Each holds one subject. Most changes take effect as you make them.

`Cmd+,` — Open Settings

### General

Run Setup Again…, the saved copy of your settings (Save Setup Now, Restore Saved Setup), where app updates come from and whether to check automatically, and the version you are running.

### Network

Which network share MediaFlow uses: shares connected now, Look for servers, Connect now and Forget. There is no built-in share; nothing is assumed until you choose one.

### Storage

The shared database: Enable Central Database, the Store (Database file or Database server), its file or connection fields, and copying records between the two. Below it, the default destination for new projects and “Verify organized copies by reading them back”.

### Cameras

The open project’s camera list (add, rename, remove), “Suggest import when a camera or card is connected”, and camera identities: the rules that turn a serial number or model into the camera name you use.

### Categories

The open project’s category list (add, rename, retire, restore, remove), Also use for new projects, and Category Learning with Reset Pattern Memory.

### Analysis

“Use a model to suggest categories” with its provider, model, API key and daily spending limit. Below it, Import Analysis: proposing a category, camera and scene after an import, and the optional Tier 1 pass that looks at pictures and listens to speech.

### Privacy

Everything that can leave this Mac for a company outside your network, with what is sent and to whom. Each outside service has its own switch and is off until you turn it on.

### Notifications

One switch for each kind of Smart Notification.

> **Tip:** The camera and category lists belong to the project, not to the app. With no project open, those two tabs show Open a Project… instead of a list.

See also: [Setting Up MediaFlow](#setting-up-mediaflow), [Choosing and Connecting Your Network Share](#choosing-and-connecting-your-network-share), [Saved Setup: A Copy of Your Settings](#saved-setup-a-copy-of-your-settings), [Updating MediaFlow](#updating-mediaflow), [Database File or Database Server?](#database-file-or-database-server), [Adding, Renaming, Retiring and Removing Categories](#adding-renaming-retiring-and-removing-categories), [Using a Model to Suggest Categories](#using-a-model-to-suggest-categories), [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [How MediaFlow Verifies Copies](#how-mediaflow-verifies-copies), [Smart Notifications](#smart-notifications)

## Privacy: What Leaves This Mac

*MediaFlow works on this Mac and your own network; each service that reaches an outside company is off until you turn it on.*

MediaFlow has no account and collects no usage data. Your media, projects and shared database stay on this Mac and on your own network.

On its own it reaches its maker in two ways. It asks mediaflowswift.com whether there is a newer version, with nothing about you or your Mac in the request, and downloads the new version when you choose to install it. And once you enter a licence key, it checks the key with MediaFlow’s licence service, sending the key, a random id it made up for this Mac, and the Mac’s name. Settings › Privacy lists both, with the exact details. A problem report reaches its maker only when you send it: from your own mail app with Email Report…, or, on a Mac set up with the maker’s report relay, when you have turned on Sending problem reports and click Send on a report you have read.

A few features need a service run by another company. Settings › Privacy lists every one: what is sent, to whom, and what it is for. Each is off until you turn it on, and you can turn it off again at any time.

### The switches

- Apple’s online speech recognition — sends the audio of the clip being transcribed to Apple, only when this Mac has no on-device speech model for the language. While it is off, speech is recognized on this Mac only, and a language without an on-device model is not transcribed.
- Historical weather lookup — sends each clip’s GPS coordinates, rounded to about 100 m, and the date it was shot to Open-Meteo. While it is off, Look Up Weather does nothing and tells you where to turn it on.
- Place names for GPS coordinates — sends each clip’s coordinates, rounded to about 100 m, to Apple. While it is off, clips show their coordinates; names already looked up are kept.
- A model that writes your YouTube title, description and tags — sends the transcript of the finished video you chose, its length, the brief you typed, and then its own drafts, to the provider chosen in Settings › Analysis. Never the video or its file name. Not needed with the model on this Mac, when nothing is sent outside; a local model you have pointed at another computer on your network receives the same text. See The SEO Agent
- Uploading to YouTube — sends the finished video you chose, with its title, description, chapters, tags, category, visibility, publish time and made-for-kids answer, the file’s size and type, and the thumbnail if you chose to send it, to Google. Signing in opens your browser at Google; MediaFlow never sees your password. Signing in and staying signed in send your client ID and secret to Google. The permission cannot read your channel or delete videos. Nothing is sent until you click Upload and confirm. While it is off, uploading is refused and sign-in does not ask for permission to upload; with both YouTube switches off, signing in is refused too. See Uploading to YouTube
- Reading your videos’ statistics from YouTube — asks Google which channel you signed in to, and sends the YouTube IDs of the videos your database records as uploaded by MediaFlow with the span of dates from the first upload to today, and nothing else. Google answers with their views, likes, comments, watch time, average view, subscribers gained, shares, visibility and publish time. Turning it on makes the next sign-in ask Google for two more permissions, both read-only, which would allow reading your whole channel; MediaFlow asks only about those videos. Read only when you click Read from YouTube Now on the Results tab. See How Your Videos Are Doing
- Maps of where you shot — showing a map sends the area you are looking at to Apple, which is how the map images arrive. While it is off, the Shoot Map and GPS scene review list locations without a map, with a Turn On Maps button.
- Sending problem reports — sends a report only when you click Send on one you have read: its text exactly as shown to you, a title, a random identifier for this copy of the app, and the crash signature if there is one, to a report relay run by MediaFlowSwift’s maker, whose address is entered in Settings › Privacy. The relay fields stay folded away until a relay is set up; a customer has no relay, and needs none. While it is off, or no relay is set up, the Send button is not there. Email Report… needs no switch: it opens the report in your own mail app, for you to send.

### A model that suggests categories

This one is set up in Settings › Analysis, and then ticked for each import you want it for. With a paid provider (Anthropic, OpenAI or Google) it sends three frames from each clip, your category list, the clip’s camera, duration and place name, the opening words of any speech, and your recent corrections. With a model on this Mac, nothing leaves it.

The local model’s Server address may be this Mac or another computer on your own network. An address on the internet is refused, and a redirect from the server is never followed, so frames go only to the computer you named.

### What stays on your network

- Your network share: finding it, connecting to it, and reading and writing media and the database file.
- Your database server, when you use one. That connection is not encrypted, so keep the server on a network you trust.

### Things that open your browser or mail app

Buttons such as a provider’s API-key page, the Ollama download or Help → Support Website open a web page only when you click them. Help → Contact Support… and Email Report… open a new message to support@mediaflowswift.com in your own mail app, with this copy’s version, your macOS version and your Mac’s chip, or the problem report you have read, for you to send. MediaFlow itself sends nothing.

> **Tip:** A saved setup keeps your Privacy switches, but they are not restored automatically on a new install — only when you choose Restore Saved Setup…, which says so before it does.

macOS may separately ask permission for speech recognition or for finding devices on your local network. Those prompts come from macOS and are managed in System Settings › Privacy & Security.

See also: [The Settings Window, Tab by Tab](#the-settings-window-tab-by-tab), [Using a Model to Suggest Categories](#using-a-model-to-suggest-categories), [Running a Model on This Mac](#running-a-model-on-this-mac), [Speech Transcription](#speech-transcription), [Historical Weather Lookup](#historical-weather-lookup), [Interactive Shoot Map](#interactive-shoot-map), [Saved Setup: A Copy of Your Settings](#saved-setup-a-copy-of-your-settings), [Contacting Support](#contacting-support)

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

See also: [Importing from iPhone or Camera](#importing-from-iphone-or-camera), [The Import Sheet and Completion Card](#the-import-sheet-and-completion-card), [Clear Card](#clear-card), [Clip Classifier, Second Pass (Tier 1)](#clip-classifier-second-pass-tier-1)

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

See also: [Importing from a Card, Drive or Folder](#importing-from-a-card-drive-or-folder), [The Import Sheet and Completion Card](#the-import-sheet-and-completion-card), [Import Not Detecting Files](#import-not-detecting-files)

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

See also: [Importing from a Card, Drive or Folder](#importing-from-a-card-drive-or-folder), [Importing from iPhone or Camera](#importing-from-iphone-or-camera), [Auto-Suggest Categories](#auto-suggest-categories), [The Analyze Hub](#the-analyze-hub)

---

# Managing Assets

## Table and Grid Views

*Browse your media as a table with sortable columns or as a grid of thumbnail cards, and switch between them.*

The media list shows the clips in the project that match the current filter. Use the Table / Grid control in the toolbar to switch between the two views.

### Table View

- One row per clip, with columns: Thumbnail, Filename, Type, Date, Duration, Category, Camera, Where, Audio, Rating, Select, Notes
- Click the Filename, Date, Where, Audio, Rating, Select or Notes header to sort by that column; click again to reverse the order. MediaFlow remembers the column and direction you chose, in every project and the next time you open the app; until you choose one, the list is sorted by Date, newest first
- A GoPro splits a long recording into several files, such as GX012324 and GX022324. In the Table they appear as one row: the first chapter, with a label such as “2 chapters · 20:54” giving the count and the total length. Click the arrow at the left of the row to show the other chapters beneath it. The recording stays together whatever column you sort by. Each row is still one file: rating, tagging or playing the first row affects that file only, so expand the row to work on the others. Files are grouped only when they come from the same camera, are the same kind of file and were made within a day of each other. To list every file on its own row, turn off Group Chapters of One Recording in the Filter menu
- A clip you made subclips of with Create Subclip… Add to This Project has an arrow too, and a label such as “2 subclips”. Its subclips are beneath it, in order of where they start in the clip, each labeled with its range, such as 0:12–0:41, whatever column you sort by. A GoPro recording’s first chapter shows its other chapters first and then its own subclips; a later chapter’s subclips are under that chapter’s own arrow, inside the recording. When a search or filter shows a subclip but not the clip it came from, or that clip has been removed from the project, the subclip is on a row of its own with a Subclip label; hold the pointer over the label to see where it came from
- Sorting by Filename follows Finder’s order, so clip2 comes before clip10, and keeps the chapters of one GoPro recording together: a GoPro splits a long recording into files such as GX012324 and GX022324, and MediaFlow lists them one after the other instead of sending the second to the end
- A Category or Camera shown in italics with a confidence badge is a proposal from import analysis. Click the cell to accept it
- Right-click any row for the context menu

### Grid View

- Shows clips as thumbnail cards in a grid that adapts to the window width
- Each card shows the filename, the category, a ★ when the clip is a favorite, a colored Where icon with its label, the camera name and, when they are set, its star rating and its Hero, Maybe or Reject badge
- Video thumbnails carry the clip’s duration in the corner
- The Grid shows every clip as a card of its own, subclips too: a subclip’s card has a Subclip badge, and holding the pointer over it names the clip it was cut from and the range
- Right-click any card for the context menu

See also: [Selecting Clips](#selecting-clips), [Context Menu Actions](#context-menu-actions), [Understanding the Where Column](#understanding-the-where-column), [Extracting Thumbnails and Subclips](#extracting-thumbnails-and-subclips)

## Selecting Clips

*Select one clip or many in the media list, and use the selection bar to act on all of them at once.*

Most commands act on the selected clips: batch editing, organizing, rating, moving to another project and removing from the project.

- Click a clip to select it
- Cmd+Click adds a clip to the selection or takes it out
- Shift+Click selects every clip between the one you last clicked and this one, in Table and Grid view alike. Shift+Click again, further up or down, re-measures from that same starting clip. Cmd+Shift+Click adds the range to what is already selected
- Cmd+A selects every clip the current filter shows. While you are typing in a field, Cmd+A selects the text in that field instead
- Delete removes the selected clips from the project while you are working in the clip list or grid, as File → Remove from Project does. While you are typing in a field, Delete only deletes text

### The Selection Bar

While anything is selected, a bar at the bottom of the media list shows how many clips are selected and offers Organize Media, Set Category, Toggle Favorite, Rate, Select (Hero, Maybe or Reject) and Remove from Project. When selected clips carry import proposals, it also offers buttons to accept them. Click Deselect All to clear the selection.

See also: [Table and Grid Views](#table-and-grid-views), [Context Menu Actions](#context-menu-actions), [Star Ratings & Selects](#star-ratings--selects)

## Context Menu Actions

*The actions you get by right-clicking a clip, or a selection of clips, in Table or Grid view.*

Right-click a clip to act on it. If the clip is part of a selection, the action applies to every selected clip.

- Organize Media… — Copy the clips into the category folders at the project destination, verifying every copy
- Add to Proxy queue / Remove from Proxy queue — Queue the clips for thumbnail and proxy generation, or take them out
- Set Category — Assign a category (B-roll, Interview, Skip (don’t copy), and so on)
- Set Camera — Assign the camera that shot the clips. Clear Camera, at the bottom of this submenu, removes the camera
- Mark Favorite / Unfavorite — Set or remove the favorite flag
- Clear Notes — Erase the notes on the clips
- Remove from Project — Take the clips out of the project. The files on disk are kept
- Move to Project… — Transfer the clips to a different project

### When a File Is Missing

Two more items appear only when the selection includes a clip whose file cannot be found:

- Relink… — Browse for the missing file yourself. Shown when a single clip is targeted
- Relink Missing Media… — Search for the missing files and reconnect them

See also: [Selecting Clips](#selecting-clips), [Filtering and Searching](#filtering-and-searching), [Relinking Missing Media](#relinking-missing-media)

## Filtering and Searching

*Narrow the media list with a filter, and search it, or every project, by name, notes, tags, category, camera or scene.*

A filter limits the media list to the clips you want to work on. One filter is active at a time; choosing another replaces it.

### Searching

`Cmd+F` — Find Clips

Type in the search field in the toolbar, or press Cmd+F to put the cursor there. With This Project chosen under the field (Cmd+F chooses it), the list narrows as you type, in Table and Grid view alike, and a line above it tells you how many clips match out of how many are in the project.

- A clip is found by its file name, its notes, its tags, its category, the camera it came from and its scene. Capital letters do not matter
- Type more than one word and every word must be found, each wherever it likes: gopro beach finds the beach clips from the GoPro, not every GoPro clip and every beach clip
- When weather lookup is on in Settings › Privacy, the conditions are searched too: rain, cloudy
- Searching works inside the current filter. With B-roll chosen in the sidebar, a search looks only at B-roll, and the line above the list says “in this filter”
- Click Clear Search, or the ✕ in the field, to see everything again. Opening another project clears the search

### Sidebar

- Library — All Media, Favorites, Proxy queue
- Smart Groups — Not at destination (clips whose file is not at the organize destination), Missing, Uncategorized, Unrated, Unreviewed (clips with an import proposal nobody has confirmed), Reject candidates
- Cameras — the clips shot by one camera
- Places — the clips shot at one place. Shown when clips have GPS data

### Toolbar Filter Menu

Click the filter menu in the toolbar (its label shows the current filter) to choose:

- All Media — Show everything
- Favorites — Show only favorites
- Proxy queue — Show only queued clips
- Category — Pick one of the project’s categories
- Scene — Pick a scene logged in the Scene Log
- Audio Quality — Audio Issues, Good, Low Level, Clipping or Silent, from the Audio analysis pass
- Rating — Clips rated at least a chosen number of stars, or Unrated
- Select — Clips marked Hero, Maybe or Reject

### Clearing a Filter

The active filter appears as a chip under the project name in the sidebar. Click the chip to remove that filter, or Clear All to return to All Media. The pipeline strip also sets filters: clicking a segment shows that step’s remaining clips.

### Searching All Projects

Choose All Projects under the search field, or press Cmd+Shift+F, to search the clips of every project in the shared database instead. The results take the list’s place, and Add to This Project copies the clips you choose into this project; see Searching All Projects.

See also: [Table and Grid Views](#table-and-grid-views), [Understanding the Pipeline Strip](#understanding-the-pipeline-strip), [Searching All Projects](#searching-all-projects)

## Editing Clip Metadata

*Change the category, favorite flag, tags and notes of one clip or many from the Edit tab of the metadata panel.*

Select one or more clips, then open the Edit tab in the metadata panel.

### Single Clip

- Category — Choose a category from the menu. It is applied immediately
- Favorite — Turn the favorite flag on or off
- Tags — Type a tag and press Enter or comma to add it. Click the X on a tag to remove it
- Notes — Type freeform notes in the text box

Retired categories are left out of the Category menu. A clip that already carries a retired category still shows it, so its value is not lost.

The tab also shows the clip’s Camera and Where, which you cannot edit here. To change the camera, right-click the clip and choose Set Camera, or click a proposed camera in the table’s Camera column to accept it.

### Batch Edit (Multiple Clips)

When several clips are selected, the Edit tab shows batch operations. Each one applies when you click its button:

- Apply Category — Set the chosen category on all selected clips
- Mark Favorite / Unfavorite — Set or remove the favorite flag on all of them
- Add Tags — Add the typed tags to the tags each clip already has
- Replace Tags — Replace every selected clip’s tags with the typed ones
- Clear Tags — Remove all tags from the selected clips
- Set Notes / Clear Notes — Write the same notes on every selected clip, or erase them

> **Tip:** Category, favorite, tag and notes changes can be undone with Edit → Undo (Cmd+Z).

See also: [Working with Tags](#working-with-tags), [Working with Categories](#working-with-categories), [Context Menu Actions](#context-menu-actions), [Undo and Redo](#undo-and-redo)

## Star Ratings & Selects

*Rate clips 1-5 stars and mark them Hero, Maybe or Reject for fast editorial triage.*

### Star Ratings

Every clip can have a rating of 1 to 5 stars. Set it by clicking a star in the Rating column or in the inspector, with the keyboard shortcuts below, with Edit → Set Rating, with the Rate menu in the selection bar, or with the number keys in Review. Click the star a clip already has to clear its rating.

### Where you see them

- Table view — a Rating column and a Select column. Click either header to sort: best first puts five stars, then Hero, at the top, with unrated and undecided clips below and Reject last
- Grid view — each card shows its stars and its Hero, Maybe or Reject badge, when it has them
- Inspector — Rating and Select rows under Organization. With several clips selected, the rows show a value only when every selected clip agrees, and setting one sets them all
- Filter menu in the toolbar — Rating shows clips with at least that many stars, or Unrated; Select shows Hero, Maybe or Reject

### Keyboard Shortcuts

`Cmd+1-5` — Set star rating (1-5 stars)

`Cmd+0` — Clear star rating

`Cmd+Shift+H` — Mark as Hero

`Cmd+Shift+M` — Mark as Maybe

`Cmd+Shift+K` — Mark as Reject

### Select Status (Hero / Maybe / Reject)

The select status sorts clips three ways:

- Hero (green) — Best takes, definitely using these
- Maybe (orange) — Worth reviewing again, possible B-roll
- Reject (red) — Definitely not using. Stored as “Kill”, which is what it used to be called

### Batch Operations

Select multiple clips and use the Rate and Select menus in the selection bar, the Rating and Select rows in the inspector, or Edit → Set Rating and Edit → Select, to apply a rating or a select status to all selected clips at once. All batch operations support undo/redo.

### Export Integration

- FCPXML: Ratings are exported as keyword annotations (for example "★★★★ (4)"); clips rated 4+ stars or marked Hero are FCP favorites
- EDL CSV: Rating and Select Status columns are included in the export

> **Tip:** Press Cmd+0 to clear a rating, or Edit → Set Rating → Clear Rating and Edit → Select → Clear Status to remove ratings or selects from every selected clip.

See also: [Selecting Clips](#selecting-clips), [Undo and Redo](#undo-and-redo), [Reviewing Clips with the Keyboard](#reviewing-clips-with-the-keyboard)

## Undo and Redo

*Edit → Undo reverses metadata edits such as category, rating and tags. It does not reverse file operations.*

Edit → Undo (Cmd+Z) and Edit → Redo (Cmd+Shift+Z) reverse and re-apply metadata edits. The menu item names the step, for example “Undo Set Category 'B-roll' on 3 Clips”, “Undo Rate ★4 on 12 Clips”, or “Undo Accept 7 Category Suggestions”.

### Undoable

- Category, favorite, notes, tags and camera changes from the Edit tab, context menu or selection bar
- Star ratings and Hero / Maybe / Reject select status, including the Cmd+1–5, Cmd+0 and Cmd+Shift+H/M/K shortcuts and ratings made in Review
- Accept All in the Category Suggestions sheet (one step for the whole batch)
- A scene set on several clips at once, including scenes applied from GPS Scenes

### Not Undoable

- Imports, Organize Media, Re-file folders by category, Free Up Space, Clear Card and Archive to USB — these copy, move or delete files. Restore from Cleanup brings back files that Free Up Space staged; files deleted by Free Up Space or Clear Card cannot be brought back
- Edits made in the Scene Log tab, and Shot List and Storyboard edits
- Removing clips from the project (they can be re-imported)

Undo restores the previous values and saves the project. When the undone step changed the category of an organized clip, MediaFlow also moves the copy at the destination back into the matching folder, in the background.

See also: [Editing Clip Metadata](#editing-clip-metadata), [Star Ratings & Selects](#star-ratings--selects), [Auto-Suggest Categories](#auto-suggest-categories)

---

# Organizing Media

## Organizing Media to Storage

*Copy clips into Category and Camera folders at the project destination, with every copy checksummed and verified.*

Organize Media copies your clips into a tidy folder layout at the project destination. The destination can be any folder: a network share, an external drive, a RAID, or a folder on this Mac. The layout is Destination / Category / Camera / Filename.

### Organizing

1. Choose Workflow → Organize Media…, or right-click clips and choose Organize Media. With clips selected it copies the selection; with nothing selected it copies the whole project. If the project has no destination yet, a folder picker opens first
2. Check the confirmation. It shows the scope (selection or whole project), the number of clips, the total size, the destination and its free space
3. To send this copy somewhere else, open the destination menu. It lists the project’s own destination, your default from Settings, places you have organized to before, and Choose… for any other folder
4. A different destination is a one-off: the project keeps pointing where it did. Tick “Make this the project destination” when you want the change to stick. When another Mac set the project’s destination, the box names it: ticking it replaces that Mac’s choice for every Mac that shares the project
5. Click Organize Media. MediaFlow creates the category and camera folders, copies each file, and verifies each copy
6. When the progress window finishes, click Done. Each copied clip now reads “At destination” in the Where column, with a green check

The confirmation can also warn you. Organize is disabled when the destination does not have enough free space. An orange line appears when the destination is on this Mac’s own drive while your setup points somewhere else — your default destination in Settings › Storage is on another drive or a share, or, with no default destination, you use a network share — since that usually means the drive or share was not connected; if you meant to use it, check that it is connected. When your default destination is on this Mac, or everything you do is, there is no warning. With a shared database set up, so that other Macs share your projects, an orange line says instead when the destination is on this Mac, or on a drive connected to it, where those Macs can’t organize. Another orange line counts clips that still carry an unconfirmed proposal; organizing does not apply proposals.

Clips that read On another Mac or Not on this Mac are left out of the copy, and the confirmation says how many. This Mac cannot read them. Organize them on the Mac they were imported on.

### When This Mac Can’t Reach the Destination

A project organizes into one destination, on every Mac that shares it, and it belongs to the Mac that set it: the Mac that started the project, until one changes it. A destination on a network share is found on each Mac however the share is mounted there, such as “Media-1” beside an older “Media”: a dash and one or two digits is how macOS numbers a second mount of a share, so a share called “Studio-2024” is a name of its own. When this Mac can’t reach the destination, because it is on another Mac’s own disk or on a share or drive that isn’t connected here, Organize Media copies nothing and never asks for another folder in its place. A folder on another Mac’s own disk, or on a drive connected to it, is that Mac’s even when a folder at the same place is on this Mac: they are different disks, and organizing here would split the project’s media. Two accounts on the same Mac share its disk. MediaFlow knows which Mac set the destination when the project was started, or its destination chosen, in this version; for an older project it doesn’t, and a folder that is at the destination’s place on this Mac is organized into, as before. MediaFlow says whose destination it is and where, for example “This project organizes into “Beach Day” in Downloads on Studio MacBook Pro, which this Mac can’t reach.”, and offers:

- Connect to the share — when the destination is on the network share chosen in Settings › Network and it isn’t connected. Once it is, Organize Media carries on. Another share is connected in the Finder
- Change Project Destination… — choose a folder every Mac reaches, such as one on a network share. When another Mac set the destination, MediaFlow first asks whether to replace it and names that Mac. Clips already organized follow when they are found at the new place, as described in Change destination folder
- Cancel — and organize on the Mac that has the destination

Free Up Space, Restore from Cleanup and Re-file folders by category say the same. The re-filing that follows a category change is left out on a Mac that can’t reach the destination, because the organized files are where this Mac can’t move them; a notice says so once for each project each time MediaFlow is opened, and names the menu item to use on the Mac that has them.

Clips organized while the share was mounted under another name, such as “Media-1”, keep that name in where their files are. Once the share is back under its own name they read Missing until you point them at their files with Workflow → Repair → Relink Missing Media….

If the clips came from a memory card, the Clear Card review opens when you click Done. Nothing is deleted unless you confirm it there.

### How copies are verified

MediaFlow computes a SHA-256 checksum of each source file as it copies it, then finishes writing the copy to the disk. By default it then reads the whole copy back and compares its SHA-256 with the source. If the check fails, the copy is deleted and made again once; if it fails a second time, that clip is reported as failed and its source is left alone.

On a drive connected to your Mac, the copy is written and read back without passing through the Mac’s memory, so the check reads it from the drive itself. On a network share, every byte is read back over the network from the server; the server may answer from its own memory.

Drives keep a little memory of their own for what is being written. Once the last file is copied, MediaFlow asks the destination drive to empty it, once for the whole run rather than after every file, and only then points your clips at the copies. Move Project, Move to Editing Drive, Return to Library, Archive, Restore and Duplicate Project do the same before they point anything at their copies or remove anything, and an archive has the drive confirm it is in place under its own name, before any older one it replaces is removed. If the drive cannot be asked, because MediaFlow is not allowed to open the folder for example, the operation says so instead of carrying on as if it had been; after Organize, the card is then not offered for clearing. Clear Card, however you open it, asks the drive again for each organized copy just before it deletes that clip from the card, and keeps the card file if it cannot.

Shortcuts inside a project folder, such as those every Final Cut Pro library keeps to its cache and its media, are copied as shortcuts by Move Project, Move to Editing Drive, Return to Library, Archive and Restore, never as copies of what they point to. One that points inside the project follows it: in the copy it points to the same file in the copy, so Final Cut finds its media wherever the project now is, and it must lead to that file before the copy counts. On archive drives it points to where its file was archived, and after a restore, into the restored project, even from an archive made by an earlier version. A shortcut counts as pointing inside the project however its path is written: in other letter case where the drive ignores case, with doubled slashes, through the disk’s other name for a folder, or, for a project on a network share that macOS has mounted again with a dash and a number added to its name (Footage-1 for Footage), one written for the share’s other name when the project has the file it names. Two shares that both carry a number (Footage-1 and Footage-2) are different drives, and a shortcut from one to the other is kept as it is. One that points anywhere else, even to a drive that is not connected, is copied as it is and does not stop the copy. Each counts as nothing in the sizes shown and in an archive’s plan for its drives. MediaFlow looks at each item itself to tell a shortcut from a file, because some network storage lists shortcuts as ordinary files. Duplicate Project copies each clip’s own footage, even for a clip that is a shortcut, so the duplicate never depends on the original’s files.

Settings › Storage › Organize Media has the switch “Verify organized copies by reading them back (slower, safest)”. With it off, MediaFlow checks the size of the copy plus three 1 MB samples at the start, middle and end. That is much faster over a network, but it does not detect corruption outside the sampled ranges.

The checksum is recorded with the clip. Clear Card relies on it later, so leave read-back verification on if you plan to clear cards.

### Organizing again over existing files

If a file with the same name and the same size is already in the target folder, MediaFlow uses it instead of copying again. That file is not read and no checksum is recorded for it, so Clear Card later lists the clip as “Organized, unverifiable”. If a file with the same name has a different size, the new copy is saved with a number added to its name, for example Clip_1.mp4.

### Default destination

Settings › Storage › Organize Media › “Default destination for new projects” fills in the destination for a project that has none. A project’s own destination always wins once it has one.

### Keeping the folder layout in sync

When you change the category or the camera of an organized clip, MediaFlow moves its copy at the destination into the matching folder. This happens in the background, keeps any edit you make meanwhile, and only interrupts you if a file fails to move or you open another project before the move could be saved. While any of these moves is still running, even when a later one has finished, MediaFlow holds back its automatic check of where your clips are, so a clip caught between two folders is not marked Missing. To bring the whole project into line at once, for example after an interrupted move or a relink, choose Workflow → Repair → Re-file folders by category.

### Cancelling a long operation

Every long file operation (organize, import, project move, cleanup move and restore, relink, re-file and archive) has a Cancel button on its progress window. Cancelling stops the work between files. The file being written at that moment is discarded, so no half-copied file is left behind. Every file that finished before you cancelled stays where it landed; nothing already copied, moved or deleted is put back. The window then reports what did finish, for example “Cancelled after 12 of 40 files, 6.2 GB copied”, and waits for you to click Done. Cancel stops the work its own window shows and nothing else: clips being moved into their category folders in the background after a category change carry on.

Importing, Organize and Relink have progress windows of their own. Every other long operation’s window says in its title how it ended: Complete; Cancelled; Finished with Problems, when some items failed, which are listed below; or Didn’t Finish, when it stopped before doing what it was asked. The summary says what state things are in, for example that the original is unchanged and the part-made copy was removed.

> **Tip:** Clips in the Skip (don’t copy) category are never copied. The category is stored as “Do Not Copy” in the .vpm file and the database; only the label changed.

Organize is part of the Studio plan; see Plans and Pricing.

See also: [Change destination folder](#change-destination-folder), [Re-check files](#re-check-files), [Freeing Up Space](#freeing-up-space), [Clear Card](#clear-card)

## Change destination folder

*Point the project at a different destination folder, and follow organized clips that have moved there. No files are copied or moved.*

The project destination is where Organize Media copies clips. It is shown under the project name in the sidebar. Hover over it for the full path; “Not set” appears in orange when there is none. The destination is first chosen when the project is created — see Creating a New Project.

1. Click Change… next to the destination in the sidebar, or choose Workflow → Repair → Change destination folder…
2. Choose the new folder
3. MediaFlow saves the new destination in the project and reports “Destination location updated.”

Changing the destination never copies, moves or deletes a file. On its own it changes only where new organizing goes; clips you organized earlier still point at the files in the old folder unless you accept the offer described next.

The destination is the project’s, for every Mac that shares it, and belongs to the Mac that set it. When another Mac set it, MediaFlow asks first whether to replace it and names that Mac; the folder you choose then becomes the destination on every Mac, that one included, and belongs to this Mac. When this Mac can’t reach the destination, Organize Media offers the same change as Change Project Destination…; see When This Mac Can’t Reach the Destination in Organizing Media to Storage.

### If you moved your organized media

When the media itself has moved, for example to a new drive or because a share now mounts under a different path, the clips still point at the old paths and read Missing. After you change the destination, MediaFlow looks for each organized clip in the new destination, in the same folder it had under the old one and with the same size. If it finds any, it asks whether to point the project at them, and tells you how many it found out of how many were organized.

Same folder and same size is not proof that a file is the one you organized: cameras that split long recordings into chapters produce files of exactly the same size. So a clip that has a checksum recorded from when it was organized is read in full, and followed only if its contents are identical. The question tells you how much data that is before you agree. Over a network it can take a while. You can stop the check: clips already checked stay pointed at the new destination, and choosing Change destination folder again with the same folder continues with the rest. Clips with no recorded checksum are followed on folder and size alone.

When it finishes, MediaFlow lists any clip that was in the right place but whose contents differ from what was organized, or that could not be read. Those are left as they were.

1. Change the destination folder to the new location, as above, and answer Point at New Destination when asked
2. For clips it did not find, choose Workflow → Repair → Relink Missing Media… and show MediaFlow where they went
3. Choose Workflow → Repair → Re-check files and confirm in the Where column that nothing still reads Missing

The offer is not made when the new destination is the old one, or when one is inside the other; that is not a move MediaFlow can follow by folder.

See also: [Organizing Media to Storage](#organizing-media-to-storage), [Re-check files](#re-check-files), [Relinking Missing Media](#relinking-missing-media)

## Re-check files

*Look at every clip’s file on disk again and update the Where column for the whole project.*

Re-check files brings the Where column back in step with what is really on disk. Choose Workflow → Repair → Re-check files.

### What it checks

- Whether each clip’s file exists at its recorded path
- For a file inside the project destination, whether its size still equals the size recorded at import
- Files in the working folder, on a card or in a source folder are checked for existence only

It does not read file contents or recompute checksums, so it cannot detect damage that leaves the size unchanged.

### What the Where column shows afterwards

- At destination — the file is inside the project destination and its size matches
- Size mismatch — the file is inside the destination but its size differs from the recorded size
- On this Mac — the file is in the working folder and has not been organized
- Only on card — the file is on a camera card and has not been copied to the destination
- Not at destination — the file is somewhere other than the destination and not on a card, such as the folder you imported from or another drive. It is not lost; hover over it to see which drive. If a whole project reads this way after a library was moved, you may have opened the old copy of the project: see After Moving Your Library to a New Drive
- Missing — no file was found at the recorded path
- Volume not connected — the drive or share the path names is not mounted right now. The file is neither checked nor called missing; its last known state stands until the drive is back
- On another Mac — the file is in the home folder of another account, where a clip imported on another Mac that shares this project is usually kept. This Mac cannot see it, so it is not called missing and nothing is changed for it. The Mac it was imported on keeps it up to date
- Not on this Mac — the file is not where the project says, and this Mac has never had it. It was most likely imported on another Mac that shares this project and kept somewhere this Mac cannot see, such as that Mac’s Shared folder or its own drive. It is not called missing and nothing is changed for it. The Mac that has it keeps it up to date

Each Mac remembers the clips it has had: the ones it imported, organized, relinked, reconnected or moved, and every file Re-check files has found on it. Only those can read Missing on that Mac when their file goes. So a clip imported on another Mac does not read Missing here, even when both Macs’ accounts share a name or the clip is kept in the Shared folder, and the two Macs stop changing it back and forth.

The first time a Mac checks a project file after the update, it checks it as before: every clip whose file is gone reads Missing, including one that went missing before the update, and one on another Mac. The same goes for the first check of any other copy of the project file, such as one made with Save As, copied in the Finder or restored from a backup. Once that first check is saved in the file, the Mac remembers what it found; if it cannot be saved, because the app quits first or the folder cannot be written to, the next check is a first check again. On a project shared with another Mac, that Mac’s clips may read Missing once; the next time the other Mac checks them, it finds them and puts them right, and they read Not on this Mac here after that.

If that memory cannot be read or kept, which is rare, the Mac puts it aside and checks as before, so every clip whose file is gone reads Missing.

Re-check files only looks at recorded paths. It does not search for files that have moved; use Workflow → Repair → Relink Missing Media… for that.

A clip whose file is being moved into its category folder at that moment, after a category change, is left to the move: its file has already left the recorded path, and the move records where it went. The clip is looked at again once the move is done. Anything else you change while the check runs, including the category itself, is kept.

> **Tip:** Run this after reconnecting a drive or moving files by hand, or when the Where column does not match what you expect.

See also: [Organizing Media to Storage](#organizing-media-to-storage), [Relinking Missing Media](#relinking-missing-media), [Understanding the Where Column](#understanding-the-where-column)

## Freeing Up Space

*Free Up Space lists every file before it stages or deletes anything. Know what it checks before you confirm.*

After you organize, the imported copies are still in the working folder (Documents → MediaFlow Projects → Imports), and the originals are usually still on the card or in the folder you imported from. Free Up Space reclaims that space in two stages: first it moves files into a Cleanup folder, and only later, when you choose, does it delete them.

### Free Up Space

Workflow → Free Up Space… scans the open project and lists three groups. Each has a file count, a total size and an expandable list of the exact files it would touch.

- “Local import copies that have an organized copy” — working-directory copies of clips that have been organized. Checked by default. Moved to Cleanup.
- “Files still on the card or source folder” — the originals on the card or in the import folder. Unchecked by default. Moved to Cleanup.
- “Staged in Cleanup” — files an earlier run already moved into Cleanup. This is the only group that deletes anything.

A running “Reclaim” total follows your checkboxes, and one red button applies the selection. When you confirm, MediaFlow acts only on files the sheet listed. A listed file that no longer qualifies is skipped; nothing new is added.

### What is checked before a file is moved

Two checks, at two moments. A quick one decides what the sheet lists; a thorough one runs on each file just before it is moved.

- To be listed, a file needs an organized copy at the destination that is exactly the same size. That applies to local copies and to card or source-folder originals alike. The sheet says how many local copies were kept back because the organized copy is missing or a different size.
- Before a listed file is moved, MediaFlow reads both it and the organized copy in full and compares their SHA-256. They must match each other, and match the checksum recorded when the clip was organized, if there is one.
- A file that cannot be proven is left exactly where it is. The summary lists each one with the reason: the organized copy could not be reached, the two do not match byte for byte, or the file has changed since it was organized.
- A file is never compared with itself. If the “local copy” and the organized copy turn out to be one file under two names, it is kept.

Reading the organized copy takes time, more so over a network: expect roughly as long as organizing the same clips took. The progress window shows “Checking and moving” and can be cancelled between files.

### Staging and deleting

The first two groups are moved into a Cleanup → &lt;Project Name> folder on the destination volume. They are not deleted, and Restore from Cleanup can bring them back.

The third group is deleted. Selecting it adds a confirmation that restates the file count, the total size and the file types, warns when the volume is a network drive with no Trash to recover from, and has a checkbox you must tick before the delete button enables.

Before MediaFlow deletes a staged file, it checks it again, the same way: a clip in this project must have an organized copy that matches it byte for byte, read at that moment. A staged file whose organized copy is missing, damaged or a different size is kept, and so is any file in the Cleanup folder that does not belong to a clip in the project — delete those in the Finder if you are sure.

> **Warning:** Deleting the staged group removes the files permanently. They are not moved to the Trash.

### Restore from Cleanup

Workflow → Restore from Cleanup, also a link inside the Free Up Space sheet, moves staged files back where they came from: the working folder, or the card or source path for files staged from there. Projects staged by earlier versions, in folders named by project ID, are still recognized. Files you deleted from the staged group cannot be restored.

A file goes back only to a place this Mac has had it. When two Macs share a project, a working copy staged on the other Mac stays in Cleanup, and the summary says so: restore it on that Mac. Otherwise, with two accounts of the same name, it would land in your home folder on the wrong Mac.

### Re-file folders by category

Workflow → Repair → Re-file folders by category (called Sync Folder Layout in earlier versions) moves every organized file at the destination into the folder that matches its current category and camera. Single edits re-file themselves in the background, so you need this only to catch up after an interrupted move or a relink.

### The End of Day Wrap template

The End of Day Wrap workflow template has a cleanup step that does not open the Free Up Space sheet. It stages local copies only, using the same check as the first group. It never touches card originals and never deletes.

### Cancelling a cleanup run

The Cancel button on the progress window stops a move, a restore, a delete or a re-file between files. Files already staged stay in the Cleanup folder, files already restored stay where they were put back, and anything already deleted is gone. The remaining files are untouched, so you can run the same command again later to finish.

See also: [Organizing Media to Storage](#organizing-media-to-storage), [Re-check files](#re-check-files), [Clear Card](#clear-card), [Workflow Templates](#workflow-templates)

## Clear Card

*Delete clips from a memory card only after each one is organized and the card file matches its recorded checksum.*

Clear Card empties a memory card safely. It lists every clip on the card, works out which ones already have an organized copy it can vouch for, and lets you delete only those. Clearing is always a separate, deliberate step from importing.

### Opening it

- File → Clear Card…, which has one item for each connected card
- The Clear Card button in the Import sheet, shown when the folder you chose is on a removable card
- After Organize Media: when the sources came from a card, the Clear Card review opens as soon as you click Done on the progress window. Nothing is deleted until you review and confirm

### What it looks at

Only the card’s DCIM folder is scanned. Nothing else on the card is read or touched. Each file is matched to a clip by the path it was imported from, or by filename and size when the card has mounted under a different name.

With the central database connected, files are matched against the clips of every project. Without it, only the open project is searched, so clips that belong to other projects read “Not imported” and are kept.

### The five states

- “Verified at destination” — the clip is organized, a checksum was recorded, the organized copy is present and the same size, and the card file passed the check below. The only state that can be deleted; it is checked for you.
- “Organized, unverifiable” — organized, but the destination is not reachable, the clip is Missing, or no checksum was recorded. Kept.
- “Imported only” — imported into a project but not organized yet. Kept.
- “Not imported” — no project knows about this file. Kept.
- “Mismatch” — a size or the checksum disagrees with the recorded clip. Kept.

Every kept row is locked, with the reason shown next to it. There is no select-all and no override.

### What “verified” proves

The Check menu chooses between two modes.

- Verified (full SHA-256), the default — reads each card file in full and compares its checksum with the checksum recorded when the clip was organized. It also checks that the organized copy is still present and is the same size as the card file.
- Standard (path and size) — matches on the import path and the size only. It is much faster but never reads the card file, and it will not act on a card that mounted under a different name.

Neither mode reads the organized copy again. The recorded checksum is the checksum of the source file at organize time. With read-back verification on (the default in Settings › Storage), the organized copy was proven identical to it when it was made. With read-back verification off, the organized copy was checked only by size and sampled ranges, so a Verified result shows that the card file is unchanged and the organized copy is the right size, not that every byte of the copy is intact.

### GoPro naming

A .MP4 owns the .LRV proxy and .THM thumbnail that share its name; they are listed and deleted with it. Chaptered recordings (GX010123, GX020123) are separate clips and are verified separately, so a verified chapter never takes an unverified one with it.

### Deleting

1. Review the list. Click Rescan if you have connected the destination or organized more clips since the scan
2. Click the red Delete button. A confirmation restates the clip count, the file count, the total size and the file types, and has a checkbox you must tick before it enables
3. MediaFlow checks again that each file is inside the card’s DCIM folder immediately before deleting it, and asks the drive holding its organized copy to finish writing it. A clip whose copy’s drive cannot be asked is kept, and the reason is listed
4. When it finishes, click Eject to eject the card, or Done

A list of everything that was removed is written to the card’s MISC folder as cleared-files-&lt;date and time>.txt. Each cleared clip is also marked in the project so the Import sheet does not offer it again. Emptied folders such as 100GOPRO are left on the card on purpose.

> **Warning:** A memory card has no Trash. Cleared files are erased at once and cannot be recovered. Clear Card will not run while an import, organize, archive, relink or the Proxy queue is running, and it refuses a card that is mounted read-only.

See also: [Freeing Up Space](#freeing-up-space), [Organizing Media to Storage](#organizing-media-to-storage), [The Import Sheet and Completion Card](#the-import-sheet-and-completion-card)

## Proposals: What Import Analysis Suggests

*After an import, MediaFlow proposes a category, camera and scene for each clip; nothing is applied until you accept it.*

When an import finishes copying, MediaFlow examines each new clip and proposes a category, a camera, a scene and a reject flag. A proposal is a suggestion only. It appears in italic grey in the Category or Camera column with a High, Medium or Low badge, and the clip keeps its real category until you accept. Organize never applies a proposal; its confirmation sheet warns you when clips still carry one.

The switch is Settings › Analysis › “Propose category, camera and scene after an import”. It is on by default. This pass runs on this Mac, four clips at a time at low priority.

### The three passes

- The basic pass — always runs when proposals are on. It reads facts from the file: frame rate, length, camera make, audio level and one sampled frame
- Tier 1 — optional, off by default. Looks at the pictures and listens to the start of the clip
- A model — optional, off by default, and chosen for each import. Shows three frames to a model on this Mac or to a paid provider

A later pass refines the proposal. It never lowers a confidence you have already seen and never overrides a fact read from the file.

### Accepting

- Click an italic proposal to accept it for that clip. Hover over it to see what is proposed and, after Tier 1, the evidence
- Accept all High-confidence (n) in the selection bar accepts every High proposal in the project
- Accept selected proposals (n) accepts the proposals on the selected clips, whatever their confidence
- In Workflow → Review, A accepts the proposal on the clip in front of you and R marks it a reject candidate

Accepting works like choosing the value yourself: it can be undone, and an organized copy is re-filed.

### Rejecting

Choose a different category yourself. The proposal disappears, and a category you have set is never proposed over again.

### How your answers improve later suggestions

- Category Learning, on this Mac — every category you assign is remembered by camera and clip length. Settings › Categories shows the totals, and Reset Pattern Memory clears them
- Shared corrections, in the shared database — each proposal you confirm or correct is recorded for every Mac on that database. Later proposals for similar clips follow what you actually chose, and a category reads High only where you have nearly always agreed. Reset Pattern Memory does not clear these

See also: [Clip Classifier, Second Pass (Tier 1)](#clip-classifier-second-pass-tier-1), [Using a Model to Suggest Categories](#using-a-model-to-suggest-categories), [Auto-Suggest Categories](#auto-suggest-categories), [What Happens to Files When You Change a Category](#what-happens-to-files-when-you-change-a-category), [Reviewing Clips with the Keyboard](#reviewing-clips-with-the-keyboard)

## Using a Model to Suggest Categories

*An optional model can refine category proposals; it runs only when enabled in Settings and ticked for that import.*

A vision model can look at three frames from each clip and pick one of your project’s own categories. It refines the proposals import analysis already makes. Its answers are proposals like any other: shown for review, never applied by themselves.

It is off unless you do two things: turn on “Use a model to suggest categories” in Settings › Analysis, and tick “Ask a model to suggest categories” in the Import sheet for that import. The checkbox always starts unticked and applies to that import only.

### Which model

- On this Mac — free and private. Frames never leave this Mac. Slow: about a minute a clip, in the background
- Claude, ChatGPT or Gemini — answers in a second or two and costs money for every clip

> **Warning:** With a paid provider, MediaFlow sends three small frames from each clip to that company, with a line of clip details, the opening words of any speech, your category names and a few examples of how you labeled similar clips. The provider bills you per clip, separately from any subscription you already pay for. On Google’s free tier, your footage is used to train Google’s models; enable billing on your Google account to avoid that.

### Setting up a paid provider

1. In Settings › Analysis, turn on “Use a model to suggest categories”
2. Choose the provider under Model runs, then a Model. A note under the picker describes each one
3. Create an API key using the link shown, paste it into API key and click Save
4. Set “Stop after” to the most you are willing to spend in a day

### The daily limit

The limit is checked before every clip, so it is never exceeded. It starts at $1.00 a day. When it is reached the pass stops; clips it did not reach keep the proposal they had. The line below shows clips and spending today, and Reset sets it back to zero. The amounts are MediaFlow’s estimates; your provider’s bill is the final word.

### API keys

Keys are kept in your Keychain, never in preferences or the saved setup. Settings shows a masked key with Replace… and Remove.

### If the checkbox is missing or dimmed

- Missing — the switch in Settings › Analysis is off, or the paid provider you chose has no API key yet
- Greyed out — “Propose category, camera and scene after an import” is off, so there is nothing for a model to refine

Turning the Settings switch off stops a pass that is running.

See also: [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [Running a Model on This Mac](#running-a-model-on-this-mac), [Proposals: What Import Analysis Suggests](#proposals-what-import-analysis-suggests), [Clip Classifier, Second Pass (Tier 1)](#clip-classifier-second-pass-tier-1), [Saved Setup: A Copy of Your Settings](#saved-setup-a-copy-of-your-settings)

## Running a Model on This Mac

*Set up a free, private vision model on this Mac with Ollama; nothing you import leaves the machine.*

The Server address may be this Mac or another computer on your own network. An address on the internet is refused, so a local model never sends frames outside your network.

A local model suggests categories without sending anything anywhere and without costing anything. The price is time: about a minute a clip, in the background after the copy. Choose it when privacy matters more than speed. If this Mac is short of memory, a paid provider may suit it better.

MediaFlow talks to a model server running on this Mac. The setup assistant in Settings › Analysis works with Ollama. MediaFlow does not install Ollama for you; the download comes from ollama.com. Once it is installed, everything else happens in Settings.

### Set it up

1. In Settings › Analysis, turn on “Use a model to suggest categories” and set Model runs to On this Mac
2. Click Download Ollama… and install it, or click Copy Homebrew command and run it in Terminal. Then click Check again
3. If Ollama is installed but not running, click Start Ollama. It takes about fifteen seconds
4. Pick a model from the suggestions and click Download. This is a one-time download of several gigabytes
5. Click Run the check. MediaFlow asks the model one question to confirm it can answer in the format it needs
6. When the assistant reads “Ready”, tick “Ask a model to suggest categories” in the Import sheet for an import you want it to look at

### Choosing a model

The suggestions are sized to this Mac’s memory. The default is comfortable with 16 GB of memory or more; the larger ones judge better and want 24 GB or 32 GB. Each line shows the download size.

### If the check fails

Models below about 8 billion parameters usually cannot hold a structured answer. Click Download a different model and try a larger one.

### Using another server

Any server that speaks the same protocol works, such as LM Studio. Enter its address in Server and the model’s name in Model. Ollama is on port 11434 and LM Studio on 1234.

See also: [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [Using a Model to Suggest Categories](#using-a-model-to-suggest-categories), [Proposals: What Import Analysis Suggests](#proposals-what-import-analysis-suggests), [Clip Classifier, Second Pass (Tier 1)](#clip-classifier-second-pass-tier-1)

## How MediaFlow Verifies Copies

*What MediaFlow checks, and when, before it treats an organized copy as safe and lets an original be removed.*

MediaFlow checks your files at three moments: when Organize copies a clip, when Clear Card offers to delete it from the card, and when Free Up Space offers to move originals aside. The checks are not equally strong. This topic says exactly what each one proves.

The short version: leave “Verify organized copies by reading them back” on, and empty cards with Clear Card in Verified mode. Together they prove the organized copy matched the original byte for byte when it was made, and that the file you are deleting is that original.

### Organize

As MediaFlow copies a clip it computes a checksum of the original (SHA-256, a fingerprint of the file’s contents). It finishes writing the copy to the destination before it checks it. The setting is in Settings › Storage.

- On (the default; slower, safest) — the copy is read back in full from the destination. Its size and its SHA-256 must both match the original
- Off — the copy is checked by size, plus a comparison of 1 MB samples at the start, middle and end. Much faster over a network. Damage outside the sampled ranges is not detected

If the check fails, the copy is deleted and made again once. A second failure fails that clip and is reported. The original’s checksum is recorded on the clip; Clear Card relies on it later.

One exception: if a file with the same name and the same size is already at the destination, Organize reuses it. It is not copied, not read, and no checksum is recorded for it.

### Read from the drive, not from memory

Every check in this topic reads with the Mac’s file cache turned off, and every copy MediaFlow checks afterwards (Organize, Move Project, Move to Editing Drive and Return to Library, Archive, Restore, Duplicate Project) is written that way too. So on a drive connected to your Mac, the read-back of a copy reads it from the drive itself, not from the memory the copy was just written from, and a fault on the way to the drive is caught rather than read past. On a network share, every byte is read back over the network from the server. Two limits: a file the Mac already holds in memory for another reason can still be read from there, such as a clip you just played, or a card file Organize has just read (so Clear Card’s check of the card, right after organizing, may come from memory; the organized copy itself was read back from its drive when it was made); and a network share’s server may answer from its own memory, which MediaFlow cannot see past.

### Clear Card

Only files in the state “Verified at destination” can be deleted, and there is no override. In both modes of the Check picker, the clip must have a recorded checksum, and its organized copy must be reachable now and be exactly the size of the card file.

- Verified (full SHA-256), the default — also reads every card file in full and compares its SHA-256 with the recorded checksum. This proves the card file is the file that was organized
- Standard (path and size) — matches the card file to the clip by its original path and size. Fast, but it never reads the bytes. A file matched only by name and size is kept

Neither mode reads the organized copy again; it is checked for presence and size only. So Clear Card is as strong as the check made at organize time. With read-back on, the copy was proven identical then. With read-back off, only its size and three samples were.

### Free Up Space

This is the step that removes your other copies, so it is the strictest. Files are moved to a Cleanup folder first and deleted only in a separate, confirmed step — and both steps prove the file first.

- To be listed at all, a file needs an organized copy of exactly the same size
- Before a file is moved, it and the organized copy are both read in full and their SHA-256 compared. They must match each other and the checksum recorded at organize time
- Before a staged file is deleted for good, the same comparison is made again, against the organized copy as it is at that moment
- Whatever cannot be proven is kept, with the reason

Unlike Clear Card, this always reads the organized copy again. The checksum recorded at organize time is the checksum of the original; it says the local copy has not changed, not that the copy at the destination is whole. Reading it is the only way to know, which is why Free Up Space takes about as long as organizing did.

See also: [Organizing Media to Storage](#organizing-media-to-storage), [Clear Card](#clear-card), [Freeing Up Space](#freeing-up-space), [The Settings Window, Tab by Tab](#the-settings-window-tab-by-tab)

## Format Conformance Checker

*Find clips whose frame rate, resolution or codec differs from the rest of the project before they cause trouble in your editor.*

The Format Conformance Checker analyzes all video clips in your project and flags format inconsistencies that could cause issues when editing in Final Cut Pro, DaVinci Resolve, or other NLEs.

### How to Use

1. Open your project with imported video clips
2. Go to Workflow → Analyze… → Format
3. Click Run Analysis
4. Review the report showing your project baseline and any detected issues
5. Click "Select Affected Clips" to highlight problem clips in the media list

### Severity Levels

- Critical (red) — Mixed frame rates: causes stuttering and dropped frames on timelines
- Warning (orange) — Mixed resolutions: clips will be scaled, may lose sharpness
- Info (blue) — Mixed codecs: may impact playback performance but generally manageable
- Info (blue) — Missing metadata: run metadata extraction to populate technical fields

### Project Baseline

The checker determines your project’s dominant resolution, frame rate, and codec (the most common values). Clips that differ from the baseline are flagged as potential issues.

> **Tip:** Run this check before exporting to an NLE to catch format mismatches early. It’s much easier to transcode a few clips now than troubleshoot timeline issues later.

Mixed frame rates are the most impactful issue — a 30fps clip on a 24fps timeline will stutter visibly. Always prioritize resolving critical issues first.

See also: [Organizing Media to Storage](#organizing-media-to-storage), [Generating Reports](#generating-reports), [Transcode](#transcode)

## Workflow Templates

*Run a fixed series of operations in order with one command: organize, end-of-day wrap, or relink and repair. Each step finishes before the next begins.*

A workflow template runs several operations in order, so you do not have to find each command yourself. Each step is the same operation you would start from the menu, with the same confirmations and the same progress window, and the template waits for it to finish before it starts the next.

### How to Use

`Cmd+Shift+R` — Open Workflow Template Picker

Choose Workflow → Run Workflow Template, select a template, then click Run. When a step needs you — to confirm a copy, choose a folder, or read a result — the template’s own window steps aside and the step’s windows appear as usual. Nothing is copied, moved or deleted until you confirm it there. When you close the step’s last window, the template comes back with what the step did and carries on. The command is unavailable while a template is running.

### Built-in Templates

- One-click Organize — Re-check files, check format conformance, organize all media, then show a summary. Organize here always means the whole project, whatever is selected. This copies to the project’s destination; Archive to USB is a separate command
- End of Day Wrap — Re-check files, generate a report, open Free Up Space, then show a summary. Free Up Space shows its usual preview: nothing is staged or deleted that you have not seen listed and confirmed
- Relink & Repair — Re-check files, relink missing media, re-file folders by category, then show a summary

### When a step does not finish

- A step that fails stops the template. The summary says which step, why, and that the remaining steps were not run. This is deliberate: Free Up Space should never follow an Organize that failed
- If you back out of an optional step, for example by cancelling the report’s save panel, that step is marked skipped and the template carries on
- If you back out of a step the template depends on, the template stops there

### Controls During Execution

- Pause/Resume — Hold the template between steps without losing progress
- Skip Step — Skip the current step if it’s marked as optional (shown with an "optional" badge)
- Cancel Workflow — Stops the template; the remaining steps are marked as skipped. To stop a copy or a scan that is already running, use Cancel on that operation’s own progress window

### Summary Report

When the template ends, a summary shows each step with a checkmark, a skip mark or an error, and the header shows the elapsed time. Each line reports what actually happened, taken from the operation itself: how many clips were organized and how many were not, what Free Up Space moved or deleted, how many missing clips were relinked.

> **Tip:** Optional steps (like Format Check in One-click Organize) can be skipped to speed up the workflow when you know your formats are consistent.

See also: [Organizing Media to Storage](#organizing-media-to-storage), [Format Conformance Checker](#format-conformance-checker), [Re-check files](#re-check-files)

## GPS Scene Detection

*Group clips into suggested scenes by where they were shot, then accept, rename or reject each suggestion.*

Place names are looked up only if you turn that on in Settings › Privacy, and the small maps only if Maps is on; otherwise each scene shows its coordinates.

GPS Scene Detection analyzes the geographic coordinates embedded in your clips to suggest logical scene groupings. Clips shot near the same location are clustered together and presented as scene suggestions you can accept, rename, or reject.

### How to Use

1. Open a project with media with GPS data (phone and drone footage typically has GPS data)
2. Choose Workflow → Analyze… → GPS Scenes and click Run. MediaFlow analyzes at once with the radius and time gap you last used
3. Review each suggestion: accept, reject, or rename the scene
4. To try a different radius or time gap, click Re-analyze, change the settings and click Analyze
5. Click the Apply button to give the accepted clusters their scene names. The button says how many scenes it will apply, and appears once you have accepted at least one

### Clustering Radius

- 25m (Tight) — Indoor or single-setup scenes
- 50m (Normal) — One building or city block
- 100m (Wide) — Park, beach, or open area
- 250m (Very Wide) — Large venue or neighborhood

### Time Gap Threshold

Even if clips are at the same GPS location, a large time gap between them may indicate a different scene. For example, morning and afternoon shoots at the same beach are likely separate scenes. Set the time gap to split same-location clusters that are separated by more than the threshold.

- Disabled — Location only, ignore time
- 1–8 hours — Clips at the same spot separated by more than this form separate scenes

### Review Interface

Each suggestion shows a mini map pin, the suggested scene name (editable), clip count, time span, and sample filenames. Use the checkmark to accept or the X to reject. You can accept or reject all at once with the bulk buttons.

> **Tip:** Run Place names first (Workflow → Analyze… → Place names, once called Geocode Locations) so clips have readable place names. GPS Scenes works with raw coordinates too, but named places make the suggestions much easier to review.

Only clips with GPS metadata are analyzed. Clips without it are skipped, and so are clips that already have a scene.

See also: [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [NLE Template Export](#nle-template-export), [Logging Scene, Shot and Take](#logging-scene-shot-and-take)

## Sun Position & Shadow Continuity

*Calculate sun position for clips with GPS data and detect shadow continuity issues across takes.*

Sun Position Analysis calculates the solar azimuth (compass direction) and elevation for every clip with GPS data using the Meeus astronomical algorithm. It then checks for shadow continuity problems where takes of the same scene were shot at different times of day, causing mismatched shadow directions that would be visible when edited together.

### How to Use

1. Open a project with media with GPS data that has timestamps
2. Choose Workflow → Analyze… → Sun
3. Review the analysis results: sun position per clip, golden hour clips, and continuity warnings

### What Gets Calculated

- Azimuth — Compass direction of the sun (0° = North, 90° = East, 180° = South, 270° = West)
- Elevation — Angle above the horizon (negative values mean the sun is below the horizon)
- Lighting Condition — Daylight (>6°), Golden Hour (0°–6°), Blue Hour (-6°–0°), Twilight (-12°–-6°), or Night (&lt;-12°)

### Shadow Continuity Warnings

When two clips in the same Scene Log scene have sun azimuths more than 30° apart, MediaFlow raises a warning. Clips with no scene produce none. Warnings are rated by severity:

- Minor (30°–45°) — Subtle shadow shift, may not be noticeable
- Moderate (45°–90°) — Noticeable shadow direction change between takes
- Severe (>90°) — Major shadow reversal, very visible in edited sequence

> **Tip:** Golden hour footage has a distinctive warm quality. Use the lighting condition badges to find your golden hour and blue hour clips for color grading.

Sun position requires both GPS coordinates and accurate timestamps. Clips without location data are skipped.

See also: [NLE Template Export](#nle-template-export), [Logging Scene, Shot and Take](#logging-scene-shot-and-take)

## Interactive Shoot Map

*View shooting locations on an interactive map with clip clustering.*

The map itself is off until you turn on Maps in Settings › Privacy, or with the Turn On Maps button: showing a map sends the area you are looking at to Apple. Until then the locations are counted without a map.

The Shoot Map displays all clips with GPS data on a map. Clips shot at the same place share one numbered pin. Click a pin to see its clips and select them in the media list.

### How to Open

`Cmd+Opt+M` — Open Shoot Map

Or choose Workflow → Plan & Deliver → Shoot Map from the menu bar.

### Map Features

- Cluster pins — Clips within 50m are grouped into numbered clusters
- Click a cluster — Highlights it in the sidebar with clip details
- Click a single pin — Selects the clip in the media list
- Select All in Browser — Selects all clips at a location for batch editing
- Map styles — Switch between Standard, Satellite, and Hybrid views

### Filters

- Category — Show only clips from a specific category (A-roll, B-roll, etc.)
- Rating — Filter to clips with a minimum star rating

### Sidebar

The sidebar lists all location clusters sorted by clip count. Each entry shows the place name, clip count, sample filenames, and category badges. Click a location to zoom the map to it.

> **Tip:** Use the Shoot Map alongside GPS Scene Detection to visually verify scene groupings before applying them.

See also: [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [GPS Scene Detection](#gps-scene-detection), [Historical Weather Lookup](#historical-weather-lookup), [Logging Scene, Shot and Take](#logging-scene-shot-and-take)

## Historical Weather Lookup

*Look up the weather at the place and time each clip with GPS data was shot and store it with the clip.*

Weather lookup is off until you turn it on in Settings › Privacy, because it sends each clip’s coordinates and date to Open-Meteo.

Weather Lookup retrieves historical weather conditions for every clip with GPS data from the free Open-Meteo service. It records temperature, sky conditions, wind, and humidity — the same information a script supervisor would note by hand for continuity.

### How to Use

1. Open a project with media with GPS data
2. Choose Workflow → Analyze… → Weather
3. Wait for the lookup to finish. It needs an internet connection. The progress HUD then reports how many clips had weather added

### Data Retrieved

- Sky condition — Clear, Partly Cloudy, Overcast, Rain, Snow, Fog, Thunderstorm, etc.
- Temperature
- Wind — Speed
- Humidity — Relative humidity percentage

### Where you see it

- In the metadata panel, select a clip and open the Weather section, below GPS & Location. The section header shows the conditions and temperature at a glance. Temperature and wind are shown in the units your region uses
- In the search field, type the conditions, for example rain or cloudy, to find the clips shot in them

Both follow the weather switch in Settings › Privacy. With it off, MediaFlow does not look weather up, and it does not show or search weather that an earlier lookup saved. Turn the switch back on and the saved weather reappears; nothing is deleted.

### Caching

Results are cached by location (to about 100 m) and hour, so clips shot at the same place within the same hour share one request. The cache lasts until you quit MediaFlow. The weather itself is saved with each clip in the project file.

> **Warning:** Weather Lookup sends data off this Mac. For each lookup it sends the clip’s coordinates, rounded to about 100 m, and the shooting date to the Open-Meteo service. No API key or account is needed.

See also: [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [NLE Template Export](#nle-template-export)

## Vision (AI Scene Analysis)

*Detect shot type, faces, indoor or outdoor, and on-screen text on this Mac, and suggest a category for each clip.*

Vision, once called AI Scene Analysis, uses Apple’s Vision framework to analyze your video clips. It detects shot types, counts faces, classifies indoor/outdoor scenes, and reads on-screen text — all on-device with zero API costs.

### How to Use

1. Open a project with video clips
2. Choose Workflow → Analyze… → Vision
3. Wait for analysis to complete (progress shown in the review sheet)
4. Review suggestions: accept individually or accept all uncategorized

### What Gets Detected

- Shot Type — Close-Up, Medium, Wide or Other, from how much of the frame the largest face fills; Establishing when there are no faces
- Face Count — Number of people/faces in the frame
- Face Position — Left, Center, or Right for composition analysis
- Indoor/Outdoor — Environment classification from scene content
- On-Screen Text — Detected text from clapperboards, signs, titles
- Category Suggestion — Interview, B-roll or Establishing Shot

### Accuracy

The category rules are simple. One or two faces with one of them centered suggests Interview. No faces suggests B-roll outdoors and Establishing Shot otherwise. Anything else, including three or more faces, suggests B-roll. These are suggestions; review them before you accept.

> **Tip:** Vision samples 5 representative frames per clip, not every frame. This keeps analysis fast while providing reliable results.

Vision runs entirely on this Mac. It needs no internet connection and no API key.

See also: [Auto-Suggest Categories](#auto-suggest-categories), [Smart Selects](#smart-selects)

## Speech Transcription

*Transcribe the speech in your video clips with Apple’s speech recognition; the text is saved with each clip.*

Speech is recognized on this Mac. Apple’s online recognition is used only if you turn it on in Settings › Privacy, and only for a language this Mac has no on-device model for.

Transcribe turns the speech in your video clips into text using Apple’s speech recognition. The text is saved with each clip in the project file, and import analysis uses it as one of its signals when it proposes a category. Audio-only files are not transcribed.

### How to Transcribe

1. Open a project with video clips that contain speech
2. Choose Workflow → Analyze… → Transcribe
3. Allow speech recognition if macOS asks
4. Wait for it to finish. The progress HUD reports how many clips were transcribed

To transcribe one clip, select it, open the Transcript tab of the metadata panel and click Transcribe This Clip.

### The Transcript tab

- Read — the clip’s lines in order, each with its time. Click a time to jump the preview to that line
- Search — type in the field to show only the lines containing every word you typed. Tick All clips to search every clip’s transcript instead; click a result to select that clip
- Correct — edit a line and press Return. The words change and the line’s timing stays as it was. Clear a line and press Return to remove it, for a cough or a false start the recognizer heard as a word
- Export — save the transcript as SubRip (.srt) or WebVTT (.vtt) subtitles, or as plain text with timecodes. The file is named after the clip
- Transcribe Again — replaces the transcript with a new one. Your corrections are replaced too

### Where the Audio Goes

MediaFlow recognizes speech on this Mac when the Mac has an on-device model for your system language. When it does not, nothing is transcribed unless you have turned on online speech recognition in Settings › Privacy; with that on, the audio is sent to Apple. The Transcript tab says which applies before you start. No API key is needed either way.

> **Tip:** Clear speech with little background noise gives the best results.

See also: [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [Clip Classifier, Second Pass (Tier 1)](#clip-classifier-second-pass-tier-1), [Proposals: What Import Analysis Suggests](#proposals-what-import-analysis-suggests)

## Smart Selects

*Score each clip for sharpness, exposure, audio and more on this Mac, and suggest a star rating you can accept.*

Smart Selects, once called AI Smart Selects, scores every clip on five measures and suggests a star rating. It runs on this Mac and needs no internet connection.

### Quality Dimensions

- Sharpness (30%) — Focus quality measured via Laplacian variance on a sample frame
- Exposure (25%) — Luminance histogram analysis detecting over/underexposure and clipping
- Audio (20%) — Audio level analysis checking for clipping, silence, or low levels
- Stability (15%) — A rough guess from the clip’s length and whether it has been logged with a scene. It does not measure camera shake
- Composition (10%) — Aspect ratio conformance and resolution scoring

### How to Use

1. Open a project with media clips
2. Choose Workflow → Analyze… → Smart Selects
3. Watch the progress row in the feedback HUD at the bottom-right of the window
4. Review the results sorted by overall quality score
5. Accept individual ratings or click Accept All to apply all suggestions

### Circle Takes

A clip that scores above 85% overall is proposed as a Circle Take. Nothing changes until you Accept that clip or click Accept All. Accepting a Circle Take also marks the clip Hero with five stars.

Sharpness analysis samples a single frame near the start of each clip. Clips that start out of focus but later become sharp may receive a lower sharpness score than expected.

See also: [GPS Scene Detection](#gps-scene-detection), [NLE Template Export](#nle-template-export)

## Audio Waveform Sync

*Synchronize multi-camera clips by cross-correlating their audio waveforms.*

Audio Waveform Sync uses normalized cross-correlation to find the time offset between clips recorded simultaneously from different cameras. By analyzing the audio tracks, it determines exactly how many seconds one clip leads or lags another.

### How It Works

1. Audio is extracted from each video clip and downsampled to 8 kHz mono
2. A coarse search finds the approximate offset by sliding one waveform over the other
3. A refinement pass narrows down to sample-accurate alignment
4. Results show the offset, confidence level, and sync quality for each pair

### How to Use

1. Open a project with at least 2 video clips
2. Choose Workflow → Analyze… → Audio Sync
3. Review the results showing offset and confidence for each clip pair
4. Use the offsets when setting up a multi-camera edit in your NLE

### Quality Levels

- Excellent (>80%) — Strong audio match, reliable sync point
- Good (50–80%) — Reasonable match, may need manual verification
- Poor (&lt;50%) — Weak correlation, clips may not share common audio

> **Tip:** For best results, ensure all cameras were recording simultaneously with ambient audio. Clips with very different audio content (for example, one indoors, one outdoors) will produce poor correlation.

Audio sync requires video clips with audio tracks. Photo-only clips are skipped.

See also: [Smart Selects](#smart-selects), [NLE Template Export](#nle-template-export)

## Shot List

*Plan the shots you need, link captured clips to them, and see coverage gaps.*

The Shot List tracks the shots you planned against the clips you captured. Choose Workflow → Plan & Deliver → Shot List…. Each item has a description, an optional scene, an optional shot type (Wide, Medium, Close-Up, Extreme Close-Up, Over the Shoulder, POV, Aerial, Insert, Establishing, Other), and a Required checkbox.

### Statuses

- Pending (orange clock) — Not yet captured
- Captured (green check) — At least one clip is linked to the shot
- Missing (red X) — You have marked the shot as not captured

The header shows “x/y shots captured” with a progress ring, and the filter bar switches between All, Captured, Pending, and Missing. The footer warns in red when required shots are still not captured.

### Overflow Menu (…)

- Import from CSV… — Paste rows of description, scene, shot type, required (true/false); a header row is detected automatically
- Auto-Match Clips — Links clips whose Scene Log scene and/or shot type match each uncaptured item and marks it Captured
- Mark Remaining as Missing — Flips every Pending item to Missing at the end of the day

Per-row buttons reset an item to Pending or remove it. Every change is saved to the project file immediately.

> **Tip:** Fill in Scene and Shot in the Scene Log tab as you review footage. Auto-Match Clips then does the linking for you.

See also: [Logging Scene, Shot and Take](#logging-scene-shot-and-take), [Storyboard](#storyboard)

## Storyboard

*Arrange clips into named sections by drag and drop to plan the edit order.*

The Storyboard lets you plan the order of the edit before you open your editor. Choose Workflow → Plan & Deliver → Storyboard… to open a board with sections on the left and an Unplaced Clips list on the right. The first time you open it in a project, MediaFlow creates five default sections: Opening, Act 1, Act 2, Act 3, and Closing.

### Working the Board

- Drag a clip from Unplaced Clips onto a section (or onto its “Drop clips here” zone) to place it
- Drag a clip from one section to another to move it; a clip lives in exactly one section
- Right-click a clip card and choose Remove from Storyboard to send it back to Unplaced (the clip itself is untouched)
- Type a name in New section name and click Add Section (or press Return); the trash icon deletes a section
- Click a section’s chevron to collapse it; the header counts clips and sections

Clip cards show the filename, duration, scene, and star rating. Unplaced Clips lists every video and image clip that is not yet in a section.

The storyboard is stored in the .vpm project file. It is a planning aid only and cannot be exported. To hand structure to your editor, use NLE Template Export or Export FCPXML.

See also: [Shot List](#shot-list), [NLE Template Export](#nle-template-export), [Star Ratings & Selects](#star-ratings--selects)

## Import Field Notes

*Match timestamped notes from a text or CSV file to the clips recorded at that time.*

Import Field Notes attaches notes you typed on set to the clips recorded at that moment. Choose Workflow → Plan & Deliver → Import Field Notes… and pick a text or CSV file. Each note is matched to the clip whose creation time is closest.

### File Formats

- Plain text — One note per line, starting with a time: “12:34 PM — great reaction shot” or “2026-04-02 12:34:00 - audio drop”
- CSV — A timestamp/time column plus a note/notes/text/comment/description column, with an optional tag/category/type column
- Timestamps may be full dates (2026-04-02 12:34, 04/02/2026 12:34 PM, …) or time only (12:34, 12:34:56 PM); time-only notes are assumed to be from today
- Tags in [brackets] or #hashtags inside the note text become the note’s tag

### Matching Confidence

- Exact (green) — Within 30 seconds of a clip’s creation time
- Probable (yellow) — Within 2 minutes
- Uncertain (orange) — Within 5 minutes
- Unmatched (red) — No clip within 5 minutes

If the camera clock and your watch disagree, adjust the TZ offset stepper (−12 to +12 hours); matching re-runs as you change it. Parse errors are listed separately so you can fix the source file.

### What Apply Does

- Appends the note text to the clip’s Notes (existing notes are kept)
- Adds the tag to the clip’s Tags if not already present
- If the tag contains hero, selects, or best and the clip is unrated, sets a 5-star rating

See also: [Working with Tags](#working-with-tags), [Editing Clip Metadata](#editing-clip-metadata), [Star Ratings & Selects](#star-ratings--selects)

## Clip Classifier, Second Pass (Tier 1)

*An optional second pass after import that looks at the pictures and listens to the start of each clip to refine proposals.*

After an import finishes copying, MediaFlow proposes a category, camera, scene and reject flag for every clip. The basic pass reads facts from the file: frame rate, recording time, camera make, audio level, one sampled frame. Tier 1 is a second, slower pass that looks at the pictures and listens to the start of the clip, so the proposals are better. Proposals appear in italics and are never applied until you confirm them.

### What Tier 1 looks at

- Faces — how many, how large, and how centered. One or two centered faces that fill a real part of the frame suggest an Interview
- Scene labels — the families Vision returns (outdoor, beach, road, vehicle, food, buildings) map to B-roll or Establishing Shot
- Signage — readable text in shot suggests an establishing shot, and gives the clip a title
- Altitude — a flying camera with nobody in frame is B-roll
- Motion — how much the picture changes between sampled frames, which separates a time-lapse or hyperlapse from a locked-off tripod
- Speech — the first 60 to 90 seconds of clips whose audio is not silent, to spot speech to camera and seed a title

Tier 1 weighs your project’s own categories against each other, and the strongest becomes the proposal. It never overrides a Tier 0 verdict that came from a hard fact such as 240 fps, never lowers the confidence Tier 0 reported, and never changes the camera Tier 0 read from the file.

### Privacy

The picture analysis (faces, scene labels, signage, motion) runs on this Mac. The speech sample uses Apple’s speech recognition: it runs on this Mac when macOS has an on-device model for your Mac’s language, and otherwise the audio sample is sent to Apple’s speech service. If you refuse speech recognition permission, Tier 1 carries on without the speech signal.

### Turning it on

Tier 1 is off by default. The switches are in Settings › Analysis, under Import Analysis:

- “Propose category, camera and scene after an import” — the first pass. It must be on before Tier 1 can be switched on
- “Also look at the pictures and listen to the first minute (Tier 1)” — Tier 1 for every project
- “Use Tier 1 for the open project” — overrides the switch above for this project only
- “Run Tier 1 over the open project now” — runs it over clips that already carry an unconfirmed proposal. It works in the background and skips clips it has already seen

Turning Tier 1 off while it runs stops it. Whatever it has already proposed stays.

### Whole-file transcripts

Tier 1 listens only to the start of a clip. To transcribe whole clips, choose Workflow → Analyze… and click Run on the Transcribe row.

> **Tip:** In Review (Workflow → Review), A accepts the proposal on the clip in front of you and R marks it a reject candidate. Both teach the category suggester.

See also: [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [Auto-Suggest Categories](#auto-suggest-categories), [Vision (AI Scene Analysis)](#vision-ai-scene-analysis), [Speech Transcription](#speech-transcription), [Reviewing Clips with the Keyboard](#reviewing-clips-with-the-keyboard)

## Audio Levels

*Flag clips with clipped, quiet, or silent audio before they reach the edit.*

The Audio pass finds sound problems before you cut. Choose Workflow → Analyze… and click Run on the Audio row. MediaFlow reads the audio track of every video or audio clip that has not been analyzed yet and records its peak level, average level and a quality flag. Progress shows in the progress HUD.

### Flags

- Clipping — more than ten samples at or near 0 dBFS
- Silent — average level below −50 dBFS
- Low — average level below −30 dBFS
- Good — none of the above

The flag appears as an icon in the Table view, and the levels are listed in the Full Metadata tab. Clips with a Clipping, Low or Silent flag are counted as audio issues in the Day Summary. Clips that already carry a flag are skipped; MediaFlow tells you when nothing is left to analyze.

See also: [Day Summary](#day-summary), [Smart Selects](#smart-selects), [Audio Waveform Sync](#audio-waveform-sync), [The Analyze Hub](#the-analyze-hub)

## Exposure

*Traffic-light exposure ratings and color-cast notes for every clip, grouped by scene.*

The Exposure pass gives you a triage list of clips that may be too bright, too dark or off-color. Choose Workflow → Analyze… and click Run on the Exposure row. MediaFlow rates each clip’s exposure, estimates its color balance, and flags clips that do not match the rest of their scene.

### Traffic lights

- Green / Good — exposure within the normal range
- Yellow / Marginal — Slightly Over (more than 2% of highlights clipped) or Slightly Under (mean luminance below 50)
- Red / Problem — Overexposed (more than 5% clipped) or Underexposed (mean luminance below 30)

Click a traffic-light count, or use the All / Good / Marginal / Problem filter bar, to narrow the list. Each row shows the scene, a mini histogram, and a note such as “Overexposed — 8.0% highlights blown out · Color: warm (cloudy/shade WB) · ISO 400 · Shutter 1/60 · f/2.8”.

### Scene color mismatches

Within a scene that has two or more clips, any clip whose average color differs noticeably from the scene average is flagged, and the header counts the scenes with mismatches. This is useful for spotting a camera left on the wrong white balance.

The ratings are estimated from each clip’s recorded exposure data (ISO, shutter, aperture, white balance), not from the decoded picture. Treat the list as a guide to which clips to look at, and confirm on a monitor.

See also: [Smart Selects](#smart-selects), [Format Conformance Checker](#format-conformance-checker), [Logging Scene, Shot and Take](#logging-scene-shot-and-take), [The Analyze Hub](#the-analyze-hub)

## Transcode

*See which codecs your editing software will struggle with and what to transcode them to.*

The Transcode pass tells you which clips to convert before you edit. Choose Workflow → Analyze… and click Run on the Transcode row. MediaFlow groups the project’s video clips by codec and compares them with what the editor you pick handles well: Final Cut Pro, Premiere Pro, DaVinci Resolve or Avid Media Composer. Your choice is remembered.

### Priorities

- Required (red) — codecs the editor handles poorly, for example HEVC/H.265 in Premiere Pro, or HEVC and H.264 in Avid
- Recommended (orange) — codecs that are neither native nor known to cause problems; proxies speed up editing
- Optional (blue) — footage larger than 4K, where proxies are suggested

Each card names the target codec (ProRes 422 or ProRes 422 Proxy; DNxHD 175 or DNxHD 36 for Avid), the number of clips affected, and an estimated output size and transcode time. The header sums the totals, or confirms that every clip is already compatible.

This sheet only advises; it does not transcode anything. To make proxies, select the clips and use the Workflow Tools tab, or use your editor’s own media management.

See also: [Format Conformance Checker](#format-conformance-checker), [NLE Template Export](#nle-template-export), [Processing the Proxy Queue](#processing-the-proxy-queue), [The Analyze Hub](#the-analyze-hub)

## Continuity

*A scene-by-angle coverage grid that shows where a camera has no footage or far fewer takes.*

The Continuity pass shows whether every scene is covered from every angle, so you can decide on a pickup before you leave a location. Choose Workflow → Analyze… and click Run on the Continuity row. MediaFlow builds a grid of scenes (rows) against cameras (columns) from the Scene Log data on your clips and counts the takes in each cell. The column for a clip comes from its Camera angle in the Scene Log; when that is empty, its camera is used.

### Cell colors

- Good (green) — the camera has takes for the scene
- Partial (yellow) — the camera has fewer than half the takes of the best-covered camera for that scene
- Missing (red) — the camera has no footage for the scene

### Coverage gaps

Below the grid, gaps are listed with missing coverage first and a one-line explanation, for example “Scene 4 only has footage from A — no backup angle”. The header summarizes the counts, or reports full coverage across all scenes and cameras.

Clips without a scene are ignored. If no clip has scene data, the sheet asks you to assign scenes and cameras first.

See also: [Logging Scene, Shot and Take](#logging-scene-shot-and-take), [Shot List](#shot-list), [Audio Waveform Sync](#audio-waveform-sync), [The Analyze Hub](#the-analyze-hub)

## Logging Scene, Shot and Take

*Record scene, shot type, take, camera angle and circle takes for each clip in the Scene Log tab.*

The Scene Log records the slate information for a clip, so later tools can group, match and export by scene. Select a single clip and open the Scene Log tab in the metadata panel. Every field saves as you type.

### Fields

- Scene — Free text such as 1A or 12
- Shot — Wide, Medium, Close-Up, Extreme Close-Up, Over the Shoulder, POV, Aerial, Insert, Establishing, or Other
- Take — A number; the + button (Cmd+Shift+T while the tab is showing) increments it
- Camera angle — Which angle the take was shot from, such as A, B or C. This is not the camera that shot the clip; that is Camera in the Edit tab
- Circle Take — Marks the director-approved take

Ticking Circle Take also marks the clip Hero and rates it five stars, unless the clip already has a select status or a rating. Unticking it does not remove them; change the select status and the rating yourself.

### Where It Is Used

- Review (Workflow → Review) shows Sc / shot / Tk / camera angle in its overlay, and C toggles the circle take
- Shot List → Auto-Match Clips links clips to planned shots by scene and shot type
- In Workflow → Analyze…, GPS Scenes proposes scene groupings, Sun compares clips within a scene, and Continuity counts takes per scene and camera angle
- Generate Dailies, NLE Template Export, and Workflow → Plan & Deliver → Export FCPXML carry scene, shot, take, and circle takes to the editor

Edits made in the Scene Log tab are saved at once and cannot be undone with Edit → Undo, so check the take number before you move on.

See also: [Shot List](#shot-list), [Continuity](#continuity), [Dailies Report](#dailies-report), [Reviewing Clips with the Keyboard](#reviewing-clips-with-the-keyboard), [NLE Template Export](#nle-template-export)

---

# Video Preview & Playback

## Video Playback Controls

*Play, pause, scrub and step frame by frame through the selected video in the preview panel.*

Select a video clip to load it in the preview panel. The controls appear below the picture:

- Seek slider — Drag to scrub through the clip. A marked in/out range is highlighted on it
- Step Back — Move back one frame
- Play / Pause — Start or stop playback
- Step Forward — Move forward one frame
- Time display — Current position and total length in minutes and seconds, for example 1:05 / 12:30
- Pop-out button — Open the video in its own window

Press Space to play or pause after clicking the preview, so that it has keyboard focus, as for I and O. Elsewhere in the window, such as the clip list or a text field, Space keeps its usual job. At the end of a clip, Play and Space start it again from the start.

> **Tip:** Use frame stepping for precise positioning when extracting thumbnails or creating subclips.

Making proxies is part of the Studio plan; see Plans and Pricing.

See also: [Pop-Out Video Window](#pop-out-video-window), [Extracting Thumbnails and Subclips](#extracting-thumbnails-and-subclips)

## Pop-Out Video Window

*Open the video preview in a separate, resizable window with its own playback controls.*

Click the pop-out button at the right end of the preview controls to open the video in a separate window. The window has its own seek slider, step back, play/pause and step forward controls, and you can resize it freely.

> **Tip:** Use the pop-out window when you want a larger preview while still seeing the media list and metadata panels.

See also: [Video Playback Controls](#video-playback-controls)

## Extracting Thumbnails and Subclips

*Save the current video frame as a PNG image, or make part of a clip a clip of its own: added to this project under the clip it came from, or saved to a folder.*

Use the Workflow Tools tab in the metadata panel for these operations:

### Extract Thumbnail

Saves the current video frame (or the full image for a photo) as a PNG file. Move to the frame you want with the playback controls, click Extract Thumbnail, and choose where to save it.

### Create Subclip

Makes part of a video a clip of its own. Mark in and out points to choose the part, then click Create Subclip in the Workflow Tools tab, or choose Workflow → Create Subclip… (Cmd+U) with one video selected. What is taken depends on the marks:

- Both marks set — the range between them
- Only an in-point — from the in-point to the end of the clip, up to 30 seconds
- Only an out-point — from the start of the clip to the out-point
- No marks — a 5-second clip around the current position, starting 2 seconds before it

MediaFlow then asks what to do with it:

- Add to This Project — The part is saved as a new file in MediaFlow’s import working folder (Documents › MediaFlow Projects › Imports): in the folder the clip was imported to, when that folder is still there, otherwise in a Subclips folder there. It joins the project the way an imported clip does, is analyzed like one, and is listed under the clip it was cut from. Organize later files it beside that clip, in the same category and camera folder. A notice says when it is done, with a Show in Finder button
- Save to a Folder… — Saves the part as a file wherever you choose, without adding it to the project. The save panel opens in the folder you used last time. You can replace a file that is already there: the old file is set aside only once the new one is finished, and put back as it was if the new one cannot take its place. If the drive cannot confirm that it has written the new file, MediaFlow says the save did not finish and keeps the old file hidden beside it until the next save under that name. MediaFlow never saves over a file of any clip in the project, the clip being cut included: the clip itself, its working copy, the original on its card, its copy in Cleanup or its proxy, however the folder is reached

### What a Subclip Keeps

A subclip added to the project takes the category, camera, scene, shot, take, camera angle, tags and notes of the clip it was cut from. It does not take its rating, Select, favorite, circle take, review state or import suggestions: you judge the part on its own. Its date is the clip’s date plus the in-point, so it sorts where it was filmed. It remembers the clip it was cut from and where in that clip it starts and ends. A subclip cut from a subclip is linked to the original clip, in that clip’s time.

### The File

A subclip keeps the clip’s own format: a .mov stays a .mov and an .mp4 stays an .mp4. The picture and sound are copied as they are, so there is no loss of quality and it is quick. For a clip where that is not possible, the part is encoded afresh at high quality instead, and the notice says so. The name says where the part lies in the clip, for example GX010042_subclip_0m12s-0m41s.MP4, so several subclips of one clip never collide. In the working folder, a subclip whose name is already taken, by a file or by a clip of the project that still records it, gets _1 added to its name.

The export shows in the activity panel at the bottom right of the window and in the Workflow Tools tab, each with a Cancel button, and carries on if you switch tabs or select another clip. Cancel stops it and keeps nothing of it, not even over a file you chose to replace. One subclip is made at a time. If MediaFlowSwift quits while it is making one, the unfinished file is hidden, and is removed the next time a subclip is saved under that name.

### Subclips in the Project

In the Table, a clip with subclips has an arrow at the left of its row and a label such as “2 subclips”. Click the arrow to see them beneath it, in order of their in-points, each labeled with its range, such as 0:12–0:41. In the Grid, each subclip is a card of its own with a Subclip badge; hold the pointer over the badge to see the clip it came from. With a subclip selected, the metadata panel shows “Subclip of” and the clip’s name with the range, and a Show Parent button that selects that clip, clearing the search and the filter first when they hide it. See Table and Grid Views.

If you remove the clip a subclip was cut from, the subclip stays in the project as an ordinary clip on its own row, and the metadata panel says its parent is not in this project. Move to Project, Duplicate, Relink and Archive keep the link when the clip goes too. A project saved by an older version of MediaFlowSwift drops the links, and its subclips become ordinary clips.

### Marking In/Out Points

In the Workflow Tools tab, click Mark In (I) or Mark Out (O) to set a mark at the current playback position. You can also press I or O after clicking the preview panel, so that it has keyboard focus. The marked range is highlighted on the seek slider, the In, Out and Duration times are listed in the tab, and the Create Subclip button shows the duration. Click Clear in the Workflow Tools tab to remove both marks.

See also: [Video Playback Controls](#video-playback-controls), [Table and Grid Views](#table-and-grid-views), [Processing the Proxy Queue](#processing-the-proxy-queue)

## Reviewing Clips with the Keyboard

*A keyboard-driven review sheet for playing, rating, rejecting and accepting proposals on clips, one after another.*

Rapid Review is a focused review sheet for evaluating clips quickly. Use the keyboard to play, rate, favorite, reject and move through your footage without touching the mouse. Open it from Workflow → Review (Cmd+Opt+R) or from the Rapid Review… button on the pipeline strip’s Review segment. Press ? at any time for an on-screen list of these keys.

### Playback Controls

- J / K / L — Shuttle reverse / stop / forward (press repeatedly to increase speed: 1×, 2×, 4×, 8×)
- Space — Play / pause, whatever you clicked last. At the end of a clip, it plays again from the start
- Left Arrow — Step back one frame
- Right Arrow — Step forward one frame
- Home — Jump to clip start
- End — Jump to clip end

### Rating & Tagging

- 1–5 — Set star rating (1 through 5 stars)
- 0 — Clear rating
- F — Toggle favorite
- X — Toggle Reject
- C — Toggle circle take

### Import Proposals

- A — Accept the category and camera import analysis proposed for this clip
- R — Mark the clip a reject candidate (files it under Skip (don’t copy) when it has no category yet)

Both keys do what the menu commands do: you can undo them, MediaFlow re-files an organized copy to match, and the category suggester learns from them. A does nothing on a clip with no proposal, and R never replaces a category you chose yourself.

### Navigation

- Down Arrow — Next clip in queue
- Up Arrow — Previous clip in queue
- T — Toggle auto-advance (when ON, moves to next clip after rating)
- Escape — Close Review

### Display

- M — Toggle metadata overlay (filename, scene/shot/take, ratings, badges)
- I — Set mark in-point at current position
- O — Set mark out-point at current position
- ? — Show or hide the keyboard help overlay (Escape also closes it)

### Auto-Advance

With auto-advance on, rating a clip with 1–5, making it a favorite with F, rejecting it with X, or pressing A or R moves to the next clip after a short delay. Taking a favorite or a Reject off, clearing the rating with 0, or pressing C stays on the clip. The last rating or mark you give a clip decides, so pressing X twice quickly stays put instead of skipping a clip, and Up or Down Arrow during the delay goes only where you asked. Auto-advance starts on; press T to turn it off or on, and MediaFlow remembers your choice. The Auto indicator in the bottom bar is green while it is on.

### Review Queue

The review queue is the clips your filters show in the main window when you open Review. Filter by category, scene, camera or smart group before you open Review to focus on a specific subset of clips. The bottom bar shows your progress (for example “12 of 47”) and how many clips in the queue have been rated.

The queue stays as it was until you close Review. A clip you rate while only unrated clips are showing stays in it: Up Arrow goes back to it, and the progress and the rated count keep moving.

> **Tip:** For the fastest selects workflow: click the Review segment of the pipeline strip to show only unrated clips, open Review, and use 1–5 to rate each clip.

See also: [Video Playback Controls](#video-playback-controls), [Extracting Thumbnails and Subclips](#extracting-thumbnails-and-subclips), [Star Ratings & Selects](#star-ratings--selects), [Keyboard Shortcuts Reference](#keyboard-shortcuts-reference)

---

# Batch Operations

## Using the Proxy Queue

*Mark clips for thumbnail and proxy generation by adding them to the Proxy queue, and take them out again.*

The Proxy queue is a list of clips you have marked for thumbnail and proxy generation. Queue the clips first, then process the whole queue in one go.

### Adding to the Queue

- Right-click a clip, or a selection of clips, and choose Add to Proxy queue
- Or select the clips and turn on Add to Proxy queue in the Workflow Tools tab of the metadata panel

### Seeing What Is Queued

Select Proxy queue in the sidebar’s Library section, or choose Proxy queue from the toolbar filter menu, to list only the queued clips. The Workflow Tools tab shows the number queued.

### Removing from the Queue

- Right-click a queued clip and choose Remove from Proxy queue
- Or click Clear in the Workflow Tools tab to empty the entire queue

Processing does not empty the queue. Clips stay queued until you remove them.

See also: [Processing the Proxy Queue](#processing-the-proxy-queue)

## Processing the Proxy Queue

*Generate thumbnails and low-resolution proxy videos for every clip in the Proxy queue, and where they are stored.*

With clips in the Proxy queue, use the buttons in the Workflow Tools tab of the metadata panel to process them:

- Process Queue (Thumbnails) — Generate a thumbnail image for each queued clip
- Process Queue (Proxies) — Generate a low-resolution MP4 proxy for each queued video. Photos and audio files are skipped
- Process Queue (All) — Generate both

A progress bar shows the name of the clip being processed. Click Cancel to stop processing; clips already finished keep their files.

### Where the Files Go

Proxies are saved as &lt;name>_proxy.mp4 in MediaFlow’s Application Support folder in your Library, in a Proxies folder for each project. They belong to this Mac: they are not stored in the project folder and do not move with the project. The Metadata tab lists each clip’s Thumbnail and Proxy paths under Generated Files, with a Proxy status line saying whether one has been generated.

### What proxies are for

Once a clip has a proxy, the preview, the pop-out player and Review play the proxy instead of the original. It is a much smaller file on this Mac’s own drive, so it starts at once and scrubs smoothly, where a large original on a network drive may not. A small badge at the top-left of the player says Proxy or Original and lets you switch. It switches at the same moment in the clip and keeps your In and Out marks, and your choice holds for the clips you look at next.

- Use Play Original before judging focus, noise or fine detail: a proxy is lower resolution and more compressed than the clip
- In and Out marks, subclips and exports always refer to the original. The proxy has the same length and timing, so a mark made while watching it lands in the same place
- If the original has been replaced since the proxy was made, the proxy is out of date and is not used; generate it again
- If the original is on a drive that is not connected, the proxy is played regardless, and the badge says the original is not reachable. This is the one way to watch a clip whose drive is on the shelf

### Clips on a Network Drive

A clip on a network share or another network drive is read across the network as it plays, and macOS does not read ahead for a file the way it does for a stream, so a short pause on the network is a pause in the picture. A large clip, such as 4K footage, over a wireless connection is where this shows. When the preview is playing such a clip and it has no proxy, a badge at the top-left says Over the network:

- Make Proxy — Makes a proxy for this clip now, without touching the Proxy queue. When it is finished the preview changes to the proxy at the same moment in the clip
- All Clips — Makes a proxy for every video in the project that has none, one after another. Each is kept as it is finished, so you can carry on working, and Cancel in the Workflow Tools tab keeps what was made

Making a proxy reads the whole clip once, so expect roughly a third of the clip’s length over a wireless connection; after that, playback does not depend on the network. The original is never changed. A wired connection to the drive helps playback of the originals themselves, in MediaFlowSwift and in your editor.

See also: [Using the Proxy Queue](#using-the-proxy-queue), [Extracting Thumbnails and Subclips](#extracting-thumbnails-and-subclips)

---

# Tags & Categories

## Working with Categories

*Give each clip one category; the category groups your clips and names the folder Organize Media files them into.*

A category says what kind of clip this is. Each clip has one. When you organize media, the category name becomes a folder at the destination.

### Default Categories

- Uncategorized — What a newly imported clip has until you change it
- A-roll, B-roll, Establishing Shot, Interview, Cutaway, Time-lapse, Slow Motion, Product Shot, Action Shot, Behind the Scenes, Outtake
- Skip (don’t copy) — A special category that Organize Media never copies. It is stored as “Do Not Copy”

### Assigning a Category

- One clip — Select it and choose from the Category picker in the Edit tab. The change applies at once
- Several clips — Select them, choose from the Category picker in the Edit tab, then click Apply Category
- Either way — Right-click the selection and choose Set Category

If the project has a destination, MediaFlow then moves the clip’s organized file to the folder for its new category. It does this quietly and tells you only if a file could not be moved.

### Changing the List

The Edit tab only offers the categories the project already has. The list belongs to the project and is stored in the project file. To add, rename, retire or remove a category, open the project and go to Settings › Categories. A new category then appears in the Category picker and the Set Category menu.

> **Tip:** Workflow → Analyze… → Categories proposes a category for each uncategorized clip.

See also: [Adding, Renaming, Retiring and Removing Categories](#adding-renaming-retiring-and-removing-categories), [What Happens to Files When You Change a Category](#what-happens-to-files-when-you-change-a-category), [Working with Tags](#working-with-tags), [Auto-Suggest Categories](#auto-suggest-categories), [Organizing Media to Storage](#organizing-media-to-storage)

## Working with Tags

*Attach free-form, searchable tags to a clip; a clip has one category but can carry any number of tags.*

Tags are free-form labels you can attach to clips. Unlike categories (one per clip), you can have multiple tags per clip.

### Adding Tags

- Select a clip and go to the Edit tab
- Type in the tag field and press Enter or comma to add
- Multiple tags can be added at once by separating with commas

### Removing Tags

Click the X button on any tag chip to remove it.

### Batch Tag Operations

With two or more clips selected, the Edit tab shows three tag buttons:

- Add Tags — Appends tags to all selected clips
- Replace Tags — Replaces all existing tags with the new ones
- Clear Tags — Removes all tags from selected clips

> **Tip:** The search field above the media list matches tags, in this project or, with All Projects chosen, in every project in the shared database.

See also: [Working with Categories](#working-with-categories), [Filtering and Searching](#filtering-and-searching)

## Adding, Renaming, Retiring and Removing Categories

*Settings › Categories edits the open project’s category list; retire a category to stop using it without touching its clips.*

The category list belongs to the project. It is stored in the project file and can differ from shoot to shoot. Settings › Categories shows the list for the open project, with the number of clips in each category. With no project open, it shows Open a Project… instead.

### Retire or remove?

- Retire — stops offering the category for new work. Clips already in it keep it, nothing moves, and it still shows in filters, marked “retired”. Restore offers it again. Choose this when you are finished with a category but have clips filed under it
- Remove (the trash button) — takes the category out of the project. If clips still use it, you must choose where they go first. Choose this for a category created by mistake

### Add and rename

- Add — type a name in the New category field and click Add
- Rename — click Rename, type the new name and click Save. Every clip in the category is renamed with it, as one step you can undo

### Removing a category that has clips

1. Click the trash button beside the category
2. The dialog says how many clips still use it
3. Click “Move clips to…” for the category that should take them. Uncategorized is always offered first

### Files that are already organized

Organized clips sit in a folder named after their category. Renaming or removing a category here does not move those files. A note under the list tells you how many files are still in a folder with the old name. Run Workflow → Repair → Re-file folders by category to move them.

### Built-in categories

Uncategorized and Skip (don’t copy) are marked “built in”. Organize relies on their exact names, so they cannot be renamed, retired or removed.

### Starting new projects with this list

Click Also use for new projects. The next project you create starts with this list instead of the built-in one.

See also: [Working with Categories](#working-with-categories), [What Happens to Files When You Change a Category](#what-happens-to-files-when-you-change-a-category), [Auto-Suggest Categories](#auto-suggest-categories), [The Settings Window, Tab by Tab](#the-settings-window-tab-by-tab)

## What Happens to Files When You Change a Category

*Changing a clip’s category applies at once and moves its organized copy to the matching folder in the background.*

Organize files each clip in a folder named after its category. When you change a clip’s category in the main window, the change applies at once, and MediaFlow then moves the clip’s organized copy into the folder for the new category. You do not start this and you do not confirm it.

### When it happens

- The project has a destination, and the clip’s file is already inside it. A clip that has not been organized yet has nothing to move; it is filed by its current category when you organize it
- You change the category of one clip, change it for a selection, or accept a proposed category
- Undoing a category change moves the file back the same way

### What you see

A row titled “Filing clips by category” appears in the progress panel while the move runs, then disappears. There is no summary and no Done button when it succeeds. You can carry on working while it runs: a rating, a note or another category change made meanwhile is kept, and the file then moves on to the folder for the newer category.

You hear about it only if it fails. If a file cannot be moved, the row stays and says so until you clear it, and the details are written to the log. The clip keeps its new category; its file is still in the old folder.

The row also stays if you open another project before the move finishes. The file has moved, but the project you left was closed before that could be saved in it, so its clip reads Missing when you open that project again. Workflow → Repair → Relink Missing Media…, pointed at the destination, finds it.

### Putting things right

Choose Workflow → Repair → Re-file folders by category. It checks every organized file in the project and moves each one into the folder its current category calls for. Use it after a failed move, for example when the destination was not connected, and after renaming a category in Settings › Categories, which does not move files by itself.

### When two projects share media

If this project shares its media files with another (see Duplicating a Project), nothing is re-filed. The category changes; the file stays where it is, because moving it would make the clip go missing from the other project. MediaFlow tells you when this happens.

See also: [Adding, Renaming, Retiring and Removing Categories](#adding-renaming-retiring-and-removing-categories), [Organizing Media to Storage](#organizing-media-to-storage), [Progress and Messages](#progress-and-messages), [Working with Categories](#working-with-categories), [Undo and Redo](#undo-and-redo)

## Auto-Suggest Categories

*Let MediaFlow propose a category for every uncategorized clip and learn from your decisions.*

The Categories pass saves you from categorizing clips one at a time. Choose Workflow → Analyze… and click Run on the Categories row. MediaFlow examines every clip whose category is empty or Uncategorized and opens a review sheet with a suggested category for each, a confidence badge and the reason.

### Signals

- Filename keywords — interview, broll, aroll, timelapse, hyperlapse, slowmo, bts, outtake, establishing, cutaway, product, action, dnc, and similar
- Learned history — what you assigned before to clips from the same camera, or with a similar duration (needs at least 3 camera samples or 5 duration samples)
- Frame rate — 100 fps and above suggests Slow Motion; 5 fps and below suggests Time-lapse
- Duration — under 3 seconds suggests Skip (don’t copy), stored as “Do Not Copy”, because the clip is probably accidental. Length alone suggests nothing else

### Confidence

- High (green) — 80% or better, typically a filename keyword or a high frame rate
- Medium (orange) — 50–79%, typically a learned pattern or a very short clip
- Low (gray) — under 50%

### Reviewing

- The green check accepts one suggestion; the gray X dismisses it
- Accept All applies every remaining suggestion as a single undoable step
- Dismiss All closes the sheet without changes

Every category you assign, by hand or by accepting a suggestion, teaches the suggester. If you pick a different category than it proposed for a camera three times, it stops making that proposal. Settings › Categories › Category Learning shows what it has learned, and Reset Pattern Memory clears it. The Uncategorized Clips smart notification offers an Auto-Suggest button when five or more clips need a category.

See also: [Working with Categories](#working-with-categories), [Vision (AI Scene Analysis)](#vision-ai-scene-analysis), [The Analyze Hub](#the-analyze-hub), [Undo and Redo](#undo-and-redo)

---

# Shared Database

## Shared Database Overview

*The optional shared database lets you search and track clips across projects; it is a database file or a database server.*

The shared database (the app calls it the Central Database) keeps a record of every project so you can search, compare and track clips across all of them. It is optional. Import, organize, preview and editing all work without it.

Each project lives in its project file (.vpm), and every project opens and works from it without the database. The database keeps a record of each project and its clips for all your Macs to share, but not the whole project: transcripts, sound levels, what Vision found, GPS, weather, sun position and camera details, the checklist, the shot list, the storyboard, the projects it shares media with and retired categories are kept only in the project file. Neither one simply overrides the other: a save sends the database what changed on this Mac, and opening a project from its file doesn’t copy the database’s clips into it.

### What a Save Sends

A save writes the project file, then sends the database what changed on this Mac since its last save there (or, the first time, since the project was open here with the database connected):

- Each clip you changed on this Mac, whole: its rating, notes, tags, category, camera and where its file is, as this copy has them, not only the part you changed
- The clips you added, and the clips you removed, recorded as removed
- What MediaFlow fills in by itself, after a project opens or when it re-checks where files are: a video’s length, picture size, frame rate and format, where its working copy is, and whether its file is at the destination, in the working folder, somewhere else or missing (the Where column). When nothing else about the clip changed here, these go on their own, without the rest of the clip, and not at all once another Mac has moved or relinked that clip
- The project’s name, where its file is and its destination, only when the database doesn’t have the project yet, when they changed on this Mac, when this copy has just become the project’s home, or in the first-time case below

Everything else is left as the database has it, with two small additions: a save that sends a clip also records when the project last changed and on which Mac, and any of the project’s category and camera names the database doesn’t have yet are added to its shared lists. A clip you didn’t change is not sent (except the first time, below), so a copy of the project that hasn’t got another Mac’s latest changes can’t undo a rating, note or tag made there. A clip your copy doesn’t have is not removed: another Mac may have added it. A clip another Mac removed is not brought back just because your copy still has it. A save doesn’t change whether the database records the project as archived, or to which drive: Archive and Restore write that themselves.

### When the File and the Database Differ

Opening a project from its file doesn’t copy clips from the database into it. The first time this Mac has a project open with this database connected, a clip whose copy here differs from the database’s (another Mac changed it and saved to its own copy of the file, say) keeps the database’s version there, while the project shows this copy’s, until you change that clip on this Mac; then your save sends the whole clip as this copy has it.

There is one exception. If this copy already has changes the database hasn’t had (saved while the database was off or out of reach, or made before it connected), every clip that differs from the database’s is sent as this copy has it instead, even one you didn’t touch, and so are the project’s name, where its file is and its destination, if they differ; see Working Offline below.

After that first time, this Mac sends what differs from what it last sent there, so a clip another Mac has changed since is left alone until you change it here. That is what “changed” means to a save: different from what this Mac last sent. So if you open an older copy of the file on this Mac than the one it last saved (a backup put back in place, say), its older clips count as changes, and a save sends them over what the database has now.

This Mac keeps its record of what it last sent for each database. Connect to another database, copy the records between a database file and a server, or reach the same server under another address or user name, and each project’s next open there is a first time again.

A few things about the project itself do come from the database. When you open a project the database records as archived, it opens archived, with the drive, path and date, even if its file has lost them; once a restore has made another copy the project, an older copy opens as not archived, when the restored copy is within reach. If the database records the project as living in another file that is still there, MediaFlow asks which copy to use before this one sends the database anything (at the latest at your first save with the database connected), and sends nothing from it until you answer; see The Old Copy of a Project in After Moving Your Library to a New Drive. And for a project out on an editing drive, the database says where its library copy is now.

### Two Macs, One Clip

Changes to different clips don’t get in each other’s way, except in the two cases under When the File and the Database Differ where a save sends clips you didn’t touch: the first time a Mac sends a copy that has changes the database hasn’t had, and an older copy of the file opened on a Mac that has saved a newer one. Then the clips that differ are sent as that copy has them, which can undo another Mac’s change to a clip this Mac never touched. Changes to the same clip can get in each other’s way whenever one Mac changes it on a copy of the project that hasn’t got the other Mac’s change to it yet. That Mac’s save sends the whole clip, so the other Mac’s change is replaced in the database, even when the two changed different things: a rating given on one Mac can take out a note written on the other. The other Mac’s project file still has its change.

That happens when the Macs work from different copies of the project file. When both work in the same file, on a share both reach, each save first takes in what the other Mac has saved to the file since this Mac last read or wrote it, so a rating given on one Mac and a note written on the other both land, and when both changed the same thing, the saving Mac’s change is kept and the other version is set aside (see Saving Projects). To work on a project from two Macs, keep one project file on a share both reach: File › Move Project To… puts it there. With a database server, MediaFlow tells you when someone else has the project open; see Who Else Has a Project Open.

### Where a Shared Project Organizes

A project organizes into one destination on every Mac that shares it, and the destination belongs to the Mac that set it: the Mac that started the project, until one changes it. The project file and the database keep, beside the folder’s path, the network share it is on and where on the share, and which Mac set it. So each Mac finds the folder however the share is mounted there, and a Mac that can’t reach it can say whose it is. A project from an earlier version gains the share part the next time a Mac that has the share connected saves it; which Mac set its destination stays unknown, so a folder on a Mac’s own disk is found where its path is, as before.

A destination on one Mac’s own disk can’t be reached from the others. Organize Media on another Mac says so, names the Mac and the folder, and offers Change Project Destination… rather than organizing anywhere else; see When This Mac Can’t Reach the Destination. To organize a shared project from any Mac, keep its destination on a network share every Mac reaches. New Project warns when it isn’t.

### What the Database Adds

- Search All Projects — Find clips in any project from the search field, and copy the ones you want into the open project
- Find Duplicates — List files with identical content across projects
- Storage Dashboard — Capacity history and database-wide counts
- Migrate Projects — Add existing .vpm files to the database
- Browse Projects — Projects → Browse Projects… shows the Projects list in the main window, with every project the database knows

### File or Server

The database is kept in one of two stores. You choose with the Store picker in Settings › Storage.

- Database file — A single file, usually on shared storage. Nothing to install. One Mac at a time: MediaFlow works on a local copy of the file and writes it back when you disconnect or quit. While one Mac is connected, another is told who has the file and can wait or work without it; see One Mac at a Time on a Database File
- Database server — A server that keeps the records itself, so several Macs can work at the same time

### Turning It On

1. Open Settings › Storage
2. For a database file, click New Database File… and choose where it will live: MediaFlow makes it there, turns the database on and connects. To use a database file another Mac already made, click Use an Existing Database File… instead
3. For a server, turn on Enable Central Database, choose Database server as the Store, fill in Host, Port, Database, User and Password, then click Test Connection

A database file is never replaced. New Database File… never makes a file at the name of the database file in use, even before that file has first been written. If the name you choose for a new one is already taken by a database file, MediaFlow asks whether to use that one or choose another name; a file that isn’t a MediaFlow database is refused, and left as it is. The new file is made on this Mac first and put in place only if nothing is there, so a file that appears in the meantime is never written over. The Save dialog opens beside the usual place on the network share chosen in Settings › Network, or in Documents on this Mac.

### Moving Between a File and a Server

With Database server selected, Settings › Storage offers Copy the Database File to This Server… and Copy This Server to a Database File…. Both copy every record and leave the source unchanged. Switching the Store picker alone does not move any records.

### Working Offline

Changes waiting to be sent are kept for the database they were made for. If you switch to another database file or server meanwhile, they are not sent there: they wait until you connect to their own database again. They go without asking only to that database, reached the same way. When MediaFlow connects to a database that may be theirs, it asks, and names both: one it can’t tell apart from theirs, one with the same identity reached another way, or a different database made since where theirs was (a new file where a deleted one was; if theirs comes back there, they go to it). One with the same identity is the same database moved, renamed or reached by another name or address, or a copy of it: a copy made in the Finder, a backup restored somewhere else or a server restored from a dump carries the same identity. Send Them Here sends them to the database connected now, only while it is still connected; if it has changed since, nothing is sent and MediaFlow asks again when it next connects. Keep Waiting keeps them for their own database; MediaFlow asks again the next time it opens. When the database connected now may be a copy, or is a different one, Return means Keep Waiting. Don’t Send stops keeping them for that database. Nothing else is deleted: the changes stay in your project files, and the next time you save one of those projects (File › Save) with a database connected, what changed is sent. An archive waiting to be recorded stays on its drives and in its project, but isn’t listed in the database. Changes waiting for any database other than the one in use, including one MediaFlow knows is another and so never asks about, are listed in Settings › Storage under Changes waiting for another database, where Don’t Send lets go of them if that database is gone for good. Changes saved while the database is turned off go to the next database you turn on. Switching also waits for your last save to reach the database in use, and for a connect already under way; if either is still going, or the last save couldn’t be written, nothing is changed and MediaFlow tells you why. A project opened from the database alone, without its file, can’t be saved to a file: close it (File › Close Project), choosing Save, then switch.

If the database cannot be reached, keep working. MediaFlow notes which projects changed and syncs them when the connection returns. The status line then reads “Connected”, or “Connected · offline changes still to sync: …” followed by the names of projects that are waiting. Open a named project to finish its sync.

### Database Menu

- Enable & Connect Database / Reconnect Database — Connect; the title changes once you are connected
- Disable & Disconnect — Close the connection and turn the database features off
- Migrate Projects… — Add existing .vpm files to the database
- Find Duplicates…, Storage Dashboard… — The cross-project tools. Searching every project is in the search field: Edit → Search All Projects… (Cmd+Shift+F)
- Reconnect Network Share — Mount the share chosen in Settings › Network again when it has dropped. It is dimmed while the share is mounted
- Status — The last line of the menu shows the connection and sync state

See also: [Database File or Database Server?](#database-file-or-database-server), [One Mac at a Time on a Database File](#one-mac-at-a-time-on-a-database-file), [Connecting to a Database Server](#connecting-to-a-database-server), [Who Else Has a Project Open](#who-else-has-a-project-open), [Copying Records Between the File and the Server](#copying-records-between-the-file-and-the-server), [Working Offline and Syncing Later](#working-offline-and-syncing-later), [Searching All Projects](#searching-all-projects), [Database Connection Issues](#database-connection-issues)

## Who Else Has a Project Open

*With a database server, when someone else has the project you open, MediaFlow tells you once, and the window title shows it while they are in.*

This works with a database server only. With a database file nothing is shown: each Mac works on its own copy of the file until it disconnects, so Macs take turns with it anyway.

While the server is connected, each Mac with a project open lets the others know, about every 45 seconds. When you open a project that someone has open on another Mac, MediaFlow tells you once: “Sheri Smith has this project open on Sheri’s MacBook Air.” When several people do, it says “Sheri and 2 others have this project open.”

While they are in, the window title says where: “Road Trip · also open on Sheri’s MacBook Air”. It appears within a minute of someone opening the project, and goes within a minute of them closing it or quitting.

### What It Means

Changes don’t arrive on the other Mac while you both work. When you both have the same project file open, what one of you saves reaches the other Mac when that Mac next saves (each save first takes in what the other saved to the file) or next opens the project, and changes to different things in the same clip both land. When you work from different copies of the project file, one Mac’s changes don’t reach the other’s file, and changing a clip the other Mac has changed replaces their change in the database; see Two Macs, One Clip in Shared Database Overview. Work on different clips, or share one project file. Taking turns doesn’t help with separate copies: one Mac’s copy doesn’t get the other’s changes, however long it waits. On one shared file you can take turns on the same clip: once the other Mac has saved its change, choose File › Revert to Saved before making yours, and neither is set aside.

### Good to Know

- Your own Mac is never announced, even if it left the project open when it quit unexpectedly and you reopen it after a restart
- A Mac that goes to sleep drops out as it does; one that crashed or lost its connection stops counting after two minutes, by the server’s clock
- The person is the name of the macOS account that is signed in, and the Mac is the name set in System Settings › General › Sharing. Macs are told apart by their hardware, so two Macs with the same network name are still two Macs
- Nothing is shown while the database is off or not connected

See also: [Shared Database Overview](#shared-database-overview), [Connecting to a Database Server](#connecting-to-a-database-server), [Database File or Database Server?](#database-file-or-database-server)

## Searching All Projects

*Search the clips of every project from the search field, and copy the ones you want into the open project. It needs a shared database: a database file on any plan, or a database server with Studio Pro.*

The search field in the toolbar has two scopes. This Project narrows the media list, as Filtering and Searching describes. All Projects searches the clips of every project in the shared database as you type, and lists what it finds in place of the media list.

### What It Needs

Searching every project needs a shared database, which keeps a record of every project’s clips so one search can look through them all. It can be either of these:

- A database file, on this Mac or on a network share. It works with any plan. One Mac uses it at a time
- A database server, so several Macs can use it at the same time. It needs Studio Pro

To set one up, open Settings › Storage; All Projects’ Set Up a Shared Database… button takes you there. For a database file, click New Database File… and choose where it will live, on this Mac or a network share: MediaFlow makes it, turns the database on and connects. Use an Existing Database File… uses one another Mac made. For a server, Database File or Database Server? has the steps.

A project is added to the shared database each time you save it with the database on. To add the projects you already have, choose Database → Migrate Projects… and pick their project files.

### Searching

`Cmd+Shift+F` — Search All Projects

1. Choose Edit → Search All Projects… (Cmd+Shift+F), or click in the search field and choose All Projects under it
2. Type a word or two. A clip is found by its file name (any part of it: 0042 finds GX010042.MP4), its notes, category, camera, scene or tags, or by its project’s name. Capital letters don’t matter, accented ones included (HĀNA finds Hāna), and every word you type must be found
3. Choose one or more clips in the results, then use the buttons above them, or right-click

### The Results

- One row for each clip in each project: a clip in two projects is listed twice, and a clip taken out of a project isn’t listed
- Each row shows the clip, its project, category, camera and tags, and where its file is. A green check means this Mac can reach the file now; an orange triangle means it can’t, and the clip can’t be added until it can
- A clip this project already has reads In this project, and can’t be added again. So does one you added before
- Clips in archived projects are listed too. Their files are usually on an archive drive: until it is connected, Where shows they can’t be reached, and Add to This Project skips them with that reason
- Choose one clip to see a preview and its details beside the list
- Up to 300 clips are listed, file-name matches first, then the newest. Type more words to narrow the search
- Choose This Project, or press Cmd+F, to go back to searching the open project

### Add to This Project

Add to This Project copies each chosen clip’s file into this project, the way an import does: into the working folder (Documents → MediaFlow Projects → Imports), where every copy is read back and compared with its file before the clip is added. Each comes in as a new clip of this project, with its category, camera, scene, shot, take, tags, notes and rating. When the other project’s file can be read, it also brings the clip’s transcript, GPS, weather and camera details. Then it goes through an import’s steps: the project is saved, the database is told, and the new clips are analyzed like any imported clip.

- A clip whose file can’t be reached, or whose copy doesn’t read back the same, is skipped. The summary says how many were added and from which project, and names each clip skipped, with the reason. The same clip chosen in two projects is copied once, from one whose file can be reached
- The other project isn’t changed, and nothing is deleted. Its clip stays where it is, and changing the copy here doesn’t change it there. The copy in the working folder is the new clip’s own original, as the card is for an imported clip: Free Up Space only ever offers that copy, Clear Card never offers the other project’s file for deletion because of it, and opening the other project later never takes the copy for its own
- A progress window shows the copying, and Cancel stops it; the clips copied before then are added. When it is done, Show in Finder in the notice shows the copies
- The working folder’s disk needs room for the clips plus 10 GB, as for an import
- Adding needs a plan that includes importing; searching doesn’t

### Open Its Project and Reveal in Finder

Open Its Project, or a double-click on a result, opens the project the clip is in, with the clip selected. If this project has unsaved changes, you are asked about them first. Reveal in Finder shows the chosen clips’ files in the Finder.

### In the Projects List

The Projects list, there when no project is open or from Projects → Browse Projects…, has the same search field in its toolbar, searching all projects only. While it has words in it, the results take the place of the list, under a line that says so, such as Showing clips in every project that match “beach”; Clear empties the field and brings the list back. Opening, switching or closing a project empties the field too, so a word left behind never hides your projects. Open Its Project (or a double-click) opens a clip’s project. With no project open, New Project with These Clips… makes a new project, exactly as File → New Project does, then adds the chosen clips to it as Add to This Project would; with the list shown over an open project, Add to This Project adds them to that project.

### When All Projects Can’t Search

Until it can search, All Projects says what it needs in place of the results, with a button for the next step. The line under the search field gives the same reason, shorter, and All Projects is dimmed there; Search All Projects (Cmd+Shift+F) still chooses it, and typing shows the whole message. This Project works as always.

- No shared database is set up — Set Up a Shared Database… opens Settings › Storage. Learn More opens this topic
- The shared database is turned off — Turn On & Connect turns it on and connects, as Database → Enable & Connect Database does
- It can’t be reached — the network share holding the file isn’t connected, or the server isn’t answering. Try Again connects once it is back. The last line of the Database menu says what happened
- Another Mac is using the database file — All Projects names that Mac, as the question at connecting does. Wait for, followed by the Mac’s name, connects as soon as that Mac has finished; see One Mac at a Time on a Database File
- Your plan doesn’t include the database server — Choose a Plan… shows the plans, and Storage Settings… opens Settings › Storage to use a database file, which works with any plan
- No other projects are in the shared database yet — said instead of “no results” when nothing else has been added. Migrate Projects… adds the projects you already have

> **Tip:** A project’s clips can be found once it has been saved with the database connected. Projects made before you turned the database on need Database → Migrate Projects.

See also: [Shared Database Overview](#shared-database-overview), [Database File or Database Server?](#database-file-or-database-server), [Migrating Projects to the Database](#migrating-projects-to-the-database), [One Mac at a Time on a Database File](#one-mac-at-a-time-on-a-database-file), [Filtering and Searching](#filtering-and-searching), [Searching All Projects Finds Nothing](#searching-all-projects-finds-nothing), [Importing from a Card, Drive or Folder](#importing-from-a-card-drive-or-folder)

## Finding Duplicate Files

*List files with identical content across projects and see how much space the extra copies use.*

1. Choose Database → Find Duplicates
2. MediaFlow looks through every project in the database for files with identical contents
3. Results are grouped. Each group shows how many copies there are, the size of each, and the space you could reclaim
4. Each group lists every copy with its location and project

Click Refresh to scan again after you make changes. Find Duplicates needs a connected database. It only reports; it does not delete anything.

See also: [Shared Database Overview](#shared-database-overview), [Storage Dashboard](#storage-dashboard)

## Migrating Projects to the Database

*Add existing .vpm project files to the shared database so its cross-project tools can see them.*

Migrate Projects reads project files and records them in the shared database. Use it for projects made before you turned the database on. It needs a connected database.

1. Choose Database → Migrate Projects
2. Click Choose Files to pick .vpm files, or Choose Folder to search a folder and everything inside it
3. Use Select All, Deselect All and the Filter files… field to decide which files to include. Add Files…, Add from Folder… and Add More… add to the list
4. Click Migrate Selected
5. A progress view shows each project as it is read
6. When it finishes, Per-Project Details shows how many clips were imported and how many were linked to entries the database already had

> **Tip:** Migration does not change your .vpm files. The database stores a copy of what they say.

To move the database itself between a database file and a database server, see Copying Records Between the File and the Server.

See also: [Shared Database Overview](#shared-database-overview), [Copying Records Between the File and the Server](#copying-records-between-the-file-and-the-server)

## Storage Dashboard

*See how full your shared storage is, how that has changed over time, and what the database holds.*

Choose Database → Storage Dashboard. It needs a connected database.

- Usage gauge — How full the volume was at the last snapshot, with total, used and available space
- Database Overview — Counts of Projects, Categories, Devices and Snapshots
- Capacity Trend — How usage has changed. It needs at least two snapshots
- Categories and Devices — What the database holds across all projects

### Where Snapshots Come From

### When a snapshot is recorded

A snapshot is a reading of how full the volume is. MediaFlow takes one when you open the dashboard, when you click Refresh, and whenever it re-checks a project’s files while the database is connected. The dashboard opens straight away on what it already has and adds the new reading a moment later, so a volume that is asleep or unplugged does not hold it up.

A reading is kept only when it tells you something the last one did not: an hour has passed, or the free space has changed by at least 1 GB (half a percent on a large volume). Two readings are never kept less than a minute apart, however often you click Refresh. A volume that cannot be read records nothing, so a disconnected drive does not show up as a drop to zero.

The bottom of the dashboard says how long ago the volume was last measured. When that is more than a day, it turns orange: the figures describe the volume as it was then. Connect the volume and click Refresh.

The dashboard shows the history of the network share chosen in Settings › Network. With no share chosen, the history is empty.

See also: [Shared Database Overview](#shared-database-overview), [Finding Duplicate Files](#finding-duplicate-files), [Storage Forecast](#storage-forecast), [Choosing and Connecting Your Network Share](#choosing-and-connecting-your-network-share)

## Database File or Database Server?

*The shared database is optional and can live in a database file for one Mac or on a database server for several.*

The shared database tracks clips across all your projects. It powers searching all projects, Find Duplicates, the Storage Dashboard and the project browser. It is optional: every project opens, imports and organizes from its project file without a database. The database is filled from what each Mac saves, and opening a project from its file never copies the database’s clips into it; Shared Database Overview says what a save sends and what it leaves alone.

If you turn it on, you choose where it keeps its records.

- Database file — a single file, usually on a network share. Nothing to install. One Mac at a time: each Mac works on its own copy of the file and writes it back when it disconnects or quits. MediaFlow keeps the turns: a second Mac is told which Mac has the file, and can wait for it or work without it
- Database server — a service that keeps the records itself, so several Macs can work at the same time. It needs network storage or a computer that stays on and can run containers

> **Tip:** Choose Database file if you work on one Mac, or have nothing that stays on to run a server. Choose Database server if two or more Macs use MediaFlow at the same time. You can move between them later, with your records.

### Choosing or switching

1. Open Settings › Storage
2. For a file, click New Database File… to make one where it will live, or Use an Existing Database File… to use one that is there, such as the one another Mac made. Either turns the database on and connects
3. For a server, turn on Enable Central Database, pick Database server under Store, and fill in Host, Port, Database, User and Password

MediaFlow works on this Mac’s own copy of a database file on a network share, and notes which file that copy belongs to. Whenever the database file changes, however it changed (the two buttons, a typed path, Reset to Default, a copy from the server, the setup wizard or a restored setup), the copy of the previous one is set aside (renamed and kept in MediaFlow’s cache folder, never deleted) and the file you chose is copied fresh, so another database never ends up in it. Changes still waiting to be sent to the previous database stay waiting for it, and go to it when you connect to it again; see Working Offline in Shared Database Overview. A copy made by an earlier version, which noted nothing, is set aside the same way the first time, unless the database itself shows it is the same one.

A working copy is removed only when MediaFlow has read it and its file whole and found them the same: it was sent back in full, and neither has changed since. Dates and sizes alone are never enough. When another Mac has written the file since this Mac last connected, the newer file replaces this Mac’s copy only when the two are the same; otherwise the copy is kept to one side first. A copy that holds only what this Mac last sent, checked the same way, is kept to one side quietly, in case the other Mac sent an older copy over it. One that may hold work the file doesn’t have is set aside the same way, and the work in it that the file lacks is sent again from your project files the next time MediaFlow connects to that file: each clip this Mac changed or added, each clip it removed or added back, and a project’s name, file and destination only if this Mac changed them. Only what this Mac wrote counts: rows the file doesn’t have, or that this Mac changed after the copy was last sent or taken. MediaFlow tells which changes came after by counting how many times the copy was sent or taken, not by the clock, so a clock that was wrong, or was changed, can’t hide a change or make an old one look new. What another Mac wrote is never counted, and Macs are told apart by their hardware, so a Mac renamed since still knows its own work and another Mac with the same network name is never taken for it. Only what this Mac’s saves sent counts. What MediaFlow filled in by itself (a clip’s length or format, or where its working copy is) is sent as your project file has it, those details alone, and only while the clip still names the same file; where a clip’s file was found is sent only while the database still shows the place this Mac’s check replaced, so another Mac’s archive or check since stays. An archive or a restore made on this Mac, which it records straight in the database, is recorded again the way it was first recorded, with its drives and its date, and a restore with where its clips are now (once its project file can be read). It isn’t when another Mac has changed that project since (archived it, restored it, even back to where it was, or saved it), or may have: an earlier version of MediaFlow saved the project last, and this Mac changed it again before archiving it. Nor is it when another Mac has given one of its drives the same number as a drive of its own, or when the project was changed on this Mac while the record waited to be recorded. What else it recorded straight in the database (a cleared card, an editing drive) isn’t sent again this way. Nothing else of those projects is sent, so a clip another Mac changed meanwhile, and you didn’t, keeps that Mac’s change. Changes an earlier version saved under this Mac’s network name alone can’t be told from another Mac’s of the same name, and changes an earlier version saved with only the clock to say when can’t be put in order for certain, so neither is sent. When it found work, found such changes, or couldn’t compare the copy with its file, MediaFlow tells you once where the copy is kept. A file that is only newer sends nothing back over it: a project another Mac deleted is never put back, a clip another Mac added back is never removed again, and a removal this Mac made that never reached the file is sent. A change MediaFlow couldn’t find stays out of the database until you change that clip again; your project files hold every change to your clips. Set-aside copies are kept for 30 days, then moved to the Trash, never deleted outright. A copy you renamed or duplicated yourself is left alone.

Switching the Store reconnects at once; you do not need to relaunch. Switching does not move any records. The other store keeps what it had, and its settings are remembered, so switching back finds it again.

### Taking your records with you

With Database server selected, two buttons copy every record in either direction: Copy the Database File to This Server… and Copy This Server to a Database File…. Neither changes its source.

See also: [Shared Database Overview](#shared-database-overview), [One Mac at a Time on a Database File](#one-mac-at-a-time-on-a-database-file), [Connecting to a Database Server](#connecting-to-a-database-server), [Copying Records Between the File and the Server](#copying-records-between-the-file-and-the-server), [Working Offline and Syncing Later](#working-offline-and-syncing-later), [Setting Up MediaFlow](#setting-up-mediaflow)

## Connecting to a Database Server

*Enter the server’s host, port, database, user and password in Settings › Storage, or use the guide to set one up.*

A database server lets several Macs use the shared database at the same time. The server keeps the records itself; nothing on this Mac is copied to or from it. The server must be PostgreSQL, free database software: one you already run will do, and Set Up a Server… starts one for you. If you already have one, fill in the fields. If you do not, Set Up a Server… walks you through making one in about ten minutes. The button is in Settings › Storage under either store, so you can prepare a server before switching to it. MediaFlow does not install anything on the server itself: the guide saves one file, docker-compose.yml, which the server’s container app runs. The guide shows the port the server will answer on, which is the one in the Port field, and offers to put it back to 5432 if it is something else; use that same port when you connect.

> **Warning:** The connection to the server is not encrypted. Use it only on a home or studio network you trust, and never forward the server’s port to the internet.

### The fields

- Host — the server’s name or address. When a network share is chosen in Settings › Network, a button beside the field offers its server. A name ending in .local keeps working when the address changes
- Port — 5432 unless you changed it
- Database and User — the names the setup guide creates are filled in for you. Change them to match an existing server
- Password — kept in your Keychain, never in preferences and never in the saved setup. What you type is saved when you press Return in the field, click Test Connection, click Set Up a Server… or close Settings, and only if it differs from what the field showed; typing and then deleting it changes nothing. Leaving it blank keeps the saved password: to remove it, click Remove Saved Password… beside the field, which asks first. If macOS would not let MediaFlow read the saved password, the field is blank, reads “Saved, but withheld by macOS” and says so under it, in Settings › Storage and in the setup wizard alike; the note goes once macOS lets MediaFlow read it. If macOS will not let MediaFlow save a password you typed, the form says so and the one saved before stays in use

Changes take effect without restarting: when Test Connection succeeds, and when you close Settings, MediaFlow connects to the server the fields now describe. When a message says the name was found, the Host is right and the Port is what to check: it must be the number the server was started with, the one before the colon on the ports line of docker-compose.yml.

The fields save as you type. On every other Mac, enter the same host, port and password; there is nothing to copy.

### Every Mac on the same version

Update MediaFlowSwift on every Mac that uses the server. Older versions saved whole copies of a project and could undo another Mac’s work, so once an up-to-date Mac has connected, the server refuses saves from those older versions. A Mac still on an older version can read the shared database, and its saves fail with “Update MediaFlowSwift on this Mac to keep working with the shared database”. Its changes stay in its project files and reach the server once it is updated. A later version that needs the same may ask every Mac to update again.

A database file can’t tell which version is writing to it, so there the refusal is up to each Mac: a Mac on this version or later won’t use a file a newer version has set up, but an older version still writes to the file as it always did. Update every Mac that uses the file too.

> **Tip:** A tool other than MediaFlowSwift that changes projects or clips on the server, such as psql, must first run SET mediaflow.protocol = '2'; without it the server refuses the change.

### Test Connection

A successful test says Connected, with the server’s version number, such as 16.4. A failed test says why:

- “…could not be found on the network” — the Host name is wrong. MediaFlow tries the name as typed and then with .local on the end, which is what most server names on a home network need; when that works, Test Connection corrects the Host field and says so. Otherwise use the server’s address
- “MediaFlow could not read the saved password from your Keychain” — the password is saved, but macOS would not hand it to this version without asking you. This happens once after an update. macOS cannot ask while the app is still opening, so MediaFlow tries again by itself a moment after its window appears: enter your Mac password when macOS asks, and click Always Allow. If you dismissed the question, choose Database → Enable & Connect Database (Reconnect Database while it is connected) to be asked again. macOS recognises an app across updates only when its maker has an Apple Developer ID; until MediaFlow has one, expect to be asked once after each update, for each password or key MediaFlow keeps
- “Nothing is listening at…” — the server is not running, or the port is wrong
- “macOS is keeping MediaFlowSwift off your local network…” — macOS has told MediaFlowSwift so. It often follows an update. Click Open Local Network Settings…, turn MediaFlowswift off and on again, and MediaFlowSwift connects by itself within a few seconds
- “…did not answer… macOS may be keeping MediaFlow off your local network” — macOS asks your leave before an app may reach other devices on your network, and refuses silently until you give it. Open System Settings › Privacy & Security › Local Network and turn MediaFlowswift on; if it is already on, turn it off and on again
- “…could not be found on the network” — the host name is wrong. Try the address instead
- “…did not answer within 10 seconds” — a firewall is blocking the port, or the server does not allow connections from this Mac
- “…is not reachable from this network” — this Mac is on a different network from the server
- “…closed the connection” — the server is configured to refuse this Mac
- A message from the server itself, such as “password authentication failed” — the password, database or user is not what the server expects

### Set Up a Server…

1. Click Save docker-compose.yml…. This file describes the server to a container app. It contains the password, so it is saved readable only by you. Keep it private
2. Put the file in a folder of its own on the network storage or computer that will run the server. The database keeps its data in a folder beside it
3. Start it: in your network storage’s container app, create a project from that folder. On a computer with Docker, run docker compose up -d in that folder. The first start takes a minute or two
4. Back in Settings, set Host and click Test Connection

### Which password goes in the file

- With no password stored yet, MediaFlow makes a new one, writes it into the file and puts it in your Keychain and the Password field
- With a password stored that macOS will not let MediaFlow read, the guide asks the same question as below. Use the password already in my Keychain then stops and says so, rather than writing a new password over the one your server may already use: choose Database → Enable & Connect Database (Reconnect Database while it is connected), click Always Allow when macOS asks, and save again
- The password goes into your Keychain before the file is written. If macOS will not let MediaFlow save it there, the file is not saved and the guide says so, since a server started from it would have a password this Mac does not know
- Use the password already in my Keychain — for saving the file again for the server you already use. A server reads its password only the first time it starts, so the file must keep the same one
- Make a new password — for a server that has never been started. It replaces the one in your Keychain, so MediaFlow can no longer sign in to the old server

The database server is part of Studio Pro; without it the app keeps working with a database file. See Plans and Pricing.

See also: [Database File or Database Server?](#database-file-or-database-server), [Copying Records Between the File and the Server](#copying-records-between-the-file-and-the-server), [Choosing and Connecting Your Network Share](#choosing-and-connecting-your-network-share), [Database Connection Issues](#database-connection-issues)

## Copying Records Between the File and the Server

*Copy every shared-database record from the database file to the database server or back; the source is never changed.*

When you move from a database file to a database server, or want a file copy of the server, MediaFlow copies every record for you. The copy reads the source and never changes or removes anything in it. Both buttons are in Settings › Storage, with Database server selected as the Store.

- Copy the Database File to This Server… — brings the records in your database file into the server. Use it when you first set up a server
- Copy This Server to a Database File… — writes the server’s records into a new file that you name. If you pick an existing file, it is replaced. Use it as a backup, or to work without the server

### If the destination already has records

The copy stops and tells you how many projects and clips are there. Click Replace to replace everything at the destination with the records being copied, or Cancel to leave it alone.

> **Warning:** Replace removes every record at the destination before copying. The source is not changed either way.

### Reading the progress list

Each table shows how many rows were copied. Two counts may appear beside it:

- Adjusted — a value was changed to fit the destination. Examples: a decimal rounded into a whole-number column, an unreadable number blanked, a reference to a category or volume that no longer exists cleared
- Left behind — a row the destination could not take. Example: a project membership that names a clip deleted long ago. Click the count to read the reason for each row

A file that has been in use for years usually holds a little of both. The search index is not copied; it is rebuilt at the destination from the copied rows.

### When it finishes

Click Switch to It Now to make the copy your store and reconnect, or Close to stay where you are.

### Cancelling or failing part-way

Click Cancel at any time. Tables already finished stay at the destination; the table in progress is undone. The destination is then incomplete, so run the copy again and choose Replace. If the two databases are at different versions, update MediaFlow on every Mac and try again.

See also: [Database File or Database Server?](#database-file-or-database-server), [Connecting to a Database Server](#connecting-to-a-database-server), [Shared Database Overview](#shared-database-overview), [Migrating Projects to the Database](#migrating-projects-to-the-database)

## Working Offline and Syncing Later

*Changes you make while the shared database is unreachable are remembered and synced when it reconnects.*

You can keep working when the shared database is out of reach, for example when the network share is offline or you are away from your network. Your edits are saved in the project file as usual. MediaFlow remembers which projects changed and syncs them to the database when it reconnects. You do not need to do anything.

### What happens on reconnect

The status line reads “Syncing offline changes…” while every project that changed is synced, not only the one that is open.

- The open project syncs, including clips you removed from it
- Every other project is read from its project file. Its clips are added and updated in the database, and the clips you removed from it on this Mac are recorded as removed. A clip the file doesn’t have is never taken out of the project: it may have been added on another Mac
- A project is left alone if the database already holds a newer version, changed on another Mac

### Projects that wait

A project stays on the waiting list, and is named in the status line, until you open it. This happens when:

- The database holds a newer version. Opening the project syncs it
- Its project file cannot be reached or read, for example because the drive it is on is not connected
- The database did not accept the sync

### The status line

The status line is at the bottom of the Database menu and in Settings › Storage. After a reconnect it takes one of two forms:

- Connected — everything is synced
- Connected · offline changes still to sync: followed by up to two project names and “and n more” — those projects are waiting. Open each one to finish

> **Tip:** With a database file, one Mac uses the database at a time; another is told which Mac has it, and can wait or work without it. With a database server, several Macs can reconnect and sync at once.

See also: [Shared Database Overview](#shared-database-overview), [Database File or Database Server?](#database-file-or-database-server), [One Mac at a Time on a Database File](#one-mac-at-a-time-on-a-database-file), [Database Connection Issues](#database-connection-issues), [Saving Projects](#saving-projects)

## One Mac at a Time on a Database File

*A database file is used by one Mac at a time. Another Mac is told which Mac has it, and can wait or work without it.*

With a database file, each Mac works on its own copy of the file and writes it back when it disconnects or quits. Two Macs using it at once would erase each other’s work, across every project. So MediaFlow lets one Mac use the file at a time. A database server has no such limit.

### How the turns are kept

A Mac that connects leaves a small file beside the database, mediaflow.session.lock. It names the person and the Mac and says since when. The Mac brings it up to date every minute while it is connected. When it disconnects, goes to sleep or quits, it writes its copy of the database back and then removes the file. If writing the copy back fails, the file is removed all the same, and the projects this Mac saved during its turn are noted and synced again the next time it connects.

### When another Mac has the database

A second Mac that tries to connect copies nothing. It says who has the file, for example “Sheri’s MacBook Pro (Sheri Williams) is using the shared database, since 10:42.” There are two choices:

- Wait — MediaFlow looks again every ten seconds and connects as soon as the other Mac disconnects or quits. The progress panel shows Waiting for the shared database, with the time it last looked. Click Stop Waiting to give up and work without it
- Work Without the Database — Keep working. Projects open and save as usual, and MediaFlow notes which ones changed and syncs them when this Mac connects, as in Working Offline and Syncing Later. The status line reads Working without the database

While you work without it, MediaFlow does not ask again each time it reconnects by itself, for example after the network share comes back. To ask again, click the database status in the toolbar or choose Database → Enable & Connect Database.

### A Mac that stopped answering

If a Mac crashes, or loses its connection to the file without disconnecting, its file stops being brought up to date. Once another Mac has seen it stand still for five minutes, counted on that Mac’s own clock so that two Macs set to slightly different times cannot mislead each other, it takes the database over and says whose it was: “Sheri’s MacBook Pro (Sheri Williams) had the shared database but stopped checking in at 10:42, so this Mac has taken it over.” A file that stopped more than a quarter of an hour ago is taken over at once. The takeover is written to the log (Help → Show Log). Anything that Mac had not written back is not in the database; its project files still have it. When that Mac next connects, its own copy of the database, which may hold that work, is set aside rather than replaced, and it says so when the copy holds work the file lacks (see Database File or Database Server?). The same Mac, opened again after a crash, takes its own turn back at once.

If a Mac finds that another took the database over while it was away, it stops using the database without writing its copy over the other Mac’s, and says so. Every project it saved during its turn, and the open one, syncs again when it next connects.

> **Tip:** If the file beside the database cannot be written, MediaFlow connects anyway, as before, and says so. Until it can, make sure no other Mac uses the database at the same time. Every Mac needs this version or later: an older one does not look for the file.

See also: [Database File or Database Server?](#database-file-or-database-server), [Working Offline and Syncing Later](#working-offline-and-syncing-later), [Shared Database Overview](#shared-database-overview), [Database Connection Issues](#database-connection-issues)

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

See also: [Re-check files](#re-check-files), [Clips Showing as Missing](#clips-showing-as-missing)

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

See also: [Storage Dashboard](#storage-dashboard), [Smart Notifications](#smart-notifications), [Organizing Media to Storage](#organizing-media-to-storage)

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

See also: [Generating Reports](#generating-reports), [Format Conformance Checker](#format-conformance-checker)

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

See also: [Smart Selects](#smart-selects), [NLE Template Export](#nle-template-export)

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

See also: [Dailies Report](#dailies-report), [Audio Levels](#audio-levels), [Generating Reports](#generating-reports)

---

# Publishing

## Preparing a Video for YouTube

*Choose your finished video, transcribe it, and get a title, description, chapters and tags to paste into YouTube.*

Prepare for YouTube works on the finished video you exported from your editor, not on the project’s clips. MediaFlow reads the file, transcribes what is said in it, and an SEO agent writes the words that go with it. You edit them, then copy them into YouTube or send the video from the Upload tab.

1. Choose Workflow → Prepare for YouTube…
2. Click Choose Video… and pick the exported video. MediaFlow shows its length and format. The file is only read; it is never changed and never sent anywhere
3. Click Transcribe. A long video takes a few minutes. The line under the button says whether the audio stays on this Mac
4. Fill in Your brief with what only you know: who the video is for, the tone you want, and anything the description must include, one item per line, such as links, credits or a call to action
5. Click Write with the SEO Agent. See The SEO Agent for what it does and what it sends. If a title, description or tags are already there, MediaFlow asks before replacing them
6. Edit anything you like. Click one of the other titles to use it instead. The checklist updates as you type
7. Click Copy beside the title, the description and the tags, and paste each into YouTube. The chapters are added to the end of the description when you copy it

Your draft is saved in the project’s folder, in Publish/publish-draft.json, a moment after each change and when you close the window. It moves, archives and restores with the project. A project that has not been saved yet has no folder, and the window says the draft cannot be kept until it has one. Choosing a different video clears the transcript, the chapters and the thumbnail’s frame, because they belong to the video they came from.

> **Tip:** You can use the checklist without the agent. Type your own title, description and tags, set the main phrase, and it checks them the same way.

See also: [The SEO Agent](#the-seo-agent), [The Publishing Checklist](#the-publishing-checklist), [Making a Thumbnail](#making-a-thumbnail), [Uploading to YouTube](#uploading-to-youtube), [Speech Transcription](#speech-transcription), [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac)

## The SEO Agent

*A model writes your title, description, chapters and tags in three passes, and checks its own work against YouTube’s rules before you see it.*

SEO means being found: in YouTube’s search, and chosen from the list of results. The agent works only from your video’s transcript and your brief. It is told never to invent facts, names, numbers or links, and never to promise what the video does not deliver.

### What It Does

1. Reads the transcript and works out what the video is, who it is for, and the main phrase: the few words someone would most likely type to find it
2. Writes a first draft: five titles that take different approaches, a description, chapters at the points where the subject changes, tags, and three suggestions for the words on the thumbnail
3. Checks the draft against the checklist, is given every fault it found, re-reads the draft as a viewer would, and revises. It always revises once, and again if something that must be fixed remains

The window shows each pass as it happens, and afterwards a line saying what the agent changed on its last revision. A revision that makes the draft worse is not used. Anything still wrong at the end shows in the checklist for you to fix: you have the last word. If the model’s chapters break YouTube’s rules and cannot be repaired, none are added and the Chapters field says why. If your API key is rejected, the spending limit is reached, or the Privacy switch is turned off while it is working, the agent stops and says so.

### Which Model

The agent uses the model chosen in Settings › Analysis: the model on this Mac, or Claude, ChatGPT or Gemini with your own API key. A paid provider writes noticeably better than a small model on this Mac, takes about a minute, and costs a few cents for a video. The model on this Mac is free and private but slow: allow ten to twenty minutes for a video, with the window showing which pass it is on. A small model sometimes cannot finish the revision. When that happens you get its first draft, the window says so, and the checklist shows what is left to fix. The daily spending limit in Settings › Analysis applies, and the agent stops before a request that would pass it.

### What Is Sent, and to Whom

With the model on this Mac, nothing leaves it. If you have pointed the local model at another computer on your network in Settings › Analysis, the transcript, the video’s length, your brief and the drafts go to that computer and no further; an address on the internet is refused. With a paid provider, the agent sends the transcript of the video you chose, the video’s length, your brief, and then its own drafts for revision, to that provider. It never sends the video, its file name, or anything else in the project.

This is off until you turn it on. In Settings › Privacy, switch on “A model that writes your YouTube title, description and tags”. While it is off and a paid provider is chosen, Write with the SEO Agent tells you where the switch is and sends nothing.

> **Warning:** Read what it writes before you publish it. The agent works from a transcript, and speech recognition mishears names, places and technical words. A wrong name in a title is your name on a mistake.

Writing with the agent is part of Studio Pro; see Plans and Pricing. The plan puts no monthly limit on it: a paid provider bills your own account, within the daily spending limit you set, and a model on this Mac costs nothing.

See also: [Preparing a Video for YouTube](#preparing-a-video-for-youtube), [The Publishing Checklist](#the-publishing-checklist), [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [Using a Model to Suggest Categories](#using-a-model-to-suggest-categories)

## The Publishing Checklist

*What the checklist checks, which items YouTube enforces and which are advice.*

The checklist beside the editor runs on whatever is in the fields, whether you or the agent wrote it. A red item is something YouTube enforces or that breaks a feature. A grey item is advice.

### Must Fix

- Title — not empty, and no more than 100 characters
- Description — not empty, and no more than 5,000 characters, chapters included
- The characters &lt; and > — YouTube does not accept them in a title or a description
- Your brief — every line under Must include appears in the description, word for word
- Chapters — the first starts at 0:00, there are at least three, none is shorter than 10 seconds, and none starts after the video ends. If any of these fails, YouTube shows no chapters at all
- Tags — no more than 500 characters in total, counted the way YouTube counts: commas included, and two extra for each tag that contains a space

### Advice

- Title length — past about 60 characters a title is cut off in search results, so the words that matter come first
- Main phrase — it appears in the title, early, and in the first 150 characters of the description, which is the part shown before “more”
- Capitals — a title written entirely in capitals is harder to scan
- Tags — there are some, and none is repeated. Tags matter less than the title and description; they help with alternate wordings and misspellings

The limits are YouTube’s. The advice is long-standing common ground about YouTube search, not a promise of how a video will rank.

See also: [Preparing a Video for YouTube](#preparing-a-video-for-youtube), [The SEO Agent](#the-seo-agent)

## Making a Thumbnail

*Pick a frame from your finished video, put a few words over it, and export a thumbnail that meets YouTube’s specification.*

The Thumbnail tab of Prepare for YouTube makes the picture that goes with your title. It works from the finished video you chose; the video is only read. Nothing leaves this Mac.

1. Choose Workflow → Prepare for YouTube…, choose your finished video if you have not, and click the Thumbnail tab
2. Drag the Frame slider to the moment you want. The picture follows roughly while you drag and settles on the exact frame when you let go
3. Or click Suggest Frames. MediaFlow looks through the video, leaving out the first and last twentieth where titles, fades and end cards live, and offers frames with the sharpest first. Click one to use it
4. Type the words. Press Return for a second line; two lines is the most. If the SEO agent has written for this video, its suggestions appear as buttons under the field
5. Choose where the words sit, their colour, and whether they have a dark band behind them. Size makes them smaller than the largest that fits
6. Click Export Thumbnail…. MediaFlow offers the project’s Publish folder

### What Is Exported

A JPEG, 1280 by 720 pixels, the 16:9 shape YouTube asks for, and under its 2 MB limit: MediaFlow lowers the JPEG quality a step at a time until the file fits, which for nearly every frame means not at all. A vertical or square video is cropped to its middle, never squashed.

### Words That Can Be Read

- The words are as large as will fit, and are shrunk to fit rather than cut off
- They have an outline in the opposite tone, so they hold against any picture. With the band off, a soft shadow lifts them off a bright background
- A thumbnail is seen small, often on a phone. Past about four words MediaFlow adds a note, because more is not read
- Let the words add to the title rather than repeat it: the stake, the result or the surprise. That is what the agent’s suggestions aim for, and they are only offered; your own words are never replaced

The frame, the words and their style are saved with your draft, so reopening the window shows the same thumbnail and exporting again gives the same file.

See also: [Preparing a Video for YouTube](#preparing-a-video-for-youtube), [The SEO Agent](#the-seo-agent)

## Uploading to YouTube

*Send the finished video, its words and its thumbnail to your channel from the Upload tab, with the visibility you choose.*

Uploading is off until you turn it on. Turn on Uploading to YouTube in Settings › Privacy, add a Google client of your own (see Setting Up Your Google Client), and sign in. Nothing is sent until you click Upload and confirm.

1. Choose Workflow → Prepare for YouTube… and click the Upload tab
2. Click Sign In to YouTube…. Your browser opens at Google; sign in there and pick the channel. MediaFlow never sees your password. It asks for the narrowest permission that can upload, which Google words as “Manage your YouTube videos”. It cannot read your channel or delete videos. It could also replace a thumbnail, watermark or banner; MediaFlow uses it only to send the video and its thumbnail
3. Choose the visibility: Private, Unlisted or Public. Or turn on Publish at a set time: the video goes up Private and YouTube makes it public at that time, which must be at least 15 minutes away
4. Answer Made for kids. YouTube requires the answer by law, and MediaFlow does not give it for you: the upload cannot start until you choose
5. Choose the category. Turn on Send the thumbnail from the Thumbnail tab if you made one; left off, YouTube picks a frame itself
6. Deal with anything listed in red. An upload does not start while the checklist on the Words tab has something that must be fixed
7. Click Upload to YouTube…. MediaFlow shows what is going, how large it is and how visible it will be. Click Upload to send it

### If Your Uploads Come Out Private

Google keeps every upload Private from a Google Cloud project that has not passed its audit, whatever visibility is asked for. A project you have just made has not. The video is safely on your channel: open it in YouTube Studio and change the visibility there. Google’s audit form is linked from the YouTube Data API page of your project.

### A Dropped Connection, or Stopping

The video is sent in pieces. If the connection drops, or YouTube is busy, MediaFlow waits, asks YouTube how much arrived, and carries on from there. It waits longer after each failure and gives up after ten in a row, a little over a quarter of an hour; being off the network altogether is simply waited out. If you click Stop or quit, what was sent is kept: the button reads Continue the Upload… next time, for about a week, unless you sign out. The upload starts again from the beginning if the video file has changed, or if you have changed the title, description, tags or settings, because an unfinished upload carries the words it was started with; MediaFlow tells you so before it begins. Only YouTube letting the upload lapse, a changed video or changed details start it again: an expired sign-in, a full allowance or a dropped connection never do. A publish time is fixed when the upload starts, so for a large video on a slow connection choose a time well ahead.

### The Thumbnail

The thumbnail is sent after the video. YouTube accepts custom thumbnails only from a channel verified by phone (youtube.com/verify). If it is refused, the video is still up: MediaFlow says so, and Send the Thumbnail to This Video tries again without uploading the video again. You can also export the thumbnail and add it in YouTube Studio.

### What Is Kept

- Your sign-in is kept in the Keychain, never in a file. Sign Out forgets it, forgets any unfinished upload, and asks Google to cancel the permission. If both YouTube switches are off in Settings › Privacy, Google is not contacted: MediaFlow says so, and you can remove it yourself at myaccount.google.com/permissions
- Removing the client secret in Settings stops any upload, signs you out the same way, and then forgets the secret
- Publish/upload-state.json in the project’s folder records which file went up, when, the video’s ID, and the words and settings it went up with. The address of an unfinished upload is kept in the Keychain, not in that file
- Uploading a video that has already gone up asks first, because it makes a second copy on your channel

### What the Database Records

When an upload finishes, MediaFlow adds the video to the shared database, if you use one. It is kept there, in the published_videos table, as the record of what you have published across all your projects. Nothing about it is sent anywhere else.

- The project, the video’s YouTube ID, its title and main phrase
- The file’s name and size, the video’s length and format
- When the upload started and finished, and how long it took from start to finish, stops included. If the app was closed as the last piece arrived, the finish is the moment MediaFlow next asked YouTube, and how long it took is left empty
- The visibility you asked for (recorded as scheduled when you set a publish time), that time, your made-for-kids answer and the category
- When it went live, where MediaFlow can know: the end of the upload for a Public video, the set time for a scheduled one, or the end of the upload if that came later. It is left empty for Private and Unlisted videos
- Whether the thumbnail was sent, and its words
- The length of the title and description, the tags and how many, the number of chapters, the number of words in the transcript, and which model wrote the words

These are the words and settings the video went up with, even if you edit the draft afterwards. If the database was not connected when the upload finished, the video is added the next time you open Prepare for YouTube for that project, or upload from it; a later upload does not push it aside. The visibility is what you asked for: MediaFlow’s permission cannot read your channel, so if Google kept a Public video Private, or you changed it in YouTube Studio, the database does not know. Turning on statistics changes that: see How Your Videos Are Doing.

> **Tip:** An upload uses most of a new Google Cloud project’s daily allowance of 10,000 units: 1,600 for the video and 50 for the thumbnail. That is about six videos a day. The allowance resets at midnight Pacific time.

Uploading, and reading results, are part of Studio Pro; see Plans and Pricing. The plan puts no monthly limit on them: they run on your own Google Cloud project, whose daily allowance is the only limit.

See also: [Setting Up Your Google Client](#setting-up-your-google-client), [How Your Videos Are Doing](#how-your-videos-are-doing), [Preparing a Video for YouTube](#preparing-a-video-for-youtube), [The Publishing Checklist](#the-publishing-checklist), [Making a Thumbnail](#making-a-thumbnail), [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac)

## Setting Up Your Google Client

*MediaFlow uploads through a Google Cloud project of your own. Making one takes about ten minutes and is free.*

Google requires every app that uploads to YouTube to identify itself with a client. MediaFlow uses one that belongs to you, so your uploads count against your own allowance and nobody else stands between you and your channel. You do this once.

1. In your browser, open console.cloud.google.com and sign in with the Google account that owns your channel
2. Create a project. Any name will do
3. Under APIs & Services › Library, find YouTube Data API v3 and click Enable. If you will read statistics, enable YouTube Analytics API too
4. Under APIs & Services › OAuth consent screen, choose External, give the app a name and your email address, and save. Add your own Google account under Test users
5. Under APIs & Services › Credentials, click Create Credentials › OAuth client ID, and choose the application type Desktop app
6. Copy the client ID and the client secret Google shows you
7. In MediaFlow, open Settings › Analysis. Under YouTube, paste the client ID, paste the secret and click Save

The client ID is kept in MediaFlow’s settings. The secret is kept in the Keychain, never in a file, the saved setup or a log.

### What to Expect at Sign-In

- Google shows a warning that the app is not verified, because the project is yours and has not been through Google’s review. Click Advanced, then continue. Only the test users you listed can sign in
- While the consent screen is in Testing, Google ends the sign-in after seven days and you sign in again. Publishing the consent screen, under the same page, makes it last
- Until the project passes Google’s audit, YouTube keeps its uploads Private. See Uploading to YouTube

> **Warning:** The type must be Desktop app. A Web application client is refused at sign-in, because it does not allow the answer to come back to this Mac.

See also: [Uploading to YouTube](#uploading-to-youtube), [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac)

## How Your Videos Are Doing

*The Results tab lists what you have published and, if you allow it, reads each video’s views, watch time and more from YouTube and keeps them over time.*

The Results tab of Prepare for YouTube shows the videos MediaFlow uploaded, from this project or from all of them: when each went up, its size and length, the visibility you asked for and when it went live. This comes from your shared database and needs nothing from YouTube. Without a database connected, the tab says so.

### Reading Statistics from YouTube

This is off until you turn it on, and it needs more permission than uploading does.

1. Turn on Reading your videos’ statistics from YouTube in Settings › Privacy
2. In your Google Cloud project, under APIs & Services › Library, enable YouTube Analytics API as well as YouTube Data API v3
3. On the Upload tab, sign out if you are signed in, then sign in again. Google now asks for two more permissions, both read-only: View your YouTube account, and View YouTube Analytics reports for your YouTube content. If you untick both at Google you can still upload, and the Results tab tells you statistics were not allowed. Ticking only one is no use, and Google cannot take back one alone, so MediaFlow hands the whole sign-in back and asks you to sign in again
4. On the Results tab, click Read from YouTube Now

MediaFlow asks Google which channel you signed in to, then sends the YouTube IDs of the videos your database records as uploaded by MediaFlow, and the span of dates from the first upload to today. Nothing else. The two permissions would allow reading your whole channel; MediaFlow asks only about those videos. If your database is shared with someone who publishes to another channel, answers about their videos are set aside, not kept as yours. Neither permission can change or delete anything.

You can turn on statistics without uploading: with only that switch on, sign-in asks for the two read-only permissions alone, and the Upload tab says the sign-in cannot upload.

### What Is Read and Kept

- Views, likes and comments, as YouTube shows them now
- Hours watched, the average view as a time and as a share of the video, subscribers gained and shares, from YouTube Analytics. These run a day or two behind the counters, so a new video shows a dash at first
- The visibility the video really has, and when it really went public. If you asked for Public and YouTube has it Private, the tab says so: Google holds uploads Private from a Google Cloud project that has not passed its audit

Each reading is kept in the published_video_stats table of your database, about one a day for each video (never within 20 hours of the last), so you can see a video at a day, a week and a month. The tab shows the latest numbers and the views gained since the reading before. Reading again sooner updates nothing but the visibility. Statistics are read only when you click the button; nothing is read in the background.

> **Tip:** MediaFlow does not read impressions or click-through rate; look for them in YouTube Studio. The YouTube Studio link beside each video opens it there.

See also: [Uploading to YouTube](#uploading-to-youtube), [Setting Up Your Google Client](#setting-up-your-google-client), [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac)

---

# Project Management

## Saving Projects

*Save the project file (.vpm), save it under a new name, or go back to the last saved version.*

- Save (Cmd+S) — Save the current project to its existing location
- Save As (Cmd+Shift+S) — Save the project file under a new name or in a new place, and carry on working in the new file. Media files are not copied. With a shared database, the new file becomes where the project lives for every Mac that shares it, and the file you left is its old copy. Save As from an old copy of a project only makes another copy: the project stays where it lives
- Revert to Saved — Discard all unsaved changes and reload from disk

A project is saved as a .vpm file. It holds the list of clips and where their files are, plus your categories, tags, ratings, notes and project settings. It does not contain the media itself.

The project file holds the whole project. When the shared database is connected, each save also sends the database what changed on this Mac, and as a rule leaves clips you didn’t change as the database has them; What a Save Sends in Shared Database Overview says when it doesn’t. If the database cannot be reached, MediaFlow notes that the project changed and sends the changes when the connection returns.

### When Another Mac Saved the File Too

Two Macs can have the same project file open, on a share both reach. Before each save, MediaFlow checks whether the file changed since this Mac opened it or last saved it. Every save writes a new save number at the start of the file; while the file’s date and size are as this Mac left them, nothing more is read, and a file that was only touched costs a look at its first few bytes, so a save over the network costs no more than before. The file is replaced only if it is still as that check found it: if the other Mac saves in the moment between, MediaFlow looks again.

- If the other Mac saved the file meanwhile, its changes are merged in before this Mac writes: the clips it added come in, with their transcripts, sound levels and other details, and the clips it removed are removed here too
- A clip changed on both Macs keeps both changes when they are to different things: a rating made there and a note written here both stay. The project’s own settings merge the same way: its name, destination, categories and devices, shot list, storyboard, the projects it shares media with, where its library copy is, and its archive record (whether it is archived, and to which drive)
- When both Macs changed the same thing differently (the same clip’s note, the storyboard, or the archive record), this Mac’s change is kept. The other Mac’s version of the whole project is kept in a folder called Copies Kept Aside, beside the project file, as “name (changed on another Mac date time).vpm”, and a notice says how many clips differed, with Show in Finder. It is written once for each such save, not at every save after it
- A clip removed on one Mac but changed on the other since is kept, and counts as a change on both sides. When the Mac that removed it saves next, the clip stays: keeping it came after the removal
- A file that holds another project, or can’t be read, is never saved over. That happens when a project opened from the shared database alone finds another project’s file where its own used to be. This Mac’s copy is saved in Copies Kept Aside as “name (this Mac’s copy date time).vpm”, and kept up to date there, until the project file can be read as this project again. New Project likewise won’t make a project where a project file of that name already is

A copy kept aside opens like any project file, to look at or to copy back from. It says it is a copy kept aside, is never sent to the shared database, and is passed over by Library Moved and by Migrate Projects. Delete the folder once you have what you need from it.

With the shared database connected, the merged project is what the database gets too. A clip brought in from the other Mac’s save doesn’t undo a removal the database has recorded for it, and isn’t written back as this Mac’s change, even when the database was out of reach at the time and MediaFlow was quit before it came back.

See also: [Moving a Project](#moving-a-project), [Renaming a Project](#renaming-a-project), [Duplicating a Project](#duplicating-a-project), [Working Offline and Syncing Later](#working-offline-and-syncing-later), [Shared Database Overview](#shared-database-overview)

## Renaming a Project

*Change the open project’s name. Its project file is renamed to match; the project folder and the media keep their names.*

1. Choose File → Rename Project
2. Enter the new project name in the dialog
3. Click Rename. The project file is renamed to match, in the folder it is already in. Click Rename, Keep File Name if you want the name changed in MediaFlow only

Renaming changes the project’s name in MediaFlow: in the window, in the recent and browse lists, and in the shared database if it is connected. The project is saved straight away, and any edits still waiting to be saved are written first.

### What happens to the file

- A project called “Alaska 2026” gets the file Alaska 2026.vpm. A slash or a colon in the name becomes a hyphen in the file name, because a file name cannot hold them
- If the folder already holds a file with that name, nothing is renamed and MediaFlow says so. Choose a different name, or keep the file name
- If the project cannot be saved under the new name, the file goes back to its old name and the project keeps its old name
- The project folder is not renamed and no media is moved, so no clip can go Missing because of a rename

See also: [Saving Projects](#saving-projects), [Moving a Project](#moving-a-project)

## Moving a Project

*Copy the whole project folder to a new place, check the copy, then decide whether to delete the original.*

1. Choose File → Move Project To
2. Select the new parent folder for the project
3. MediaFlow copies the entire project folder to the new location. If a folder with the project’s name is already there, the move stops before copying anything
4. All internal paths (clip URLs, thumbnails, etc.) are updated automatically, and the project is saved in its new folder
5. When you close the progress window, MediaFlow asks whether to delete the original folder

### What is checked before the original can go

Every file is read back after it is copied and compared with its original by checksum, and the copy must account for every file in the original folder, including hidden files. Permissions, Finder tags, and dates travel with each file. If any file fails, the partial copy is removed, the original is left exactly as it was, and the project stays where it is. The summary tells you how many files were copied and verified.

The question about deleting the original is answered some time after the copy was made, so MediaFlow checks again at that moment. It deletes the original only if the copy can still be reached, still holds every file of the original, and is where the open project now lives, and only if the original is still exactly what was copied. Before copying, MediaFlow notes each file’s size and when it was last changed; a file added to the original since, or changed since even under the same name (an editing app saving into the old folder, say), keeps the original, and the message names the file. So does a shortcut in the copy that still points into the original, which would lead nowhere once the original is gone (the copy’s shortcuts into the project point into the copy). So does a file or folder whose name starts with .incoming- or .superseded- followed by an eight-character code of digits and the letters A to F, and a dash: MediaFlow gives those names to its own unfinished copies, so no copy, move or archive ever takes them, and a Move leaves them exactly where they are. Rename it if it holds your work. The project file itself is the exception: the moved project writes its own afresh, and MediaFlow may save the old one while the copy runs. A rewrite to the same size within a second or two of the copy cannot be told apart on some network shares, so close any app using the old folder first. If the drive holding the copy has been unplugged, or you have opened a different project, the original is kept and MediaFlow says why. On a local drive the original goes to the Trash; on a network volume there is no Trash and it is deleted outright.

If the project cannot be saved in its new folder, MediaFlow puts the project back at its original location and tells you. The copy is left in place for you to inspect or delete.

The progress window shows each file being copied and then checked, as the Copying and Checking steps. To save time, the next file is already being copied while the last one is checked; a file counts only once its own check has passed, and if any check fails, everything stops and the partial copy is removed. The bar and the time left move through both, even inside a single large file.

Cancel on the progress window stops the copy at once, even part-way through copying or checking a large file. The original project folder is never touched, so nothing is lost, and the partly copied folder is removed.

> **Tip:** Moving copies every file in the project folder, so check that the new location has enough free space first.

See also: [Saving Projects](#saving-projects), [Deleting a Project](#deleting-a-project)

## Editing on an Editing Drive

*Copy the project you are editing to your fastest drive, keep the library copy safe where it is, and bring the project back when the edit is done.*

A library lives on large storage, which is rarely the fastest you own. An editing drive is a folder on fast storage, such as an SSD volume on your network storage or an external SSD, for the projects you are editing now. Clips there start sooner, scrub more smoothly and drop fewer frames, in MediaFlowSwift and in your editor.

1. Open Settings → Storage and choose the Editing drive folder. You do this once
2. Open the project and choose File → Move to Editing Drive…
3. MediaFlowSwift measures the project and shows how many files and how much will be copied, where to, and how much room is free there. Click Move to Editing Drive

### What Happens

- The whole project folder is copied into the editing drive folder, under its own name. Every file is read back and compared with the original, and the number of files is checked. If anything differs the copy is removed and the project stays where it was: the progress window then says the move didn’t finish, that the copy in your library is unchanged, and that the part-made copy was removed. The progress window shows each file being copied and then checked, with the bar and the time left moving even inside a large file
- A Final Cut Pro library keeps shortcuts of its own inside it: to its cache, which is often on another drive, and to its media, usually in the project’s own folders. Each is copied as a shortcut, never as a copy of what it points to. One that points inside the project follows it: in the copy it points to the same file in the copy, so Final Cut finds its media on the editing drive. One that points anywhere else, even to a drive that is not connected, is copied as it is and does not stop the move. Shortcuts count as nothing in the size shown. MediaFlowSwift looks at each item itself to tell a shortcut from a file, because some network storage lists shortcuts as ordinary files
- The project then points at the copy: its project file, its destination and every clip inside the project folder. Clips kept outside the project folder are not copied and keep pointing where they did
- The copy in your library is kept exactly as it is. Nothing is deleted and nothing in it is changed, including its project file. The project remembers where that copy is
- Cancel stops the copy at once, even part-way through a large file or its check; the partial copy is removed and the project is unchanged. The same happens if the project cannot be saved in the copy
- This Mac also keeps its own note of where the library copy is, so the way back is not lost if the editing drive is unplugged and the project is opened another way

### When It Is Refused

Nothing is copied if no editing drive folder has been chosen or it cannot be reached, if the project is already on the editing drive, if a folder with the project’s name is already there, if one folder is inside the other, or if the editing drive does not have room for the project and a little over. Nor if the project folder cannot be reached, or while an import, organize, archive, proxy run or Library Moved is running: it is refused with a message, not queued. Everything is asked again when you click Move to Editing Drive, in case the sheet has been open a while.

### Returning to the Library

When the edit is finished, open the project from the editing drive and choose File → Return to Library…. MediaFlowSwift looks at both copies and shows what is new or changed on the editing drive, such as exports, renders and notes. Everything is ticked to begin with; untick anything you do not want in the library. It also says how many files are in both places already, and how many are in the library only, which are left as they are.

- Each ticked file is copied to the library, read back and compared. A shortcut, such as one a Final Cut Pro library made, is carried as a shortcut; one that points into the editing copy points to the same file in the library, and must lead to it. A shortcut that is in both places counts as the same when it points to the same place in each. A new file is never written over something already there
- A changed file goes in beside the library’s own version, which is kept and renamed with “(before return)”. Nothing in the library is replaced or deleted
- Every file that is in both places is read in both places and compared. The same name and the same size is not taken as proof
- If anything cannot be carried or proved, the project stays on the editing drive, nothing is removed, and the list says which files. What was already carried stays in the library. A file that turned out to differ from the library’s, although it is the same size, is on the checklist as changed the next time you choose Return to Library, so it can be carried in beside the library’s own
- Close your editor first. A file that is written to while it is being read or copied is not counted, and one that changes after it was checked keeps the editing copy from being removed
- Then the project is saved in the library, pointing at the library’s files. The project file that was in the library is kept beside it as Name.vpm.before-repoint
- Afterwards, choose Remove the editing copy or Keep the editing copy. It is removed only after one more look finds every file in it still exactly as it was when it was carried or checked, apart from those you unticked, and after the shared database, if you use one, has been told the project is home. A file named like MediaFlow’s own unfinished copies (starting .incoming- or .superseded-), or like the notes it keeps on archive drives (.mediaflow-leg.json, .mediaflow-archive), is never carried home, so it keeps the editing copy, and is named. It goes to the Trash where that works; on a network share, which has no Trash, it is deleted. Kept, its project file is renamed Name.vpm.returned, so there are not two of the project to open
- If you untick files and choose to remove the editing copy, those files exist nowhere else. MediaFlowSwift names them and asks first

Proving the library copy means reading it, so expect roughly the time it would take to copy the project from the library. Stop abandons the file being carried or checked at once: a half-carried file is removed and the library’s own version, if it had one, is put back. The project stays on the editing drive and nothing is removed. Once everything is checked and the project is being saved in the library, Stop is no longer offered. If you use a shared database it must be connected.

### In the Projects List, and on Another Mac

- A project that is out shows On editing drive beside its name in the projects list. Hover over it to see where its library copy is
- If the editing drive is not connected when you open such a project, MediaFlowSwift offers to open the library copy instead, to look at. It is as the project was when it went out, and changes made in it are not brought across
- With a shared database, every Mac sees which projects are out. Opening the library copy on another Mac says what it is, and Cleanup and Free Up Space on that Mac leave it alone from then on. A return made on one Mac is picked up by another the next time it opens the project with the database connected, once it can see that the editing copy is gone. Until then that Mac goes on treating the library copy with care, which is the safe mistake
- Opening the library copy never moves the project: the projects list and the database go on pointing at the editing drive, and nothing saved in the library copy is sent to the database
- If you move your library while a project is out, run Library Moved as usual. It points the library copy at the new location like any other project, leaves the projects list and the database pointing at the editing drive, and tells the project where its library copy is now, so Return to Library goes to the right place. Close the library copy first if you have it open. Return to Library itself checks that the folder it is about to use holds this very project, and does nothing if it does not

> **Warning:** While a project is on the editing drive, work in that copy. The library copy is a safety net, not a second place to edit: changes made to it are not brought across. If you open the library copy on this Mac while the project is out, MediaFlowSwift says so.

On a Mac that knows a project is out, Cleanup and Free Up Space never take a file out of its library copy, even where it looks like a spare copy of a clip on the editing drive. The Mac that sent it out knows at once; another Mac knows from the first time it opens the project or its library copy with the shared database connected.

> **Tip:** Copying writes the whole project across. Over a wireless connection that can be slow; a wired connection to the drive is many times faster.

The editing drive is part of the Studio plan; see Plans and Pricing.

See also: [Moving a Project](#moving-a-project), [After Moving Your Library to a New Drive](#after-moving-your-library-to-a-new-drive), [Processing the Proxy Queue](#processing-the-proxy-queue)

## After Moving Your Library to a New Drive

*When you have copied your whole library to a new drive yourself, Library Moved points every project at the new place. Nothing is copied.*

Use this when the footage is already where you want it: you copied your projects folder to a new drive or network share, keeping the folders inside it as they were, and every project still points at the old one. Move Project is for the other case, where MediaFlowSwift does the copying.

1. Make sure both drives are connected
2. Choose Workflow → Repair → Library Moved…
3. Set Was in to the folder your projects used to be in, and Is now in to the folder that holds the same projects now. MediaFlowSwift suggests the folder your recent projects share, and the destination new projects use
4. Click Find Projects. Nothing is changed yet. Each project file found under the old folder is listed with how many of its clips are at the same place under the new one
5. Click Check and Point. Projects are done one at a time, and you can stop at any point

### What Is Checked

A clip is followed only if a file is at the same place under the new folder and is the same size. If the clip was checksummed when it was organized, the file at the new place is also read in full and compared, because Clear Card later trusts that checksum: same name and same size is not proof. A clip with no recorded checksum is followed on its size. A clip that is missing, a different size, or different inside keeps pointing where it did and is listed.

### What Changes

- The project is saved at the new location, with its proved clips, its destination, and any proxies and thumbnails kept with it pointing there
- If a copy of the project file came across with the folder, MediaFlowSwift works out which of the two holds your latest work. A plain copy is older than the file you have been using, so the work starts from the old one. If you have opened and changed the project at the new location, or part of it was followed before, the work continues from that one, so nothing you did there is lost. If the project has been worked in at the new location and the old file was changed again afterwards, neither holds everything: the list says “changed at both places” and the project is left alone for you to decide. Open the one you want to keep, save it, and run Library Moved again. Otherwise the file that was at the new location is kept beside the new one as Name.vpm.before-repoint, never overwritten, and the new file is written and read back before anything is put in its place
- If a different project is at the same place under the new location, neither is touched, and the list says so. If a project file has been copied in Finder, the two are one project: only one is followed, the one already followed on an earlier run, or else the one your projects list knows
- The project you have open is followed like any other, from what is on screen rather than what was last saved, and stays open at the new location. If the open project was opened from the file that is not being used, it is left alone: close it and run Library Moved again
- A project with no organized clips, such as one you are still planning, is pointed at the new location too; there is nothing to check
- The library copy of a project that is out on an editing drive is pointed at the new location too, but the projects list and the database go on pointing at the editing drive, and the project is told where its library copy is now
- The projects list and the shared database are updated. If you use a shared database it must be connected before Check and Point will start, because only the database records where an archived project was archived to, and that record is carried into the project before anything is written
- Nothing is copied, moved or deleted on either drive, and the old project file is not touched. Keep the old drive until you are satisfied; MediaFlowSwift does not use it again for a project that was fully followed

### The Old Copy of a Project

Library Moved never changes or removes the project file at the old location, so that file still opens, under the same name. It is an old copy: its clips point at the old location, so they read Not at destination, and work done in it stays in it. When you open one on the Mac that ran Library Moved, MediaFlowSwift says “This is an old copy” and offers to open the current copy instead. It knows from its own note of what Library Moved did. For a library moved before this version, choose Library Moved again with the same two folders and click Find Projects: every project already followed is noted, and nothing is changed. Another Mac has no such note until Library Moved has been opened on it the same way. Separately, if a project file is kept apart from its destination folder and another file for the same project is found in that folder, MediaFlowSwift says “There is another copy”, shows where each is and when each was saved, and does not claim to know which is current. With the shared database connected, the database settles it: if it records the copy you opened as the project, nothing is asked, and if it records the other copy, the question says so. Your answer is a decision about where the project lives, and is recorded at once in this Mac’s projects list and in the shared database. Open the Current Copy (or Open the Other Copy) makes that copy the project’s home, so it is the one that opens next time. Use This Copy and Don’t Ask Again, offered when MediaFlowSwift does not know which copy is current, makes the open copy the home and stops the question for that file. Stay Here only looks: nothing is recorded, this Mac’s projects list points at the other copy, saves made here are not sent to the database (the status line says Not synced), and you are asked again next time.

The same question is asked when the shared database records the project as living in another file that is still there. A project is written to the database only from the file the database says it lives at, unless that file is gone, Library Moved has noted it as the old copy, or you have said otherwise. That is what keeps a stale copy, opened by mistake on any Mac, from overwriting what every Mac sees. When the old drive is retired, the old copies go with it.

If the file the database names is not there at all when you open a project from the projects list — the drive is off, or the project was moved without Library Moved — MediaFlowSwift looks for the project where it may be: where Library Moved noted it went, in its destination folder, and in its library folder if it is out on an editing drive. A file that holds this very project is opened, and the projects list and the database are pointed at it. If none is found, the project opens from the database alone and one notice says so. Your changes are then kept in the shared database, and the project file is left as it is until its drive is back, when saving to it resumes on its own (what only the file keeps is kept), or until you choose Save As to give the project a new home. If you quit before the drive is back, the file has not caught up: open the project from the projects list again rather than by the file, and it comes from the database.

When the file the database names is in someone else’s user folder (/Users/…), it is on another Mac, and this Mac will never reach it. The notice says so first, then what happens to your changes and what to do, and names the folder last; it does not offer Save As. Your changes still go to the shared database, but the project file on that Mac does not get them. To work on a project from two Macs, open it on the Mac that has its file and choose File › Move Project To… to put it on a share both Macs reach.

The database’s copy of a project is not all of it. Transcripts, sound levels, GPS, weather and camera details, the checklist, the shot list, the storyboard and retired categories are kept only in the project file. So Save As from a project opened from the database alone asks first, and says what the new file will be without. If you save onto a file of this same project (a copy someone put on the share, say), the two are merged: what the database keeps comes from the database, what only that file keeps is kept, and clips only that file has stay in the project unless they were removed. Saving onto such a file needs the database connected, to know which clips were removed.

### Stopping and Running It Again

Stop ends the reading within a moment and leaves the project being checked exactly as it was; projects already finished stay finished. Running Library Moved again skips projects that already point at the new location and reads only what is left: a project whose folder you copied across later, or the clips of a project that could not be followed the first time. It cannot start while an import, organize, archive, move, relink or Clear Card is running. While it runs, organizing, refiling, Clear Card, Free Up Space, archiving and restoring, Move Project, Change Destination, relinking, workflow steps and installing an update are all refused until it has finished. Importing is not: new clips join the open project and are kept.

The progress bar moves as each clip is finished, not while one is being read. The line under it names the clip being read and its size, so a long clip does not look like a stall.

> **Tip:** Reading every checksummed clip takes as long as copying it would. On a wireless connection expect about a minute for every 4 GB.

See also: [Moving a Project](#moving-a-project), [Change destination folder](#change-destination-folder), [Clear Card](#clear-card)

## Deleting a Project

*Take a project off the project list, or also delete its folder and everything in it.*

Choose Projects → Browse Projects… to show the Projects list, right-click a project and choose Delete Project…. You are offered two things:

- Remove from List Only — Takes the entry off the list. Every file stays on disk
- Move Folder to Trash — Takes the entry off the list and deletes the project folder with everything in it

Move Folder to Trash does not act at once. MediaFlow first counts what is in the folder and shows a second confirmation with the number of files and their total size. You must tick “I understand this cannot be undone” before the confirm button works.

After you confirm, a progress window shows the folder being deleted. Clicking its Cancel in the moment before the deleting starts keeps the folder; the project is still taken off the list. Once the deleting has started it runs to the end.

> **Warning:** The project folder usually holds media files as well as the project file. On a disk in this Mac the folder goes to the Trash, where you can still recover it. A network share has no Trash, so the folder is deleted outright and cannot be recovered.

See also: [Moving a Project](#moving-a-project), [Opening an Existing Project](#opening-an-existing-project)

## Moving Clips Between Projects

*Move selected clips out of the open project and into another project.*

1. Select the clips you want to move
2. Choose File → Move Assets to Project, or right-click and choose Move to Project…
3. The project picker shows all available projects
4. Select the target project and click the Move button, which shows how many clips will move
5. MediaFlow adds the clips to the target project and removes them from this one

> **Tip:** Both projects are saved automatically after the transfer. If the database is connected, both are synced.

See also: [Selecting Clips](#selecting-clips), [Saving Projects](#saving-projects)

## Duplicating a Project

*Duplicate asks whether the new project shares this one’s media files or gets verified copies of its own.*

Duplicate gives you a second project that starts as a copy of this one: the same clips, categories, tags, ratings, notes, shot list and storyboard. It asks one question first, because the answer decides what deleting a clip will mean.

### Share Media

A second project over the same files. It is quick and takes no space, and it suits a second edit of the same shoot. But the files are shared: deleting or moving a clip in either project affects both.

- Both projects are marked, each naming the other. Before anything that deletes or moves media — Free Up Space, deleting the original after Move Project, deleting the project folder, deleting the organized copy after an archive — the confirmation says which project uses the same files
- Shared files are never re-filed. Changing a clip’s category still changes the category, but the file stays where it is, because moving it would make it go missing from the other project. Re-file folders by category does nothing for the same reason, and says why
- Notes, ratings, categories and tags are separate from then on. A change in one project does not appear in the other

### Copy Media Too

Every clip is copied into a folder you choose for the duplicate. Each copy is read back and its SHA-256 compared with the original before the duplicate points at it. It takes as long, and as much space, as the media itself, and you can keep working while it runs.

- A clip that cannot be copied — the file is not reachable, or the copy does not verify — is listed with the reason. It stays shared with the original, and both projects are marked. A copy that fails to verify is removed, not left behind
- You can stop part way. What was copied is kept; the rest stays shared
- The duplicate is saved as its own project file and added to File → Open Recent. The project you were working in stays open

### To duplicate a project

1. Choose File → Duplicate
2. Choose Share Media or Copy Media Too…
3. Choose a name and place for the new project file. MediaFlow suggests the project name followed by “Copy”
4. For Copy Media Too, choose or create the folder the copies go in

With Share Media the duplicate becomes the open project; open the original again with File → Open Recent. Clips in the proxy queue are not queued in the duplicate.

> **Tip:** To stop two projects sharing, duplicate the one you want to keep working in with Copy Media Too. The new project has files of its own and can be re-filed freely.

See also: [Saving Projects](#saving-projects), [Moving a Project](#moving-a-project), [Deleting a Project](#deleting-a-project), [Freeing Up Space](#freeing-up-space), [What Happens to Files When You Change a Category](#what-happens-to-files-when-you-change-a-category)

## Archiving a Project to USB

*Copy a finished project folder to a numbered USB drive for long-term storage, with every file checked before the original may go.*

Archive to USB frees your working storage by copying a finished project to a drive you can put on a shelf. It copies the whole project folder to a removable drive, checks the copy, and records where it went in the central database. Archive volumes are numbered (USB #0001, USB #0002, …) so a project can always be found again. Only the project folder is copied; media organized to a destination outside the project folder is not included.

### Archiving

1. Plug in the drive and choose Workflow → Archive to USB…; click Scan if it is not listed
2. A drive that has never been used shows “(not initialized)”. Select it, give it an optional label such as “Interviews 2026”, and click Set Up. MediaFlow writes a hidden marker file to the drive and assigns the next number. Numbers are permanent
3. Pick a drive. The smallest initialized drive that still fits is marked Recommended; drives that are too small show an orange warning
4. Click Archive. Progress moves through Preparing, Copying and Checking (each file is written, then read back; the bar and the time left move through both, even inside a large file), Flushing, Verifying, Updating Database, and Done
5. Dismiss the progress dialog to reach the completion screen described below

Every file is read back from the drive after it is written and compared with its original by checksum, so a file damaged on the way — even one that kept its size — fails the archive rather than being recorded. The Verifying step then confirms the number of files and their total size. Because each file is read twice, archiving takes longer than a plain copy, most of all on a USB hard drive or with a project made of many small files; to save time, the next file is already being copied while the last one is checked, and a file counts only once its own check has passed. File contents and dates are archived; Finder tags and similar extras are not, because most archive drives are formatted in a way that cannot hold them. On success the project is marked Archived with the volume number, date, and path. Its project file records the archive too, so the project still shows as archived when you open it again. The copy of the project file on the drive is left exactly as it was checked, and it shows as archived too when you open it from the drive, even with no shared database: the drive and the project folder on it say so, and the pipeline strip names the drive. In the project browser the row reads “Archived → USB #0007”.

### Completion screen

After the progress dialog closes, an Archive Complete screen summarizes the result — “Archived 312 files (48.2 GB) to USB #0007 · verified” — and lists the drive (or every drive, for a split archive) with an Eject button for each one that is still connected. “Keep Original” closes the screen and leaves both copies in place. “Delete Original…” removes the original project folder, wherever it is stored. It scans the folder first and then shows the same confirmation used when you delete staged files or delete a project: the file count, the total size, a warning when the folder is on a network volume (where there is no Trash to recover from), and a checkbox you must tick before the delete button enables. Confirming moves the folder to the Trash, or deletes it outright on a network volume.

Before it offers, and again at the moment of deleting, MediaFlow checks the folder against what this archive copied. Just before archiving it notes each file’s size and when it was last changed, and it keeps that note only for the files the archive then copied and checked. The folder is deleted only if every file in it is one of those, unchanged. A file the archive did not copy (one added since, one added after a split archive was planned, or one moved out of the folder while the archive ran and put back afterwards) or one changed since, even under the same name, keeps the folder; the message names it and offers Archive Again. Finder’s own .DS_Store files are left out. Once the archive is done, MediaFlow writes where the archive is into the project file; that change of its own does not count, but any other change to the project file does, and the delete button waits until that write is over. A file or folder whose name starts with .incoming- or .superseded- followed by an eight-character code of digits and the letters A to F, and a dash is never archived, because MediaFlow gives those names to its own unfinished copies; nor is a .mediaflow-leg.json or .mediaflow-archive file, a note MediaFlow keeps on an archive drive about that drive. Either keeps the folder and is named, and the Archive Complete screen stays open, saying why, so that once you have renamed or removed the file, Delete Original works. An archive that cannot finish says why in the progress window. A split archive that picked up drives written in an earlier session is not deleted from here, because those drives were matched by size only; archive the project again in one go, or delete the folder by hand. A change of the same size within a second or two of the note cannot be told apart on some drives.

> **Warning:** Deleting the original leaves the USB drive as the only copy of the project. Every file on it was compared with its original by checksum, but a single drive can still fail on the shelf; for footage you cannot replace, archive to a second drive as well before you delete. “Delete Original…” is disabled when the database update was queued instead of saved; keep the original until the database has recorded the archive.

### Archiving a project again

If the drive already holds an archive of the project, the new archive is written beside it and checked first. Only when every file has passed is the old archive replaced. If the new archive fails or you cancel, the old one is left exactly as it was.

- MediaFlow will not archive a project folder that holds none of the project’s clips. This matters most after you have deleted the original: the archive on the drive may be the only copy, and archiving an empty folder over it would destroy it
- MediaFlow will not replace an archive with one that holds fewer files. If the project really has shrunk because you removed clips on purpose, archive it to a different drive, or remove the old archive from the drive yourself first
- If the app quits or the drive is unplugged at the moment of replacement, the previous archive is put back the next time you archive or restore that project

### Splitting Across Drives

If the project is larger than any one drive, click Split Across Drives…. MediaFlow plans which folders go on Drive 1, Drive 2, and so on, hidden files and folders included, then asks for each drive in turn. Every file is read back and checked as it is copied, and the archive fails if a drive then no longer holds every file copied to it, in full. Files an earlier run left on the drive do not make up for one that is missing. If a run is interrupted, opening the sheet again detects the partial copies and the button reads Resume Archive. Shortcuts inside the project, such as a Final Cut Pro library’s, take no room in the plan and are archived as shortcuts. One that points inside the project points to where its file was archived: on the same drive, or on an earlier one of the set; one whose file goes on a later drive points to the same place on its own drive. After a restore every one of them points into the restored project, and so does one archived by an earlier version of MediaFlow, which still points into the project’s own folder, even when that folder is gone.

### Cancelling

Cancel on the progress window stops an archive between files. Files already written to the drive stay there. A split archive that is stopped part way can be picked up later with Resume Archive.

Archiving needs the central database to record volumes and projects.

See also: [Restoring an Archived Project](#restoring-an-archived-project), [Managing Archive Volumes](#managing-archive-volumes), [Shared Database Overview](#shared-database-overview), [Freeing Up Space](#freeing-up-space), [Moving a Project](#moving-a-project)

## Restoring an Archived Project

*Bring a project back from its USB archive drive, or drives, with every file checked against the archive.*

To bring an archived project back, open the project browser, right-click the archived project, and choose Restore from Archive…. Restoring needs the central database, which records which drive holds each project.

1. Plug in the archive drive. It does not have to mount under the same name it had when you archived; MediaFlow looks for the project on every connected archive drive
2. Choose the folder to restore into. The project comes back as a folder inside it, with the name it was archived under. If a folder with that name is already there, the restore stops before copying anything; choose a different folder
3. For a project split across drives, MediaFlow asks for each drive in turn and merges them into the one folder
4. When it finishes, the project is no longer marked Archived and its clips point at the restored files. An earlier copy of it, such as the original you kept after archiving, is not marked Archived either when you open it with the database connected and this Mac can reach the restored copy: the database records the restored copy as the project

A restore is checked more strictly than an archive. Every file is read back after it is copied and compared with the file on the drive by checksum. Each drive is also checked against the number of files recorded when the project was archived, so a drive that has lost a file since then stops the restore rather than quietly bringing back less than you archived. (Projects archived before this check was added have no recorded count for a single drive; those are checked file by file only.) If anything fails, the partly restored folder is removed, the project stays marked Archived, and nothing on the drive is changed. The same happens if you click Cancel, which stops at once, even part-way through copying or checking a large file.

If the project lists a clip that was not on any of the drives, the restore still completes and tells you which clips: they are marked Missing, not shown as present. Media the project used from outside its own folder was never copied to the archive, so it is left where it was and shown as In Place if it is still there, or Missing if it is not.

> **Warning:** Do not erase an archive drive just because a restore succeeded. Open the restored project and play a few clips first.

See also: [Archiving a Project to USB](#archiving-a-project-to-usb), [Managing Archive Volumes](#managing-archive-volumes), [Shared Database Overview](#shared-database-overview)

## Managing Archive Volumes

*See every numbered archive drive, what is on it, and whether it is connected.*

File → Manage Archive Volumes lists every registered drive with its number, label, used space, and whether it is currently connected. Select a volume to edit its label, see capacity and creation date, and view the projects archived on it with their sizes. A drive that carries a marker but is missing from the database is registered automatically the next time it appears in the archive sheet.

> **Tip:** Label each drive on the outside with its USB number so the numbers in the app match the shelf.

See also: [Archiving a Project to USB](#archiving-a-project-to-usb), [Restoring an Archived Project](#restoring-an-archived-project)

---

# Settings & Preferences

## Plans and Pricing

*Two plans, Studio and Studio Pro, a 14-day trial of the full app, and what stays open when a plan ends.*

MediaFlowSwift comes in two plans. Studio is all the file management: importing from cards, phones and folders; categorizing, reviewing, rating and tagging; Organize with every copy proved; Free Up Space; Archive and restore; proxies; the editing drive; Library Moved; reports; Help; updates and problem reports. Studio Pro is everything in Studio, plus the title, description, chapters and tags written for you, uploading to YouTube with thumbnail and schedule, results read back from YouTube, and the database server that gives every Mac the same projects list. Neither plan limits how often you use what it opens.

### The trial

The first time this copy is opened, a 14-day trial of Studio Pro begins. No card is asked for. Settings › Plan shows how many days are left, and a banner in the main window says so too; Later hides it for this session. The trial’s start is kept in your Keychain, not in the preferences, so installing the app again does not start it again, and a clock turned back does not lengthen it.

### When a plan ends

Nothing you have made is taken away. Every project opens, every clip shows where it is, restoring from an archive and copying footage out work, and so do Help, reports, updates and problem reports. What pauses is what makes new work: importing, Organize, proxies, moving a project to the editing drive, writing, publishing, and the database server. Each of those says which plan opens it, with a Plans… button that shows the plans side by side.

### Buying a plan

Studio is $4.99 a month or $49.99 a year; Studio Pro is $9.99 a month or $99.99 a year, in US dollars, plus tax where it applies. Plans are bought on mediaflowswift.com; the app never asks for a card. The checkout is run by Paddle, who handle payment, tax and invoices, and whose receipt has the link for managing or cancelling a subscription.

### Changing your plan

Already subscribed, and want Studio Pro instead of Studio, Studio instead of Studio Pro, or yearly instead of monthly? Do not buy again on the website: that starts a second subscription, with a second key, while the first one goes on billing. Write to support@mediaflowswift.com instead. Support changes the subscription you have, and your key stays the same: Settings › Plan shows the new plan at the next daily check, or at once when you click Check now.

While a subscription is entered on this Mac, the Plans window and Settings › Plan say this in place of Buy on the website…, with an Email Support… button. The button only opens a new message to support in your mail app, addressed and with the last group of your key in it, for you to finish and send; MediaFlowSwift sends nothing itself. When a licence has ended, Buy on the website… comes back, since a new plan is a new purchase.

### Your licence key

After buying, the thank-you page shows a licence key of the form MF-XXXXX-XXXXX-XXXXX-XXXXX. Enter it in Settings › Plan (or in the Plans window that a paused feature opens) and click Activate. The key follows you, not a Mac: it works on up to three Macs at once, and Settings › Plan lists them by name. Release this Mac frees its place for another; it needs a connection, so that the place is really freed before the key is forgotten here. Settings shows only the last group of the key, so a screenshot does not hand it on. Lost the key? The website’s Lost your key page finds it from the transaction number on your receipt.

Once a day, and when you click Check now, the app asks the licence service whether the key still stands: it sends the key and a random id it made up for this Mac, nothing more (the Mac’s name goes only with the activation), and it says so in Settings › Privacy. Without a connection the last answer holds for two weeks, so a trip does not pause your work. When a subscription ends, or is refunded, the plan reads as ended at the next check, and everything you made still opens. A complimentary key, one given rather than bought, has no subscription behind it: Settings › Plan shows the date it is valid until instead of a renewal date, and the plan reads as ended at the first check after that date.

See also: [The Settings Window](#the-settings-window), [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [Importing from a Card, Drive or Folder](#importing-from-a-card-drive-or-folder), [Organizing Media to Storage](#organizing-media-to-storage), [Preparing a Video for YouTube](#preparing-a-video-for-youtube), [Connecting to a Database Server](#connecting-to-a-database-server)

## The Settings Window

*What each of the nine Settings tabs is for: General, Network, Storage, Cameras, Categories, Analysis, Privacy, Notifications and Plan.*

Choose MediaFlow → Settings (Cmd+,). The window has nine tabs. This topic says what each one is for; the related topics go into detail.

### General

- Setup — Run Setup Again… reopens the first-run setup questions. MediaFlow saves your setup whenever you quit and puts it back if this Mac’s settings are ever lost. Save Setup Now saves it at once. Restore Saved Setup puts every saved setting back, replacing what is set now. Passwords and API keys are not part of the saved setup; they stay in the Keychain
- Updates — New versions come from mediaflowswift.com. “Check for new versions automatically” looks shortly after launch, on wake and every few hours; a new version asks Install Now, Later or Skip This Version, never while something is running, while you are typing or while another dialog is open. A version you skipped is shown here, with Offer It Again. To look now, choose MediaFlow → Check for Updates…, which always offers the newest version
- About — The version and build you are running, the maker, what MediaFlowSwift needs to run (a Mac with Apple silicon and macOS 14 Sonoma or later), links to the website, the support page, the terms of use and the privacy page, and Acknowledgements… for the open-source packages it is built with. The same as MediaFlowSwift → About MediaFlowSwift

### Network

Where you choose the network share that MediaFlow reconnects to. Nothing is assumed: until you choose one, the tab says “No network share chosen yet”.

- Shares already mounted on this Mac are listed. Click Use this beside the one you want; it then reads In use
- Look for servers searches the network. Connect to… opens a found server in Finder, which asks for the password and shows its shares. Mount one, then click Use this
- Type the address instead takes an smb:// address. A name ending in .local keeps working when the server gets a new address
- Once a share is chosen, the tab shows Connected or Not connected. Connect now mounts it again. Forget stops using it, and the settings that follow the share go back to unset

### Storage

- Enable Central Database — Turns the shared database on and connects
- Store — Database file or Database server. Changing it reconnects; it does not move any records
- Database file — New Database File… asks where a new database file will live, makes it there and connects; Use an Existing Database File… picks one that is already there, such as the one another Mac made. Neither ever replaces a file. The line under them says what a database file is for. Type the path instead is there if you need it. The line below says whether the file can be reached. Reset to Default points at MediaFlow/mediaflow.db on the chosen network share, and is dimmed until a share is chosen
- Database server — Host (a button beside it offers the server of the chosen network share), Port, Database, User and Password. The password is kept in your Keychain. Test Connection shows the server version or the reason it failed. Set Up a Server… is a guide to making one. Two Copy buttons move every record between the file and the server
- Organize Media — “Default destination for new projects” (Choose… or Clear) fills in the destination for a project that has none; a project’s own destination always wins
- Verify organized copies by reading them back — On: every copy is read again in full and its SHA-256 compared with the source; slowest and safest. Off: copies are checked by size plus 1 MB samples at the start, middle and end; much faster over a network

### Cameras

- The open project’s camera list: add, rename or remove cameras, with the number of clips that use each. Also use for new projects makes the list the starting point for new projects. With no project open, there is nothing to edit
- Suggest import when a camera or card is connected — Shows a banner that offers to start Import when you connect an SD card, a camera or an iPhone
- Camera identities — How MediaFlow knows which camera shot a clip. It matches by serial number first, then by model. Cameras it has seen but you have not named are under Not yet named: type a name and click Save. Those you have named are under Named. You can also add one by hand, by Serial or Model

### Categories

- The open project’s category list: add, rename, retire, restore or remove categories, with the number of clips in each. Categories marked “built in” cannot be renamed or removed. Also use for new projects makes the list the starting point for new projects
- Category Learning — What this Mac has learned from the categories you assign. Reset Pattern Memory clears what this Mac has learned. It does not clear the shared corrections recorded in the shared database, which every Mac on that database learns from

### Analysis

- Use a model to suggest categories — Lets you use an AI model, running on this Mac or at a provider you pay. An import uses the model only when you tick the box for it in the Import sheet. For a paid provider you add an API key, which is kept in the Keychain, and can set a spending limit with “Stop after … a day”
- Propose category, camera and scene after an import — After an import finishes, MediaFlow examines each clip on this Mac and proposes values. Proposals appear in italic and are not applied until you confirm them
- Also look at the pictures and listen to the first minute (Tier 1) — A second, slower pass. Off by default. You can turn it on for the open project only, or run it over the open project now

### Privacy

Every connection MediaFlow can make to a service outside this Mac, each with its own switch. All are off until you turn them on. Each row says what is sent and to whom. See Privacy: What Leaves This Mac.

### Notifications

One switch for each Smart Notification: Uncategorized Clips, Missing Cards, Format Mismatch, Storage Warning, Unrated Clips and Stale Project.

See also: [The Settings Window, Tab by Tab](#the-settings-window-tab-by-tab), [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [Setting Up MediaFlow](#setting-up-mediaflow), [Choosing and Connecting Your Network Share](#choosing-and-connecting-your-network-share), [Saved Setup: A Copy of Your Settings](#saved-setup-a-copy-of-your-settings), [Updating MediaFlow](#updating-mediaflow), [Database File or Database Server?](#database-file-or-database-server), [Connecting to a Database Server](#connecting-to-a-database-server), [Adding, Renaming, Retiring and Removing Categories](#adding-renaming-retiring-and-removing-categories), [Using a Model to Suggest Categories](#using-a-model-to-suggest-categories), [How MediaFlow Verifies Copies](#how-mediaflow-verifies-copies), [Smart Notifications](#smart-notifications)

## Smart Notifications

*The banner at the top of the window that points out unfinished work in the open project.*

When a project opens or changes, MediaFlow checks it against these conditions and shows the first one that applies as a banner above the media list. Each banner has an action button where one makes sense, and an X button that opens a menu with Dismiss and “Don’t show again for this project”.

### Notification Types

- Uncategorized Clips — 5 or more clips without a category; action: Auto-Suggest
- Unorganized Media — not a banner. The Organize segment of the pipeline strip always shows the pending count, and turns orange at 10 or more clips when a destination is set
- Missing Cards — One camera has far fewer clips than the others (under 30% of the average), which may mean a card was not imported
- Format Mismatch — 3 or more clips differ from the dominant resolution or frame rate; action: Check Formats
- Storage Warning — The destination volume is 85% full or more; action: Storage Forecast
- Unrated Clips — 20 or more clips have no star rating
- Stale Project — No changes for 7 days or more

Turn individual types off in Settings › Notifications. A “Don’t show again for this project” choice is remembered across launches; a plain Dismiss hides the banner only until MediaFlow next checks the project, so it can come back. A device-connection banner takes precedence while a card or phone is being detected.

See also: [The Settings Window](#the-settings-window), [Understanding the Pipeline Strip](#understanding-the-pipeline-strip), [Auto-Suggest Categories](#auto-suggest-categories), [Storage Forecast](#storage-forecast), [Format Conformance Checker](#format-conformance-checker)

---

# Keyboard Shortcuts

## Keyboard Shortcuts Reference

*Every keyboard shortcut in MediaFlow, grouped by menu, plus the single keys used in Review and the video preview.*

Menu shortcuts work anywhere in the main window. The Review keys work while Review is open (Workflow → Review); they are single keys with no modifier. In Review and in the Import sheet, Space plays and pauses the video showing, whatever you clicked last, except while you are typing in a text field. The Video Playback keys work while the video preview has keyboard focus: click the preview first.

### File Operations

`Cmd+N` — New Project

`Cmd+Shift+N` — Create Project From Folder…

`Cmd+O` — Open…

`Cmd+S` — Save

`Cmd+Shift+S` — Save As…

`Cmd+W` — Close Project

---

### View

`Cmd+Opt+T` — Move Media to Top/Bottom

`Cmd+Opt+P` — Move Preview to Left/Right

---

### Search & Projects

`Cmd+Shift+F` — Search All Projects…

`Cmd+Shift+P` — Browse Projects…

---

### Editing

`Cmd+F` — Find Clips… (search this project)

`Delete` — Remove from Project (in the clip list or grid, not while typing)

---

### Ratings & Selects

`Cmd+1` — Rate 1 Star

`Cmd+2` — Rate 2 Stars

`Cmd+3` — Rate 3 Stars

`Cmd+4` — Rate 4 Stars

`Cmd+5` — Rate 5 Stars

`Cmd+0` — Clear Rating

`Cmd+Shift+H` — Select › Hero

`Cmd+Shift+M` — Select › Maybe

`Cmd+Shift+K` — Select › Reject

---

### Workflow

`Cmd+Shift+R` — Run Workflow Template…

`Cmd+Opt+R` — Review

`Cmd+Opt+M` — Shoot Map…

`Cmd+U` — Create Subclip… (one video selected)

`Cmd+Shift+T` — Increment Take (Scene Log tab)

---

### Review

`Space` — Play or pause

`J / K / L` — Shuttle reverse, stop, forward (press again to go faster)

`← / →` — Step one frame back or forward

`Home / End` — Jump to the start or end of the clip

`↑ / ↓` — Previous or next clip

`1–5` — Set the star rating

`0` — Clear the star rating

`F` — Toggle Favorite

`X` — Toggle Reject

`C` — Toggle circle take

`I / O` — Mark the in or out point

`A` — Accept proposed category / camera (in Rapid Review)

`R` — Mark reject candidate (in Rapid Review)

`T` — Toggle auto-advance (in Rapid Review)

`M` — Show or hide the metadata overlay

`?` — Show or hide the key help

`Esc` — Close the key help, or leave Review

---

### Import

`Space` — Play or pause the preview

`Esc` — Close the sheet without importing

---

### Video Playback

`Space` — Play or pause the preview

`I` — Mark In Point

`O` — Mark Out Point

---

### Help

`Cmd+/` — MediaFlow Help

---

### Settings

`Cmd+,` — Settings…

---

### Undo and Redo

These come from the standard Edit menu. They undo and redo changes to categories, tags, notes, ratings and selects.

`Cmd+Z` — Undo

`Cmd+Shift+Z` — Redo

See also: [Reviewing Clips with the Keyboard](#reviewing-clips-with-the-keyboard), [Star Ratings & Selects](#star-ratings--selects), [Undo and Redo](#undo-and-redo), [Extracting Thumbnails and Subclips](#extracting-thumbnails-and-subclips)

---

# Troubleshooting

## Clips Showing as Missing

*A red X in the Where column means MediaFlow cannot find the file; usually a drive or share is not mounted, or the file moved.*

Symptom: a clip shows a red X and the word Missing in the Where column. MediaFlow cannot find the file at any path it has recorded for it.

### Causes

- The drive or network share that holds the file is not mounted
- The file was moved or renamed outside MediaFlow
- The share or drive mounted under a different name than before

### Fixes

1. Mount the drive or share. For the network share you chose in Settings › Network, click Connect now there, or choose Database → Reconnect Network Share. Then choose Workflow → Repair → Re-check files
2. If the files moved, choose Workflow → Repair → Relink Missing Media and pick the folder they are in now
3. If the whole destination moved, choose Workflow → Repair → Change destination folder
4. For one file, right-click the clip, choose Relink… and pick the file

### On another Mac and Not on this Mac are not Missing

A clip imported on another Mac that shares this project usually sits in that person’s home folder. When its file is in another account’s home folder, it reads On another Mac on this Mac, in grey, not Missing. It is not in the Missing group or the missing counts, and Relink Missing Media leaves it alone. Work with it on the Mac it was imported on. To use a copy you have on this Mac instead, right-click the clip, choose Relink… and pick the file.

A clip the other Mac keeps anywhere else, such as in the Shared folder, on its own drive, or in a home folder with the same name as yours, reads Not on this Mac instead, in grey, for as long as this Mac has never had it. Each Mac remembers the clips it has imported, organized or relinked, and the files Re-check files has found on it; only those can read Missing on it. Everything above holds for it too: it is not counted as missing, and Relink… can point it at a copy on this Mac. If you use only this Mac, a clip that reads Not on this Mac may have been moved or deleted: use Relink… to find it.

The first time a Mac checks a project file after the update, or another copy of it such as one made with Save As, it checks it as before, so a file that went missing before the update reads Missing. A clip from the other Mac may read Missing once, until that Mac checks it again.

See also: [Relinking Missing Media](#relinking-missing-media), [Change destination folder](#change-destination-folder), [Understanding the Where Column](#understanding-the-where-column), [Choosing and Connecting Your Network Share](#choosing-and-connecting-your-network-share)

## Reporting a Problem

*Put together a report of what went wrong, with personal details taken out, to email to support from your own mail app, copy or save.*

Choose Help → Report a Problem…, or click Report a Problem… where it is offered: on an error message, and under the list of files that failed in a copy. Say what happened and what you were doing, and leave an email address if you would like a reply. MediaFlowSwift adds what helps find a fault, and shows you the whole report before anything else happens. You can change any of it.

### What Is in a Report

- What you wrote, exactly as you wrote it
- The version of MediaFlowSwift and of macOS, whether the Mac is Apple silicon or Intel, the kind of shared database you use (never its address), and how many clips are in the open project
- A summary of any crashes and hangs macOS recorded for MediaFlowSwift in the last two weeks: what kind of failure, how often (times are in UTC), and where in the program it happened. Two sources say so: the report files macOS writes in Logs/DiagnosticReports in your Library, of which MediaFlowSwift reads only the ones about itself, not those of another program that shares its name, and MetricKit, Apple’s service that hands an app its own crash and hang diagnostics on a later launch. The same fault told by both is counted once. Neither leaves your Mac unless you send a report
- Whether the last run ended without quitting
- The last 150 lines of MediaFlowSwift’s log (Help → Show Log)

### What Is Taken Out

Before you see the report, MediaFlowSwift takes out of everything it adds, including an error message it quotes: your account name and home folder; the names of your drives; every folder and file name in a path, which becomes /…/&lt;file>.mp4, keeping only the kind of file; the names of the projects this Mac knows and of the open project’s clips and cameras; the names and addresses of your computers and servers; email addresses; and map coordinates. Drives, computers, projects and clips are numbered, so the same drive is &lt;drive-1> all the way through and the report can still be followed. From a crash report it takes only the fields listed above: the device identifier and account details Apple puts in those files are never picked up. Passwords, keys and tokens are never in the log or a report; they live only in your Keychain.

It errs on the side of taking out too much. It cannot know a name it has never been told, such as a project on another Mac mentioned in the log, so read the report over; and what you type yourself is left exactly as you typed it. Once you edit the report, the fields above it stop changing it, so nothing you wrote is lost; Start Again from the Fields Above makes it afresh.

### Sending It

Email Report… opens a new message to support@mediaflowswift.com in your own mail app, with the report exactly as it is in the window, for you to read and send. A short report is filled in for you. A longer one, which most are once the log is in, would not fit in a new message in every mail app, so MediaFlowSwift puts it on the clipboard instead and the message asks you to paste it in (⌘V). MediaFlowSwift itself makes no connection: the report goes only if you send the message, from your own email, so support can reply to you there.

Copy Report puts the text on the clipboard; Save… writes it to a file; sending it however you like is up to you.

On a Mac set up with a report relay run by MediaFlowSwift’s maker there is also a Send button. It needs Sending problem reports turned on in Settings › Privacy, and the relay’s address and key entered there; until a relay is set up those fields are folded away, since a customer has no relay and emails reports instead. Send sends the text exactly as it is in the window, with a title, a random identifier for this copy of the app, and the crash signature if there is one, to that relay, which files it as an issue for the people who make MediaFlowSwift, and the window then shows the report’s number. If the same crash has been reported before, your report is added to it. Nothing is ever sent on its own, and while the switch is off MediaFlowSwift makes no connection to do with reports.

### After a Crash

If MediaFlowSwift quit unexpectedly, or did not quit cleanly (a force-quit, or the Mac losing power), it says so once, the next time it opens, and offers a report. If macOS itself stopped the app, for instance because of how this copy was installed or signed, it says that instead: it is not something you did.

### Problems That Are Yours to Fix

A full disk, a drive that is locked, cannot be read or written, or is no longer connected, a network drive that stopped answering, a folder MediaFlowSwift is not allowed to use: these are not faults in the program, and a report about one would tell nobody anything. On an error message, and under the list of files that failed in an import, organize, archive or move, MediaFlowSwift says which it is and what to do about it, and does not offer to report it. Help → Report a Problem… is always there if you disagree.

Some failures could be either. A file that is not where it was expected may be on a drive that is unplugged, or may be a mistake in the program; so may a timeout, or a damaged database file. For these MediaFlowSwift says what to try and offers a report as well.

See also: [Contacting Support](#contacting-support), [Database Connection Issues](#database-connection-issues), [Clips Showing as Missing](#clips-showing-as-missing)

## Contacting Support

*Write to support from your own mail app, or read the support page on the website. MediaFlowSwift sends nothing itself.*

Choose Help → Contact Support… to write to support@mediaflowswift.com. It opens a new message in your own mail app, addressed to support, with this copy’s version and build, your macOS version and your Mac’s chip filled in at the bottom: the first things support needs to know. Nothing else about you, your Mac or your projects is in it. Write your question above them and send it as you would any email; support replies to the address you send from. We aim to reply within two working days.

Choose Help → Support Website to open mediaflowswift.com’s support page in your web browser, with answers to common questions.

Something went wrong? Help → Report a Problem… puts together what support needs to find a fault, with personal details taken out, and Email Report… there hands it to your mail app in the same way. See Reporting a Problem.

> **Tip:** If your mail app does not open, or you write from webmail that is not set up as your Mac’s mail app, write to support@mediaflowswift.com from wherever you read your email. Include the version shown in Settings › General.

Neither item makes a connection of its own: the message goes only when you send it, and the page is fetched by your browser. Settings › Privacy lists both.

See also: [Reporting a Problem](#reporting-a-problem), [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac)

## Database Connection Issues

*What to check when the shared database will not connect, for a database file and for a database server.*

The shared database is optional: every project opens and works from its project file (.vpm) without it. When the database is unreachable you can keep working; only the cross-project tools stop, and what you save is sent once it is back. The current state is on the last line of the Database menu and in Settings › Storage.

### If You Use a Database File

Symptom: the status reads “Connection failed: …”, “Database file offline” or “Waiting for the network share…”. Cause: the file, or the drive or share it is on, cannot be reached.

1. Open Settings › Storage and read the line under Database. “Database file accessible” means the file can be reached. “Database file not found (will be created on connect)” means the path is reachable but holds no file yet. “No database file chosen yet” means you need to click New Database File… or Use an Existing Database File…
2. If the file is on a network share, open Settings › Network. If it says Not connected, click Connect now, or choose Database → Reconnect Network Share
3. Choose Database → Enable & Connect Database (Reconnect Database while it is connected)
4. If the path is wrong, click Change… and pick the file. Reset to Default points at MediaFlow/mediaflow.db on the chosen network share; it is dimmed until you choose a share in Settings › Network

MediaFlow watches the volume and connects again by itself when it comes back, including after the Mac wakes from sleep.

### If You Use a Database Server

Open Settings › Storage and click Test Connection. It shows the server’s version, or one of these messages:

- “Nothing is listening at host, port …” — the database server is not running there, or the Port is wrong. Start the server, or correct the Port (usually 5432)
- “… could not be found on the network. Check the host name.” — The Host is misspelled, or this Mac is on a different network
- “… did not answer within 10 seconds” — Something between this Mac and the server, often a firewall, is dropping the connection. Check that the server allows connections from this Mac
- “… is not reachable from this network.” — This Mac has no route to the server. Check your network or VPN
- “… closed the connection” — The server is set to refuse this Mac. Whoever runs the server needs to allow this Mac’s address in pg_hba.conf
- A message in the server’s own words, such as a failed password or a database or role that does not exist — Correct the Password, Database or User field

If there is no server yet, Set Up a Server… walks you through making one.

### It Stopped Connecting After an Update

Symptom: the database connected yesterday, and after an update it does not, with the same settings. The status reads “macOS is keeping MediaFlowSwift off your local network…”. Cause: macOS asks once whether an app may reach devices on your network, and after an update it sometimes stops applying your yes to the new version, even though the switch still shows on. The server and your settings are fine.

1. Open Settings › Storage and click Open Local Network Settings…, or open System Settings › Privacy & Security › Local Network yourself
2. Turn MediaFlowswift off, then on again. If it is listed more than once, turn every one on
3. Go back to MediaFlowSwift. It keeps checking, every few seconds at first and then less often, for as long as macOS holds it back, and connects by itself as soon as macOS lets it through. There is no need to restart it, or to choose Reconnect Database. macOS sometimes lets the new version through by itself later on; the switch makes it happen now, and MediaFlowSwift checks again the moment you come back to it

MediaFlowSwift knows this within a few seconds of trying, where it used to wait ten and then guess. It asks macOS why the connection is being held back, looks twice, and still gives the connection itself three seconds to get through before saying so. If macOS will say nothing, you get the ordinary message about a server that did not answer instead, which still mentions the switch. You may also be asked once for leave to read the saved password after an update; choose Always Allow.

### The Log

Help → Show Log reveals app.log in the Finder (it is in Logs/MediaFlow in your Library). MediaFlowSwift writes what it does there, and warnings and errors with their reasons in the database’s or the system’s own words, such as why a sync failed. It names projects, clips, cameras and the database server’s address. It never holds passwords or keys, nor the contents of a rejected database row. A new file is started when it passes two megabytes, and the one before is kept as app.previous.log. Nothing is sent anywhere: it is yours to read, or to attach when you report a problem.

### Several Macs

A database file is for one Mac at a time. Each Mac works on its own local copy and writes the file back when it disconnects or quits, so MediaFlow lets only one Mac connect at a time. A second Mac is told which Mac has it, and can wait or work without the database; see One Mac at a Time on a Database File. A Mac that stopped answering loses its turn after five minutes. Every Mac needs this version or later, because an older one does not take turns. For several Macs at once, switch to a database server. Your project files are not harmed either way: a save writes the project file whenever its folder can be reached, whether or not the database is connected.

### What the Status Line Means

- Connected, Synced — All is well
- Connecting…, Reconnecting…, Waiting for the network share… — MediaFlow is trying; give it a moment
- Sleeping, Disconnected — The connection was closed for sleep, or by Disable & Disconnect
- Database file offline — The drive or share that holds the database file is not connected
- Connection failed: … — The reason follows the colon
- In use on …, Waiting for … — Another Mac has the database file; see One Mac at a Time on a Database File
- Working without the database — You chose to work without it while another Mac had it. Changes are noted and synced when this Mac connects
- Sync failed — A save could not be written to the database. Your project file is saved. MediaFlow has noted the project and syncs it after the next successful connection. The reason is in the log: choose Help → Show Log
- Syncing offline changes… — MediaFlow is sending the database what changed while it was away
- Connected · offline changes still to sync: … — The named projects are still waiting. Open each one to finish its sync

See also: [Shared Database Overview](#shared-database-overview), [Working Offline and Syncing Later](#working-offline-and-syncing-later), [One Mac at a Time on a Database File](#one-mac-at-a-time-on-a-database-file), [Connecting to a Database Server](#connecting-to-a-database-server), [Database File or Database Server?](#database-file-or-database-server), [Choosing and Connecting Your Network Share](#choosing-and-connecting-your-network-share), [Searching All Projects Finds Nothing](#searching-all-projects-finds-nothing)

## Searching All Projects Finds Nothing

*Why the search field’s All Projects scope can come back empty, or says what it needs instead of searching, and what to do about each.*

Symptom: with All Projects chosen, a clip you know is in another project isn’t listed, or All Projects says what it needs instead of searching. This Project works without a shared database.

### When All Projects Says What It Needs

- “Searching every project needs a shared database” — no database file or server is set up. A network share chosen in Settings › Network is not a database on its own: the message stays until a database file is on it. Click Set Up a Shared Database… to open Settings › Storage, turn on Enable Central Database, and choose a database file (any plan) or a database server (Studio Pro). Learn More opens Searching All Projects, which has the steps
- “The shared database is turned off” — click Turn On & Connect, or choose Database → Enable & Connect Database
- “The shared database can’t be reached” — for a file, connect the network share it is on; for a server, check that it is on and that this Mac is on its network. Then click Try Again. The last line of the Database menu says what happened; see Database Connection Issues
- “The shared database is in use” — another Mac has the database file, and only one Mac can use a file at a time. Click the button that reads Wait for, followed by that Mac’s name: this Mac connects as soon as the other has finished, and All Projects searches then. See One Mac at a Time on a Database File
- “Your plan doesn’t include the database server” — click Choose a Plan… for Studio Pro, or Storage Settings… to use a database file, which works with any plan
- “No other projects are in the shared database yet” — only projects saved with the database on are in it. Click Migrate Projects… to add the ones you already have

### When It Searches but Finds Nothing

- The project has been saved with the database connected. A project reaches the database when it is saved; projects made before you turned the database on need Database → Migrate Projects
- The clip is still in its project. A clip taken out of a project isn’t listed
- Every word you type must be found in the clip or its project’s name. Try one word, or part of the file name
- Up to 300 clips are listed. If the line above the results says it shows the first 300, type more words to narrow the search

See also: [Searching All Projects](#searching-all-projects), [Database Connection Issues](#database-connection-issues), [Migrating Projects to the Database](#migrating-projects-to-the-database), [One Mac at a Time on a Database File](#one-mac-at-a-time-on-a-database-file), [Database File or Database Server?](#database-file-or-database-server)

## Network Share 'Resource Busy' Errors

*Why deleting or moving a project folder on a network share can fail with “resource busy”, and what to try.*

Symptom: deleting or moving a project folder on a network share fails with a “resource is busy” error.

Cause: a file in the folder is still open, often because a preview has only just closed. Network shares release files more slowly than a disk in this Mac.

### Fixes

- Wait a few seconds and try again. MediaFlow already retries up to 3 times by itself
- Close any preview of a file in that folder
- Disconnect the share in Finder and connect it again
- If the folder is still stuck, relaunch Finder: hold Option, right-click the Finder icon in the Dock and choose Relaunch

See also: [Clips Showing as Missing](#clips-showing-as-missing), [Deleting a Project](#deleting-a-project)

## Import Not Detecting Files

*What to check when Import shows no files: the file types MediaFlow accepts, the drive, and the iPhone’s Trust prompt.*

Symptom: you open Import and the list is empty, or some files are not in it.

### Cause: The File Type Is Not One MediaFlow Imports

Import lists only these types, by file extension:

- Video — MP4, MOV, M4V, AVI
- Images — JPG, JPEG, PNG, HEIC, DNG
- Audio — WAV, MP3, AAC, M4A

Anything else is left out. That includes TIFF images and camera raw formats other than DNG, such as CR2, NEF and ARW. A folder that holds only those looks empty to Import. Convert them first, for example to DNG or JPG.

### Cause: The Source Cannot Be Read

- Card or drive — Check that it appears in Finder, then click Rescan in the Import sheet
- iPhone — Unlock the phone and tap Trust when it asks, then click Refresh in the Import sheet. If it still does not appear, unplug the cable and plug it in again
- Folder — Check that you can open the folder in Finder. Import looks inside its subfolders too

See also: [Importing from a Card, Drive or Folder](#importing-from-a-card-drive-or-folder), [Importing from iPhone or Camera](#importing-from-iphone-or-camera), [The Import Sheet and Completion Card](#the-import-sheet-and-completion-card)

## Understanding the Where Column

*What each icon and label in the Where column says about where a clip’s file is right now.*

The Where column (once called Location) shows where each clip’s file is. The same seven states appear on the grid badge and in the legend behind the info button above the media list:

- Green check (At destination) — The file is at the project’s destination and has been verified
- Blue folder (On this Mac) — The file is in the project’s working folder and has not been organized yet
- Orange arrow (Only on card) — The file is on a camera card and has not been copied to the destination
- Orange arrow (Not at destination) — The file is on another drive or folder, not a card, and not at the destination. The tooltip names the drive
- Green link (Referenced) — The file stays where it was (Create Project From Folder) and is not copied
- Red X (Missing) — The file cannot be found at any recorded path
- Yellow triangle (Size mismatch) — The file is at the destination, but its size does not match the source
- Gray question mark (Unknown) — MediaFlow has not checked this file yet

Three more labels can appear in grey instead, when this Mac cannot see the file. Volume not connected means the drive or share it is on is not mounted. On another Mac means the file is in another account’s home folder, usually because it was imported on another Mac that shares this project. Not on this Mac means this Mac has never had the file and cannot find it, usually because it was imported on another Mac and kept somewhere else there. The legend has a row for each, and none of them is Missing. A clip on another Mac or not on this Mac is also left out of the Missing and Not at destination groups and of the pipeline’s Organize count, because it is that Mac’s to organize. One in another account’s home folder is left out of the Free up space count too.

The sidebar’s Smart Groups filter the media list to clips that still need attention: Not at destination, Missing, Uncategorized, Unrated, Unreviewed and Reject candidates. Unreviewed holds clips with an import-analysis proposal nobody has confirmed. Reject candidates holds clips import analysis flagged as probable rejects.

> **Tip:** Choose Workflow → Repair → Re-check files to bring every Where badge up to date.

See also: [Re-check files](#re-check-files), [Clips Showing as Missing](#clips-showing-as-missing), [Proposals: What Import Analysis Suggests](#proposals-what-import-analysis-suggests)
