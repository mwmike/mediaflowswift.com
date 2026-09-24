# What's New in MediaFlow

MediaFlow takes your footage from the card to the finished upload, and keeps every clip safe along the way. Here is what each new version brings.

*Every finished piece of work adds its line under "Coming next" before it is closed. When a version ships, that section takes the version's name.*

## Coming next

Nothing waiting. Everything finished so far is in 1.10.30.

## 1.10.30 · September 24, 2026

**Back on your database after an update, by itself.**

- **Back on your database after an update, without flipping a switch.** When macOS keeps a freshly updated MediaFlowSwift off your local network, the app no longer gives up after ten minutes: it keeps checking, less often as time goes on, checks again the moment you come back to it, and connects as soon as macOS lets it through. Nothing connects before you agree to the terms, either.

## 1.10.29 · September 24, 2026

**Your shared drive reconnects by itself.**

- **Your share comes back by itself.** When the network blinks or the server stops answering and macOS drops the share you chose in Settings › Network, MediaFlowSwift now reconnects it for you: after a few seconds, then every few minutes until it is back, with a strip at the top of the window saying so. It never asks for a password on its own, leaves a share you eject in Finder alone, and waits while your Mac sleeps.

## 1.10.28 · September 24, 2026

**Ready for customers: terms of use, and every copy updated from the website.**

- **Clear Card counts one clip properly.** Its finish screen now says “1 clip that could not be verified was left on the card”, not “were”, and “1 file was refused”; when nothing was kept, it leaves the line out rather than counting zero clips. The confirmation before deleting leaves out its zero too.
- **Every copy updates from the website.** New versions now come from mediaflowswift.com for everyone, checked every few hours and every half hour while you are offline, so there is nothing to choose in Settings › General › Updates. The option to update from a copy of the app on a share of your own is gone.
- **Terms of use, agreed once.** The first time MediaFlowSwift opens, it shows the terms it is sold under, with the main points in four short paragraphs, and starts once you click Agree; until then it connects to nothing and opens nothing. It asks again only when the terms change, and says what changed. Help › Terms of Use shows them any time. Your agreement is kept on your Mac and nowhere else, and on a new copy the free trial's 14 days start when you agree.

## 1.10.27 · September 24, 2026

**Ready to sell: your licence key, and new versions from the website.**

- **Only a real plan counts.** A shortcut the maker uses while building MediaFlowSwift, which could grant a plan without one, now works only in development builds, never in the app you install.
- **Your licence key.** Plans are bought on mediaflowswift.com, and the key from the thank-you page goes into Settings › Plan. One key works on up to three Macs, which Settings lists by name and can release. The app checks the key once a day and keeps the last answer for two weeks, so a trip without a connection pauses nothing. Settings › Privacy says exactly what the check sends, and to whom.
- **New versions from the MediaFlow website.** MediaFlowSwift can now update itself from mediaflowswift.com, and a fresh install does so from the start: one small file names the newest version, the download is checked against what the site promised and for its maker’s signature, and then it installs as before. A folder or share of your own still works, and is what a Mac already set up that way keeps using until you choose the website in Settings › General › Updates.

## 1.10.26 · September 22, 2026

**Your local network, kept after an update.**

- **Your local network, kept after an update.** The copy of the last version that MediaFlowSwift keeps for Revert now lives in its own support folder instead of beside the app in Applications. With two copies there, macOS sometimes judged the wrong one when the app asked for your local network after an update, and the shared database stayed out of reach until you flipped the switch. A copy still beside the app is moved the first time this version opens.

## 1.10.25 · September 22, 2026

**Hangs noticed, shares connected the direct way.**

- **Hangs noticed too.** MediaFlowSwift now also hears from Apple’s own diagnostics service about crashes and, new, about times it stopped responding, and tells you at the next launch, with the details ready for a report. The same fault told two ways is counted once.
- **Connecting your share, the direct way.** MediaFlowSwift now asks macOS to connect your network share itself, in one step, instead of going through a script: quicker, and when a password is needed it is macOS’s own dialog that asks.

## 1.10.24 · September 22, 2026

**Nothing new inside; a first run for the new installer.**

- **The same app, installed the new way.** This version changes nothing you will see. It exists so that the installer introduced in 1.10.23, which tells macOS which copy is the app before reopening, gets its first real run. If your local network connects without a trip to System Settings afterwards, it worked.


## 1.10.23 · September 22, 2026

**An update that introduces itself.**

- **An update that introduces itself.** After installing a new version, MediaFlowSwift now tells macOS which copy is the app before it reopens, so the permission you gave it for your local network is meant to carry over instead of asking for the switch once more. Help says plainly what to do if macOS still asks.

