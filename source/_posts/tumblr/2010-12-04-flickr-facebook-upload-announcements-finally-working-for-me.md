---
layout: post
title: Flickr->Facebook upload announcements, finally working for me
tags:
- software
comments: true
---
I mostly share my photos on Flickr, but want the uploads announced on Facebook
so that my friends know about them. Flickr has long offered a way to do this;
it hasn't always worked great for me. (It worked up until a few months ago
when Yahoo redid their notification system to use Yahoo Pulse; after that it
stopped working; I disabled the feature and re-enabled it and it started
working again, then stopped working again, and I didn't have time to figure
out why.)

Lately since it hasn't been working at all for me but has for my friends, I
decided to get to the bottom of it, and started with Flickr's help system. I
found it somewhat noteworthy that of the help topics linked [directly from the
top of their help system](http://www.flickr.com/help/), which asks "What are
you having trouble with", "Facebook updates" is the 2nd thing in the list.
Good, so I'm not the only one.

Anyway, this link rapidly takes you to [a list of troubleshooting
steps](http://www.flickr.com/help/with/facebook); kidding aside, this is
really useful. It basically says to make sure your images are public, safe and
searchable, shows you how to verify this for your existing images and change
it for future uploads, and says if this doesn't work, unlink and relink your
Yahoo and Facebook accounts (which was the big hammer I already tried twice,
once with and once without success.)

Looking at my own recently uploaded images, they were marked safe and public
but not searchable. Huh? Flickr's settings confirmed that I haven't disabled
this globally; hmm; it must be something to do with the way I'm uploading the
images, using [Jeffrey's "Export to Flickr" Lightroom
Plugin](http://regex.info/blog/lightroom-goodies/flickr). First I check the
settings I'm using and they look fine; then I check Jeffrey's release notes
and sure enough, there was a bug with image visibility, fixed newer than the
version of the plugin I'm using.

Hopefully, once I update the plugin to the version that fixes this bug, it
actually works end to end for me now.

