---
layout: post
title: Not the modem after all
tags:
- network,
- cable
- last-mile
- openwrt
comments: true
---
My outbound Internet connection stopped working again this morning, and (like
the last couple times) evidence pointed towards my router, not the modem or
anything provided by Comcast.

(As I said [last time](http://blog.metamatt.com/blog/2011/06/13/update-on-
comcast-last-mile-isp-connection/), I'm convinced there were originally
multiple problems leading to confusion and increasing troubleshooting
difficulty, but it appears I owe Comcast at least a partial apology.)

The good news is there's a software fix, which can be invoked remotely
(unfortunately not from outside the house since outbound connectivity is down,
but it does mean I don't have to walk over to the equipment closet to power
cycle modems or routers): "mii-tool -r -R eth1" made everything happy again.

The router in question is a [Netgear
WNDR3700](http://www.netgear.com/home/products/wirelessrouters/high-
performance/WNDR3700.aspx) running [OpenWrt 10.03
"backfire"](http://backfire.openwrt.org/10.03/README). I wonder whether this
happens to others and whether it's a hardware or software bug. I'm hoping a
newer version of OpenWrt might fix it (but since release candidates of 10.03.1
have been appearing for 15 months now, I'm giving up hope for a new official
release; newer version probably just means trunk); alternately, it won't be
too hard to whip up a monitoring script that tries to ping the modem and does
the mii-tool reset whenever it doesn't see a response.

