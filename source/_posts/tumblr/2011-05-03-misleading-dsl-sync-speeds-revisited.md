---
layout: post
title: Misleading DSL sync speeds, revisited
tags:
- dsl
- last-mile
- network
---
In response to my previous articles about frustrations with my DSL modem,
Sonic.net sent me a replacement modem to see if it would fare better. It had
one specific improvement but for the most part duplicated the previous
results; however I promised to post an update, and during the extra testing I
learned one more useful fact, so this is that update with that one useful
fact.

That useful fact: if you have two DSL lines in bonded mode, but the DSL lines
sync at different speeds, the Comtrend 5361 modem cares a lot about which
order you connect the lines (which of the fast/slow lines is master and which
is slave).

In more detail: the testing I was doing involved different ways of connecting
the modem to the DSL lines (one line at a time or both lines bonded, if bonded
then testing both ways to pair the incoming lines with the modem, with and
without DSL filters, with and without additional indoor wiring, and with both
Annex A and Annex M spectrum allocation modes).

If the modem is configured for Annex A operation and is connected to the MPOE
with no filter and minimal indoor wiring, I see it provide the good results
you'd expect: on either line alone, it transfers real bits at about 85% of
that line's claimed sync speed, and connecting both lines together, I get the
sum of the individual speeds (or 85% of the combined sync speed, which is the
same thing), and it doesn't matter which line is master and which line is
slave.

That's all as it should be. Where it gets weird is if I deviate from that
exact configuration. If I add a DSL filter, or enable Annex M, then the modem
may deliver only 1/3 of the claimed sync speed, depending on the way I connect
the 2 lines for bonded operation. Single-line operation still yields data
transfers at 85% of sync speed, and if I connect it for bonded operation with
the fast line as the master and slow line as slave I get the expected combined
rate, but if I connect the slow line as the master and the fast line as the
slave, real-world performance drops drastically. This is extra weird because
the line order doesn't affect the sync speed; in the bad ordering, the modem
still claims a nice fast sync speed and just can't transfer data nearly as
fast as it should. I'm still at a loss to know where the performance is going
or why.

Now, if you know this is a problem and know how to fix it, you can route
around it. And most people probably don't end up with 2 DSL lines that sync at
different speeds, and I presume that if they sync at the same speed the modem
doesn't care how you connect them. But this weird behavior sure caused me a
lot of grief and lost time.

On the bright side, the newer modem did perform correctly for single-line
operation on either line, which does address my initial complaint.

Previously:

  * [DSL Modem Annoyances](http://blog.metamatt.com/blog/2011/04/13/dsl-modem-annoyances/)
  * [DSL Disappointments: Annex M edition](http://blog.metamatt.com/blog/2011/04/18/dsl-disappointments-annex-m-edition/)
  * [DSL Disappointments: Misleading sync speed edition](http://blog.metamatt.com/blog/2011/04/18/dsl-disappointments-misleading-sync-speed-edition/)

