---
layout: post
title: State of the last-mile internet connection, year 2009
tags:
- comcast
- network
- last-mile
- cable
comments: true
---
In summer 2009, Comcast rolled out [DOCSIS 3.0](http://en.wikipedia.org/wiki/DOCSIS#Speed_tables) in the Bay Area,
including my neighborhood in San Francisco. Specific offerings included speeds
as high as 50mbps/10mbps up/down, and a pretty decent price on 30mbps/6mbps.

So: I abandoned [my Astound 18/2 connection](http://blog.metamatt.com/blog/2011/04/07/state-of-the-last-mile-internet-connection-year-2008/) and signed up for Comcast 30/7. That was
September 2009. Looking back, I see that it was only 4 months later that I
signed up for [pingdom monitoring](http://pingdom.com/) of my home IP address.
That's a bad sign -- I wouldn't need to monitor something that was working
properly, would I?

I spent a lot of time traveling in the middle of 2010 so I didn't realize
quite how bad it was getting, but it was getting bad -- the [Comcast connection would drop out entirely](http://stats.pingdom.com/sh6fgl3lqqrd/150515/history) a couple times
a month, then a couple times a week, then almost daily, getting worse and
worse over time. I don't remember thinking it was really bad until November
2010, but looking back at the data, the problems dated all the way back to
January.

Click on the [Pingdom history link for the pretty graphs](http://stats.pingdom.com/sh6fgl3lqqrd/150515/history), which
unfortunately don't tell the whole story: they show the amount of uptime (or
downtime), but the problem is more insidious. At first, the connection
failures would happen at night or when I wasn't home, and would fix themselves
after a few hours, and I just assumed the whole network was down. Over time,
as this happened more and more, sometimes when I was home, and I gained
familiarity with the problem, it acquired a very distinct signature: when I
noticed an Internet connectivity failure, I'd ping the modem on its LAN
address (192.168.100.1), it would fail to respond, I'd reboot it by unplugging
and restoring power to it, and it would work fine immediately after reboot.
This looks a lot less like a problem with the network itself and a lot more
like a problem with my modem. So, Pingdom sees very little downtime because
each time it goes down, if I'm home I immediately notice and bring it back up
-- it's the number, not the length, of the outages that's annoying me. You can
click on the month links in the Pingdom status page to see the details;
December 2010 through February 2011 sure isn't pretty, with about 10 outages
per month.

So I arrived at a succinct description of the problem: modem suddenly stops
carrying traffic; at this point it also stops responding to ICMP or HTTP
requests on its local address. Reboot. It comes back fine. Speaking as a
software engineer, this looks like a bug in the modem firmware -- something
goes wrong and the modem crashes. But I have no way of telling what went
wrong, since the modem doesn't have any useful logs or diagnostics accessible
to me (even though I own the modem, its firmware and operational parameters
are controlled by the network provider, namely Comcast, not me).

I tried calling Comcast to see if they had any suggestions, but instantly lost
a lot of faith in their monitoring acumen when they said they couldn't see any
history of problems, at a time when the modem was actually unplugged. I tried
replacing the modem, but a brand new modem (different brand, Zoom) failed the
same way within days. (I went back to the original modem, a Motorola SB-6120,
since it reboots much faster, and given how often I have to reboot it, that's
actually an important feature. Plus it was already paid for.) I tried calling
Comcast and had them send a troubleshooting tech out, twice. Both times, the
tech measured the signal at the modem, said it looked great, then for good
measure went around inspecting wiring (and the first time replaced a
splitter). The problem persisted, albeit less frequently. Meanwhile, a few
more calls to Comcast support yielded only suggestions to remove every
splitter in the path (which is weird because (a), I didn't realize that
splitters are the root of all evil, but apparently everyone who's worked on
cable networks considers them the first thing to check, and (b), most
customers have to be using splitters -- how else are you supposed to connect
your cable modem and your TV at the same time?).

I do have to hand it to the first Comcast tech, who not only replaced one
splitter but found an uncrimped connector on one end of a homemade cable (made
by, er, me). It's funny to me that this poorly made cable had no effect on
speed or measurable signal quality at a given time, and not all that much
effect on reliability, since the cable modem connected via that cable worked
at a good speed for weeks or months between outages. But I'm sure it's better
to have that cable connected tightly. I'm also at a loss to explain why poor
wiring causes modem crashes -- it seems much more likely to cause signal
degradation that causes persistent speed loss; it's hard for me to see how
(without measurably degrading the signal) it can occasionally just crash the
modem. But hey, I'm not a cable modem designer. Maybe the bad wiring or rogue
splitter would occasionally push the modem outside some operational parameter,
electrically, and the modem responds by entering some untested area of its
firmware and locking up. Who knows. Now they've removed all the splitters and
then put back exactly one professionally installed one, checked the cabling,
measured the signal and it all looks good, and yet the problem persists.

Summary: the problem persists, and at this point Comcast charges me extra
every time they send a tech out to not fix it. Right now, I'm just living with
an Internet connection that forces me to reboot the modem once a week when it
crashes.

Pros: fastest Internet connection available in my area; pretty cheap at
introductory rate; serious upload speed; I haven't seen any speed degradation
due to other customers on the same cable -- I get full speed any time of day
I've tried.

Cons: Flaky connection; Comcast customer support and policies (no servers,
per-month cap of 250GB, past bad behavior including throttling, entire Comcast
address block is on the [Spamhaus PBL](http://www.spamhaus.org/pbl/) so my NAS
can't email my Yahoo account to tell me about firmware upgrades); listening to
[ads for pay-per-view boxing matches](http://blog.metamatt.com/blog/2011/01/26/reason-number-7-its-weird-getting-internet-service-from-a-cable-company/)
when calling tech support; opaque pricing (between bundles and introductory
rates, just try using Comcast's website to figure out how much it actually
costs).

Summary: The network itself is competently run on the best technology
available in this area, but nobody knows how to troubleshoot my problem and
it's apparently not worth it to Comcast to care for the price of one consumer
connection.
