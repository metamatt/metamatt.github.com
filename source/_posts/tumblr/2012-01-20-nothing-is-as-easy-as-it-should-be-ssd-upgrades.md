---
layout: post
title: ! 'Nothing is as easy as it should be: SSD upgrades'
tags:
- apple
- gadgets
- ssd
comments: true
---
Santa, bless the guy, heard me getting annoyed at the sounds of hard drives
spinning up and down in the night, and decided to help me out by bringing me
SSD's for my and Vanessa's computers.

So, the week after Christmas, I replaced the spinning rust in my (2006) Mac
Pro and her (2009) iMac with [Crucial M4 solid state drives](http://amzn.to/wUySKX).

This was really easy in the Mac Pro; this machine is the easiest to work on
I've ever owned or used, and that's probably why a machine from 2006 is still
ticking along so happily in 2012 -- I've upgraded the RAM twice, the hard
drives three times for bigger/better hard drives and twice more to supplement
and now replace them with SSDs -- I don't really feel bottlenecked by 5-year-
old CPUs.

Drive upgrades are not as easy in the iMac. First of all, there are no screws
on the outside of the case; all the guts are behind the glass of the screen,
which is held on by magnets, and you need to remove it with a suction cup.
Seriously. (If you already know this, you probably don't find it surprising,
but when I first learned it, I was really surprised.) It's actually not as
hard as it sounds, but I did have to buy a suction cup. Then you have to
carefully disconnect a bunch of miniature ribbon cables. I followed the
[walkthrough here](http://www.btobey.com/learn/imac-ssd-install.php) because
it has nice pictures, except I couldn't actually follow it because the 2009
iMac I was working on, unlike the more recent models, doesn't have a 2nd SATA
port. Which means I had to replace the hard drive, instead of adding the SSD
alongside it. That was actually the goal, since I didn't want to hear drives
spinning up and down, but it means I had to contend with the [temperature sensor issue](http://blog.macsales.com/2751-proprietary-cable-can-put-the-brakes-on-upgrading-late-09-imacs).

There seem to be 5 ways people deal with this:

  * ignore it and deal with loud fans
  * use aftermarket software to control the fan speed, ignoring drive temperature
  * buy the cable from the previous generation iMac, which had the temperature sensor outside the hard drive
  * short out the temperature sensor circuit, which is apparently temperature-sensor code for "it's cool"
  * (only on newer iMacs with 2 SATA ports) leave the OEM factory hard drive attached, and add the SSD as a 2nd drive

I opted for shorting the pins, as I don't want loud fans, don't really trust a
software solution, don't want to pay and wait for the extra part which seems
to be hard to find now anyway, and don't have the newer model with the 2nd
SATA port.

This just leaves the question of how to short the pins. Jumpers from old PC
hard drives would probably do the trick, but I don't have any lying around. I
could cut the cable and just short the wires, but I wanted to leave the option
to reverse this procedure if things didn't work out.

I ended up making a jumper out of a short piece of one conductor from solid-
core Category 6 network wire. Strip that, bend it in a tight U, jam it inside
the connector at the end of the sensor cable, and it fits nicely. Seems to be
working fine.