## 1.10.22 · September 22, 2026

**Studio and Studio Pro, with a trial of everything.**

- **Two plans, and a trial of everything.** MediaFlowSwift now comes as Studio, all the file management, and Studio Pro, which adds the writing, publishing and the database server. Every copy starts with 14 days of Studio Pro, no card asked. When a plan ends nothing you made is taken away: every project still opens and every clip still shows where it is; only new imports, Organize, proxies, the editing drive, writing, publishing and the server wait. Settings › Plan shows where you stand. Prices come with the first public release.

## 1.10.21 · September 22, 2026

**See what is new before you install it.**

- **Know what you are installing.** The update window now lists what is new in the version it offers: the headline and the points of every version you have not seen, straight from these notes. The banner carries the headline too.

## 1.10.20 · September 22, 2026

**The import list, in your order.**

- **Sort the import list your way.** In the Import sheet, click Filename, Date, Type, Length or Size to sort the clips on a card, a drive or a folder, click again to reverse, and MediaFlowSwift remembers your choice for the next import.

## 1.10.19 · September 22, 2026

**Your footage, found where it is.**

- **Signed by Apple's Developer ID.** From this version MediaFlowSwift carries Apple-verified signing and notarization, so macOS opens it without a warning on any Mac, and future updates no longer need the Local Network switch flipped or a password re-entered. This first time, macOS asks once.
- **Your share, connected when you need it.** MediaFlowSwift now connects the network share you chose by itself: shortly after launch, after your Mac wakes, and before opening any project that lives on it. And a clip whose drive is simply not plugged in is no longer called missing: it reads Volume not connected until the drive is back, and nothing about it is changed meanwhile.
- **A moved project opens where it is.** Open a project from the projects list and MediaFlowSwift now finds it even when it has moved since the list last saw it, and quietly points the list and your shared database at the new place. If the drive it lives on is not connected, the project opens from your shared database and says so once, with a Save As button, instead of failing to save three times a minute.

## 1.10.18 · September 21, 2026

**Ready for what comes next.**

- **The last update that asks.** MediaFlowSwift is moving to a signature from Apple’s Developer ID. This version is the bridge: it knows the new signature and will accept it. From the version after this one, an update no longer needs the network switch flipped or a password re-entered.
- **Reports get a first look within the hour.** Every problem report that reaches us gets an automatic first assessment, matched against the code and against earlier reports, usually within the hour, so a real fault stands out the day it is sent.

## 1.10.17 · September 21, 2026

**When something goes wrong, we hear about it, and you stay in control.**

- **Tell us what went wrong, in one click.** Help → Report a Problem puts together everything that helps find a fault, takes out your name, your drives, your folders and file names, the projects it knows and your computers, and shows you every word before you copy, save or send it. Sending is off until you turn it on, and even then nothing goes anywhere until you click Send. And if MediaFlowSwift ever quits on you, it notices next time and has the details ready.
- **Plain answers for plain problems.** A full disk, a locked card, a drive that dropped off: when a copy, an import or a save fails for one of those reasons, MediaFlowSwift now says which, and what to do about it.

## 1.10.16 · September 21, 2026

**One project, one truth, on every Mac.**

- **Your shared database, truly shared.** On a database server, saved changes to a project were not reaching the database at all: it kept only what it started with. Saves now reach it, so your projects list, your search and your other Macs see today’s work, not last week’s. And an old copy of a project, opened by mistake, can no longer overwrite the real one’s record.
- **Pick a copy once.** When MediaFlowSwift finds two copies of a project, your answer now sticks: the copy you choose is the one that opens next time.
- **A log you can read.** When something goes wrong behind the scenes, Help → Show Log now tells you what, and why.

## 1.10.15 · September 21, 2026

**Looks right on every screen.**

- **A tidy grid at any size.** On a smaller window, Grid view let each thumbnail spill over the tile beside it. Every tile now keeps to its own space, however narrow the window.

## 1.10.14 · September 21, 2026

**The right copy, every time.**

- **No more working in the wrong copy.** After you move your library, the old project files are still sitting on the old drive, looking just like the real thing. Open one by mistake and MediaFlowSwift now tells you, and takes you to the current copy in one click. And clips that are safe on another drive no longer claim to be "Only on card": they say where they really are.

## 1.10.13 · September 21, 2026

**It knows where everything is, and tells you when something is in the way.**

- **Always know where a project is.** Projects out on your editing drive now wear a badge in the projects list, on every Mac that shares your database. Drive not plugged in? MediaFlowSwift offers the library copy to look at instead. And if you move your library while a project is out, it still finds its way home.

