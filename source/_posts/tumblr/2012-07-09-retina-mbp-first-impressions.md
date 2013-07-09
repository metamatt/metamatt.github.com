---
layout: post
title: Retina MBP first impressions
tags:
- apple
- macbook
- gadgets
comments: true
---
I ordered the Retina MacBook Pro the second day they were available. (In that
day, the order backlog went from 1 week to 3 weeks, so I just got it a week
ago.)

**The screen** It's super high resolution, as you'd expect. The front glass covering it is super thin, like on the "retina" iPad and iPhone models, giving the appearance that the (invisible) pixels are painted on the surface, instead of trapped inside. It looks great. But it's still too glossy for my taste. (Apple says it's 4 times less glare-prone than their previous glossy screens; I don't know how to measure that; it may be _less_ glare-prone but [it's still glare-prone](http://www.zdnet.com/blog/apple/macbook-pro-retina-display-only-slightly-less-glossy/13133).)

Apple's using their usual pixel-doubling trick (same as on "retina"-branded
iOS devices) to increase the number of physical pixels while pretending not
to, to improve compatibility with existing software; as deployed on the rMBP
with OS X 10.7.4, it seems to work better than the experimental "hiDPI" pixel-
doubled modes on other recent Macs running OS X 10.7. While the rMBP doesn't
claim a new OS version, the Displays panel in System Preferences looks
different than on other machines running 10.7.4, with the list of pixel
resolutions removed and replaced with a choice between "best for Retina
display" and 5 "scaled" choices ranging from "more space" to "larger text".
(The option to show the display settings in the menubar is missing, somehow,
though the search feature in System Preferences still thinks it should be
there.)

**The physical design** It's thin. Apple achieved this thinness, controversially, by removing a bunch of components you'd expect in a high-end laptop — an optical drive, ethernet and Firewire ports — and also sacrificing upgradability by using custom components and connections to save space. I don't care at all about the missing optical drive (in fact, in my last laptop, I removed it and replaced it with an SSD), but I do care about the lack of upgradability. Typically I've extended the life of my laptop by upgrading memory and replacing the hard drive with an SSD. With this machine, the RAM is soldered in, and upgrades are not gonna happen. I countered that by ordering 16GB, more than my old desktop machine had, and hopefully enough for the life of this machine. I also ordered the Thunderbolt to gigabit Ethernet adapter; the way I use laptops, Wi-Fi is usually fine but occasionally not; the performance of the external Thunderbolt dongle is just fine, as long as I have it where I need it when I need it (the perennial problem with dongles/adapters).

And finally, in what may sound like a nitpick, I'm sad that Apple removed the
external battery status light. I always found that useful, especially if I
haven't used the machine in a couple days and am about to take it somewhere
and don't know if I need to take the charger with me. (I guess the MacBook Air
doesn't have this light either, so there's precedent, but I don't have to like
it.)

**The speed** The CPU is _fast_. Most of what I (and most of us) do with computers is no longer CPU-bound, but I was coming from a dual-core Core 2 machine, and this rMBP's Core i7 cores are palpably faster at the same clock speed, and this machine has 4 of them, and they're hyperthreaded so Mac OS thinks it has 8 of them. The only taxing thing I've tried so far is telling Serato Itch to analyze an 800-song music library, which took 3 or 4 hours on my old laptop and about 15 minutes on this one. I don't think I'll be complaining about CPU speed for a while.

Meanwhile, while [I've been all-SSD for a while](http://blog.metamatt.com/blog/2012/01/20/nothing-is-as-easy-as-it-should-be-ssd-upgrades/), this is the first time I've had Apple install the
SSD as a factory option instead of going aftermarket and choosing and
installing it myself. Mostly because I had no choice, but also because
[it looks like Apple finally chose a top-shelf model](http://www.anandtech.com/show/5997/ssd-and-usb-30-performance-of-the-retina-display-macbook-pro).

**The software** Given the pixel-doubling trick Apple is using on all their retina-branded models to avoid text and UI elements getting too small to see/interact with normally, software needs to be updated to actually take advantage of the additional resolution. Otherwise, it'll run as well as before but at the old resolution, and look somewhat blocky/pixelated. Apps that are mostly text and standard UI widgets using Apple's text rendering and widget libraries turn out fine; apps with a lot of custom graphical UI elements need to provide double-resolution versions of their images but look mostly okay in the meantime; apps that do their own text rendering look pretty much horrible without an update.

I normally use Google Chrome as my web browser. Chrome (and Firefox) is one of
those rare apps that does its own text rendering, which means it severely
needs an update, not just to be "optimized for Retina display" but really to
look good at all. [This update has already happened](http://chrome.blogspot.com/2012/06/chrome-and-new-shiny.html) in the
"Canary" channel (12 weeks into the future of the stable version, because
Chrome updates every 6 weeks, and updates flow from the Canary double-beta
version to the beta version to the stable version); this means if you want
text to look good, you can wait 12 weeks, use Safari, or use Chrome Canary.
I'm using Canary, and for the most part it works fine, but Google Maps doesn't
work. At all. (And more into nitpick territory, the Canary version is clearly
not intended for daily use; the yellow dock icon is an eyesore, and it won't
allow you to set it as the default system browser without [resorting to external means](http://justinlee.sg/2011/05/09/setting-google-chrome-canary-build-for-mac-as-default-browser/).) So I've got Chrome Canary for most
things, and normal Chrome and Safari as fallbacks for whatever doesn't work in
Canary, which so far is just Google Maps.

**The summary** It's got the highest resolution screen most of us have ever seen; it's thin and light given that screen size; it's fast, packing very respectable compute+storage hardware; it's basically the right silicon wrapped around an amazing screen in an amazingly tiny package. I'm theoretically annoyed by the need for an Ethernet dongle, but I expect it won't be a real problem. I'm theoretically annoyed by the non-upgradable RAM, but 16GB should be enough for anybody. Seriously, over the years usually RAM upgrades are the last straw that force me to upgrade laptops; it's hitting the RAM ceiling that forces me to upgrade the whole machine; time will tell if this rMBP model is a good or bad decision for me, but by ordering it with the maximum (in place of starting lower and upgrading later) it feels relatively well future-proofed.

I like it. I have a hard time imagining a better 4½ pound computer today.
