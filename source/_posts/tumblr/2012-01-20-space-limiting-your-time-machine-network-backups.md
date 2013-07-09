---
layout: post
title: Space limiting your Time Machine network backups
tags:
- apple
- nas
- backup
comments: true
---
As part of the [aforementioned office-quieting project](http://blog.metamatt.com/blog/2012/01/20/nothing-is-as-easy-as-it- should-be-ssd-upgrades/), I wanted spinning disks out of the office, so I
garbage collected 2 1TB drives from external enclosures that had served for
Time Machine, and [moved them into a NAS enclosure](http://blog.metamatt.com/blog/2012/01/20/nothing-is-as-easy-as-it-should-be-nas-upgrades/) in the basement.

That solved the noise problem and gave me a bunch more network-attached
storage, but turned off Time Machine; the next step was to re-enable TIme
Machine but back up to the network.

A few years ago setting up Time Machine to back up over the network, to
anything but the Time Capsule mini-NAS that Apple designed for it, took some
minor rocket science (and in my experience caused no shortage of kernel panics
on the client machines); now it's more stable and easy to set up, especially
if the network file services are provided by Apple's own AFP server. I have
some free space on another RAID array attached to a Mac Mini also in the
basement, perfect for this sort of thing, and so all I had to do was mount
that drive from the client machine, then go to the Time Machine prefpane and
select it for backup. Time Machine creates itself a disk image and goes to
town.

The one problem with this is that it creates a disk image with the same size
as the underlying physical volume. It's a sparse image, so it doesn't
immediately fill the whole volume, but it will grow to do so over time. That's
not good, since I want multiple Time Machine backups to be able to share that
volume, and they're not the only thing that lives there.

Googling for solutions to this, I found an article on how to [pre-create the sparseimage with whatever size you want](http://code.stephenmorley.org/articles/time-machine-on-a-network- drive/). I tried that, but when I enabled Time Machine, it ignored the
hostname_macaddress.sparseimage directory and just created a new
hostname.sparseimage directory next to it. (Which, IMHO, is a good thing,
since keying the backup name from the MAC address is not going to work well
with machines with multiple network interfaces, for example a laptop which is
sometimes using Ethernet and sometimes using Wi-Fi.) Maybe that's a holdover
from a previous OS version; who knows. So then I tried precreating the image
file as just hostname.sparseimage, but then when I enabled Time Machine to the
same volume, it noticed the existing one, decided not to use it, and created
"hostname 1.sparseimage" instead.

Then I stumbled on a simpler recipe:

  1. Enable Time Machine the normal way (mount a network volume, open System Preferences, go to Time Machine preferences, click Select Disk, and choose the network volume).
  2. Let Time Machine do its thing. It will create a sparse image there with the same size as the underlying volume, and do the initial backup, and (eventually) unmount the sparse image.
  3. Later, when Time Machine is not running, use hdiutil to resize the sparseimage to something smaller. I used "hdiutil resize -size 750g hostname.sparseimage" (down from its original 3TB size).

Boom. Seems to work fine. After having backed up a little over 400GB, Time
Machine now displays the backup status with "Available: 385 GB of 3 TB", so
after backing up another 385GB, it'll start pruning the backup set, instead of
filling the volume and getting confused.
