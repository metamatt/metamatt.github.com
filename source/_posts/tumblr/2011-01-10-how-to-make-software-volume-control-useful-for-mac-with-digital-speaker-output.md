---
layout: post
title: How to make software volume control useful for Mac with digital speaker output?
tags:
- software
- mac
- apple
comments: true
---
I bought a pair of Beringer MS40 speakers for my Mac and connected them via an
optical digital cable, and immediately the master volume control on the Mac
became useless -- as in disabled. (The speakers have their own volume control,
a physical knob on the left speaker itself, which is slightly out of arm's
reach.)

For convenience, though, I miss having the software volume control, which I
could change from the menubar, my keyboard, and a variety of other places.
Sure, you get the best sound quality by using just one volume control (in this
case, the one on the speakers) and leaving the rest set to maximum, but I
don't need that enforced so strictly; it's useful having a systemwide volume
setting under software control, and the resulting quality impact isn't
immediately horrible. (It's not like the analog out has a fixed level just
below clipping -- it has a variable level! And Windows lets you vary the level
of a digital output.)

A corollary to this is that the volume +/-/mute buttons on my keyboard (a
standard USB keyboard, not from Apple) no longer do anything useful (they
bring up the normal Mac OS change-volume overlay, except further overlaid with
the international sign of the You Can't Do That Here).

Anyway, that's how it is and I can't change it. But individual apps that play
music, e.g. iTunes, do have their own software volume control. (With the same
impact on sound quality that Apple's trying to prevent me from inflicting on
myself systemwide! But hey.) So if I can convince Mac OS to interpret the
volume +/-/mute buttons as normal keys, not mapped directly to the now-useless
master volume setting, but instead let me remap them as systemwide shortcuts
for the iTunes volume setting, then I'd get back convenient keyboard control
over music volume.

Can this be done? The Keyboard prefpane in System Preferences lets me add
systemwide shortcuts to an individual app's menu commands, like iTunes'
"Increase Volume" command, from any key combination it considers legal for
such a shortcut, but it doesn't notice me pressing the volume buttons,
presumably because the part of the system that maps them to the master volume
is intercepting them too early. (Can that be turned off?)

Update: [USB Overdrive](http://www.usboverdrive.com/USBOverdrive/News.html)
solves this. It's got builtin support for recognizing every special key on my
keyboard, and for changing iTunes volume; even if it didn't, it would let me
set weirdo keys to either perform some action from an extensive and
customizable builtin list, or remapped to send some other key combination
which could then be used in the system Keyboard prefpane.

