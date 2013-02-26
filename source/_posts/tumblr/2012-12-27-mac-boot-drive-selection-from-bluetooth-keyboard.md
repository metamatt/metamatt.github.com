---
layout: post
title: Mac boot drive selection from Bluetooth keyboard
tags:
- apple
- mac os
---
Twice in the last few months1 I've had to do troubleshooting steps on
Vanessa's iMac that involved booting from alternate volumes2. This is normally
easy on a Mac, but not quite so easy on a Mac with a wireless Bluetooth
keyboard3.

Both times, it was an exercise in frustration, as I give the reboot command
and wait about 10 seconds for the reboot to actually happen; then I hold
Command-R, watch the screen blink black, wait, watch it blink white, wait,
chime, wait, Apple logo, wait, and… oh hello, login screen! That's not right.
I've just wasted a minute and I'm back where I started.

Apple's [support document on recovery
mode](http://support.apple.com/kb/HT4718) makes it sound so easy:

> Restart your Mac and hold down the Command key and the R key (Command-R),
and keep holding them until the Apple icon appears, indicating that your Mac
is starting up. After the Recovery System is finished starting up, you should
see a desktop with a OS X menu bar and a "Mac OS X Utilities" application
window. Note: If you see a login window or your own desktop and icons, it is
possible that you didn't hold Command-R early enough. Restart and try again.

After reading and rereading that, I try a few more times, holding Command-R
earlier and earlier as Apple recommends, and, no luck. Wait a minute, I'm
using a Bluetooth keyboard. Does that cause complications, like, the computer
and keyboard aren't able to communicate right at the beginning of the boot
process? Yes4. Do I need to go find a USB keyboard to plug in? Not quite.

It turns out the magic answer is to reboot the computer, wait for the LED on
the keyboard to flash (which is after the computer starts booting and chimes
and does a self-test which on this iMac with 12GB of memory all takes about 20
seconds), and _then_ immediately press and hold Command-R. Any earlier than
that, and you'll be ignored.

You'd think Apple's help docs could mention this, since they've been shipping
Bluetooth keyboards by default with all their desktop machines for years now.

* * *

  1. Both of these occasions involved disk failures in the [Crucial M4 SSD I installed a year ago](http://blog.metamatt.com/blog/2012/01/20/nothing-is-as-easy-as-it-should-be-ssd-upgrades/). You can probably guess that I'm not quite as happy with these as I wanted to be. ↩

  2. [Booting from CD](http://support.apple.com/kb/HT1533) to upgrade firmware, or [booting from the recovery partition](http://support.apple.com/kb/HT4718) to attempt disk repair. Each of these requires holding a certain key down while the computer is booting. ↩

  3. I put the same SSD model in my own computer, a Mac Pro tower with easily accessible drive bays and an old-school wired keyboard. It's a lot easier to troubleshoot and a lot easier to repair. Murphy's Law dictates that if we're going to have problems with one SSD, it'll be the one [tucked away under the glass front of the iMac](http://www.ifixit.com/Guide/iMac+Intel+27-Inch+EMC+2309+and+2374+Hard+Drive+Replacement/1634/1). ↩

  4. Try googling for "[boot Mac from CD](https://www.google.com/search?q=boot+mac+from+cd)" versus "[boot Mac from CD bluetooth](https://www.google.com/search?q=boot+mac+from+cd+bluetooth)". Big difference. The first one leads you to a simple answer (but deceptively simple in the case you have a Bluetooth keyboard); the second one leads you through a muddle of hundreds of confused people. ↩

