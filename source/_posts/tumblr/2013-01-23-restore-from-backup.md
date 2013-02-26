---
layout: post
title: Restore from backup
tags:
- apple
- software
---
The SSD in Vanessa's iMac died and needed to be replaced. In theory, this is
pretty simple since we have backups — replace the faulty hardware, restore the
backup, and get on with life.

In reality, it's a little more complicated. I suppose these are small
complaints since in the big picture, she didn't lose any data. Still.

The way I carried out the restore was to

  * Attach the replacement SSD in an external USB enclosure (the "drive toaster")
  * Boot off the recovery partition of the failing SSD, which still worked well enough for this purpose (otherwise I would have had to make a bootable USB stick or DVD)
  * Invoke restore from Time Machine onto the new drive
  * Power down, open the computer, and install the new SSD in place of the old one. (This is the hard part on a recent iMac, involving taking the screen off with suction cups, and so on.)

And we're done, right? Not quite. Even after the Time Machine restore, a bunch
of things were wonky:

  * There's no recovery partition on the new drive. You'd think Time Machine would recreate that, too, but it doesn't. Internet wisdom says all you need to do is reinstall the current version of Mac OS X over itself and it will automatically recreate the recovery partition; I tried it and that wasn't the case. What this means is the next failure will be harder to deal with because I'll need alternate boot media; the manual means of creating the recovery partition at this point seem just as hard as dealing with that problem when it arises, so I'm ignoring it for now.
  * Legitimate licensed Adobe CreativeSuite apps had their copy protection crap out, and refused to run with scary messages from the licensing subsystem using the word "catastrophic". I called Adobe tech support, and they took 20 minutes to tell me to uninstall and reinstall the apps, which took another 20 minutes but worked.
  * CrashPlan backups weren't running because their software uses Java and Mac OS X ships without Java until you launch an interactive Java app at which point you're prompted whether you want to automatically install a Java runtime.
  * Time Machine backups weren't running because who knows why, until I went into System Preferences and manually prodded them to run once, after which they kept running fine automatically.
  * Mac App Store wasn't automatically updating software until I launched it and manually signed in.

These problems could have been caused by the hard drive replacement, the
restore from backup, or the OS reinstall; I don't really know which. I just
know there was a lot more to getting a working system back than letting Time
Machine restore the files.

