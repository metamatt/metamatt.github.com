---
layout: post
title: Observations on mobile platform speed
tags:
- apple
- ios
- android
- webos
- systems
- gadgets
comments: true
---
Over the past 5 years, I've used smartphones from Apple and Palm (powered by
iOS and webOS), and played around with Android devices over the same timeframe
though I've never owned one for daily use.

Still, I find the different design choices at the system level to be very
different, and the results pretty much what you'd expect for each one:

  * webOS as Palm originally shipped it: apps are written in Javascript and run in an interpreter; the platform doesn't swap out virtual memory. I never saw apps crash; it was pretty common to get out-of-memory errors (in the guise of a message that says you're trying to do too many things at once and need to close some apps). Apps were pretty slow.
  * webOS as reinterpreted by the hacker/modder community: apps are still Javascript running in an interpreter, but now there's a swapfile pretending there's more memory. (I think Palm liked this patch enough they eventually folded it back into their official kernels, actually. And if swapping caused a hit to speed, it was compensated for by the fact that the hacker kernels also overclocked the CPU.) The result with this was a platform on which apps never crashed, and also never run out of memory, but they could be glacially slow. The poster child here was the Google Maps app, which often took so long just to launch — over a minute, no kidding — that it would apparently become confused about why it had launched in the first place, and just draw a white screen. (The bit about confusion is just my narrative, but it often would draw nothing but a white screen, and that seemed to correlate highly with the times it took forever to launch.) You can certainly make the argument that an app that takes a minute to launch to a broken state is no more helpful than an app that crashed; there's no panacea here.
  * iOS: apps are written in Objective C and compiled to native code; there's no swapfile I'm aware of. There are two results here: apps run fast, and they crash often. They crash because they segv from bad code, they crash because malloc returns null and they segv instead of checking for that, and they crash because the platform kills them for using too much memory.
  * Android: apps are written in Java and run in a JIT-compiled VM (which has gotten faster over time, notably in the 2.3 release); I don't know if there's a swapfile, but I suspect stock Android releases don't have one and mods like CyanogenMod allow one. As I said above, I don't have deep experience with Android devices, but my general perception is that on contemporary roughly equivalent hardware, it feels significantly faster than webOS and significantly slower than iOS. (I'm talking about user perception of speed here, which has to do both with how responsive the UI is and how fast real work gets done. iOS and webOS both pay more attention than Android to keeping the UI responsive, to the best of my knowledge.)

So. This evidence is relatively unsurprising and easy to explain — interpreted
code that can have as much memory as it wants never crashes but takes forever
to do anything useful; native code under tight memory management is much
faster and much more crash prone — what's interesting to me is that all 3 of
these approaches were considered viable in the marketplace. And I don't even
know that the dog slowness of webOS is the reason it failed in the marketplace
(and if HP had poured the right resources into it and actually shipped what
they said they would in 2011, a better optimized webOS 3 running on 2011-class
hardware might not have even felt slow). But even discounting webOS, the other
two approaches are both provably market-viable.

