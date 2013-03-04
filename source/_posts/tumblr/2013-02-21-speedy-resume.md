---
layout: post
title: Speedy resume
tags:
- apple
- gadgets
comments: true
---
My initial reason for switching from Windows laptops to Mac laptops 7 years
ago — which has remained a primary benefit across those 7 years — was better
power management. The details are many but the result is simple: a laptop that
sleeps and wakes consistently and quickly, which never crashes on wakeup,
never drops the Wi-Fi connection on wakeup, and is on the network and ready
for me to type almost as soon as I open the lid. Almost like what we expect
from a tablet or smartphone.

That's the dream, anyway. I've never owned or used a Windows laptop (or Linux
laptop, for that matter) that pulled that off, and not for lack of trying. It
was much truer of Apple laptops running Mac OS X, ever since their
introduction in 2001. It remained one of my favorite things about more recent
Macbooks, but I've found it getting less true over time, culminating in my
2012 "Macbook Pro with Retina Display" (henceforth rMBP), which seems to take
like 30 seconds to wake from sleep, then sometimes crashes immediately as the
crowning touch.

After getting frustrated enough by the slow wakeup time to get to the bottom
of it, I think there are 3 pieces to the puzzle.

  1. The rMBP (like Macbook Air models) has no external status lights. No charge level indicator on the battery like older models with removable batteries, no charge level indicator on the side of the unit like previous unibody Macbook Pro models, no power light that winks while asleep and glows while awake like all previous Macbook models. So when you open the lid, if it wakes up and is ready for use, great, but if not, you don't know whether it's powered off, has a dead battery, or is already trying to wake up and just taking its sweet time.

  2. The default power-management plan is "Safe Sleep", which means that when you close the lid the computer writes a suspend image to disk, then suspends to RAM1. Then wakeup is normally fast because RAM contents are still present, but if power is lost for any reason (battery dies, battery is removed on models where that's possible, or the computer decides to power itself off to stop expending battery power to support the RAM), it can still resume from where you left it, just more slowly, by reading from disk. This last bit about deciding to power itself off is crucial; it's controlled by a parameter known as `standbydelay`, and on this computer at least (rMBP running OS X 10.8) the default value of `standbydelay` was 4200 seconds, or 70 minutes, just over an hour. This means if you suspend the computer and wake it up again within 70 minutes, it will resume from RAM, but if you leave it asleep for more than 70 minutes, it will have powered off entirely, and will resume from disk. On my previous laptop (a 13" Macbook Pro from 2010, also now running OS X 10.8), `standbydelay` was not set at all, which I assume means it will try to keep RAM supplied with power until the battery dies. I don't know the reason for the different defaults.

  3. This rMBP has 16 gigabytes of RAM, more than any laptop I've owned in the past. Now, it also has a fast SSD, so I wouldn't have thought it would take that much longer to resume from disk vs RAM (and in actual usage it shouldn't have to save and restore all of it anyway) but it's likely a factor: if it had to transfer the entire 16GB, even at 500 MB/sec that would be 32 seconds. It actually only needs to save/restore the active pages; say on average that's 60% of memory and add a few seconds to get the hardware devices from cold boot to powered on, and you're in the 20 second ballpark that is long enough to annoy me.

So boiled down: this machine feels slower to resume than previous ones because
it's suspending to disk, has a lot of memory to restore from disk, and doesn't
show any visible signs of progress while restoring from disk.

I changed the `standbydelay` value to 12 hours on battery (`sudo pmset -b
standbydelay 43200`) and disabled it entirely on AC power (`sudo pmset -c
standby 0`) and things seem much better now2.

Oh. And sleep reliability3? That's even more important. When I first got the
rMBP, it would kernel panic and show "Your computer must be restarted" when
resuming from sleep once in a while, roughly once a month. That was
intolerable; at a guess I disabled PowerNap; I don't know whether it was the
actual problem but I haven't had reliability problems since.

So these are my current recommendations for power management on a rMBP or
Macbook Air:

  * Increase `standbydelay` value enough that you don't notice the computer resuming from disk in normal use
  * Disable PowerNap

* * *

  1. The difference between suspend-to-disk and suspend-to-RAM is that suspend-to-RAM expends battery power to keep the contents of RAM alive, so wakeup is faster, while suspend-to-disk extends battery life at the expense of slower wakeup. ↩

  2. I didn't realize the import of this at first, but Mac OS maintains separate sleep policies for battery and AC power, and pmset can set either one (-b for battery, -c for charger) or both (-a for both, which is also the default); so there are two `standbydelay` values. I have my computer set to never sleep on AC power, but I sleep it manually by closing the lid when I'm not using it. After having applied the longer standbydelay to battery, I was annoyed to find the computer slow to wake after leaving it asleep and charging for a while. Hence the second command to entirely disable the `standby` behavior on AC power. ↩

  3. When talking about sleep reliability, what's actually important is the ability to _wake back up_ reliably, just like when talking about backup reliability, what's important is the ability to restore from backups. It's the round trip that matters. ↩

