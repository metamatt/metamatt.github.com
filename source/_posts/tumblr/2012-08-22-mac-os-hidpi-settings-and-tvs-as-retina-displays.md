---
layout: post
title: Mac OS "HiDPI" settings and TVs as "Retina" displays
tags:
- apple
- mac os
- gadgets
comments: true
---
Apple has been dabbling with [resolution independence](http://en.wikipedia.org/wiki/Resolution_independence)
in Mac OS since 2005; in 2011 they shipped double-resolution "Retina" displays in iPhone
and iPad, and in that year's Mac OS release (10.7 "Lion"), renamed the
tentative resolution-independence support "HiDPI" and capped it to a 2x
scaling factor, hinting strongly at the future release of Retina Macs. In
2012, they released the Retina MacBook Pro and soon thereafter, Mac OS 10.8
"Mountain Lion", bringing the HiDPI modes out from behind the developer tools
and debug flags.

My question was whether Apple would ever make Mac OS usable for media-watching
purposes, connected to an HDTV, aka an
[HTPC](http://en.wikipedia.org/wiki/Home_theater_PC). Connected to our living
room 1080P LCD TV, we have an Apple TV, an Xbox 360, and a Mac Mini; the Mac
is there as an HTPC basically to handle whatever the dedicated media devices
can't; the list of things the ATV and Xbox can't handle has been shrinking
over time, but still. The pain point in this arrangement has been that if I
set the Mac Mini to full 1080P output, text onscreen is too small to read. If
I set it to 720P, text is borderline readable but still on the small side, and
images are scaled by 1.5X in the TV, so there's some loss of picture quality
once we get into a movie.

This scenario seems a pretty good match for the HiDPI modes — specifically
960x540 HiDPI, meaning text and UI elements are rendered for a virtual 960x540
resolution but the display itself is running at its native 1080P (1920x1080,
exactly double the virtual resolution in each direction) and images get to
address every pixel. (It seems faintly ridiculous to me that Mac OS had to
wait until 2012 to offer any kind of control over the size of UI elements, and
that after waiting until 2012 it arrives in such limited form; Microsoft
Windows has offered control over UI element text size since forever; in
practice apps with custom skins would often misrender some controls if you
used custom text sizes, and I suppose Apple was trying to limit exposure to
that problem by exposing such a little and late form of resolution
independence. Did it work? Read on….)

Note that by Apple's definition, a 32" 1080P display from a distance of 8
feet, across our living room, very much qualifies as a "Retina" display. You
can't see individual pixels, and both text and images ought to look pretty
darn great.

In my experience with the "960x640 (HiDPI)" mode in both Mac OS 10.7 and 10.8,
by forcing the 2X scaling factor and automatically pixel-doubling unaware
apps, Apple has successfully avoided the problem with both Windows' themed UI
font sizes and Mac OS 10.4-10.6 scaling factors where some UI elements would
be clipped to the wrong size. On the other hand, by giving me 960x540 as the
only resolution that both addresses every physical pixel and has readably
larger text, they've introduced a new problem: nobody cares about making apps
actually fit on screen sizes this small. (Typically, the archaic and once-
grand XGA, 1024x768, resolution is taken as the smallest possible, and indeed
Mac OS warns you if you select a resolution smaller than that in either
direction that apps may not fit.)

The problem starts with Apple's own apps; here's Software Update (from 10.7)
on the 960x540 screen. (A couple notes here. First, the sad thing is this app
is not design-intensive and does not require any special UI elements; the
window itself and the individual panes are resizable; there's no reason it
couldn't run perfectly well at 960x540. Second, in 10.8 this app has been
replaced with the Mac App Store app, which does a better, but still not good,
job of fitting at 960x540.)

[![Screen Shot 2012-04-05 at 6.58.22 PM](http://farm9.staticflickr.com/8426/7839608446_2a59f28012.jpg)](http://www.flickr.com/photos/67861147@N00/7839608446)

Note that the initial window size (above) doesn't even try to use all the
available screen height; note also that enlarging it (below) helps not at all
with the real problem.

[![Screen Shot 2012-04-05 at 6.58.45 PM](http://farm8.staticflickr.com/7258/7839608226_95d17378a9.jpg)](http://www.flickr.com/photos/67861147@N00/7839608226)

Hoping that 10.8 (the first OS X release conceived and shipped for Retina
Macs) might fix this oversight, I upgraded the OS on this machine. The initial
results are not pretty. The first thing you see when launching the Mountain
Lion installer:

[![Screen Shot 2012-08-20 at 12.58.33 PM](http://farm8.staticflickr.com/7267/7839606716_ea7f39b90d.jpg)](http://www.flickr.com/photos/67861147@N00/7839606716)

Such crisply rendered text! (Click through for a high-res version.) Nice large
cougar image! Such beautiful use of whitespace! But… where's that promised
Continue button?

(I cheated, changed display resolution to reveal the Continue button, pressed
it, then changed resolution back to 960x540 for the next screenshot.) Again,
the same problem.

[![Screen Shot 2012-08-20 at 1.04.53 PM](http://farm9.staticflickr.com/8294/7839607938_e66ef0823c.jpg)](http://www.flickr.com/photos/67861147@N00/7839607938)

OK, you say, but those images are still from OS X 10.7. It's an app designed
for and as part of 10.8, to be sure, but maybe 10.8 itself will be better?
Reboot into the new OS install, and:

[![Screen Shot 2012-08-21 at 9.48.12 PM](http://farm8.staticflickr.com/7117/7839606564_852af9b7d8.jpg)](http://www.flickr.com/photos/67861147@N00/7839606564)

Rats. Foiled again. At least the clickable buttons are onscreen, but the
screen was obviously cropped, and not intentionally.

[![Screen Shot 2012-08-21 at 9.48.40 PM](http://farm8.staticflickr.com/7265/7839606366_167da70f92.jpg)](http://www.flickr.com/photos/67861147@N00/7839606366)

No, Apple, thank _you_. (And a special extra thanks for not starting the
screen sharing daemon until after I click these two right arrows from the
local display, preventing people from upgrading their Mac OS installs
remotely. You can do the rest over screen sharing / remote desktop, but you
need a local display and mouse to get past these two screens.)

The real problem here isn't that TV-as-Retina-display-with-HiDPI couldn't
work, it's that apparently nobody cares. Nobody cares about screens smaller
than 1024x768 because nobody's shipping those any more; nobody cares about
making 960x540 work as a special case for TV use, because you're just supposed
to buy an Apple TV instead of hooking a Mac up to your TV, I guess.

So close, but yet so far.
