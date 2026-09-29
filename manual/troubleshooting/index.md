---
layout: manual
title: "Troubleshooting — MediaFlowSwift Manual"
description: "A red X in the Where column means MediaFlow cannot find the file; usually a drive or share is not mounted, or the file moved."
permalink: /manual/troubleshooting/
generated: tools/import-guide.sh
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

See also: [Relinking Missing Media](/manual/storage-maintenance/#relinking-missing-media), [Change destination folder](/manual/organizing-media/#change-destination-folder), [Understanding the Where Column](#understanding-the-where-column), [Choosing and Connecting Your Network Share](/manual/setup-network/#choosing-and-connecting-your-network-share)

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

See also: [Reporting a Problem](#reporting-a-problem), [Privacy: What Leaves This Mac](/manual/setup-network/#privacy-what-leaves-this-mac)

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

See also: [Shared Database Overview](/manual/shared-database/#shared-database-overview), [Working Offline and Syncing Later](/manual/shared-database/#working-offline-and-syncing-later), [One Mac at a Time on a Database File](/manual/shared-database/#one-mac-at-a-time-on-a-database-file), [Connecting to a Database Server](/manual/shared-database/#connecting-to-a-database-server), [Database File or Database Server?](/manual/shared-database/#database-file-or-database-server), [Choosing and Connecting Your Network Share](/manual/setup-network/#choosing-and-connecting-your-network-share), [Searching All Projects Finds Nothing](#searching-all-projects-finds-nothing)

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

See also: [Searching All Projects](/manual/shared-database/#searching-all-projects), [Database Connection Issues](#database-connection-issues), [Migrating Projects to the Database](/manual/shared-database/#migrating-projects-to-the-database), [One Mac at a Time on a Database File](/manual/shared-database/#one-mac-at-a-time-on-a-database-file), [Database File or Database Server?](/manual/shared-database/#database-file-or-database-server)

## Network Share 'Resource Busy' Errors

*Why deleting or moving a project folder on a network share can fail with “resource busy”, and what to try.*

Symptom: deleting or moving a project folder on a network share fails with a “resource is busy” error.

Cause: a file in the folder is still open, often because a preview has only just closed. Network shares release files more slowly than a disk in this Mac.

### Fixes

- Wait a few seconds and try again. MediaFlow already retries up to 3 times by itself
- Close any preview of a file in that folder
- Disconnect the share in Finder and connect it again
- If the folder is still stuck, relaunch Finder: hold Option, right-click the Finder icon in the Dock and choose Relaunch

See also: [Clips Showing as Missing](#clips-showing-as-missing), [Deleting a Project](/manual/project-management/#deleting-a-project)

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

See also: [Importing from a Card, Drive or Folder](/manual/importing-media/#importing-from-a-card-drive-or-folder), [Importing from iPhone or Camera](/manual/importing-media/#importing-from-iphone-or-camera), [The Import Sheet and Completion Card](/manual/importing-media/#the-import-sheet-and-completion-card)

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

See also: [Re-check files](/manual/organizing-media/#re-check-files), [Clips Showing as Missing](#clips-showing-as-missing), [Proposals: What Import Analysis Suggests](/manual/organizing-media/#proposals-what-import-analysis-suggests)

<div class="chapter-nav" role="navigation" aria-label="Chapters">
<a rel="prev" href="/manual/keyboard-shortcuts/">&larr; Keyboard Shortcuts</a>
<a href="/manual/">All chapters</a>
<span></span>
</div>
