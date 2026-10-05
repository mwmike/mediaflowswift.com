---
layout: manual
title: "Publishing — MediaFlowSwift Manual"
description: "Choose your finished video, transcribe it, and get a title, description, chapters and tags to paste into YouTube Studio, where you upload the video."
permalink: /manual/publishing/
generated: tools/import-guide.sh
---
# Publishing

## Preparing a Video for YouTube

*Choose your finished video, transcribe it, and get a title, description, chapters and tags to paste into YouTube Studio, where you upload the video.*

Prepare for YouTube works on the finished video you exported from your editor, not on the project’s clips. MediaFlow reads the file, transcribes what is said in it, and an SEO agent writes the words that go with it. You edit them, then put them into YouTube Studio: the Into YouTube Studio strip above the tabs has Copy Title, Copy Description and Copy Tags, and Open YouTube Studio…, which opens YouTube’s upload page in your browser. Upload the video there and paste the words in. That is how the video goes public.

1. Choose Workflow → Prepare for YouTube…
2. Click Choose Video… and pick the exported video. MediaFlow shows its length and format. The file is only read; it is never changed and never sent anywhere
3. Click Transcribe. A long video takes a few minutes. The line under the button says whether the audio stays on this Mac
4. Fill in Your brief with what only you know: who the video is for, the tone you want, and anything the description must include, one item per line, such as links, credits or a call to action
5. Click Write with the SEO Agent. See The SEO Agent for what it does and what it sends. If a title, description or tags are already there, MediaFlow asks before replacing them
6. Edit anything you like. Click one of the other titles to use it instead. The checklist updates as you type
7. Click Open YouTube Studio… and upload the video there. Then click Copy Title, Copy Description and Copy Tags in turn, or the small Copy beside each field, and paste each into the upload page. The chapters are added to the end of the description when you copy it

Open YouTube Studio… only opens a page in your browser, when you click it; MediaFlow sends nothing. The Upload tab is a separate, advanced and optional path: until MediaFlowSwift can sign you in through its own verified Google project, a video sent from there is a private copy for review, not the public video. See Uploading to YouTube.

Your draft is saved in the project’s folder, in Publish/publish-draft.json, a moment after each change and when you close the window. It moves, archives and restores with the project. A project that has not been saved yet has no folder, and the window says the draft cannot be kept until it has one. Choosing a different video clears the transcript, the chapters and the thumbnail’s frame, because they belong to the video they came from.

> **Tip:** You can use the checklist without the agent. Type your own title, description and tags, set the main phrase, and it checks them the same way.

