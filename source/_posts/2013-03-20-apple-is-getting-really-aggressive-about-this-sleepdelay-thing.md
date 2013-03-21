---
layout: post
title: "Apple is getting really aggressive about this sleepdelay thing"
date: 2013-03-20 09:01
comments: true
categories: 
tags:
- apple
- power
- pmset
---
Last night I installed the OS X 10.8.3 update on my laptop (updating from 10.8.2). This morning,
upon plugging my laptop into the external Thunderbolt display as I always do, and it didn't wake
up when I opened the lid, nor when I started tapping on the external keyboard.

[As I noted before](http://blog.metamatt.com/blog/2013/02/21/speedy-resume/), a retina MBP
(or MacBook Air) that doesn't immediately wake when you open the lid is annoying not only because
it slows you down, but because Apple's removed all the battery indicator buttons, and there's
absolutely no sign of life from a powered off (or hibernating) machine until you press the power
button.

So I woke it up with the power button on the builtin keyboard, and watched it boot to the preboot
login screen associated with an encrypted boot drive[^1], and was further annoyed that at this
screen it was still ignoring the external keyboard plugged into the Thunderbolt display. Having
to use the builtin keyboard for a docked laptop is suboptimal. Anyway.

When it finished booting, I fired up pmset to ask it what's going on, first on AC power:

```
magi@duality ~> pmset -g
Active Profiles:
Battery Power     -1
AC Power          -1*
Currently in use:
 standbydelay         4200
 standby              0
 womp                 1
 halfdim              1
 hibernatefile        /var/vm/sleepimage
 darkwakes            0
 gpuswitch            2
 networkoversleep     0
 disksleep            10
 sleep                0
 autopoweroffdelay    14400
 hibernatemode        3
 autopoweroff         1
 ttyskeepawake        1
 displaysleep         10
 acwake               0
 lidwake              1
```

And then again[^2] on battery:

```
magi@duality ~> pmset -g
Active Profiles:
Battery Power     -1*
AC Power          -1
Currently in use:
 standbydelay         4200
 standby              1
 halfdim              1
 hibernatefile        /var/vm/sleepimage
 darkwakes            0
 gpuswitch            2
 disksleep            10
 sleep                10
 autopoweroffdelay    14400
 hibernatemode        3
 autopoweroff         1
 ttyskeepawake        1
 displaysleep         2
 acwake               0
 lidwake              1
```

As [posted before](http://blog.metamatt.com/blog/2013/02/21/speedy-resume/), I'd previously changed `standbydelay`
to 43200 seconds on battery power, and disabled `standby` entirely on AC power. Apparently the 10.8.3
upgrade reverted the former change to Apple's new default of 4200 seconds, though it left the latter
change alone.

Note that's not quite consistent with my observation that my rMBP (bought in 2012 and shipped with
OS X 10.8) had `standby` enabled by default, while my previous MBP (bought in 2010 and shipped with
OS X 10.6 and subsequently upgraded to 10.7 and then 10.8) never had `standby` enabled at all.

[^1]: The FileVault preboot login screen also annoys me because it's got a pretty poor keyboard driver, and if I type my password at natural speed, it reproducibly detects one keystroke more than I intended to make. The same sequence of keystrokes is interpreted correctly by the real OS X keyboard stack. I reported this bug to Apple and they said they know and don't care.

[^2]: As an aside: anyone know how to get pmset to report the profile that's not active? `pmset -g` reports all settings for battery when on batter, and all settings for charger/AC when plugged into AC, and I have found no way to get all settings for both profiles short of running pmset twice, and physically plugging or unplugging the power connector between runs. Note that the set mode of pmset takes an optional `-a`/`-b`/`-c` argument to specify whether to change the values for battery, charger, or both profiles, but those aren't honored in conjunction with `-g`.
