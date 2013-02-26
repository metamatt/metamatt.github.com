---
layout: post
title: Tips for re-uploading photos from Lightroom to Flickr
tags:
- software
- iusethis
---
If you use both Flickr and Adobe Lightroom, and upload from Lightroom to
Flickr using [Jeffrey's "Export to Flickr" Lighroom
Plugin](http://regex.info/blog/lightroom-goodies/flickr), you might find that
sometimes images don't get uploaded, or get uploaded and forgotten.

I typically find this out, for example, when I edit keywords or other metadata
for a bunch of images, then use the File->Plug-in Extras->jf Flickr Extras
command to resync the metadata at Flickr for hundreds of images at once. Often
I'll be told "the metadata for 471 images was updated but 2 images were not
found at Flickr".

At this point, you need to know how to do 2 things:

- assuming the images were really uploaded, you want to reassociate the Lightroom copy with the Flickr copy  
- if that fails because the images were not really uploaded, you want to identify them and actually upload them to Flickr

The first one is easy; also in the jf Flickr Extras dialog, there's a command
"associate images". Try this. If you're lucky, it'll just work. If it fails,
you need an easy way to tell which images it failed for; that's where this tip
comes in:

Switch to grid view if you're not already there. Select all of the images in
the batch you're working with. Make sure the filter bar is shown (this can be
toggled in the View menu: "Show Filter Bar"), then filter by text, and filter
on: Text | Any Searchable Plug-in Field | Doesn't Contain | "flickr". This
works because the jf Flickr plugin adds a field with Flickr in the name to any
image it uploads.