See also: [The SEO Agent](#the-seo-agent), [The Publishing Checklist](#the-publishing-checklist), [Making a Thumbnail](#making-a-thumbnail), [Uploading to YouTube](#uploading-to-youtube), [Speech Transcription](/manual/organizing-media/#speech-transcription), [Privacy: What Leaves This Mac](/manual/setup-network/#privacy-what-leaves-this-mac)

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

See also: [Preparing a Video for YouTube](#preparing-a-video-for-youtube), [The Publishing Checklist](#the-publishing-checklist), [Privacy: What Leaves This Mac](/manual/setup-network/#privacy-what-leaves-this-mac), [Using a Model to Suggest Categories](/manual/organizing-media/#using-a-model-to-suggest-categories)

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

*Advanced and optional: send a private copy of the finished video to your channel for review from the Upload tab. The public video is uploaded in YouTube Studio, with the words MediaFlow prepared.*

### A Private Copy for Review

The Upload tab is the advanced, optional path, and what it sends is a private copy for review. Uploading goes through a Google Cloud project of your own, and Google restricts every video uploaded through a project made since July 2020 that has not passed its audit to private viewing, whatever visibility or publish time you choose. A project you made for yourself has not passed it. The lock cannot be lifted in YouTube Studio, and there is nothing to appeal. Only an audited project avoids it, for the uploads that come after, and a video already locked stays locked: Google’s own advice is to upload it again. Until MediaFlowSwift can sign you in through its own verified Google project, treat an upload from here as a private copy for review, which you can see in YouTube Studio.

The public video is uploaded in YouTube Studio. Click Open YouTube Studio… in the Into YouTube Studio strip above the tabs of Prepare for YouTube, upload the file there, and paste in the title, description and tags that Copy puts on the clipboard. See Preparing a Video for YouTube.

### Sending the Private Copy

Uploading is off until you turn it on. Turn on Uploading to YouTube in Settings › Privacy, add a Google client of your own (see Setting Up Your Google Client), and sign in. Nothing is sent until you click Upload and confirm.

1. Choose Workflow → Prepare for YouTube… and click the Upload tab
2. Click Sign In to YouTube…. Your browser opens at Google; sign in there and pick the channel. MediaFlow never sees your password. It asks for the narrowest permission that can upload, which Google words as “Manage your YouTube videos”. It cannot read your channel or delete videos. It could also replace a thumbnail, watermark or banner; MediaFlow uses it only to send the video and its thumbnail
3. Choose the visibility: Private, Unlisted or Public. Or turn on Publish at a set time: the video goes up Private and YouTube makes it public at that time, which must be at least 15 minutes away. From a project that has not passed Google’s audit, neither takes effect: the video stays Private, as above
4. Answer Made for kids. YouTube requires the answer by law, and MediaFlow does not give it for you: the upload cannot start until you choose
5. Choose the category. Turn on Send the thumbnail from the Thumbnail tab if you made one; left off, YouTube picks a frame itself
6. Deal with anything listed in red. An upload does not start while the checklist on the Words tab has something that must be fixed
7. Click Upload to YouTube…. MediaFlow shows what is going, how large it is and the visibility you asked for. Click Upload to send it

### If Your Uploads Come Out Private

Google keeps every upload Private from any Google Cloud project made since July 2020 that has not passed its audit, whatever visibility is asked for. A project you have just made has not. The video is safely on your channel, and YouTube Studio cannot change that. Use it as the private copy it is: for review, for a last look at the words and the thumbnail. For the public video, upload the file in YouTube Studio with the words MediaFlow prepared. Google’s audit form is linked from the YouTube Data API page of your project; it is Google’s review of an app and how it uses YouTube, Google gives no time for it, and it does not unlock a video already uploaded.

### If Google’s Sign-In Service Is Busy

An upload renews your sign-in with Google as it goes, about once an hour on a long one. If Google’s sign-in service is busy just then, MediaFlow waits and asks again, for a minute or so, and the upload carries on. If it is still busy after that, the upload stops and says so: what was sent is kept, and Continue the Upload… carries on from there. Reading statistics asks only once.

### A Dropped Connection, or Stopping

The video is sent in pieces. If the connection drops, or YouTube is busy, MediaFlow waits, asks YouTube how much arrived, and carries on from there. It waits longer after each failure and gives up after ten in a row, a little over a quarter of an hour; being off the network altogether is simply waited out. If you click Stop or quit, what was sent is kept: the button reads Continue the Upload… next time, for about a week, unless you sign out. The upload starts again from the beginning if the video file has changed, or if you have changed the title, description, tags or settings, because an unfinished upload carries the words it was started with; MediaFlow tells you so before it begins. Only YouTube letting the upload lapse, a changed video or changed details, or your own Start Again… after an upload another account began, start it again: an expired or refused sign-in, signing in again, a full allowance or a dropped connection never do. A publish time is fixed when the upload starts, so for a large video on a slow connection choose a time well ahead.

### The Thumbnail

The thumbnail is sent after the video. YouTube accepts custom thumbnails only from a channel verified by phone (youtube.com/verify). If it is refused, the video is still up: MediaFlow says so, and Send the Thumbnail to This Video tries again without uploading the video again. You can also export the thumbnail and add it in YouTube Studio.

### If Your Sign-In Expires or Is Not Accepted

If your sign-in expires, or you remove MediaFlow’s permission at Google, MediaFlow says the sign-in has expired and offers Sign In Again… beside the message, which takes you straight to Google. If YouTube does not accept a sign-in, MediaFlow says so and offers the same. That usually means the Google account chosen has no YouTube channel, or is not the one that manages the channel you upload to: it is easy to pick the wrong one when Google asks you to choose an account. Click Sign In Again… and choose the account and channel you upload to; if you have no channel yet, create one at youtube.com first.

Either way MediaFlow lets that sign-in go, and the video’s details and any upload already under way are kept: after signing in, click Continue the Upload… and it carries on from where it stopped. There is no need to sign out, which would forget the unfinished upload. MediaFlow renews a sign-in YouTube did not accept only once, and never tries it again on its own: if YouTube still does not accept it after you have signed in again, MediaFlow says so again.

### Signing In Again Without Signing Out

While you are signed in, the Upload tab shows Sign In Again… beside Sign Out. It opens Google in your browser, as signing in does, and asks for what the switches in Settings › Privacy allow now. Use it to add the statistics permissions, to add the permission to upload after signing in for statistics only, or to choose another account. Unfinished uploads are kept, and Continue the Upload… carries on afterwards. Wherever MediaFlow says a sign-in lacks a permission, or that another account is needed, it offers the same button beside the message. It asks only for what the switches allow now: with Uploading off, the new sign-in will not upload, and when you turn Uploading on, MediaFlow asks you to sign in again for it.

If you untick the permission to upload at Google, tick only one of the two read-only permissions, or the sign-in does not finish, the sign-in you had is kept as it was and nothing new is kept. Unticking both read-only permissions is allowed: the new sign-in then uploads, without statistics. Signing in again does not cancel the permission you gave before, because Google cancels everything one account gave MediaFlow together, the new sign-in included; Sign Out later cancels it all. If you chose another account, you can remove MediaFlow from the first one at myaccount.google.com/permissions. The same goes for another account whose Sign In Again could not be used: MediaFlow does not hand that one back while your earlier sign-in is kept, so it may still list MediaFlow there.

### An Upload Begun with Another Account

An unfinished upload belongs to the Google account that began it. If you have signed in again since, with another account, YouTube may not let the new sign-in carry it on. MediaFlow then says so and stops that upload only: your sign-in is kept, and so is what was sent. Click Sign In Again… and choose the account that began it to carry on where it stopped, or click Start Again… to send the video from the beginning with the account you are signed in to now; the unfinished upload is let go once the new one is under way. If you already chose the account that began it and YouTube still will not carry it on, click Start Again: if YouTube does not accept that account at all, MediaFlow then says so. If YouTube does carry it on, the video goes to the channel it was begun on.

### What Is Kept

- Your sign-in is kept in the Keychain, never in a file. Sign Out forgets it, forgets any unfinished upload, and asks Google to cancel the permission. To add a permission or choose another account, use Sign In Again… instead, which keeps them. When an unfinished upload from about the last week is kept, in this project or another, Sign Out asks first and says how many would have to start again from the beginning; Cancel keeps them. Older ones are not counted: YouTube lets an unfinished upload go after about a week. If both YouTube switches are off in Settings › Privacy, Google is not contacted: MediaFlow says so, and you can remove it yourself at myaccount.google.com/permissions
- Removing the client secret in Settings stops any upload, signs you out the same way, and then forgets the secret. When an unfinished upload from about the last week is kept, it asks first in the same way
- Publish/upload-state.json in the project’s folder records which file went up, when, the video’s ID, and the words and settings it went up with, and, while an upload is unfinished, a random name for the sign-in that began it, which says nothing about your account. The address of an unfinished upload is kept in the Keychain, not in that file
- Uploading a video that has already gone up asks first, because it makes a second copy on your channel

### What the Database Records

When an upload finishes, MediaFlow adds the video to the shared database, if you use one. It is kept there, in the published_videos table, as the record of what you have published across all your projects. Nothing about it is sent anywhere else.

- The project, the video’s YouTube ID, its title and main phrase
- The file’s name and size, the video’s length and format
- When the upload started and finished, and how long it took from start to finish, stops included. If the app was closed as the last piece arrived, the finish is the moment MediaFlow next asked YouTube, and how long it took is left empty
- The visibility you asked for (recorded as scheduled when you set a publish time), that time, your made-for-kids answer and the category
- When it was to go live, as arranged: the end of the upload for a Public video, the set time for a scheduled one, or the end of the upload if that came later. It is left empty for Private and Unlisted videos. Whether it did go live, only YouTube can say, and the Results tab says live only once YouTube has: see How Your Videos Are Doing
- Whether the thumbnail was sent, and its words
- The length of the title and description, the tags and how many, the number of chapters, the number of words in the transcript, and which model wrote the words

These are the words and settings the video went up with, even if you edit the draft afterwards. If the database was not connected when the upload finished, the video is added the next time you open Prepare for YouTube for that project, or upload from it; a later upload does not push it aside. The visibility is what you asked for: MediaFlow’s permission cannot read your channel, so if Google kept a Public video Private, as it does from a project that has not passed its audit, or you changed a video’s visibility in YouTube Studio where that is allowed, the database does not know. Turning on statistics changes that: see How Your Videos Are Doing.

> **Tip:** An upload uses most of a new Google Cloud project’s daily allowance of 10,000 units: 1,600 for the video and 50 for the thumbnail. That is about six videos a day. The allowance resets at midnight Pacific time.

Uploading, and reading results, are part of Studio Pro; see Plans and Pricing. The plan puts no monthly limit on them: they run on your own Google Cloud project, whose daily allowance is the only limit.

See also: [Setting Up Your Google Client](#setting-up-your-google-client), [How Your Videos Are Doing](#how-your-videos-are-doing), [Preparing a Video for YouTube](#preparing-a-video-for-youtube), [The Publishing Checklist](#the-publishing-checklist), [Making a Thumbnail](#making-a-thumbnail), [Privacy: What Leaves This Mac](/manual/setup-network/#privacy-what-leaves-this-mac)

## Setting Up Your Google Client

*The Upload tab, which is advanced and optional, uploads through a Google Cloud project of your own. Making one takes about ten minutes and is free; what it uploads is a private copy for review.*

This is only for the Upload tab, the advanced and optional path. To publish, you need none of it: upload the video in YouTube Studio and paste in the words MediaFlow prepared, as Preparing a Video for YouTube describes.

Google requires every app that uploads to YouTube to identify itself with a client. MediaFlow uses one that belongs to you, so your uploads count against your own allowance and nobody else stands between you and your channel. You do this once. Because the project is yours and has not passed Google’s audit, every video it uploads is kept Private by Google, and YouTube Studio cannot change that: an upload is a private copy for review. See Uploading to YouTube.

1. In your browser, open console.cloud.google.com and sign in with the Google account that owns your channel
2. Create a project. Any name will do
3. Under APIs & Services › Library, find YouTube Data API v3 and click Enable. If you will read statistics, enable YouTube Analytics API too
4. From the menu, open Google Auth platform › Branding and click Get Started. Give the app a name and your email address, choose External for the audience, give your email address for contact, agree to Google’s user data policy, and click Create
5. Under Google Auth platform › Clients, click Create Client, choose the application type Desktop app, give it any name, and click Create
6. Copy the client ID and the client secret Google shows you
7. Under Google Auth platform › Audience, click Publish app and confirm, so that the publishing status reads In production. For a project that only you sign in to, this needs no review from Google. Left in Testing, Google ends every sign-in after seven days. If you leave it in Testing, add your own account under Audience › Test users: otherwise Google refuses the sign-in, and MediaFlow says it was declined
8. In MediaFlow, open Settings › Analysis. Under YouTube, paste the client ID, paste the secret and click Save

The client ID is kept in MediaFlow’s settings. The secret is kept in the Keychain, never in a file, the saved setup or a log.

### What to Expect at Sign-In

- Google shows a warning that the app is not verified, because the project is yours and has not been through Google’s review. Click Advanced, then continue
- If the publishing status is still Testing, Google ends the sign-in after seven days. MediaFlow then says your YouTube sign-in has expired, and Sign In Again… takes you straight to Google. The video’s details, and any upload already under way, are kept: after signing in, click Upload or Continue the Upload again. Publishing the app (step 7) stops this. The same happens if you remove MediaFlow’s permission at Google
- Until the project passes Google’s audit, YouTube keeps every upload through it Private, whatever visibility or publish time is chosen, and YouTube Studio cannot change that. See Uploading to YouTube

> **Warning:** The type must be Desktop app. A Web application client is refused at sign-in, because it does not allow the answer to come back to this Mac.

See also: [Uploading to YouTube](#uploading-to-youtube), [Privacy: What Leaves This Mac](/manual/setup-network/#privacy-what-leaves-this-mac)

## How Your Videos Are Doing

*The Results tab lists what you have published and, if you allow it, reads each video’s views, watch time and more from YouTube and keeps them over time.*

The Results tab of Prepare for YouTube shows the videos MediaFlow uploaded, from this project or from all of them: when each went up, its size and length, the visibility you asked for and when it was to go live, as arranged. This comes from your shared database and needs nothing from YouTube, so it says live only once YouTube has confirmed it; until then it reads to go live, or was to go live, and from a Google Cloud project that has not passed its audit that time never comes. Without a database connected, the tab says so.

### Reading Statistics from YouTube

This is off until you turn it on, and it needs more permission than uploading does.

1. Turn on Reading your videos’ statistics from YouTube in Settings › Privacy
2. In your Google Cloud project, under APIs & Services › Library, enable YouTube Analytics API as well as YouTube Data API v3
3. On the Upload tab, click Sign In Again… if you are signed in, or Sign In to YouTube… if not. There is no need to sign out: unfinished uploads are kept, and Continue the Upload… carries on afterwards. Google now asks for two more permissions, both read-only: View your YouTube account, and View YouTube Analytics reports for your YouTube content. If you untick both at Google you can still upload, and the Results tab tells you statistics were not allowed, with Sign In Again… beside it. Ticking only one is no use, so MediaFlow keeps nothing new and asks you to sign in again. A sign-in you already had is kept as it was; otherwise the new one is handed back, because Google cannot take back one permission alone
4. On the Results tab, click Read from YouTube Now

MediaFlow asks Google which channel you signed in to, then sends the YouTube IDs of the videos your database records as uploaded by MediaFlow, and the span of dates from the first upload to today. Nothing else. The two permissions would allow reading your whole channel; MediaFlow asks only about those videos. If your database is shared with someone who publishes to another channel, answers about their videos are set aside, not kept as yours. Neither permission can change or delete anything.

You can turn on statistics without uploading: with only that switch on, sign-in asks for the two read-only permissions alone, and the Upload tab says the sign-in cannot upload. To upload later, turn on Uploading to YouTube and click Sign In Again….

### What Is Read and Kept

- Views, likes and comments, as YouTube shows them now
- Hours watched, the average view as a time and as a share of the video, subscribers gained and shares, from YouTube Analytics. These run a day or two behind the counters, so a new video shows a dash at first
- The visibility the video really has, and when it really went public. If you asked for Public and YouTube has it Private, the tab says so: Google holds uploads Private from a Google Cloud project that has not passed its audit, and YouTube Studio cannot change that. The public video is uploaded in YouTube Studio; see Uploading to YouTube

Each reading is kept in the published_video_stats table of your database, about one a day for each video (never within 20 hours of the last), so you can see a video at a day, a week and a month. The tab shows the latest numbers and the views gained since the reading before. Reading again sooner updates nothing but the visibility. Statistics are read only when you click the button; nothing is read in the background.

> **Tip:** MediaFlow does not read impressions or click-through rate; look for them in YouTube Studio. The YouTube Studio link beside each video opens it there.

See also: [Uploading to YouTube](#uploading-to-youtube), [Setting Up Your Google Client](#setting-up-your-google-client), [Privacy: What Leaves This Mac](/manual/setup-network/#privacy-what-leaves-this-mac)

<div class="chapter-nav" role="navigation" aria-label="Chapters">
<a rel="prev" href="/manual/reports/">&larr; Reports</a>
<a href="/manual/">All chapters</a>
<a rel="next" href="/manual/project-management/">Project Management &rarr;</a>
</div>
