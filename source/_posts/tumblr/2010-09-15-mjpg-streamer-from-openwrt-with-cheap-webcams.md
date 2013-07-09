---
layout: post
title: mjpg-streamer from OpenWRT with cheap webcams
tags:
- gadgets
- software
- openwrt
- linux
comments: true
---
One thing OpenWRT can do (if you run it on a router with USB ports) is stream
video from a webcam using mjpg-streamer. Pretty useful if you want to put a
webcam in some random place.

(The current version of OpenWRT, backfire, needs additional nondefault
packages involved: see [http://blog.bashroom.com/2010/05/04/webcam-streaming-with-openwrt-backfire/](http://blog.bashroom.com/2010/05/04/webcam-streaming-with-openwrt-backfire/).)

I tried this with an old webcam I had lying around, but the old webcam
predated the UVC (USB Video Class) standard, and I couldn't get it to work. So
then I bought a couple of the cheapest webcams on Amazon that claimed UVC
support.

Not too surprisingly, neither one worked right away -- when I start mjpg-
streamer as described in the abovelinked article, it would say "Unable to set
format: invalid argument". This turns out to be because these cheaper cameras
don't support MJPG in hardware, only YUV output; mjpg-streamer can convert but
you have to pass -y to it.

So for OpenWRT, I edited /etc/init.d/mjpg-streamer to add -y to the --input
argument.

The resulting stream is choppy, and gets backed up several frames, but is good
enough for my purposes. It also spikes the router CPU to 100%, even on a newer
faster router I have, so I told mjpg-streamer to stream at 1 fps, which is not
that much choppier and still good enough for my purposes (edit /etc/config
/mjpg-streamer to do this).

Moral of the story: it's probably better to buy a webcam known to support MJPG
in hardware.

(Thanks to [https://forum.openwrt.org/viewtopic.php?pid=98294](https://forum.openwrt.org/viewtopic.php?pid=98294)and [http://arthurhong-linux.blogspot.com/2008/11/mjpgstreamer-or-uvcstreamer-always.html](http://arthurhong-linux.blogspot.com/2008/11/mjpgstreamer-or-uvcstreamer-always.html) for helping me figure out the YUV format problem and solution.)
