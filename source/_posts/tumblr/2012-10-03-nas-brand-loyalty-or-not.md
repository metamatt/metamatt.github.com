---
layout: post
title: NAS brand loyalty (or not)
tags:
- gadgets
---
2006: The first RAID/storage appliance I bought was the original Infrant
ReadyNAS NV. It was medium-expensive for its time, well-built, and at first I
liked it a lot. However a few missteps by Infrant (one about spending years
stonewalling user requests for ssh access while sitting on a MAC-address-based
backdoor password, one about essentially a product recall of the fan which if
you read between the lines just meant they'd installed it backwards and
customers who want proper cooling should flip it around but it will get
louder), one power supply failure, and some mediocre experiences with their
generally well regarded tech support around buggy CIFS and AFP coexistence,
then the fact that Infrant sold itself to Netgear (the conventional wisdom on
which had it that there goes their tech support, although I didn't notice any
difference, and their jedi council is still at it today), combined with
extremely middling performance, meant when I needed more space, I went
elsewhere. (As you'll see, in hindsight this feels misguided; 6 years later
and the little ReadyNAS NV is still humming along fine, Infrant continues to
support it with software updates, and it's been far less frustrating and more
useful than my next couple purchases.)

2008: Elsewhere meant Promise; I bought an NS4300N. It offered a fairly
similar feature set to the ReadyNAS, but was half the price and slightly
faster. It was also of notably lower build quality, a lot more rickety and a
lot louder. Over time the firmware situation got sketchier; the product
stopped evolving; I moved it to a friend's house to use as offsite backup,
then slowly stopped using it; now it's gathering dust.

2010: Soured on the consumer-priced NAS market mostly due to poor performance
(Infrant and Promise had both claimed speeds of around 30MB/second but that
seems to involve way too many arcane dances and incantations involving jumbo
frames and disabling journaling and other bad ideas, even for me; configured
sanely, I see a reliable 10MB/second from the ReadyNAS, which is overkill for
music storage and backup and frustrating for anything else, so guess what? I
use it for music storage and backup), and still dreaming of fast centralized
storage for photos and videos and home directories and data I care about, I
tried a DAS solution next. The Promise DS4600, cabled via Firewire 800 to a
Mac Mini which is on all the time anyways. (The decision calculus that lead to
my original NAS purchase in 2006 involved servers that drew 100+ watts and
marketing claims that the consumer NAS units performed fine and had reasonable
AFP implementations; here in 2010 I was betting that I'd get better
performance and correctness from the real Apple AFP server on a real (Intel
Core 2 Duo) CPU and now that only draws 10 watts.) In retrospect, this was the
worst of the bunch. On a good day it reads and writes at 50MB/sec, but on the
much more common bad day it reads and writes at less than 1 MB/sec; as
originally shipped it would somehow cause the host computer to slow to a crawl
and need rebooting every few days, spending all its time in unbillable kernel
space (how a Firewire device accomplishes this, I have no idea); a firmware
update eventually fixed that, but to this day years later, performance is
unpredictable and generally slow, especially for small random writes, and if I
reboot the host computer, the DS4600 array won't be visible until several
minutes after boot. Also twice the array thought there was no volume
configured (and it came back up reboot, but that's still pretty scary, and
meant I had to stop using this for anything important).

Oh, and the configuration app for Mac OS that ships with the DS4600 creates
1024 threads (for what unholy purpose, I have no idea) and causes 16 identical
copies of the mouse cursor to appear onscreen, offset vertically by 64 pixels.
Keep in mind that while I didn't buy this from Apple, this is a product that
Apple actually stocked and sold specifically for use with Macs, so I shouldn't
have been that far off the beaten path here. (This is tied with another
Promise software disaster inflicted on me a few years ago for reasons not to
keep buying their products. Their hardware seems to perform well for a low
price, but riddled with software/firmware bugs as it is, no more for me. The
other case I speak of: I bought a low-end 2-port SATA RAID controller for a
Windows PC in 2006. All configuration for this PCI card was carried out by a
Java app with an in-browser interface, meaning you need a Java VM and a web
browser to twiddle a few hardware registers on a PCI card. Also, the installer
failed to create any front door to invoke the web browser, so I had to run
tcpview to figure out what port it was listening on to invoke it. All this for
something I only had to use once, for one-shot configuration. The RAID
controller worked fine for years, but what a horrible out-of-box experience.
The resulting web UI for the PCI card and the standalone NS4300 RAID appliance
was almost identical, I can almost cross my eyes far enough to envision a
world where it made sense to do write-once-limp-anywhere for the configuration
UI, but not quite, and in no case does that excuse making me run tcpview to
figure out where to point the browser. Though to bring this full circle, this
division of labor between the embedded software development and real-OS
software development, or lack thereof, probably explains the 1024 threads the
"SmartNAVI" app creates, somehow.)

2012: Thoroughly frustrated with the DS4600 and its foibles, lack of
reliability, and unpredictable speed. And we're shooting lots of video of
Dominic, so I need somewhere big and fast to store video files. DAS no longer
sounds like a good idea, largely because how am I going to connect it? My
current home server, the Mac Mini, has only USB2 and Firewire 800 and those
are no longer considered fast. Apple continues to willfully ignore eSATA;
their anointed storage bus is Thunderbolt which is (still) a tiny expensive
low-volume ecosystem which tends to point back to Promise, and which is not
available on any of my current machines anyway; USB3 is starting to creep into
their machines but as of October 2012 is still inexplicably only available on
portables; there's just no DAS array that I could plausibly connect to my
current server and a future server and expect good performance. Now you're
probably wondering why I'm talking about Apple hardware anyway; clearly they
have no desire to let us do external storage anywhere near the price-
performance of the PC world; I should just build my own box and run Linux or
Nexenta and soak in the ZFS goodness and… no thanks. I'm crazy enough to
[build my own networking hardware](http://blog.metamatt.com/blog/2012/03/19
/custom-built-linux-router-no-thanks-to-realtek/), but don't want to deal with
storage hardware.

So…. back to NAS? The last day the DS4600 thoroughly irked me, a few hours
later Ars Technica ran [this gushing review of the Synology
DS-412+](http://arstechnica.com/gadgets/2012/09/synology-ds-412-is-fast-fun-
and-flexible/). Sounds good to me. I ordered one (actually the 5-bay DS-1512+,
which cost hardly any more) and am setting it up now. Wish me luck. In first
impressions, the hardware is well built, it runs quieter than either the
ReadyNAS NV or the DS4600 that it's meant to replace, and I like that they
gave some thought to fan replacement and memory upgrades. The browser UI is a
little too flashy for its own good, but is impressive in its own way. I
haven't done any real performance testing yet. Wish me luck.

