---
layout: post
title: Updated version of Palm-Evernote importer
tags:
- evernote
- software
- my software
comments: true
---
I've updated my [utility for importing notes from Palm Desktop into Evernote](http://www.maddogsw.com/evernote-utilities/evernote-palm-importer/) to take advantage of feedback and fix the most-reported bugs:

* There's now an option to specify character encoding, and a reasonable default if you don't know
* Dates (which only exist notes exported from the Mac OS version of Palm Desktop) can be recognized in languages other than English now. (I've only tested French, since that's the only language people complained about, but if it doesn't work for others, I'm sure somebody will let me know and supply sample data.)
* If the importer chokes while processing a note (less likely with the above two fixes, but still possible) it continues with the rest of the notes instead of immediately giving up entirely.

Download here: [http://www.maddogsw.com/evernote-utilities/evernote-palm-importer/](http://www.maddogsw.com/evernote-utilities/evernote-palm-importer/)