- **Back online in seconds after an update.** Sometimes macOS quietly keeps a freshly updated app off your network, and your shared database stops connecting for no visible reason. MediaFlowSwift now spots that in a few seconds, tells you exactly which switch to flip, takes you there with one click, and reconnects by itself the instant you do.

## 1.10.12 · September 21, 2026

**Cut fast. Keep safe.**

- **Edit on your fastest drive.** Tell MediaFlowSwift where your fast storage is, and Move to Editing Drive puts the project you are cutting right on it, every file checked. Your library copy stays exactly where it is, untouched, as your safety net. When the cut is done, Return to Library shows what you made, carries back what you tick, checks every file against the library, and only then clears the fast drive for the next project.

## 1.10.11 · September 20, 2026

**Press play. It just plays.**

- **Smooth playback from your NAS, in one click.** Big 4K clips on a network drive can stutter when the network hiccups. When MediaFlowSwift sees you playing one, it offers to make a small, fast copy for previewing, for that clip or for the whole project, and switches to it right where you were watching. Your originals are never touched.

## 1.10.10 · September 20, 2026

**Moving house, made easy.**

- **New drive? One command.** Copied your library to a new NAS or drive? Library Moved points every project at the new place in one go. Nothing is copied, and MediaFlowSwift only follows a clip it has checked is the same file.

## 1.10.9 · September 20, 2026

**It remembers, so you don’t have to.**

- **No more silent stalls after an update.** If macOS needs your okay before MediaFlow can read a saved password, MediaFlow now tells you, and tells you exactly what to click.
- **Sorted the way you left it.** Pick a column to sort your clips or your projects by, and MediaFlow keeps it that way, next project and next launch.
- **One recording, one row.** When your GoPro splits a long take into several files, MediaFlow now shows it as a single row with the number of chapters and the total length. Click the arrow to see each piece. However you sort the list, the take stays together.
- **A welcome that knows when to leave.** The welcome tour opens once, not every time. A checkbox on it, and in Settings, brings it back whenever you want it.
- **Opens ready to work.** The main window now opens at a comfortable size, and MediaFlowSwift remembers where you left it, along with the rest of your view choices.

## 1.10.8 · September 20, 2026

**Your workspace, the way you want it.**

- **Resize the preview your way.** Drag the divider between the preview and the panel beside it to make either as wide as you like. The panel’s tabs now slide sideways when space is tight, and MediaFlow remembers the tab you were on.
- **GoPro clips in the right order.** Sort by filename and the pieces of one long GoPro recording now stay side by side, in the order you shot them, instead of being scattered down the list.

## 1.10.7 · September 20, 2026

**One app, update after update.**

- **Permissions that stick.** macOS now recognises every MediaFlow update as the same trusted app, so what you have allowed it, like reaching your NAS, stays allowed from one version to the next. If you are on 1.10.6 or earlier, install this version by hand once.
- **Safer updates.** MediaFlow checks that each update is genuine and from the same maker before installing it, and keeps your previous version ready in case you want to go back.
- **A straight answer about the network.** If macOS is keeping MediaFlow off your local network, MediaFlow now says so, and tells you where to switch it on.

## 1.10.6 · September 20, 2026

**A steadier connection to your shared library.**

- **No more false alarms.** With your library on a database server, MediaFlow no longer tells you the NAS is offline when it is not. And when that banner does have something to say, it sits in its own strip at the top, clear of your project list.
- **Your server, found instantly.** Version 1.10.5 could lose track of a server named with ".local" a moment after finding it. It now finds it straight away, every time, and stays connected.

## 1.10.5 · September 20, 2026

**Connecting your shared library just got easier.**

- **Finds your server by name.** Type your NAS’s name the way you know it and MediaFlow finds it, even when the network wants ".local" on the end. If something is off, it tells you whether to look at the name or the port.
- **Changes take effect at once.** Point MediaFlow at a different database server and it connects there and then. No more quitting and reopening.

## 1.10.4 · September 20, 2026

**Share your library with every Mac in the studio.**

- **A shared library, easier to start.** Setting up a database server for several Macs is now one click away in Settings, whichever kind of library you use today. The guide tells you exactly what it will create, and what to do next.

## 1.10.3 · September 20, 2026

**Updates you can count on.**

- **Updates that install, first time.** Version 1.10.1 could find an update but not finish installing it: it safely put itself back and reopened instead. That is fixed. If you are on 1.10.1 or 1.10.2, install this version by hand once, and every update after it takes care of itself.
- **A tidy update banner.** The "update available" banner now has its own strip at the top of the window, so it never sits on top of your project list.

## 1.10.2 · September 20, 2026

**Open a project the way you expect to.**

