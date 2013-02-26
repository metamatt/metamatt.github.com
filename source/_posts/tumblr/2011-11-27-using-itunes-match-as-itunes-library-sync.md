---
layout: post
title: Using iTunes Match as iTunes library sync
tags:
- apple
- iTunes
- sync
---
Apple recently added two new features to iTunes: "[iTunes in the
Cloud](http://www.apple.com/icloud/features/)", which adds all your iTunes
music purchases to a cloud library which can be streamed or downloaded as
often as you want to any of your devices (iPhone, iPod, iPad, computer with
iTunes), and "iTunes Match", which adds all the music you _didn't_ buy from
iTunes to that same cloud library, enabling all the same "iTunes in the Cloud"
features.

Apple is billing this primarily as a way to get your music from your iTunes
library onto your phone or iPad without having to plan ahead and pre-sync the
music onto the device.

However, in addition to using iCloud to sync music between devices, iTunes
Match also has another benefit: it syncs the library metadata between multiple
iTunes libraries that enable iTunes Match using the same account.

This subtle addition is actually something important that I've wanted from
iTunes as long as I've been using it: iTunes has a bunch of organization
features including smart playlists which work best if it knows what you listen
to and how much you like it. It tracks how many times you play each song and
allows you to rate songs, and it automatically syncs this between one iTunes
library and any connected iPods, but until now each iTunes library has been an
island: if you have two computers, say a desktop and a laptop, each has its
own library, with its own play counts and ratings and playlists, and its own
idea of your preferences, and any iPods or other Apple devices you have were
able to sync songs and metadata from a single one of these libraries.

Now, with iTunes Match enabled, all my computers with iTunes see the same
library — all of the songs on any one of them are synced up to iCloud and then
back to the other computers, and metadata including play counts, ratings and
playlists are also kept in sync. This joining of the libraries also means it
matters a lot less which of my computers I sync a given iPod with, since
effectively they all use the same library.

There's one minor remaining annoyance given the way I use iTunes at home: I
have a file server with all my music, a Mac Mini in the living room which can
play music and movies, and my main desktop computer, and each of these Macs
uses the network file server for the music files instead of storing a local
copy. (My laptop spends enough time disconnected from the home network that it
does deserve a local copy of the music.) This means that if I add music to the
library on one of the desktop computers, it's already accessible in the
expected location from any of the other computers that can access the file
server, though the other computers won't know it until I tell iTunes to add
the files to the local library. The storage is shared; the library metadata is
still per-computer. Using iTunes Match, the libraries are kept in sync
automatically, but iTunes doesn't notice that some of the files are magically
already local — it will show such files with the cloud icon, and offer to
stream them or download them even though that's unnecessary. Streaming works
fine, and downloading works, but actually downloads the file to the same
folder, notices that the file already exists, and adds a numeric suffix to
make the filename unique.

It would be nice if there was a way to tell iTunes to notice local copies of
files that it thinks are only in iCloud. Also, I occasionally found myself
having downloaded extra copies of songs, noticing this cluttering up the music
folder, and deleting the extra files outside of iTunes (using Finder) — this
left me in a broken state where iTunes has an entry for the song in the
library, and the file exists in the filesystem and in iCloud, but iTunes
thinks it's local so won't stream or download from iCloud and thinks it has a
different name so it won't play the local file, at which point things are
pretty broken. What's needed here is a way to stuff the file back into the
cloud, making iTunes think there is no local copy so it will go get it from
iCloud again the next time it's needed — I couldn't figure out how to do this
until I read this [Q&A article at Ars
Technica](http://arstechnica.com/apple/news/2011/11/more-itunes-match-answers-
dj-sets-how-to-replace-music-and-more.ars,) which has the secret: select the
song, hold the option key while pressing the delete key, and the normal delete
confirmation dialog will grow a new checkbox "also delete this song from
iCloud". Leaving that option unchecked, you can delete the local copy of the
song (or, a broken link to a missing local copy of a song) while leaving it in
the cloud library, the cloud icon comes back, and iTunes will go back to
getting the data from iCloud as needed again.

