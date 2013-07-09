---
layout: post
title: State of the last-mile internet connection, year 2011
tags:
- data
- last-mile
- comcast
- sonic.net
- cable
- dsl
comments: true
---
Given the reliability problems I'm experiencing with [my otherwise nicely fast Comcast DOCSIS 3 connection](http://blog.metamatt.com/blog/2011/04/07/state-of-the-last-mile-internet-connection-year-2009/), I'm looking for something
new. It has to be reliable, and it has to be at least competitive on speeds
for both download and upload, though I'm willing to sacrifice some speed for
reliability and better policies.

The long and short of the Comcast connection: it's flaky (manifesting as modem
crashes. I've called Comcast multiple times and they've twice told me to
remove splitters, twice visited and measured the signal and said it looks good
and once replaced a poorly wired splitter; after all this the problem is less
frequent but still occurs multiple times per month.

So what are my other options? [Astound worked ok for me](http://blog.metamatt.com/blog/2011/04/07/state-of-the-last-mile-internet-connection-year-2008/) but is too slow (esp. for uploads); AT&T's best is
U-verse which also has slower upload speeds and apparently isn't available
here anyway; other DSL options have even slower upload speeds; then there's
this newer indie ISP, Sonic.net, with a DSL option I haven't seen before.

[Sonic.net Fusion Broadband](http://sonic.net/solutions/home/internet/fusion/)
is intriguing: an ADSL2+ connection advertised as 20mbps/1mbps, but supporting
an optional Annex M mode where you might get can get upload speeds as high as
3mbps by sacrificing some download speed, and it allows you to bond 2 lines
together for double the speed in each direction. Even accounting for some
falloff due to distance (I'm estimated to be about 3000 wire feet from the
central office, which should be [just fine for ADSL2+](http://www.dslreports.com/forum/r21245835-ADSLADSL2-Speeds-VS-Distance)), it seems like dual-line Fusion should get me back in the ballpark
of 30mbps/6mbps like I have now. And from a company whose entire business is
data, not trying to tie me to legacy TV or voice business models, to boot.

So, provisionally, I'm trying out Sonic: The plan was to get the lines
installed, see a nice 40mbps/2mbps connection, then see how good Annex M
actually does for upload speed (nobody will make solid predictions, so I just
have to try it for myself), and if (across 2 lines with Annex M enabled and at
my loop distance) the resulting speed is even, say, 75% of what I was getting
from Comcast (30/6mbps), consider it a keeper, due to friendlier policies and
reliability.

Easy in theory. In reality, signing up with Sonic was easy, but the going got
rougher right after that. Sonic doesn't own the wires to my house; they have
to [rent them from AT&T](http://en.wikipedia.org/wiki/Unbundled_Network_Element); as I found
[last time I tried indie DSL in 2001](http://blog.metamatt.com/blog/2011/03/31/state-of-the-last-mile-internet-connection-year-2001/), this isn't a perfect
recipe for success. The day they were supposed to connect the wires, AT&T
showed up 7 hours late, then told me they couldn't do the job because it was
too late in the day and they'd have to come back the next day. The next day,
they connected the wires, I plugged in the DSL modem from Sonic, and found
myself the proud owner of two 4mbps/1mbps DSL circuits. This wasn't going
exactly as planned.

I called Sonic; they looked at the statistics they monitor from their end of
the DSL equipment and immediately agreed this was a problem that AT&T would
have to look into; they made an appointment and AT&T sent someone back to my
house a few days later; the AT&T tech measured a bunch of stuff, said "looks
good to me", and left without anything having improved.

Fast forward a few weeks. Sonic seems to be going to heroic lengths to get
AT&T to up the quality of the wiring, but the fact that heroic lengths are
necessary, and haven't succeeded after 6 weeks, is disheartening. They've
managed to speed up one line and not the other, so one line syncs at
18mbps/1mbps and the other at 4mbps/1mbps. (Now that one line is behaving as
promised, it's also hard to believe they can't get the other one into shape --
before that, I was starting to think the distance to the CO was wrong and
there was another 6000 feet of wire in my loop.) In any case, I have yet to
even get to the second step of my plan, after dozens of calls to Sonic and 5
visits from AT&T service technicians.

At this point, it continues to be a race to see who can give me fast reliable
access. I'm continuing to try to get Sonic to get AT&T to provide the promised
line quality and speeds. The more time that passes, the harder it is to remain
optimistic about this. Meanwhile Comcast seems to remain the owners of the
highest-bandwidth wires into my house, so at the same time I keep trying to
get them to fix their reliability problem, though they've been charging me $30
for troubleshooting visits which didn't find or fix the problem, which is not
cool.

My current plan is still to stick with Sonic -- I really want to like them --
but the difficulty of getting AT&T to give me a good line (after 6 weeks and
counting) is disheartening, and even when they do get that fixed, I'll have to
cross my fingers and hope that Annex M works out ok. Also, the Comtrend 5361
modem Sonic sent me has now crashed 3 times even though I'm barely using it,
and generally seems buggy (which is scary since, you'll recall, I only reached
this point because of cable modem crashes). And worse, the reported 22mbps
speed I've reached so far is just the sync speed reported by the modem --
actual usable transfer speeds to any site I've tried top out around 7mbps
down, which I suspect might also be a bug in the modem firmware when bonding
lines of different speeds (maybe it won't shove any more data over the fast
line than the slow line). If once the lines are the same speed, usable speed
remains only 1/3 of nominal sync speed, I'll be sorely disappointed.

So. Maybe all these problems will be resolved and I'll get a reliable modem
that syncs at 30+/5+ and actually delivers that as usable speed. And maybe
I'll have to consider other options.

Backup plan 1: Get Comcast to fix the crashtastic-cable-modem problem. I'm
losing hope in that, too, after multiple service visits, all they want to do
is yank on wires, and that hasn't fixed it; also their monitoring is poor (I
called in while modem was down and they say they have no record of outages and
I say what about right now?); also I filled out a survey about customer
service and got a phone call from a manager saying "ok I see you've been
having this problem for a while, we'll make sure to send you the good tech
guy" and the next tech guy they sent did seem better but still didn't fix it.

Backup plan 2: Maybe Comcast's
[business](http://business.comcast.com/internet/plans.aspx)
[options](http://business.comcast.com/enterprise/Index/Services/teleworker)
have better tech support, troubleshooting abilities, or reliability
guarantees. A business-class line of my own costs a lot more than what I'm
paying now; the teleworker plan is actually cheaper but relies on support from
my employer, which may or may not exist.

Backup plan 3: Stick with Comcast, but route around the crashtastic modem:
install a USB-controlled kill switch/[STONITH device](http://en.wikipedia.org/wiki/STONITH), connect that to my router, and
teach the router to reboot the cable modem when necessary.

Backup plan 4: A low-tech version of #3; run a pull cord toggle switch (like
those used for lamps), controlling the cable modem's power line, from the
modem's home in my server closet up through the furnace duct to my office.

Backup plan 5: Hmm, I wonder how much [fiber from fastmetrics](http://fastmetrics.com/metricfiber_diagram.htm) would actually
cost. Way too much, I'm sure. But still.