- **Double-click to open.** In the projects list, double-click any project and you are in. Right-click anywhere on its row for more, and one clear Open Selected button stays at the top.

## 1.10.1 · September 19, 2026

**Updates that finish the job.**

- **Never miss a new version.** MediaFlow now tells you when an update is ready, with a quiet banner at the top of the window. It keeps looking until it can reach your update folder, so a drive that connects late no longer means a missed update.
- **Click Install, and carry on.** MediaFlow closes, updates itself and comes straight back, ready to work. No more hunting for the icon to open it again.
- **Safe if anything goes wrong.** If an update cannot be installed, MediaFlow puts back the version you had and reopens it.

*One note: this improvement arrives with 1.10.1 itself, so you will see it from the next update onward. Installing 1.10.1 from an older version may still need you to reopen MediaFlow by hand, one last time.*

## 1.10.0 · September 19, 2026

**From final cut to YouTube, without leaving MediaFlow.**

- **Prepare for YouTube.** Choose your finished video and MediaFlow listens to it, then writes a title, description, chapters and tags built to be found. It works only from what you actually said, and checks its own work against YouTube's rules before you see a word. Every line is yours to edit.
- **Thumbnails that stop the scroll.** Pick the perfect frame, or let MediaFlow suggest the sharpest ones. Add a bold headline that stays readable on any picture, and export at exactly the size YouTube asks for.
- **Upload from where you work.** Sign in with your own Google account, choose Private, Unlisted, Public or a scheduled time, and send. A dropped connection picks up where it left off, even if you quit and come back tomorrow.
- **See how your videos are doing.** The new Results tab keeps a record of everything you publish. Turn on statistics and watch views, likes, comments, watch time and new subscribers grow over days, weeks and months.
- **Your privacy, your call.** Uploading and statistics are both off until you switch them on. MediaFlow tells you exactly what is sent and to whom, and never sees your Google password.

## 1.9.0 · September 18, 2026

**Find it faster. Trust it completely.**

- **Your footage, proven safe.** Before MediaFlow ever offers to delete an original, it now proves the copy is identical, file by file. That goes for archiving to a drive, moving a project, restoring, clearing a card and freeing up space.
- **Search your clips.** A search field for the clip list finds what you need by name, notes, tags and more. Press Command-F and type.
- **Find clips by what was said.** A new transcript panel lets you read, search, correct and export the words in any clip.
- **Remember the weather.** See the conditions a clip was shot in, and find your footage by them.
- **Stars and selects, everywhere.** Rate and mark your best clips in the table, the grid and the inspector.
- **Smoother playback.** When a lighter preview copy of a clip exists, MediaFlow plays it, and switches to the original with one click.
- **Privacy you control.** A new Privacy page in Settings lists every outside service MediaFlow can use. Each one is off until you turn it on.
- **Help where you need it.** Small ⓘ buttons beside the trickier controls explain them on the spot, and the full user guide is built from the same Help.
- **Plus:** workflow templates that wait for each step to finish, Select All and Shift-click in the grid, renaming a project renames its file, and a Storage Dashboard that opens at once.

## 1.8.0 · September 18, 2026

**Room to grow.**

- **A shared library for a whole team.** MediaFlow can now keep its library on a database server as well as in a single file, so several Macs can work from the same library with confidence.
- **Move between them in a few clicks.** Copy your whole library from one to the other, in either direction. Nothing is left behind.
- **Guided setup.** The setup assistant offers both choices and walks you through creating the server, step by step.

## 1.7.0 · September 17, 2026

**Up and running in minutes.**

- **A friendly first-run setup.** Three simple questions and you are ready: where your footage lives, whether you want a shared library, and where organized media should go. Skip any of them and come back later.
- **Settings that stay put.** Your setup now survives updates and reinstalls, and can be carried to a second Mac.

## 1.6.0 · September 11, 2026

**Make it yours.**

- **Works with your storage.** Nothing about your network is assumed. Let MediaFlow find your network drive, pick it, and go. It also works beautifully with no network drive at all.
- **Tidier Settings.** Everything is grouped into clear tabs, so the option you want is where you expect it.
- **Retire a category without losing history.** Old categories step aside quietly, and the clips that used them keep their labels.
- **Choose where updates come from.** Point MediaFlow at any folder and it will look there for new versions.

## 1.5.1 · September 11, 2026

**Polish.** Steadier syncing of your library in the background, and a round of small fixes.

## 1.5.0 · September 10, 2026

**A smarter import.**

- **Let MediaFlow suggest the category.** Tick one box when you import and MediaFlow looks at each clip and proposes where it belongs. It learns from every correction you make, and nothing is applied until you say so.
