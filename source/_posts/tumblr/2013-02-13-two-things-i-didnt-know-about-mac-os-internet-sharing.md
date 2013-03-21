---
layout: post
title: Two things I didn't know about Mac OS internet sharing
tags:
- apple
- networking
- gadgets
comments: true
---
On a recent trip to Mexico, we stayed in a hotel that charged a significant extra fee for fairly slow Internet access. After paying for an access code, we could associate one device at a time to the Wi-Fi network; we could use multiple devices only by paying for multiple codes (which we didn't want to do because for the speed, even paying once was a poor value) or by disconnecting the previous device.

Of course, I went looking for ways around this. We had at our disposal a Mac laptop, two iPads and two iPhones. Mac OS X has [built-in Internet connection sharing](http://support.apple.com/kb/PH6589), but it operates only between separate network adapters: you can share an Ethernet-connected Internet connection over Wi-Fi, or vice versa, but you can't share Wi-Fi over Wi-Fi[^1]. There's some reason to hope that this would be possible -- it's "just" a software problem[^2]; Windows and Linux generally support multiple virtual Wi-Fi interfaces from the same physical device, as used by [Connectify Hotspot](http://www.connectify.me/hotspot/) for Windows or the multi-SSID feature in many Linux-based Wi-Fi access points -- but this software feature doesn't exist for Mac OS X.

So, no sharing Wi-Fi over Wi-Fi with my Mac laptop, unfortunately. But there's another option that works without additional hardware; this is where the learning comes in. **First new fact**: you can share an Internet connection over Bluetooth. I'd thought this was only for sharing a cellular data connection from a phone to a computer (under the oxymoronic misnomer of "wireless tethering"), but it turns out to work in the other direction (known as "reverse tethering"). If you pair an iPhone or iPad with a Mac over Bluetooth, your Mac will grow a new network adapter called "Bluetooth PAN" (for Personal Area Network); you can then use the normal Sharing preference panel to enable Internet Sharing from Wi-Fi to Bluetooth PAN. Bingo.

(I can claim only partial success here, but it was good enough for me at the time. This technique works fine for iPads, but not iPhones. I don't know why; [nobody else seems to know why either](https://discussions.apple.com/message/20996155#20996155).)

That got us past our trip, and I was happy to have a new tool for my cheap-connectivity-while-traveling toolbox. However, when we returned home, I had an unpleasant surprise, though it took me a while to connect the dots. My Mac laptop was getting really hot when I left it plugged in overnight to charge. I eventually realized this was because it wasn't asleep, even with the lid closed (and with the lid closed, it generates more heat than it can comfortably dissipate, even at idle). This was frustrating because there are so many things that can keep a Mac from sleeping; this is where more learning comes in. Googling for ways to identify causes of Mac insomnia, I learned of the `pmset -g log` command, which I now highly recommend. It pointed me right at the culprit. **Second new fact**: Internet connection sharing prevents the Mac from sleeping while plugged in. (This is actually incredibly obvious in retrospect; it says so right in the Sharing panel: "Computers connected to AC power won't sleep while Internet Sharing is turned on." I hadn't read that while enabling Internet Sharing because I thought I already knew how to use it; by the time it was causing problems, the problems were too disconnected from the cause.)

In summary: Internet connection sharing is useful, and the Bluetooth PAN variant is further useful, but don't leave it on when you're not using it.

[^1]: Well, you can share Wi-Fi over Wi-Fi if you have multiple physical Wi-Fi interfaces. My laptop only has the one built-in Wi-Fi interface. It might be worth carrying a cheap additional USB Wi-Fi device for this reason. That would probably be the cheapest reliable solution to this problem.

[^2]: At the physical layer, a single Wi-Fi radio can only be tuned to a single channel, but nothing stops it from participating in multiple SSIDs as long as they're all on that channel.
