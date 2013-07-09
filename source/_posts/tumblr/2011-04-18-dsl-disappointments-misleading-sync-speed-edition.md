---
layout: post
title: ! 'DSL disappointments: misleading sync speed edition'
tags:
- dsl
- network
- last-mile
comments: true
---
Another [annoying behavior](http://blog.metamatt.com/blog/2011/04/13/dsl-modem-annoyances/) of the Comtrend modem I got from Sonic.net: it doesn't
always transfer real data at anywhere near the claimed "sync" speed.

As noted in [my initial post about Sonic.net's Fusion Broadband](http://blog.metamatt.com/blog/2011/04/09/state-of-the-last-mile- internet-connection-year-2011/), I have 2 DSL lines from Sonic.net, which each
in theory should support up to 20mbps downstream, but right now one of them
syncs at 18mbps and one of them at only 4mbps, due to overly high attenuation
in the wiring supplied by AT&T. Still, I should be able to get a combined
22mbps, right?

Well, with the modem deployed the way I intend to use it (in a back room near
my other networking equipment and my UPS, connected to a DSL filter with a
normal telephone patch cord), according to [Sonic's own speed test site](http://speedtest.sonic.net/ookla/), I get about 4mbps download and
1.83mbps upload. Whoa, that's a lot lower.

To make things weirder, if I disconnect the slow line (the one that syncs at
only 4mbps) and leave only the fast line (synced at 18mbps) connected, the
same speed test result is 15.71mbps download, 0.95mbps upload. How is one line
alone faster than the two lines together? At first I suspected a bug in the
modem when bonding lines of different speeds, but then I repeated the test at
the MPOE, and got the expected results: the two lines bonded together were
slightly faster than the fast line alone.

Curious, and suspicious of everything at this point, I decided to run a bunch
of tests: both at the MPOE (not depending on my own internal wiring) and in my
network closet (adding ~50 feet of internal wiring), with and without the DSL
filter supplied with the modem, and with different patch cables (the patch
cable that came with the modem, the separate Y cable Sonic gave me, and an old
patch cable I had lying around); for various combinations of each of these
variables I tested both lines together, and where possible each line alone
(that's easy to do at the MPOE and hard to do at the server room, [due to the way the modem is wired for single-line operation](http://blog.metamatt.com/blog/2011/04/13/dsl-modem-annoyances/)).

The results are pretty weird. I'll list the results, one per line, with a
description of the test configuration, the modem's reported sync speed
(down/up), the actual usable speed as reported by speedtest.sonic.net, and a %
number which is the ratio of usable download speed to claimed downlink sync
speed. First, testing one line at a time:

  * At MPOE, fast line, no filter, Y cable:  sync 18.46/1.14, speed test 15.76/0.95 (85%)
  * At network closet, fast line, with filter, Y cable: sync 18.49/1.14, speed test 15.71/0.95 (85%)
  * At MPOE, slow line, no filter, Y cable: sync 4.93/1.08, speed test 4.02/0.90 (82%)
  * At network closet, slow line, with filter, Y cable: sync 3.48/1.02, speed test won't run (because modem has sync on slave line only)

The result of these single line tests shows that my internal wiring (between
MPOE and network closet) and filter don't seem to affect the speed at all --
the modem syncs at the same speed, and tests at the same speed, in both
locations.

But then, dual line tests (sorted by descending actual speed):

  * At MPOE, both lines, no filter, Y cable: sync 23.60/2.23, speed test 20.06/1.83 (85%)
  * At MPOE, both lines, no filter, Y cable + their patch cable: sync 22.99/2.23, speed test 18.94/1.83 (82%)
  *  At network closet, both lines, no filter, my patch cable: sync 22.84/2.23, speed test 12.05/1.83 (53%)
  * At network closet, both lines, no filter, their patch cable: sync 22.86/2.23, speed test 10.38/1.83 (45%)
At MPOE,  both lines, with filter, Y cable + their patch cable: sync
22.09/2.23, speed test 6.12/1.83 (28%)

  * At network closet, both lines, with filter, their patch cable: sync 21.83/2.23, speed test 4.23/1.83 (19%)

Note how the sync speed does not change appreciably across all these tests,
but the actual speed changes hugely. Every single difference from the minimal
MPOE configuration results in decreased speed!

Some additional notes: first, bonded upload speed is completely stable at
1.83mbps in every single test I've run. Second, I have tried various other
speed test sites, and FTP of a large test file hosted by Sonic.net in case
Flash/Java speed tests aren't reliable indicators, but I got roughly
equivalent results from all of them, so I stick with the speedtest.sonic.net
numbers for comparison here.

First complaint: where are the bits going? Why is the sync speed not a
reliable indicator of real speed? It's annoying losing speed, and it's
annoying not being able to trust the sync speed, and this makes
troubleshooting speed problems a lot harder (it takes longer to run a speed
test than just check the sync speed, and Sonic.net's support system shows them
my sync speed but not, I presume, my actual transfer speeds). Presumably if
the modem can't actually transfer data at the sync rate, that's due to errors
and dropped frames at the ATM level, but the modem's status page shows 0 for
every ATM and DSL error category.

Second complaint: why do the filter, patch cable, and my internal wiring all
result in a speed loss, but only in bonded operation, and not one line at a
time, and without affecting the sync speed?

It's looking increasingly unlikely that I'm going to get a fast and trouble-
free connection via DSL. I mean, I _could_ put the modem by the MPOE (with no
UPS and no filter), but that wasn't the intent, and I don't understand why I
should have to.

And one final note: in response to my earlier article about this modem, Sonic
is already sending me a new one; I don't really want to take time to repeat
all of these experiments but I'll at least see if the new modem or new filter
does better in the cases that were worst here. (If nothing else, it should be
easier to do apples-to-apples comparisons, using the same cables and getting
all data points at both locations.)
