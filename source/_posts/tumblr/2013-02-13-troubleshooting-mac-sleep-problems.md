---
layout: post
title: Troubleshooting Mac sleep problems
tags:
- apple
- gadgets
- pmset
comments: true
---
Here's a useful nugget if you're inclined to poke at computers to see how they work: `pmset -g log`.

I had a problem where my rMBP would sleep just fine on battery power but [not when plugged into its charger](http://blog.metamatt.com/blog/2013/02/13/two-things-i-didnt-know-about-mac-os-internet-sharing/). Even with the lid closed, and even if I explicitly poked the Sleep button first. This meant my chair got really warm if I left the computer sitting there plugged in to charge overnight. (NB: I did have the slider in energy saver preferences set to sleep:never for AC, but that should only affect sleep-after-idle, not lid-close or explicit sleep request.)

The command `pmset -g log` helped me learn that this state, where the computer is awake with the lid closed and no external display or keyboard is attached, is called DarkWake and that InternetSharing was the entity requesting that over sleep.

Now that I know about DarkWake, I'm curious what the relationship is between it and [PowerNap](http://support.apple.com/kb/ht5394). On this same rMBP, I disabled PowerNap because it would occasionally kernel panic when waking from sleep; I forget how I decided that was PowerNap but it hasn't happened since disabling.
