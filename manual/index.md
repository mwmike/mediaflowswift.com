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

- [Setup & Network](#setup--network)
  - [Setting Up MediaFlow](#setting-up-mediaflow)
  - [Choosing and Connecting Your NAS](#choosing-and-connecting-your-nas)
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
  - [Global Search](#global-search)
  - [Finding Duplicate Files](#finding-duplicate-files)
  - [Migrating Projects to the Database](#migrating-projects-to-the-database)
  - [Storage Dashboard](#storage-dashboard)
  - [SQLite File or PostgreSQL Server?](#sqlite-file-or-postgresql-server)
  - [Connecting to a PostgreSQL Server](#connecting-to-a-postgresql-server)
  - [Copying Records Between the File and the Server](#copying-records-between-the-file-and-the-server)
  - [Working Offline and Syncing Later](#working-offline-and-syncing-later)

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
  - [Project Checklist](#project-checklist)
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
  - [Database Connection Issues](#database-connection-issues)
  - [Global Search Finds Nothing](#global-search-finds-nothing)
  - [NAS 'Resource Busy' Errors](#nas-resource-busy-errors)
  - [Import Not Detecting Files](#import-not-detecting-files)
  - [Understanding the Where Column](#understanding-the-where-column)

---

# Getting Started

## What Is MediaFlow?

*What MediaFlow does for a video creator, the basic workflow from card to archive, and where to find help.*

MediaFlow keeps track of the footage from a shoot. You import clips from cards, phones and folders, sort them into categories, review them, and copy them into a tidy folder structure at the project’s destination folder, ready for editing and archiving.

### Key Capabilities

- Import media from SD cards, USB drives, folders, iPhones and cameras connected over USB
- Organize clips into category folders at the project’s destination folder — a network share, an external drive, or a folder on this Mac
- Preview video with frame-by-frame playback controls
- Add categories, tags, notes and star ratings to your clips
- Generate PDF, HTML, and CSV reports for your projects
- Search across projects and find duplicates with an optional shared database — a single file, or a PostgreSQL server several Macs can use

### Basic Workflow

1. Create or open a project
2. Import media from your cards, phones and folders
3. Categorize and review your clips
4. Organize the clips to the project’s destination folder
5. Generate a report for your editor, then archive the project

The pipeline strip under the toolbar follows these steps and always offers the next one.

### First-Run Setup

The first time you open MediaFlow, a short tour explains the app. A Setup Wizard follows it with three questions: your NAS, a shared database, and where organized media goes. You can skip any of them. To answer them later, choose Settings › General › Run Setup Again…

### Where to Get Help

- Help → MediaFlow Help (Cmd+/) opens this searchable help window
- Help → User Guide opens a printable version of every topic in your web browser
- Help → Keyboard Shortcuts jumps straight to the shortcut reference
- Help → Getting Started Guide re-opens the welcome tour shown the first time MediaFlowSwift opens. It opens by itself once only; to have it open every time, tick “Show this welcome when MediaFlowSwift opens” on the tour, or the same switch in Settings › General
- MediaFlowSwift keeps its own copy of your setup, including what you have already seen, the size and place of its windows and your view choices, and puts it back at launch if macOS has lost them

See also: [Setting Up MediaFlow](#setting-up-mediaflow), [Creating a New Project](#creating-a-new-project), [Opening an Existing Project](#opening-an-existing-project), [Understanding the Pipeline Strip](#understanding-the-pipeline-strip), [Keyboard Shortcuts Reference](#keyboard-shortcuts-reference)

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

An orange “This folder is on this Mac’s own drive” note appears when the destination is on this Mac’s own disk rather than an external or network volume. If that is where you want your organized media, you can ignore it.

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

The Project Browser shows all known projects, including those registered in the shared database. Access it via Projects → Browse Projects (Cmd+Shift+P) or from the main screen when no project is open.

- Double-click a project to open it. Or select it and click Open Selected at the top right, or press Return
- Right-click anywhere on a project’s row for options: Open, Delete Project…, Remove from List, Show in Finder
- Use the search bar to filter by project name
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

- Seven tabs: Workflow Tools, Edit, Full Metadata, Metadata, Enhanced, Scene Log and Transcript. When the panel is too narrow to show them all, scroll the row of tabs sideways. The tab you last used is remembered
- Drag the divider between the preview and this panel to give either more room; the panel can be as narrow as the tabs’ contents allow and much wider than before
- Workflow Tools — Extract a thumbnail, mark in and out points, create a subclip, and manage and process the Proxy queue
- Edit — Change the category, favorite flag, tags and notes of the selected clips
- Full Metadata — Every available metadata field in one long listing
- Metadata — Basic file and media information (size, dates, dimensions, duration)
- Enhanced — Technical details such as codec, bit rate, frame rate, and camera/lens data
- Scene Log — Scene, shot type, take, Camera angle and Circle Take for the selected clip

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
- Free up space — an estimate of the space the working-directory copies of organized clips still take on this Mac. Button: Free Up Space…, which scans the disk and shows exactly what it will reclaim
- Archive — Pending, or the volume the project was archived to (“USB #0007”) with the date. Button: Archive…
- Eject — removable cards and drives still mounted. Button: Eject &lt;name>, or an Eject menu when more than one is connected

### Clicking a Segment

Clicking a segment filters the media list to that step’s remaining work and reveals its one primary button on the right. Import shows all media, Categorize shows the uncategorized clips, Review shows the unrated ones and Organize shows the Not at destination smart group. Free up space, Archive and Eject leave the current filter alone because their work is not a subset of the list.

Until you click one, the strip follows the first step that still has work to do. A finished step shows a green check instead of its icon.

The Organize count turns orange once 10 or more clips are still waiting and the project has a destination.

### The Old Screens

Workflow → Plan & Deliver → Project status (legacy)… and Workflow → Plan & Deliver → Project Checklist (legacy)… still open the earlier overview screens. They count categorized, organized and verified clips with the same rules the strip uses, so the three always agree.

See also: [Understanding the Interface](#understanding-the-interface), [Organizing Media to Storage](#organizing-media-to-storage), [Freeing Up Space](#freeing-up-space), [Smart Notifications](#smart-notifications)

## What Things Are Called Now

*One word per concept: the names that changed this release, and the old names they answer to.*

The same thing used to have several names and the same name used to mean several things. This release settles on one word per concept. Nothing stored in your projects changed — a .vpm file written before this release loads unchanged, and one written after it still opens in an older build. Only the words on screen moved.

### The Table

- Organize Media keeps its name, and the pipeline strip now says Organize too instead of Copy to NAS — the menu item, the toolbar button, the right-click action, the strip and the confirmation sheet all read the same. With clips selected it copies the selection; with nothing selected it copies the whole project, and the sheet says which
- Device is now Camera wherever it means the camera that shot the clip — the table column, the sidebar section, the Import sheet’s picker and the Set Camera menu. “Device” now means an import source: a card, a drive, an iPhone.
- The Scene Log’s Camera field is now Camera angle — A, B, C, the angle a take was shot from, not the camera body
- The Location column is now Where, and the sidebar’s Locations section is now Places. Where is about the file; Places is about the world
- Sync Folder Layout (Entire Project) is now Re-file folders by category, under Workflow → Repair
- Reconnect Destination is now Change destination folder, under Workflow → Repair
- Refresh Storage Locations is now Re-check files, under Workflow → Repair
- Do Not Copy now reads Skip (don’t copy). It is still stored as “Do Not Copy”
- Dashboard is now Project status
- Batch Queue is now Proxy queue — the queue for thumbnails and proxies
- Remove Selected Assets is now Remove from Project
- Kill is now Reject. It is still stored as “Kill”
- Favorite and Circle Take fold into Hero. A favorite becomes a Hero when the project loads; a circle take becomes a Hero rated five stars. Both flags stay in the file so an older build still reads it

### Where the Workflow Menu Went

- Import…, Organize Media…, Review, Free Up Space…, Archive to USB… — the five things you do to footage, at the top level. Restore from Cleanup sits under Free Up Space…
- Analyze… — one sheet holding every optional analysis pass. See The Analyze Hub
- Plan & Deliver — Shot List, Storyboard, Shoot Map, Day Summary, Storage Forecast, Import Field Notes, Generate Dailies, NLE Template Export, Export FCPXML, Report, and the two legacy overview screens
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

### Failed Operations

An operation that fails keeps its row, tinted red, with the reason in place of the progress bar. It stays until you dismiss it, so a failure that happened while you were away is still there when you come back.

### While a Sheet Is Open

Messages raised inside a sheet — the Import sheet’s “No card selected”, a folder scan that failed — appear inside that sheet, next to the button that caused them, instead of behind the sheet, where you could not read them.

> **Tip:** When no project is open the same status appears in the centre of the window instead, where there is nothing else to look at.

See also: [Understanding the Interface](#understanding-the-interface), [Understanding the Pipeline Strip](#understanding-the-pipeline-strip), [Smart Notifications](#smart-notifications)

---

# Setup & Network

## Setting Up MediaFlow

*The welcome tour explains the app; the Setup Wizard then asks three questions, and you can skip any of them.*

A new copy of MediaFlow knows nothing about your equipment: no NAS, no shared database, no destination. Two things greet you on first launch. The welcome tour explains the app. The Setup Wizard then asks three questions so the app can find your storage.

You do not have to answer anything. MediaFlow works without a NAS and without a database, and every answer can be changed later in Settings.

### The welcome tour

Four pages: Welcome, the workflow, your workspace, and a closing page of tips. Use Next to move on, Skip to leave, and Get Started on the last page. Help → Getting Started Guide opens it again at any time.

### The Setup Wizard

The wizard opens when the tour closes, if nothing is set up yet. It does not open when your saved setup was put back at launch.

1. Your NAS — shares that are connected now are listed with a Use this button. Look for servers searches the network, and Connect to… opens a server in Finder so you can sign in and mount a share. Use this takes effect as soon as you click it
2. Shared database — choose None, SQLite file or PostgreSQL server. For a SQLite file, click Choose… to pick the file. For a server, fill in the connection fields
3. Where organized media goes — click Choose… to pick the default destination for new projects. A project can always use a different one

### Skipping

- To pass over one step, click Next without answering it
- Skip (Skip setup on the first page) closes the wizard and keeps the answers you have given so far
- A step you leave unanswered changes nothing, including a setting that was already in place

### Running it again

Choose Settings › General › Run Setup Again…. The wizard opens showing your current settings, not an empty form. Choosing None on the database step turns the shared database off.

See also: [Choosing and Connecting Your NAS](#choosing-and-connecting-your-nas), [SQLite File or PostgreSQL Server?](#sqlite-file-or-postgresql-server), [Saved Setup: A Copy of Your Settings](#saved-setup-a-copy-of-your-settings), [The Settings Window, Tab by Tab](#the-settings-window-tab-by-tab), [What Is MediaFlow?](#what-is-mediaflow)

## Choosing and Connecting Your NAS

*Settings › Network is where you tell MediaFlow which network share holds your projects and media.*

MediaFlow has no built-in NAS. Until you choose one, Settings › Network reads “No NAS chosen yet” and nothing is assumed. A NAS is optional: you can organize to any folder, including a drive attached to this Mac.

When you do choose a share, MediaFlow uses it as the starting point for file pickers, as the suggested place for the shared database file, as the host offered for a PostgreSQL server, and as the place it looks for app updates. It also connects the share when it is needed: see below.

### Choose a share

1. Open Settings › Network
2. If the share is already connected, it appears in the list. Click Use this beside it. The button reads In use for the share you have chosen
3. If it is not listed, click Look for servers, then pick the server from the Connect to… menu. The server opens in Finder, which asks for the password and shows its shares
4. Mount the share you want in Finder, return to Settings, and click Use this

Picking a mounted share fills in both the share name and its address, so there is nothing to type. If you prefer, open “Type the address instead” and enter an smb:// address. A name ending in .local keeps working when the NAS gets a new network address.

### Connected when it is needed

Once a share is chosen, MediaFlowSwift connects it by itself whenever something needs it and it is not mounted: a couple of seconds after launch, a few seconds after the Mac wakes, and before opening a project whose file lives on it. The status area reads “Connecting to ‘share’…” meanwhile. The launch and wake attempts are made once, so a share that cannot be reached raises at most one password prompt; opening a project tries again, because you are there to answer. If the share still cannot be connected, the project is not opened and a message says so, rather than opening it from the database with every clip called missing. A project on some other drive that is unplugged gets the same treatment: the message names the drive.

While a drive is not connected, the clips on it read Volume not connected in the Where column, in grey, and Re-check files leaves their last known state alone. Nothing is called Missing because its drive is away.

### Passwords

macOS asks for the NAS password, not MediaFlow. MediaFlow never sees or stores it. If you let macOS remember the password, macOS keeps it in your Keychain and uses it to reconnect.

### Connect now and Forget

- The status line reads Connected with the mount path, Looking for the NAS…, or Not connected
- Connect now tries the stored address, then searches the network, then mounts the share. It is available only while the share is not connected
- Forget stops using this NAS. Settings that follow it, such as the update source, go back to unset. The path to your database file is kept

### No servers found

Check that the NAS is switched on and on the same network. Also check that MediaFlow is allowed to use the local network: System Settings › Privacy & Security › Local Network.

See also: [Setting Up MediaFlow](#setting-up-mediaflow), [Updating MediaFlow](#updating-mediaflow), [SQLite File or PostgreSQL Server?](#sqlite-file-or-postgresql-server), [Database Connection Issues](#database-connection-issues), [NAS 'Resource Busy' Errors](#nas-resource-busy-errors)

## Saved Setup: A Copy of Your Settings

*MediaFlow keeps a copy of your settings outside macOS preferences and puts it back if the settings are ever lost.*

The saved setup is a small file that holds your MediaFlow settings. It lives apart from the macOS preferences file, so a lost or reset preferences file does not take your setup with it. You do not need to do anything: it is written every time you quit, when you finish the Setup Wizard, and before an update installs.

Passwords and API keys are never in it. They stay in your Keychain.

### What it holds

- Your NAS share and its address
- The shared database settings: on or off, the store, the file path, and the server host, port, database and user
- The default destination, recent destinations and the verification setting
- The update source and whether to check automatically
- Import analysis and model settings, including the daily spending limit
- The category and camera lists that new projects start with

### What it never holds

API keys and the database password. They stay in your Keychain. The saved setup is a plain file, and a secret copied into it would be readable by anyone who opened it. After a restore on a Mac with an empty Keychain, enter those again.

### When it is restored automatically

Only at launch, and only into a copy of MediaFlow that has nothing configured: no NAS, no database file, no server and no default destination. It never overwrites settings you are already using.

### Doing it by hand

- Settings › General › Save Setup Now writes the file immediately. The line above the buttons shows when it was last saved
- Restore Saved Setup puts every saved setting back

> **Warning:** Restore Saved Setup overwrites the settings on this Mac with the saved ones. It asks you to confirm first. The saved copy is normally the one written when you last quit.

See also: [Setting Up MediaFlow](#setting-up-mediaflow), [Updating MediaFlow](#updating-mediaflow), [The Settings Window, Tab by Tab](#the-settings-window-tab-by-tab), [Connecting to a PostgreSQL Server](#connecting-to-a-postgresql-server)

## Updating MediaFlow

*MediaFlow updates itself from a copy of the app on your NAS or in a folder you choose, and keeps your settings.*

MediaFlow does not download updates from the internet. It compares itself with a newer copy of the app that you keep in one place, normally on your NAS, and installs that copy when you say so. Your settings and projects are not touched by an update.

### Where updates come from

Settings › General › Updates shows the source. Until you choose something else, it follows the NAS chosen in Settings › Network and looks for the app in the MediaFlowSwift folder on that share.

- Choose… picks a different copy of the app, on a share or on this Mac
- Follow the NAS goes back to the default
- Not set means no NAS is chosen and nothing was picked, so MediaFlow does not look for new versions
- “No app found there” means the share is not connected or the app is somewhere else

### Who may sign an update

An update is installed only if it was signed by the maker of the copy you are running, or by MediaFlowSwift’s Apple Developer ID. Nothing else in that folder can be handed to you as an update. From MediaFlowSwift 1.10.18 the app is moving to the Developer ID: after the first update signed with it, macOS treats the app as one it knows, so your Keychain asks once more and then not again. The Local Network switch is another matter: on some versions of macOS the new build is still treated as a stranger, and the switch needs turning off and on once after an update. MediaFlowSwift now tells Launch Services about the new copy before reopening, which is meant to stop that; if it does not, the app says so and offers the switch.

### Automatic checks

With “Check for new versions automatically” on, MediaFlow looks shortly after launch and when the Mac wakes. Checking reads one small file. A newer version appears as a banner, never a dialog, and never while an import or organize is running.

- Install… opens the Software Update window
- Later hides the banner until a version newer than that one appears
- The banner waits its turn: while a card has just been connected, or the NAS is unreachable, that banner is shown instead

### Installing

1. Choose Check for Updates… in the app menu, or click Install… on the banner
2. Click Install Update. The button is unavailable while a background operation is running; wait for it to finish
3. MediaFlow copies the new version, checks that it is genuine and from the same maker as the one you are running, closes, puts it in place of the old one and reopens. It reopens only once the old copy has fully closed, which can take some seconds while the shared database is saved. Do not quit or reopen it yourself while it works

The update window lists what is new in the version on offer: every version newer than yours, its headline and its points, taken from the change log inside the new copy of the app. The copy is checked for its maker’s signature when it is installed, not when its notes are read, so treat the list as a preview. A copy made before this feature carries no change log, and the list is simply absent.

Your settings are written to disk and to the saved setup before the app restarts.

MediaFlow looks for a new version a few seconds after launch, again every minute until it can reach the place new versions come from, and then every few hours, as well as after the Mac wakes. If anything about the new version does not check out, nothing is changed and the version you had reopens. The version you updated from is kept beside the app as “MediaFlowswift (previous)” for Revert. Every version is the same signed app to macOS, and before the new one reopens the installer tells Launch Services about it and unregisters the copy kept for Revert, so that permissions you have given MediaFlow carry over from one update to the next; the Keychain’s do. Reaching your local network is the one macOS has sometimes made the new version ask for again; see It Stopped Connecting After an Update. What the installer did is written to Library/Logs/MediaFlow/update.log in your home folder.

### Going back

After an update, the Software Update window shows Revert to Previous Version (or Revert to a named version). It puts the version you had before back in place and relaunches.

See also: [Choosing and Connecting Your NAS](#choosing-and-connecting-your-nas), [Saved Setup: A Copy of Your Settings](#saved-setup-a-copy-of-your-settings), [The Settings Window, Tab by Tab](#the-settings-window-tab-by-tab)

## The Settings Window, Tab by Tab

*A map of the eight Settings tabs, so you know which one holds the setting you are looking for.*

Settings has eight tabs. Each holds one subject. Most changes take effect as you make them.

`Cmd+,` — Open Settings

### General

Run Setup Again…, the saved copy of your settings (Save Setup Now, Restore Saved Setup), where app updates come from and whether to check automatically, and the version you are running.

### Network

Which NAS share MediaFlow uses: shares connected now, Look for servers, Connect now and Forget. There is no built-in NAS; nothing is assumed until you choose one.

### Storage

The shared database: Enable Central Database, the Store (SQLite file or PostgreSQL server), its file or connection fields, and copying records between the two. Below it, the default destination for new projects and “Verify organized copies by reading them back”.

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

See also: [Setting Up MediaFlow](#setting-up-mediaflow), [Choosing and Connecting Your NAS](#choosing-and-connecting-your-nas), [Saved Setup: A Copy of Your Settings](#saved-setup-a-copy-of-your-settings), [Updating MediaFlow](#updating-mediaflow), [SQLite File or PostgreSQL Server?](#sqlite-file-or-postgresql-server), [Adding, Renaming, Retiring and Removing Categories](#adding-renaming-retiring-and-removing-categories), [Using a Model to Suggest Categories](#using-a-model-to-suggest-categories), [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [How MediaFlow Verifies Copies](#how-mediaflow-verifies-copies), [Smart Notifications](#smart-notifications)

## Privacy: What Leaves This Mac

*MediaFlow works on this Mac and your own network; each service that reaches an outside company is off until you turn it on.*

MediaFlow has no account, collects no usage data and contacts no server of its own. Your media, projects and shared database stay on this Mac and on your own network.

A few features need a service run by another company. Settings › Privacy lists every one: what is sent, to whom, and what it is for. Each is off until you turn it on, and you can turn it off again at any time.

### The switches

- Apple’s online speech recognition — sends the audio of the clip being transcribed to Apple, only when this Mac has no on-device speech model for the language. While it is off, speech is recognized on this Mac only, and a language without an on-device model is not transcribed.
- Historical weather lookup — sends each clip’s GPS coordinates, rounded to about 100 m, and the date it was shot to Open-Meteo. While it is off, Look Up Weather does nothing and tells you where to turn it on.
- Place names for GPS coordinates — sends each clip’s coordinates, rounded to about 100 m, to Apple. While it is off, clips show their coordinates; names already looked up are kept.
- A model that writes your YouTube title, description and tags — sends the transcript of the finished video you chose, its length, the brief you typed, and then its own drafts, to the provider chosen in Settings › Analysis. Never the video or its file name. Not needed with the model on this Mac, when nothing is sent outside; a local model you have pointed at another computer on your network receives the same text. See The SEO Agent
- Uploading to YouTube — sends the finished video you chose, with its title, description, chapters, tags, category, visibility, publish time and made-for-kids answer, the file’s size and type, and the thumbnail if you chose to send it, to Google. Signing in opens your browser at Google; MediaFlow never sees your password. Signing in and staying signed in send your client ID and secret to Google. The permission cannot read your channel or delete videos. Nothing is sent until you click Upload and confirm. While it is off, uploading is refused and sign-in does not ask for permission to upload; with both YouTube switches off, signing in is refused too. See Uploading to YouTube
- Reading your videos’ statistics from YouTube — asks Google which channel you signed in to, and sends the YouTube IDs of the videos your database records as uploaded by MediaFlow with the span of dates from the first upload to today, and nothing else. Google answers with their views, likes, comments, watch time, average view, subscribers gained, shares, visibility and publish time. Turning it on makes the next sign-in ask Google for two more permissions, both read-only, which would allow reading your whole channel; MediaFlow asks only about those videos. Read only when you click Read from YouTube Now on the Results tab. See How Your Videos Are Doing
- Maps of where you shot — showing a map sends the area you are looking at to Apple, which is how the map images arrive. While it is off, the Shoot Map and GPS scene review list locations without a map, with a Turn On Maps button.

### A model that suggests categories

This one is set up in Settings › Analysis, and then ticked for each import you want it for. With a paid provider (Anthropic, OpenAI or Google) it sends three frames from each clip, your category list, the clip’s camera, duration and place name, the opening words of any speech, and your recent corrections. With a model on this Mac, nothing leaves it.

The local model’s Server address may be this Mac or another computer on your own network. An address on the internet is refused, and a redirect from the server is never followed, so frames go only to the computer you named.

### What stays on your network

- Your NAS: finding it, connecting to it, and reading and writing media, the database file and app updates.
- Your PostgreSQL server, when you use one. That connection is not encrypted, so keep the server on a network you trust.
- App updates: from a folder you choose, never from a web site.

### Things that open your browser

Buttons such as a provider’s API-key page or the Ollama download open a web page only when you click them. MediaFlow itself sends nothing.

> **Tip:** A saved setup keeps your Privacy switches, but they are not restored automatically on a new install — only when you choose Restore Saved Setup…, which says so before it does.

macOS may separately ask permission for speech recognition or for finding devices on your local network. Those prompts come from macOS and are managed in System Settings › Privacy & Security.

See also: [The Settings Window, Tab by Tab](#the-settings-window-tab-by-tab), [Using a Model to Suggest Categories](#using-a-model-to-suggest-categories), [Running a Model on This Mac](#running-a-model-on-this-mac), [Speech Transcription](#speech-transcription), [Historical Weather Lookup](#historical-weather-lookup), [Interactive Shoot Map](#interactive-shoot-map), [Saved Setup: A Copy of Your Settings](#saved-setup-a-copy-of-your-settings)

---

# Importing Media

## Importing from a Card, Drive or Folder

*Pick a card, drive or folder, choose the files and the camera that shot them, and copy them into your project.*

An import copies media from a card, a drive or a folder into your project’s working folder on this Mac and adds the clips to the project. The original files are not changed.

1. Choose File → Import… (File → Import from Folder… opens the same sheet with the Folder segment selected)
2. Pick a source at the top of the sheet: Cards & drives lists the SD cards and USB drives MediaFlow has detected; Folder lets you browse to any directory
3. For a card, choose it from the Choose Card… menu (a single connected card is picked for you; Rescan looks again). For a folder, click Choose Folder…
4. MediaFlow scans the source, including subfolders, for supported video, image and audio files
5. Review the file list and check or uncheck the items to include
6. Set the Camera picker to the camera that shot the footage; click New camera… to add one that is not listed
7. Optionally tick “Ask a model to suggest categories” — see below
8. Click Import Selected

Once the copy starts, the bottom of the sheet shows “Importing to:” with the folder the files are going to.

### Duplicates

Files that are already in the project are marked Duplicate in the list. A line at the bottom of the sheet says how many duplicates were detected, and they are skipped when you import.

### Disk Space

The working folder’s disk needs room for the selected files plus 10 GB of headroom. If it has less, the import does not start and MediaFlow tells you there is not enough free space.

### Cancelling

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
2. Choose File → Import from iPhone…, or choose File → Import… and select the iPhone segment at the top of the sheet
3. Select your device from the Device picker
4. Check the items to import in the list. Items already in the project are marked Duplicate and are skipped
5. Click Import Selected

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

File → Import… opens a single Import sheet. The segment at the top chooses the source: Cards & drives (detected SD cards and USB drives), iPhone (phones and cameras over USB), or Folder (any directory). Import from Folder… and Import from iPhone… open the same sheet with that segment preselected. The banner that appears when a card or phone is plugged in opens the sheet on Cards & drives.

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
- Sorting by Filename follows Finder’s order, so clip2 comes before clip10, and keeps the chapters of one GoPro recording together: a GoPro splits a long recording into files such as GX012324 and GX022324, and MediaFlow lists them one after the other instead of sending the second to the end
- A Category or Camera shown in italics with a confidence badge is a proposal from import analysis. Click the cell to accept it
- Right-click any row for the context menu

### Grid View

- Shows clips as thumbnail cards in a grid that adapts to the window width
- Each card shows the filename, the category, a ★ when the clip is a favorite, a colored Where icon with its label, the camera name and, when they are set, its star rating and its Hero, Maybe or Reject badge
- Video thumbnails carry the clip’s duration in the corner
- Right-click any card for the context menu

See also: [Selecting Clips](#selecting-clips), [Context Menu Actions](#context-menu-actions), [Understanding the Where Column](#understanding-the-where-column)

## Selecting Clips

*Select one clip or many in the media list, and use the selection bar to act on all of them at once.*

Most commands act on the selected clips: batch editing, organizing, rating, moving to another project and removing from the project.

- Click a clip to select it
- Cmd+Click adds a clip to the selection or takes it out
- Shift+Click selects every clip between the one you last clicked and this one, in Table and Grid view alike. Shift+Click again, further up or down, re-measures from that same starting clip. Cmd+Shift+Click adds the range to what is already selected
- Cmd+A selects every clip the current filter shows. While you are typing in a field, Cmd+A selects the text in that field instead

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

*Narrow the media list with a filter, and search within it by name, notes, tags, category, camera or scene.*

A filter limits the media list to the clips you want to work on. One filter is active at a time; choosing another replaces it.

### Searching

`Cmd+F` — Find Clips

Type in the search field in the toolbar, or press Cmd+F to put the cursor there. The list narrows as you type, in Table and Grid view alike, and a line above it tells you how many clips match out of how many are in the project.

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

### Searching Across Projects

To find a clip in any project, choose Database → Global Search… This needs the shared database.

See also: [Table and Grid Views](#table-and-grid-views), [Understanding the Pipeline Strip](#understanding-the-pipeline-strip), [Global Search](#global-search)

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
- Edits made in the Scene Log tab, and Shot List, Storyboard and Project Checklist edits
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
4. A different destination is a one-off: the project keeps pointing where it did. Tick “Make this the project destination” when you want the change to stick
5. Click Organize Media. MediaFlow creates the category and camera folders, copies each file, and verifies each copy
6. When the progress window finishes, click Done. Each copied clip now reads “At destination” in the Where column, with a green check

The confirmation can also warn you. Organize is disabled when the destination does not have enough free space. An orange line reading “This folder is on this Mac’s own drive” appears when the destination is on this Mac’s startup disk rather than a mounted drive or share; if you meant to use a drive, check that it is connected. Another orange line counts clips that still carry an unconfirmed proposal; organizing does not apply proposals.

If the clips came from a memory card, the Clear Card review opens when you click Done. Nothing is deleted unless you confirm it there.

### How copies are verified

MediaFlow computes a SHA-256 checksum of each source file as it copies it, then finishes writing the copy to the disk. By default it then reads the whole copy back and compares its SHA-256 with the source. If the check fails, the copy is deleted and made again once; if it fails a second time, that clip is reported as failed and its source is left alone.

Settings › Storage › Organize Media has the switch “Verify organized copies by reading them back (slower, safest)”. With it off, MediaFlow checks the size of the copy plus three 1 MB samples at the start, middle and end. That is much faster over a network, but it does not detect corruption outside the sampled ranges.

The checksum is recorded with the clip. Clear Card relies on it later, so leave read-back verification on if you plan to clear cards.

### Organizing again over existing files

If a file with the same name and the same size is already in the target folder, MediaFlow uses it instead of copying again. That file is not read and no checksum is recorded for it, so Clear Card later lists the clip as “Organized, unverifiable”. If a file with the same name has a different size, the new copy is saved with a number added to its name, for example Clip_1.mp4.

### Default destination

Settings › Storage › Organize Media › “Default destination for new projects” fills in the destination for a project that has none. A project’s own destination always wins once it has one.

### Keeping the folder layout in sync

When you change the category or the camera of an organized clip, MediaFlow moves its copy at the destination into the matching folder. This happens in the background and only interrupts you if a file fails to move. To bring the whole project into line at once, for example after an interrupted move or a relink, choose Workflow → Repair → Re-file folders by category.

### Cancelling a long operation

Every long file operation (organize, import, project move, cleanup move and restore, relink, re-file and archive) has a Cancel button on its progress window. Cancelling stops the work between files. The file being written at that moment is discarded, so no half-copied file is left behind. Every file that finished before you cancelled stays where it landed; nothing already copied, moved or deleted is put back. The window then reports what did finish, for example “Cancelled after 12 of 40 files, 6.2 GB copied”, and waits for you to click Done.

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

Re-check files only looks at recorded paths. It does not search for files that have moved; use Workflow → Repair → Relink Missing Media… for that.

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
3. MediaFlow checks again that each file is inside the card’s DCIM folder immediately before deleting it
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

See also: [Logging Scene, Shot and Take](#logging-scene-shot-and-take), [Storyboard](#storyboard), [Project Checklist](#project-checklist)

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

The flag appears as an icon in the Table view, and the levels are listed in the Full Metadata tab. Clips with a Clipping, Low or Silent flag are counted as audio issues in the Day Summary and in Project status (legacy). Clips that already carry a flag are skipped; MediaFlow tells you when nothing is left to analyze.

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

> **Tip:** Use frame stepping for precise positioning when extracting thumbnails or creating subclips.

Making proxies is part of the Studio plan; see Plans and Pricing.

See also: [Pop-Out Video Window](#pop-out-video-window), [Extracting Thumbnails and Subclips](#extracting-thumbnails-and-subclips)

## Pop-Out Video Window

*Open the video preview in a separate, resizable window with its own playback controls.*

Click the pop-out button at the right end of the preview controls to open the video in a separate window. The window has its own seek slider, step back, play/pause and step forward controls, and you can resize it freely.

> **Tip:** Use the pop-out window when you want a larger preview while still seeing the media list and metadata panels.

See also: [Video Playback Controls](#video-playback-controls)

## Extracting Thumbnails and Subclips

*Save the current video frame as a PNG image, or export part of a clip as an MP4 using in and out points.*

Use the Workflow Tools tab in the metadata panel for these operations:

### Extract Thumbnail

Saves the current video frame (or the full image for a photo) as a PNG file. Move to the frame you want with the playback controls, click Extract Thumbnail, and choose where to save it.

### Create Subclip

Exports part of a video as an MP4 file. Mark in and out points to choose the range, then click Create Subclip and choose where to save it. What is exported depends on the marks:

- Both marks set — the range between them
- Only an in-point — from the in-point to the end of the clip, up to 30 seconds
- Only an out-point — from the start of the clip to the out-point
- No marks — a 5-second clip around the current position, starting 2 seconds before it

### Marking In/Out Points

In the Workflow Tools tab, click Mark In (I) or Mark Out (O) to set a mark at the current playback position. You can also press I or O after clicking the preview panel, so that it has keyboard focus. The marked range is highlighted on the seek slider, the In, Out and Duration times are listed in the tab, and the Create Subclip button shows the duration. Click Clear in the Workflow Tools tab to remove both marks.

See also: [Video Playback Controls](#video-playback-controls), [Processing the Proxy Queue](#processing-the-proxy-queue)

## Reviewing Clips with the Keyboard

*A keyboard-driven review sheet for playing, rating, rejecting and accepting proposals on clips, one after another.*

Rapid Review is a focused review sheet for evaluating clips quickly. Use the keyboard to play, rate, favorite, reject and move through your footage without touching the mouse. Open it from Workflow → Review (Cmd+Opt+R) or from the Rapid Review… button on the pipeline strip’s Review segment. Press ? at any time for an on-screen list of these keys.

### Playback Controls

- J / K / L — Shuttle reverse / stop / forward (press repeatedly to increase speed: 1×, 2×, 4×, 8×)
- Space — Play / pause
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

With auto-advance on, rating a clip with 1–5, rejecting it with X, or pressing A or R moves to the next clip after a short delay. Auto-advance starts on; press T to turn it off or on, and MediaFlow remembers your choice. The Auto indicator in the bottom bar is green while it is on.

### Review Queue

The review queue is based on your current filters in the main window. Filter by category, scene, camera or smart group before you open Review to focus on a specific subset of clips. The bottom bar shows your progress (for example “12 of 47”) and how many clips have been rated.

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

A clip on a NAS or another network drive is read across the network as it plays, and macOS does not read ahead for a file the way it does for a stream, so a short pause on the network is a pause in the picture. A large clip, such as 4K footage, over a wireless connection is where this shows. When the preview is playing such a clip and it has no proxy, a badge at the top-left says Over the network:

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

> **Tip:** The search field above the media list matches tags, and so does Global Search across every project in the shared database.

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

A row titled “Filing clips by category” appears in the progress panel while the move runs, then disappears. There is no summary and no Done button when it succeeds.

You hear about it only if it fails. If a file cannot be moved, the row stays and says so until you clear it, and the details are written to the log. The clip keeps its new category; its file is still in the old folder.

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

*The optional shared database lets you search and track clips across projects; it is a SQLite file or a PostgreSQL server.*

The shared database (the app calls it the Central Database) keeps a record of every project so you can search, compare and track clips across all of them. It is optional. Import, organize, preview and editing all work without it.

The project file (.vpm) is the authority. The database holds a copy of what the project file says, and MediaFlow updates that copy each time you save.

### What the Database Adds

- Global Search — Find clips in any project by filename, tag or note
- Find Duplicates — List files with identical content across projects
- Storage Dashboard — Capacity history and database-wide counts
- Migrate Projects — Add existing .vpm files to the database
- Browse Projects — Projects → Browse Projects lists every project the database knows

### File or Server

The database is kept in one of two stores. You choose with the Store picker in Settings › Storage.

- SQLite file — A single file, usually on shared storage. Nothing to install. One Mac at a time: MediaFlow works on a local copy of the file and writes it back when you disconnect or quit, so Macs must take turns, and the last Mac to quit wins
- PostgreSQL server — A server that keeps the records itself, so several Macs can work at the same time

### Turning It On

1. Open Settings › Storage and turn on Enable Central Database, or choose Database → Enable & Connect Database
2. Choose the Store: SQLite file or PostgreSQL server
3. For a file, click Choose… and pick the database file. If you chose a NAS in Settings › Network, Reset to Default points at MediaFlow/mediaflow.db on it. A file that does not exist yet is created when you connect
4. For a server, fill in Host, Port, Database, User and Password, then click Test Connection

### Moving Between a File and a Server

With PostgreSQL server selected, Settings › Storage offers Copy the SQLite File to This Server… and Copy This Server to a SQLite File…. Both copy every record and leave the source unchanged. Switching the Store picker alone does not move any records.

### Working Offline

If the database cannot be reached, keep working. MediaFlow notes which projects changed and syncs them when the connection returns. The status line then reads “Connected”, or “Connected · offline changes still to sync: …” followed by the names of projects that are waiting. Open a named project to finish its sync.

### Database Menu

- Enable & Connect Database / Reconnect Database — Connect; the title changes once you are connected
- Disable & Disconnect — Close the connection and turn the database features off
- Migrate Projects… — Add existing .vpm files to the database
- Global Search…, Find Duplicates…, Storage Dashboard… — The cross-project tools
- Reconnect to NAS — Mount the share chosen in Settings › Network again when it has dropped. It is dimmed while the share is mounted
- Status — The last line of the menu shows the connection and sync state

See also: [SQLite File or PostgreSQL Server?](#sqlite-file-or-postgresql-server), [Connecting to a PostgreSQL Server](#connecting-to-a-postgresql-server), [Copying Records Between the File and the Server](#copying-records-between-the-file-and-the-server), [Working Offline and Syncing Later](#working-offline-and-syncing-later), [Global Search](#global-search), [Database Connection Issues](#database-connection-issues)

## Global Search

*Search every project in the shared database by filename, tag or note, then add a result to the open project.*

Global Search finds clips in any project the shared database knows about. It needs a connected database; when there is none, the window says “Database not connected” and Search is dimmed.

1. Choose Database → Global Search (Cmd+Shift+F)
2. Type a filename, tag or word from a note, then press Return or click Search. Results do not update as you type
3. Narrow the results with the Category and Camera filters
4. Each result shows the clip and the project it belongs to
5. Select a result to see a preview and its details

From a result you can choose Add to Current Project, or Reveal in Finder to find the file on disk.

> **Tip:** If search finds nothing on a database file made by an early version, connect once with this version. MediaFlow rebuilds the search index on its own.

See also: [Shared Database Overview](#shared-database-overview), [Filtering and Searching](#filtering-and-searching), [Database Connection Issues](#database-connection-issues)

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

To move the database itself between a SQLite file and a PostgreSQL server, see Copying Records Between the File and the Server.

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

The dashboard shows the history of the NAS chosen in Settings › Network. With no NAS chosen, the history is empty.

See also: [Shared Database Overview](#shared-database-overview), [Finding Duplicate Files](#finding-duplicate-files), [Storage Forecast](#storage-forecast), [Choosing and Connecting Your NAS](#choosing-and-connecting-your-nas)

## SQLite File or PostgreSQL Server?

*The shared database is optional and can live in a SQLite file for one Mac or on a PostgreSQL server for several.*

The shared database tracks clips across all your projects. It powers Global Search, Find Duplicates, the Storage Dashboard and the project browser. It is optional. Your project files are the authority: every project opens, imports and organizes without a database, and the database is filled from the project files, not the other way round.

If you turn it on, you choose where it keeps its records.

- SQLite file — a single file, usually on the NAS. Nothing to install. One Mac at a time: each Mac works on its own copy of the file and writes it back when it disconnects or quits, so Macs must take turns, and the last one to quit wins
- PostgreSQL server — a service that keeps the records itself, so several Macs can work at the same time. It needs a NAS or a computer that stays on and can run containers

> **Tip:** Choose the SQLite file if you work on one Mac or have no NAS. Choose the server if two or more Macs use MediaFlow at the same time. You can move between them later, with your records.

### Choosing or switching

1. Open Settings › Storage and turn on Enable Central Database
2. Under Store, pick SQLite file or PostgreSQL server
3. For a file, click Choose… beside Database and pick the file. For a server, fill in Host, Port, Database, User and Password

Switching the Store reconnects at once; you do not need to relaunch. Switching does not move any records. The other store keeps what it had, and its settings are remembered, so switching back finds it again.

### Taking your records with you

With PostgreSQL server selected, two buttons copy every record in either direction: Copy the SQLite File to This Server… and Copy This Server to a SQLite File…. Neither changes its source.

See also: [Shared Database Overview](#shared-database-overview), [Connecting to a PostgreSQL Server](#connecting-to-a-postgresql-server), [Copying Records Between the File and the Server](#copying-records-between-the-file-and-the-server), [Working Offline and Syncing Later](#working-offline-and-syncing-later), [Setting Up MediaFlow](#setting-up-mediaflow)

## Connecting to a PostgreSQL Server

*Enter the server’s host, port, database, user and password in Settings › Storage, or use the guide to set one up.*

A PostgreSQL server lets several Macs use the shared database at the same time. The server keeps the records itself; nothing on this Mac is copied to or from it. If you already have a server, fill in the fields. If you do not, Set Up a Server… walks you through making one in about ten minutes. The button is in Settings › Storage under either store, so you can prepare a server before switching to it. MediaFlow does not install anything on the NAS itself: the guide saves one file, docker-compose.yml, which the NAS’s container app runs. The guide shows the port the server will answer on, which is the one in the Port field, and offers to put it back to 5432 if it is something else; use that same port when you connect.

> **Warning:** The connection to the server is not encrypted. Use it only on a home or studio network you trust, and never forward the server’s port to the internet.

### The fields

- Host — the server’s name or address. Use NAS fills in the NAS chosen in Settings › Network. A name ending in .local keeps working when the address changes
- Port — 5432 unless you changed it
- Database and User — the names the setup guide creates are filled in for you. Change them to match an existing server
- Password — kept in your Keychain, never in preferences and never in the saved setup

Changes take effect without restarting: when Test Connection succeeds, and when you close Settings, MediaFlow connects to the server the fields now describe. When a message says the name was found, the Host is right and the Port is what to check: it must be the number the server was started with, the one before the colon on the ports line of docker-compose.yml.

The fields save as you type. On every other Mac, enter the same host, port and password; there is nothing to copy.

### Test Connection

A successful test shows the server’s version, such as PostgreSQL 16. A failed test says why:

- “…could not be found on the network” — the Host name is wrong. MediaFlow tries the name as typed and then with .local on the end, which is what most NAS names need; when that works, Test Connection corrects the Host field and says so. Otherwise use the server’s address
- “MediaFlow could not read the saved password from your Keychain” — the password is saved, but macOS would not hand it to this version without asking you. This happens once after an update. macOS cannot ask while the app is still opening, so MediaFlow tries again by itself a moment after its window appears: enter your Mac password when macOS asks, and click Always Allow. If you dismissed the question, choose Database → Reconnect Database to be asked again. macOS recognises an app across updates only when its maker has an Apple Developer ID; until MediaFlow has one, expect to be asked once after each update, for each password or key MediaFlow keeps
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
2. Put the file in a folder of its own on the NAS or computer that will run the server. The database keeps its data in a folder beside it
3. Start it: in the NAS’s container app, create a project from that folder. On a computer with Docker, run docker compose up -d in that folder. The first start takes a minute or two
4. Back in Settings, set Host and click Test Connection

### Which password goes in the file

- With no password stored yet, MediaFlow makes a new one, writes it into the file and puts it in your Keychain and the Password field
- Use the password already in my Keychain — for saving the file again for the server you already use. A server reads its password only the first time it starts, so the file must keep the same one
- Make a new password — for a server that has never been started. It replaces the one in your Keychain, so MediaFlow can no longer sign in to the old server

The database server is part of Studio Pro; without it the app keeps working with a database file. See Plans and Pricing.

See also: [SQLite File or PostgreSQL Server?](#sqlite-file-or-postgresql-server), [Copying Records Between the File and the Server](#copying-records-between-the-file-and-the-server), [Choosing and Connecting Your NAS](#choosing-and-connecting-your-nas), [Database Connection Issues](#database-connection-issues)

## Copying Records Between the File and the Server

*Copy every shared-database record from the SQLite file to the PostgreSQL server or back; the source is never changed.*

When you move from a SQLite file to a PostgreSQL server, or want a file copy of the server, MediaFlow copies every record for you. The copy reads the source and never changes or removes anything in it. Both buttons are in Settings › Storage, with PostgreSQL server selected as the Store.

- Copy the SQLite File to This Server… — brings the records in your SQLite file into the server. Use it when you first set up a server
- Copy This Server to a SQLite File… — writes the server’s records into a new file that you name. If you pick an existing file, it is replaced. Use it as a backup, or to work without the server

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

See also: [SQLite File or PostgreSQL Server?](#sqlite-file-or-postgresql-server), [Connecting to a PostgreSQL Server](#connecting-to-a-postgresql-server), [Shared Database Overview](#shared-database-overview), [Migrating Projects to the Database](#migrating-projects-to-the-database)

## Working Offline and Syncing Later

*Changes you make while the shared database is unreachable are remembered and synced when it reconnects.*

You can keep working when the shared database is out of reach, for example when the NAS is off or you are away from your network. Your edits are saved in the project file as usual. MediaFlow remembers which projects changed and syncs them to the database when it reconnects. You do not need to do anything.

### What happens on reconnect

The status line reads “Syncing offline changes…” while every project that changed is synced, not only the one that is open.

- The open project syncs in full, including clips you removed from it
- Every other project is read from its project file. Clips are added and updated in the database, but never unlinked from a project while nobody is looking at it
- A project is left alone if the database already holds a newer version, changed on another Mac

### Projects that wait

A project stays on the waiting list, and is named in the status line, until you open it. This happens when:

- Clips were removed from it while offline. Opening the project finishes the sync
- The database holds a newer version. Opening the project syncs it
- Its project file cannot be reached or read, for example because the drive it is on is not connected
- The database did not accept the sync

### The status line

The status line is at the bottom of the Database menu and in Settings › Storage. After a reconnect it takes one of two forms:

- Connected — everything is synced
- Connected · offline changes still to sync: followed by up to two project names and “and n more” — those projects are waiting. Open each one to finish

> **Tip:** With a SQLite file, only one Mac should use the database at a time. With a PostgreSQL server, several Macs can reconnect and sync at once.

See also: [Shared Database Overview](#shared-database-overview), [SQLite File or PostgreSQL Server?](#sqlite-file-or-postgresql-server), [Database Connection Issues](#database-connection-issues), [Saving Projects](#saving-projects)

---

# Storage Maintenance

## Relinking Missing Media

*Point missing clips at their files again, one at a time or by scanning a folder for matching names.*

When a file is moved or renamed outside MediaFlow, its clip shows as Missing (a red X in the Where column). Relinking tells MediaFlow where the file is now.

### Single Clip Relink

Right-click a missing clip and choose Relink…, then pick the file. Relink… appears only when one missing clip is selected. Whenever the selection includes a missing clip, the same menu offers Relink Missing Media…, which scans a folder for the selected clips.

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

Writing with the agent is part of Studio Pro, with a monthly fair-use limit; see Plans and Pricing.

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

Uploading, and reading results, are part of Studio Pro, each with a monthly fair-use limit; see Plans and Pricing.

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
- Save As (Cmd+Shift+S) — Save the project file under a new name or in a new place, and carry on working in the new file. Media files are not copied
- Revert to Saved — Discard all unsaved changes and reload from disk

A project is saved as a .vpm file. It holds the list of clips and where their files are, plus your categories, tags, ratings, notes and project settings. It does not contain the media itself.

The project file is the authority. When the shared database is connected, each save also updates the database. If the database cannot be reached, MediaFlow notes that the project changed and syncs it when the connection returns.

See also: [Moving a Project](#moving-a-project), [Renaming a Project](#renaming-a-project), [Duplicating a Project](#duplicating-a-project), [Working Offline and Syncing Later](#working-offline-and-syncing-later)

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

The question about deleting the original is answered some time after the copy was made, so MediaFlow checks again at that moment. It deletes the original only if the copy can still be reached, still holds every file of the original, and is where the open project now lives. If the drive holding the copy has been unplugged, or you have opened a different project, the original is kept and MediaFlow says why. On a local drive the original goes to the Trash; on a network volume there is no Trash and it is deleted outright.

If the project cannot be saved in its new folder, MediaFlow puts the project back at its original location and tells you. The copy is left in place for you to inspect or delete.

Cancel on the progress window stops the copy between files. The original project folder is never touched, so nothing is lost, and the partly copied folder is removed.

> **Tip:** Moving copies every file in the project folder, so check that the new location has enough free space first.

See also: [Saving Projects](#saving-projects), [Deleting a Project](#deleting-a-project)

## Editing on an Editing Drive

*Copy the project you are editing to your fastest drive, keep the library copy safe where it is, and bring the project back when the edit is done.*

A library lives on large storage, which is rarely the fastest you own. An editing drive is a folder on fast storage, such as an SSD volume on a NAS or an external SSD, for the projects you are editing now. Clips there start sooner, scrub more smoothly and drop fewer frames, in MediaFlowSwift and in your editor.

1. Open Settings → Storage and choose the Editing drive folder. You do this once
2. Open the project and choose File → Move to Editing Drive…
3. MediaFlowSwift measures the project and shows how many files and how much will be copied, where to, and how much room is free there. Click Move to Editing Drive

### What Happens

- The whole project folder is copied into the editing drive folder, under its own name. Every file is read back and compared with the original, and the number of files is checked. If anything differs the copy is removed and the project stays where it was
- The project then points at the copy: its project file, its destination and every clip inside the project folder. Clips kept outside the project folder are not copied and keep pointing where they did
- The copy in your library is kept exactly as it is. Nothing is deleted and nothing in it is changed, including its project file. The project remembers where that copy is
- Cancel stops the copy; the partial copy is removed and the project is unchanged. The same happens if the project cannot be saved in the copy
- This Mac also keeps its own note of where the library copy is, so the way back is not lost if the editing drive is unplugged and the project is opened another way

### When It Is Refused

Nothing is copied if no editing drive folder has been chosen or it cannot be reached, if the project is already on the editing drive, if a folder with the project’s name is already there, if one folder is inside the other, or if the editing drive does not have room for the project and a little over. Nor if the project folder cannot be reached, or while an import, organize, archive, proxy run or Library Moved is running: it is refused with a message, not queued. Everything is asked again when you click Move to Editing Drive, in case the sheet has been open a while.

### Returning to the Library

When the edit is finished, open the project from the editing drive and choose File → Return to Library…. MediaFlowSwift looks at both copies and shows what is new or changed on the editing drive, such as exports, renders and notes. Everything is ticked to begin with; untick anything you do not want in the library. It also says how many files are in both places already, and how many are in the library only, which are left as they are.

- Each ticked file is copied to the library, read back and compared. A new file is never written over something already there
- A changed file goes in beside the library’s own version, which is kept and renamed with “(before return)”. Nothing in the library is replaced or deleted
- Every file that is in both places is read in both places and compared. The same name and the same size is not taken as proof
- If anything cannot be carried or proved, the project stays on the editing drive, nothing is removed, and the list says which files. What was already carried stays in the library. A file that turned out to differ from the library’s, although it is the same size, is on the checklist as changed the next time you choose Return to Library, so it can be carried in beside the library’s own
- Close your editor first. A file that is written to while it is being read or copied is not counted, and one that changes after it was checked keeps the editing copy from being removed
- Then the project is saved in the library, pointing at the library’s files. The project file that was in the library is kept beside it as Name.vpm.before-repoint
- Afterwards, choose Remove the editing copy or Keep the editing copy. It is removed only after one more look finds every file in it still exactly as it was when it was carried or checked, apart from those you unticked, and after the shared database, if you use one, has been told the project is home. It goes to the Trash where that works; on a network share, which has no Trash, it is deleted. Kept, its project file is renamed Name.vpm.returned, so there are not two of the project to open
- If you untick files and choose to remove the editing copy, those files exist nowhere else. MediaFlowSwift names them and asks first

Proving the library copy means reading it, so expect roughly the time it would take to copy the project from the library. Stop abandons a file that is being checked at once, and waits for one that is being copied to finish; the project stays on the editing drive and nothing is removed. Once everything is checked and the project is being saved in the library, Stop is no longer offered. If you use a shared database it must be connected.

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

Use this when the footage is already where you want it: you copied your projects folder to a new drive or NAS, keeping the folders inside it as they were, and every project still points at the old one. Move Project is for the other case, where MediaFlowSwift does the copying.

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

Library Moved never changes or removes the project file at the old location, so that file still opens, under the same name. It is an old copy: its clips point at the old location, so they read Not at destination, and work done in it stays in it. When you open one on the Mac that ran Library Moved, MediaFlowSwift says “This is an old copy” and offers to open the current copy instead. It knows from its own note of what Library Moved did. For a library moved before this version, choose Library Moved again with the same two folders and click Find Projects: every project already followed is noted, and nothing is changed. Another Mac has no such note until Library Moved has been opened on it the same way. Separately, if a project file is kept apart from its destination folder and another file for the same project is found in that folder, MediaFlowSwift says “There is another copy”, shows where each is and when each was saved, and does not claim to know which is current. Your answer is a decision about where the project lives, and is recorded at once in this Mac’s projects list and in the shared database. Open the Current Copy (or Open the Other Copy) makes that copy the project’s home, so it is the one that opens next time. Use This Copy and Don’t Ask Again, offered when MediaFlowSwift does not know which copy is current, makes the open copy the home and stops the question for that file. Stay Here only looks: nothing is recorded, this Mac’s projects list points at the other copy, saves made here are not sent to the database (the status line says Not synced), and you are asked again next time.

The same question is asked when the shared database records the project as living in another file that is still there. A project is written to the database only from the file the database says it lives at, unless that file is gone, Library Moved has noted it as the old copy, or you have said otherwise. That is what keeps a stale copy, opened by mistake on any Mac, from overwriting what every Mac sees. When the old drive is retired, the old copies go with it.

If the file the database names is not there at all when you open a project from the projects list — the drive is off, or the project was moved without Library Moved — MediaFlowSwift looks for the project where it may be: where Library Moved noted it went, in its destination folder, and in its library folder if it is out on an editing drive. A file that holds this very project is opened, and the projects list and the database are pointed at it. If none is found, the project opens from the database alone and one notice says so. Your changes are then kept in the shared database, and the project file is left as it is until its drive is back, when saving to it resumes on its own, or until you choose Save As to give the project a new home. If you quit before the drive is back, the file has not caught up: open the project from the projects list again rather than by the file, and it comes from the database.

### Stopping and Running It Again

Stop ends the reading within a moment and leaves the project being checked exactly as it was; projects already finished stay finished. Running Library Moved again skips projects that already point at the new location and reads only what is left: a project whose folder you copied across later, or the clips of a project that could not be followed the first time. It cannot start while an import, organize, archive, move, relink or Clear Card is running. While it runs, organizing, refiling, Clear Card, Free Up Space, archiving and restoring, Move Project, Change Destination, relinking, workflow steps and installing an update are all refused until it has finished. Importing is not: new clips join the open project and are kept.

The progress bar moves as each clip is finished, not while one is being read. The line under it names the clip being read and its size, so a long clip does not look like a stall.

> **Tip:** Reading every checksummed clip takes as long as copying it would. On a wireless connection expect about a minute for every 4 GB.

See also: [Moving a Project](#moving-a-project), [Change destination folder](#change-destination-folder), [Clear Card](#clear-card)

## Deleting a Project

*Take a project off the project list, or also delete its folder and everything in it.*

Choose Projects → Browse Projects, right-click a project and choose Delete Project…. You are offered two things:

- Remove from List Only — Takes the entry off the list. Every file stays on disk
- Move Folder to Trash — Takes the entry off the list and deletes the project folder with everything in it

Move Folder to Trash does not act at once. MediaFlow first counts what is in the folder and shows a second confirmation with the number of files and their total size. You must tick “I understand this cannot be undone” before the confirm button works.

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

## Project Checklist

*Track nine milestones of a project, from import through archive, in the older checklist screen.*

The Project Checklist shows how far a project has come. Choose Workflow → Plan & Deliver → Project Checklist (legacy)… to open a sheet with nine fixed milestones. Six carry an Auto badge and are ticked from the state of your clips. Three you mark yourself with the Done button beside them; Undo unmarks them. The pipeline strip above the media list now shows the same progress at a glance, which is why the menu item says legacy.

### Milestones

- Media Imported (auto) — At least one clip in the project
- All Clips Categorized (auto) — Every clip has a category other than Uncategorized
- Media Organized (auto) — Every clip is at the destination: its Where column reads At destination or Size mismatch
- Organized Copies Verified (auto) — Every clip reads At destination, with no Size mismatch. This reflects the size check made by Re-check files; it does not re-read the files
- Selects Picked (auto) — At least one clip marked Hero or Maybe
- Exported to NLE (manual)
- Local Originals Cleaned (manual)
- Project Backed Up (manual)
- Archived (auto) — Ticked when Archive to USB completes

### Phase and Progress

The header shows the project phase — Setup, then Production once media is imported, Post-Production once it is organized, and Delivered when all nine items are complete — together with an n/9 progress ring (orange below 50%, blue above, green at 100%). Completed items show the date they were completed.

Click Refresh to re-evaluate the automatic items after you make changes. The checklist is saved inside the .vpm project file, and the automatic items are recomputed every time the project loads.

See also: [Understanding the Pipeline Strip](#understanding-the-pipeline-strip), [Organizing Media to Storage](#organizing-media-to-storage), [Archiving a Project to USB](#archiving-a-project-to-usb), [Star Ratings & Selects](#star-ratings--selects)

## Archiving a Project to USB

*Copy a finished project folder to a numbered USB drive for long-term storage, with every file checked before the original may go.*

Archive to USB frees your working storage by copying a finished project to a drive you can put on a shelf. It copies the whole project folder to a removable drive, checks the copy, and records where it went in the central database. Archive volumes are numbered (USB #0001, USB #0002, …) so a project can always be found again. Only the project folder is copied; media organized to a destination outside the project folder is not included.

### Archiving

1. Plug in the drive and choose Workflow → Archive to USB…; click Scan if it is not listed
2. A drive that has never been used shows “(not initialized)”. Select it, give it an optional label such as “Interviews 2026”, and click Set Up. MediaFlow writes a hidden marker file to the drive and assigns the next number. Numbers are permanent
3. Pick a drive. The smallest initialized drive that still fits is marked Recommended; drives that are too small show an orange warning
4. Click Archive. Progress moves through Preparing, Copying, Flushing, Verifying, Updating Database, and Done
5. Dismiss the progress dialog to reach the completion screen described below

Every file is read back from the drive after it is written and compared with its original by checksum, so a file damaged on the way — even one that kept its size — fails the archive rather than being recorded. The Verifying step then confirms the number of files and their total size. Because each file is read twice, archiving takes noticeably longer than a plain copy, most of all on a USB hard drive or with a project made of many small files. File contents and dates are archived; Finder tags and similar extras are not, because most archive drives are formatted in a way that cannot hold them. On success the project is marked Archived with the volume number, date, and path, and the Project Checklist’s Archived item completes. In the project browser the row reads “Archived → USB #0007”.

### Completion screen

After the progress dialog closes, an Archive Complete screen summarizes the result — “Archived 312 files (48.2 GB) to USB #0007 · verified” — and lists the drive (or every drive, for a split archive) with an Eject button for each one that is still connected. “Keep Original” closes the screen and leaves both copies in place. “Delete Original…” removes the original project folder, wherever it is stored. It scans the folder first and then shows the same confirmation used when you delete staged files or delete a project: the file count, the total size, a warning when the folder is on a network volume (where there is no Trash to recover from), and a checkbox you must tick before the delete button enables. Confirming moves the folder to the Trash, or deletes it outright on a network volume.

> **Warning:** Deleting the original leaves the USB drive as the only copy of the project. Every file on it was compared with its original by checksum, but a single drive can still fail on the shelf; for footage you cannot replace, archive to a second drive as well before you delete. “Delete Original…” is disabled when the database update was queued instead of saved; keep the original until the database has recorded the archive.

### Archiving a project again

If the drive already holds an archive of the project, the new archive is written beside it and checked first. Only when every file has passed is the old archive replaced. If the new archive fails or you cancel, the old one is left exactly as it was.

- MediaFlow will not archive a project folder that holds none of the project’s clips. This matters most after you have deleted the original: the archive on the drive may be the only copy, and archiving an empty folder over it would destroy it
- MediaFlow will not replace an archive with one that holds fewer files. If the project really has shrunk because you removed clips on purpose, archive it to a different drive, or remove the old archive from the drive yourself first
- If the app quits or the drive is unplugged at the moment of replacement, the previous archive is put back the next time you archive or restore that project

### Splitting Across Drives

If the project is larger than any one drive, click Split Across Drives…. MediaFlow plans which folders go on Drive 1, Drive 2, and so on, then asks for each drive in turn. If a run is interrupted, opening the sheet again detects the partial copies and the button reads Resume Archive.

### Cancelling

Cancel on the progress window stops an archive between files. Files already written to the drive stay there. A split archive that is stopped part way can be picked up later with Resume Archive.

Archiving needs the central database to record volumes and projects.

See also: [Restoring an Archived Project](#restoring-an-archived-project), [Managing Archive Volumes](#managing-archive-volumes), [Project Checklist](#project-checklist), [Shared Database Overview](#shared-database-overview), [Freeing Up Space](#freeing-up-space), [Moving a Project](#moving-a-project)

## Restoring an Archived Project

*Bring a project back from its USB archive drive, or drives, with every file checked against the archive.*

To bring an archived project back, open the project browser, right-click the archived project, and choose Restore from Archive…. Restoring needs the central database, which records which drive holds each project.

1. Plug in the archive drive. It does not have to mount under the same name it had when you archived; MediaFlow looks for the project on every connected archive drive
2. Choose the folder to restore into. The project comes back as a folder inside it, with the name it was archived under. If a folder with that name is already there, the restore stops before copying anything; choose a different folder
3. For a project split across drives, MediaFlow asks for each drive in turn and merges them into the one folder
4. When it finishes, the project is no longer marked Archived and its clips point at the restored files

A restore is checked more strictly than an archive. Every file is read back after it is copied and compared with the file on the drive by checksum. Each drive is also checked against the number of files recorded when the project was archived, so a drive that has lost a file since then stops the restore rather than quietly bringing back less than you archived. (Projects archived before this check was added have no recorded count for a single drive; those are checked file by file only.) If anything fails, the partly restored folder is removed, the project stays marked Archived, and nothing on the drive is changed.

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

MediaFlowSwift comes in two plans. Studio is all the file management: importing from cards, phones and folders; categorizing, reviewing, rating and tagging; Organize with every copy proved; Free Up Space; Archive and restore; proxies; the editing drive; Library Moved; reports; Help; updates and problem reports. Studio Pro is everything in Studio, plus the title, description, chapters and tags written for you, uploading to YouTube with thumbnail and schedule, results read back from YouTube, and the database server that gives every Mac the same projects list.

### The trial

The first time this copy is opened, a 14-day trial of Studio Pro begins. No card is asked for. Settings › Plan shows how many days are left, and a banner in the main window says so too; Later hides it for this session. The trial’s start is kept in your Keychain, not in the preferences, so installing the app again does not start it again, and a clock turned back does not lengthen it.

### When a plan ends

Nothing you have made is taken away. Every project opens, every clip shows where it is, restoring from an archive and copying footage out work, and so do Help, reports, updates and problem reports. What pauses is what makes new work: importing, Organize, proxies, moving a project to the editing drive, writing, publishing, and the database server. Each of those says which plan opens it, with a Plans… button that shows the plans side by side.

### Fair use

Writing with the agent, uploading and reading results cost us something each time, so each has a monthly limit — generous, and shown in Settings › Plan. Reaching one pauses that feature until the start of the next month; nothing else is affected.

### Buying a plan

Prices are announced with the first public release, monthly or yearly. A plan follows you, not a Mac: the Macs you use share it. Until plans go on sale, Choose a plan… explains them and asks for nothing. Nothing on the Plan tab is sent anywhere.

See also: [The Settings Window](#the-settings-window), [Importing from a Card, Drive or Folder](#importing-from-a-card-drive-or-folder), [Organizing Media to Storage](#organizing-media-to-storage), [Preparing a Video for YouTube](#preparing-a-video-for-youtube), [Connecting to a PostgreSQL Server](#connecting-to-a-postgresql-server)

## The Settings Window

*What each of the nine Settings tabs is for: General, Network, Storage, Cameras, Categories, Analysis, Privacy, Notifications and Plan.*

Choose MediaFlow → Settings (Cmd+,). The window has nine tabs. This topic says what each one is for; the related topics go into detail.

### General

- Setup — Run Setup Again… reopens the first-run setup questions. MediaFlow saves your setup whenever you quit and puts it back if this Mac’s settings are ever lost. Save Setup Now saves it at once. Restore Saved Setup puts every saved setting back, replacing what is set now. Passwords and API keys are not part of the saved setup; they stay in the Keychain
- Updates — “New builds come from” is where MediaFlow looks for a newer version: Choose… a location, or Follow the NAS. Until one is set, the app does not look. “Check for new versions automatically” looks shortly after launch and on wake, and shows a banner, never a dialog. To look now, choose MediaFlow → Check for Updates
- About — The version and build you are running

### Network

Where you choose the NAS that MediaFlow reconnects to. Nothing is assumed: until you choose one, the tab says “No NAS chosen yet”.

- Shares already mounted on this Mac are listed. Click Use this beside the one you want; it then reads In use
- Look for servers searches the network. Connect to… opens a found server in Finder, which asks for the password and shows its shares. Mount one, then click Use this
- Type the address instead takes an smb:// address. A name ending in .local keeps working when the NAS gets a new address
- Once a NAS is chosen, the tab shows Connected or Not connected. Connect now mounts it again. Forget stops using it, and the settings that follow the NAS go back to unset

### Storage

- Enable Central Database — Turns the shared database on and connects
- Store — SQLite file or PostgreSQL server. Changing it reconnects; it does not move any records
- SQLite file — Choose… or Change… picks the database file; Type the path instead is there if you need it. The line below says whether the file can be reached. Reset to Default points at MediaFlow/mediaflow.db on the chosen NAS, and is dimmed until a NAS is chosen
- PostgreSQL server — Host (Use NAS fills in the chosen NAS), Port, Database, User and Password. The password is kept in your Keychain. Test Connection shows the server version or the reason it failed. Set Up a Server… is a guide to making one. Two Copy buttons move every record between the file and the server
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

See also: [The Settings Window, Tab by Tab](#the-settings-window-tab-by-tab), [Privacy: What Leaves This Mac](#privacy-what-leaves-this-mac), [Setting Up MediaFlow](#setting-up-mediaflow), [Choosing and Connecting Your NAS](#choosing-and-connecting-your-nas), [Saved Setup: A Copy of Your Settings](#saved-setup-a-copy-of-your-settings), [Updating MediaFlow](#updating-mediaflow), [SQLite File or PostgreSQL Server?](#sqlite-file-or-postgresql-server), [Connecting to a PostgreSQL Server](#connecting-to-a-postgresql-server), [Adding, Renaming, Retiring and Removing Categories](#adding-renaming-retiring-and-removing-categories), [Using a Model to Suggest Categories](#using-a-model-to-suggest-categories), [How MediaFlow Verifies Copies](#how-mediaflow-verifies-copies), [Smart Notifications](#smart-notifications)

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

Menu shortcuts work anywhere in the main window. The Review keys work while Review is open (Workflow → Review); they are single keys with no modifier. The Video Playback keys work while the video preview has keyboard focus: click the preview first.

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

`Cmd+Shift+F` — Global Search…

`Cmd+Shift+P` — Browse Projects…

---

### Editing

`Cmd+F` — Find Clips…

`Delete` — Remove from Project

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

### Video Playback

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

1. Mount the drive or share. For the NAS you chose in Settings › Network, click Connect now there, or choose Database → Reconnect to NAS. Then choose Workflow → Repair → Re-check files
2. If the files moved, choose Workflow → Repair → Relink Missing Media and pick the folder they are in now
3. If the whole destination moved, choose Workflow → Repair → Change destination folder
4. For one file, right-click the clip, choose Relink… and pick the file

See also: [Relinking Missing Media](#relinking-missing-media), [Change destination folder](#change-destination-folder), [Understanding the Where Column](#understanding-the-where-column), [Choosing and Connecting Your NAS](#choosing-and-connecting-your-nas)

## Reporting a Problem

*Put together a report of what went wrong, with personal details taken out, to copy or save. Nothing is sent.*

Choose Help → Report a Problem…, or click Report a Problem… where it is offered: on an error message, and under the list of files that failed in a copy. Say what happened and what you were doing, and leave an email address if you would like a reply. MediaFlowSwift adds what helps find a fault, and shows you the whole report before anything else happens. You can change any of it.

### What Is in a Report

- What you wrote, exactly as you wrote it
- The version of MediaFlowSwift and of macOS, whether the Mac is Apple silicon or Intel, the kind of shared database you use (never its address), and how many clips are in the open project
- A summary of any crashes and hangs macOS recorded for MediaFlowSwift in the last two weeks: what kind of failure, how often (times are in UTC), and where in the program it happened. Two sources say so: the report files macOS writes in Logs/DiagnosticReports in your Library, of which MediaFlowSwift reads only the ones about itself, and MetricKit, Apple’s service that hands an app its own crash and hang diagnostics on a later launch. The same fault told by both is counted once. Neither leaves your Mac unless you send a report
- Whether the last run ended without quitting
- The last 150 lines of MediaFlowSwift’s log (Help → Show Log)

### What Is Taken Out

Before you see the report, MediaFlowSwift takes out of everything it adds, including an error message it quotes: your account name and home folder; the names of your drives; every folder and file name in a path, which becomes /…/&lt;file>.mp4, keeping only the kind of file; the names of the projects this Mac knows and of the open project’s clips and cameras; the names and addresses of your computers and servers; email addresses; and map coordinates. Drives, computers, projects and clips are numbered, so the same drive is &lt;drive-1> all the way through and the report can still be followed. From a crash report it takes only the fields listed above: the device identifier and account details Apple puts in those files are never picked up. Passwords, keys and tokens are never in the log or a report; they live only in your Keychain.

It errs on the side of taking out too much. It cannot know a name it has never been told, such as a project on another Mac mentioned in the log, so read the report over; and what you type yourself is left exactly as you typed it. Once you edit the report, the fields above it stop changing it, so nothing you wrote is lost; Start Again from the Fields Above makes it afresh.

### Sending It

Copy Report puts the text on the clipboard; Save… writes it to a file; sending it by email or however you like is up to you. There is also a Send button, if Sending problem reports is turned on in Settings › Privacy; it needs the address and key of a report relay entered there, and Test tells you whether the relay is reachable. Whoever supports your copy of MediaFlowSwift gives you both, and can tell you whether the reports they receive are kept private; an email address you give for a reply goes with the report. Send sends the text exactly as it is in the window, with a title, a random identifier for this copy of the app, and the crash signature if there is one, to that relay, which files it as an issue for the people who make MediaFlowSwift. The window then shows the report’s number. If the same crash has been reported before, your report is added to it. Nothing is ever sent on its own, and while the switch is off MediaFlowSwift makes no connection to do with reports.

### After a Crash

If MediaFlowSwift quit unexpectedly, or did not quit cleanly (a force-quit, or the Mac losing power), it says so once, the next time it opens, and offers a report. If macOS itself stopped the app, for instance because of how this copy was installed or signed, it says that instead: it is not something you did.

### Problems That Are Yours to Fix

A full disk, a drive that is locked, cannot be read or written, or is no longer connected, a network drive that stopped answering, a folder MediaFlowSwift is not allowed to use: these are not faults in the program, and a report about one would tell nobody anything. On an error message, and under the list of files that failed in an import, organize, archive or move, MediaFlowSwift says which it is and what to do about it, and does not offer to report it. Help → Report a Problem… is always there if you disagree.

Some failures could be either. A file that is not where it was expected may be on a drive that is unplugged, or may be a mistake in the program; so may a timeout, or a damaged database file. For these MediaFlowSwift says what to try and offers a report as well.

See also: [Database Connection Issues](#database-connection-issues), [Clips Showing as Missing](#clips-showing-as-missing)

## Database Connection Issues

*What to check when the shared database will not connect, for a SQLite file and for a PostgreSQL server.*

The shared database is optional, and the project file (.vpm) is the authority. When the database is unreachable you can keep working; only the cross-project tools stop. The current state is on the last line of the Database menu and in Settings › Storage.

### If You Use a SQLite File

Symptom: the status reads “Connection failed: …”, “NAS offline” or “Waiting for NAS…”. Cause: the file, or the drive or share it is on, cannot be reached.

1. Open Settings › Storage and read the line under Database. “Database file accessible” means the file can be reached. “Database file not found (will be created on connect)” means the path is reachable but holds no file yet. “No database file chosen yet” means you need to click Choose…
2. If the file is on a NAS, open Settings › Network. If it says Not connected, click Connect now, or choose Database → Reconnect to NAS
3. Choose Database → Reconnect Database
4. If the path is wrong, click Change… and pick the file. Reset to Default points at MediaFlow/mediaflow.db on the chosen NAS; it is dimmed until you choose a NAS in Settings › Network

MediaFlow watches the volume and connects again by itself when it comes back, including after the Mac wakes from sleep.

### If You Use a PostgreSQL Server

Open Settings › Storage and click Test Connection. It shows the server’s version, or one of these messages:

- “Nothing is listening at host, port …” — PostgreSQL is not running there, or the Port is wrong. Start the server, or correct the Port (usually 5432)
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
3. Go back to MediaFlowSwift. It looks again every few seconds for about ten minutes and connects by itself as soon as macOS lets it through. There is no need to restart it, or to choose Reconnect Database. After ten minutes, choose Database → Reconnect Database

MediaFlowSwift knows this within a few seconds of trying, where it used to wait ten and then guess. It asks macOS why the connection is being held back, looks twice, and still gives the connection itself three seconds to get through before saying so. If macOS will say nothing, you get the ordinary message about a server that did not answer instead, which still mentions the switch. You may also be asked once for leave to read the saved password after an update; choose Always Allow.

### The Log

Help → Show Log reveals app.log in the Finder (it is in Logs/MediaFlow in your Library). MediaFlowSwift writes what it does there, and warnings and errors with their reasons in the database’s or the system’s own words, such as why a sync failed. It names projects, clips, cameras and the database server’s address. It never holds passwords or keys, nor the contents of a rejected database row. A new file is started when it passes two megabytes, and the one before is kept as app.previous.log. Nothing is sent anywhere: it is yours to read, or to attach when you report a problem.

### Several Macs

Symptom: work done on one Mac is missing from the database after another Mac has used it. Cause: a SQLite file is for one Mac at a time. Each Mac works on its own local copy and writes the file back when it disconnects or quits, so the last Mac to quit wins. Fix: take turns, or switch to a PostgreSQL server, which several Macs can use at once. Your projects are not harmed either way, because the project files are the authority.

### What the Status Line Means

- Connected, Synced — All is well
- Connecting…, Reconnecting…, Waiting for NAS… — MediaFlow is trying; give it a moment
- Sleeping, Disconnected — The connection was closed for sleep, or by Disable & Disconnect
- NAS offline — The volume that holds the database file is not mounted
- Connection failed: … — The reason follows the colon
- Sync failed — A save could not be written to the database. Your project file is saved. MediaFlow has noted the project and syncs it after the next successful connection. The reason is in the log: choose Help → Show Log
- Syncing offline changes… — MediaFlow is sending the database what changed while it was away
- Connected · offline changes still to sync: … — The named projects are still waiting. Open each one to finish its sync

See also: [Shared Database Overview](#shared-database-overview), [Working Offline and Syncing Later](#working-offline-and-syncing-later), [Connecting to a PostgreSQL Server](#connecting-to-a-postgresql-server), [SQLite File or PostgreSQL Server?](#sqlite-file-or-postgresql-server), [Choosing and Connecting Your NAS](#choosing-and-connecting-your-nas), [Global Search Finds Nothing](#global-search-finds-nothing)

## Global Search Finds Nothing

*Why Global Search can come back empty on an older database file, and how this version repairs the search index itself.*

Symptom: Global Search returns no results, even for a filename you know is in a project.

Cause: SQLite database files made by an early version have a search index that stores nothing, so every search comes back empty. A PostgreSQL server never had this fault.

Fix: nothing to do by hand. The first time this version connects to the file, it replaces the index and fills it again from the clips already in the database. If search is still empty, choose Database → Reconnect Database, or quit and open MediaFlow again.

### Other Things to Check

- The database is connected. If the search window says “Database not connected”, see Database Connection Issues
- You pressed Return or clicked Search. Results do not appear as you type
- The Category and Camera filters are not hiding the clip
- The project is in the database. Projects made before you turned the database on need Database → Migrate Projects

See also: [Global Search](#global-search), [Database Connection Issues](#database-connection-issues), [Migrating Projects to the Database](#migrating-projects-to-the-database)

## NAS 'Resource Busy' Errors

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

The sidebar’s Smart Groups filter the media list to clips that still need attention: Not at destination, Missing, Uncategorized, Unrated, Unreviewed and Reject candidates. Unreviewed holds clips with an import-analysis proposal nobody has confirmed. Reject candidates holds clips import analysis flagged as probable rejects.

> **Tip:** Choose Workflow → Repair → Re-check files to bring every Where badge up to date.

See also: [Re-check files](#re-check-files), [Clips Showing as Missing](#clips-showing-as-missing), [Proposals: What Import Analysis Suggests](#proposals-what-import-analysis-suggests)
