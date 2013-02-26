---
layout: post
title: ! 'DSL disappointments: too bad that didn''t work'
tags:
- dsl
- last-mile
- network
---
I'm giving up on DSL. There are really 3 separate reasons that it's not
performing as I'd hoped and expected:

  * Reliance on AT&T's wiring, and no incentives for AT&T to provide good enough wiring. There's apparently no clear agreement between Sonic.net (and more importantly their DSL equipment) and AT&T as to what constitutes acceptable wiring. AT&T claims they've met their side of the bargain, but I have one line that syncs at 18mbps and one that syncs at 3-5mbps. Clearly, there's an important difference between them, but it's one that AT&T isn't required to care about.
  * [Annex M doesn't deliver, for me](http://blog.metamatt.com/blog/2011/04/18/dsl-disappointments-annex-m-edition/). Maybe it works in other cases, but for both my fast line and slow line, it caused a significant decrease in downstream performance and no increase whatsoever in upstream performance.
  * The modem is finicky: depending on exactly how I connect it (which cabling, whether I use a filter, and what order I connect the two lines), [it delivers as little as 30% of the sync speed as usable performance](http://blog.metamatt.com/blog/2011/04/18/dsl-disappointments-misleading-sync-speed-edition/).

I was hoping to see Annex A speeds syncing at the expected 40mbps down/2mbps
up, which using Annex M could be reallocated as something like 30mbps
down/5mbps up. But instead I'm getting 22mbps/2mbps from the wires in Annex A,
and Annex M reallocates that as 15mbps/2mbps, which there's no reason to do.
The highest real transfer speeds (not sync speeds) I've seen, sticking with
the Annex A configuration, are 20mbps down, 1.8mbps up.

That 1.8mbps upstream is the clincher -- that's only a quarter of what I'm
getting from Comcast. That might be fine for people who don't want to run
offsite backups across the WAN, but I've grown addicted to faster upload
speeds.

I really like Sonic.net as a company -- their policies and their attitude
towards customers are preferable to any of the incumbents that own their own
wires. But the wiring they're able to rent from AT&T doesn't cut it for me. If
in the future they're able to connect my house with something better than AT&T
phone wiring, I'd certainly consider it.

