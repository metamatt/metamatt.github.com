---
layout: post
title: Tumblr editor bug leaves CSS metadata in my data
tags:
- tumblr
- bug
- software
comments: true
---
Tumblr's editor turned t[his post](http://blog.metamatt.com/blog/2011/04/11/this-is-why-you-need-a-groklaw/) into [![](http://farm6.static.flickr.com/5263/5621005740_174256464b.jpg)](http://www.flickr.com/photos/metamatt/5621005740/in/photostream/)

between the time I pressed "Create Post" (at which time there was no CSS gunk
visible) and the time it was actually published (where some CSS crept into the
post body itself).

(This happened both on Tumblr itself and in the wall post that the Tumblrbot
made on Facebook -- I immediately went and fixed the damage in the original
post, but the Facebook publish feature is basically instant and doesn't allow
after the fact edits, so the CSS gunk is forever baked into that post and
that's why the screenshot shows Facebook and not Tumblr. Also, Tumblr
apparently bakes the RSS feed with enough delay that my subsequent edit to fix
the post made it into the RSS version, unlike the Facebook version.)

This problem isn't incredibly common, but common enough to be annoying --
maybe something like 5% of the time.
