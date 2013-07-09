---
layout: post
title: ! 'Nothing is as easy as it should be: NAS upgrades'
tags:
- nas
- readynas
comments: true
---
After [the SSD upgrade project](http://blog.metamatt.com/blog/2012/01/20/nothing-is-as-easy-as-it-should-be-ssd-upgrades/), I now have a stack of unused 1TB hard drives. I also have an old NAS unit (ReadyNAS NV) which is currently hosting 4 320GB hard drives, is almost full, and while old is still compatible with the 1TB drives. Sounds like a good match — time to upgrade.

Reading about [ReadyNAS' vaunted X-RAID technology](http://www.readynas.com/?cat=54), a proprietary extension to RAID
that allows resizing, this sounds easy — one by one, replace each drive with a
larger one, and wait for the RAID to rebuild onto the new drive. When the
drives are different sizes, the array will be limited to 4x the size of the
smallest, but after upgrading all 4 to 1TB, I simply reboot and will have
access to the full new size. And since the ReadyNAS supports hot swap and has
the drives mounted in nice hot swappable sleds, I don't even have to reboot
except for that final resize (and I'm not really clear on why I have to then,
but whatever).

Sounds easy… until I actually try swapping out the drives. The drives are in
sleds, see, and the sleds have this latch, and the latch has this release
button… and nothing happens when I press the release button. I try reading the
manual, which talks about how easy it is to add drives but doesn't go into any
details on what to do if you have trouble removing one. I try reading "[The definitive guide to the ReadyNAS NV+](http://www.readynas.com/?page_id=193)"
(a slightly newer but very similar model) for tips; it talks about how disk
replacement eases the stress of disk failure; my mind jumps to bad puns about
stressing the ease while easing the stress, and thinking I'm glad I'm not
dealing with the stress of a failed disk that I can't remove.

Eventually I find a [forum thread on the problem](http://www.readynas.com/forum/viewtopic.php?p=30550), with the
solution. It's 5.5 years old, and still kicking. Much like my ReadyNAS NV, I suppose.
