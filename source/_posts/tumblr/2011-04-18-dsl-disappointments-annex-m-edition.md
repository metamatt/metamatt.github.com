---
layout: post
title: ! 'DSL disappointments: Annex M edition'
tags:
- dsl
- network
- last-mile
comments: true
---
Yet another disappointment with the DSL connection and/or modem from
Sonic.net: Annex M doesn't seem to do any good at all for upload speeds.

[As I wrote in my introductory post on Sonic.net,](http://blog.metamatt.com/blog/2011/04/09/state-of-the-last-mile- internet-connection-year-2011/) the whole reason I was willing to consider
them (or DSL technology at all) was the promise of decent upload speeds. The
last DSL connection I had was only 768kbps upstream, and even ADSL2+ promises
only about 1mbps upstream, but Sonic.net offers this Annex M configuration
which trades some downstream bandwidth for upstream bandwidth, with upstream
speeds theoretically as high as 3.3mbps (Sonic claims 2.5mbps is more typical
real-world performance on a good line). Given that Sonic makes it easy to
double these speeds by combining two lines together, now we're talking -- a
combined 5mbps upstream would compare decently with what I'm getting from
Comcast's DOCSIS 3 technology.

(It's hard to know exactly what real-world speeds to expect from Annex M.
Sonic's baseline for a single ADSL2+ line under good conditions, using the
default Annex A configuration, is 20mbps/1mbps, or 40mbps/2mbps across 2
lines. Annex M should increase upload speeds to as much as 2.5mbps per line,
but at at unknown cost to downstream speeds -- I haven't found anyone willing
to predict that. It seems a reasonable estimate would be somewhere between the
following hypothetical best case and worst case: best case, I added 1.5mbps of
upstream, so it should cost me 1.5mbps of downstream; worst case, I multiplied
upstreams speed by 2.5, so my downstream speed will be divided by 2.5. Using
those as upper and lower bounds, I should expect something between 8mbps and
18mbps remaining downstream per line, or 16-36mbps/5mbps combined, with Annex
M. That would compare favorably enough with the 32mbps/7.5mbps I'm getting
from Comcast that, given the reliability problems and caps I'm also getting
from Comcast, I'd be happy to switch.)

As described in my [earlier](http://blog.metamatt.com/blog/2011/04/09/state-of-the-last-mile-internet-connection-year-2011/) [posts](http://blog.metamatt.com/post/4719413815/dsl-modem-annoyances-misleading-sync-speed-edition), after two months of asking Sonic to ask AT&T
to provide wiring that will sustain a good ADSL2+ signal, I have one line
syncing at 18mbps and one line syncing at only 4mbps (downstream speeds, using
Annex A). Still, I figured I might as well see the results of the Annex M
spectrum reallocation, so last Friday I called Sonic and asked them to enable
Annex M on both lines.

Then I went to the modem's status page to see the effect on sync speeds. (If
you followed my recent post on [sync speeds vs actual transfer speeds](http://blog.metamatt.com/post/4719413815/dsl-modem-annoyances-misleading-sync-speed-edition), all tests here were done at the MPOE with no
filter, that is, the best case from those earlier tests.)

First annoyance: the modem wouldn't sync at all, on either line, until I
enabled Annex M on both lines. Maybe this is how it's designed to work, but
from earlier reading of Sonic's site (2 months ago when I first signed up, all
excited by Annex M) that's not the impression I got. Reading again now, the
[Annex M FAQ](http://sonic.net/support/faq/advanced/annexm.shtml) doesn't say
one way or the other, but [Dane's post introducing Annex M](http://corp.sonic.net/ceo/2010/04/20/fusion-annex-m-available-for-testing-in-santa-rosa/) seems to imply it's safe to leave it on on the network end and
toggle it at will on your end. That would be more convenient, but for my
Comtrend 5361 at least, the behavior is: if the network end is set to Annex A
and the modem is set to Annex M, it syncs using Annex A (good), but if the
network end is set to Annex M and the modem is set to Annex A, it doesn't sync
at all (bad).

Annoying, but not a deal-breaker. Let's see how the speeds compare. I'll give
numbers even for the broken configurations that didn't sync, since I did test
those combinations and the results are interesting.

All of the following tests are with Annex M enabled for both lines on Sonic's
end, and at my end with the modem plugged directly into the MPOE with no
filter. Speed test results are from speedtest.sonic.net.

Both master and slave lines set to Annex M:

  * Master sync: 2.54/1.08
  * Slave sync: 12.51/1.14
  * Combined sync: 15.06/2.23
  * Speed test: 5.92/1.83

Master on Annex M, slave on Annex A:

  * Master sync: 2.54/1.08
  * Slave sync: no sync
  * Combined sync: 2.54/1.08
  * Speed test: 2.17/0.88

Master on Annex A, slave on Annex M:

  * Master sync: no sync
  * Slave sync: 12.62/1.14
  * Combined sync: 12.62/1.14
  * Speed test: 10.82/0.96

Both master and slave set to Annex A:

  * Master sync: no sync
  * Slave sync: no sync
  * Speed test: N/A

As a comparison point, here are my most recent numbers for a comparable test
with Annex A on both ends:

  * Master sync: 4.84/1.08
  * Slave sync: 18.36/1.15
  * Combined sync: 23.12/2.23
  * Speed test: 19.72/1.83

So, two things to note here.

First, Annex M significantly decreases downstream speed without increasing
upstream speed at all, for me. Compare the sync speeds above for Annex A and
Annex M. The best sync speed I saw for the slow line was 53% of what it was
without Annex M; the best sync speed I saw for the fast line was 69% of what
it was without Annex M; the combined sync speed was 76% of what it was without
Annex M.

Second, Annex M hurt my transfer speeds even more than the claimed sync
speeds. Note the oddity that while bonded operation results in a faster sync
speed than connecting the fast line only, when I measure the actual transfer
speed, it actually got slower. (That's reminiscent of [the earlier bonding experiments I ran with Annex A](http://blog.metamatt.com/post/4719413815/dsl-modem-annoyances-misleading-sync-speed-edition).). The single-line Annex M
tests both transferred data at the 85% of claimed sync speed that I've come to
expect, but using both lines bonded together, this ratio drops to only 39%.

Again, I'm curious why bonding the lines results in slower operation than one
line alone, without this effect being visible in sync speeds or ATM errors.
And unless something is completely wrong here, it looks like Annex M does not,
for me, bring DSL back into the realm of competitive upload speeds.
