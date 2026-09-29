---
layout: manual
title: "Publishing — MediaFlowSwift Manual"
description: "Choose your finished video, transcribe it, and get a title, description, chapters and tags to paste into YouTube."
permalink: /manual/publishing/
generated: tools/import-guide.sh
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

See also: [Setting Up Your Google Client](#setting-up-your-google-client), [How Your Videos Are Doing](#how-your-videos-are-doing), [Preparing a Video for YouTube](#preparing-a-video-for-youtube), [The Publishing Checklist](#the-publishing-checklist), [Making a Thumbnail](#making-a-thumbnail), [Privacy: What Leaves This Mac](/manual/setup-network/#privacy-what-leaves-this-mac)

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

See also: [Uploading to YouTube](#uploading-to-youtube), [Privacy: What Leaves This Mac](/manual/setup-network/#privacy-what-leaves-this-mac)

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

See also: [Uploading to YouTube](#uploading-to-youtube), [Setting Up Your Google Client](#setting-up-your-google-client), [Privacy: What Leaves This Mac](/manual/setup-network/#privacy-what-leaves-this-mac)

<div class="chapter-nav" role="navigation" aria-label="Chapters">
<a rel="prev" href="/manual/reports/">&larr; Reports</a>
<a href="/manual/">All chapters</a>
<a rel="next" href="/manual/project-management/">Project Management &rarr;</a>
</div>
