---
layout: post
title: State of the last-mile internet connection, year 2008
tags:
- network
- last-mile
- dsl
- cable
comments: true
---
When I moved between houses in 2008, since I was moving anyway it seemed like
a good time to re-evaluate my options for Internet providers.

In this neighborhood of San Francisco, I actually have a lot more choices than
are available in most of the USA: 2 cable providers (Comcast & Astound),
first-party DSL from AT&T, or 3rd-party DSL over AT&T's wires.

I wanted speeds faster than DSL (the only affordable DSL connections topped
out at 6mbps/768kbps), so I decided to try cable. The 2 cable providers
offered similar speeds at the time, and I'd heard bad things about Comcast, so
I signed up with Astound.

Unlike telephone wires (one company has a local monopoly and owns all the
wires, but is required to share the wires for rental by other companies, hence
the existence of 3rd-party DSL), cable companies don't have to share their
wires, that I'm aware of. That's why there's no 3rd party cable internet, and
most areas don't have multiple cable providers. But this area does. So, there
are 3 different sets of wires running along the poles along my street (4 if
you count AC power): Comcast coax carrying Comcast signals, Astound coax
carrying Astound signals, and AT&T twisted pairs carrying who-knows-who's
signals. There was already a Comcast wire running to my building, but not an
Astound wire, so when I first signed up, they had to run a new wire.

They did it wrong. I didn't realize at first, but over the first 2 weeks, my
Internet connection would be reliable and plenty of fast most of the time, and
then every couple days would break entirely for half an hour or so. I called
Astound a couple times and they tried various troubleshooting purely from
their dispatch center and couldn't find any problems; eventually they sent a
tech guy to my house, but he decided the problem was with the wiring which he
couldn't reach. It turns out that Astound, as the newest company on the pole,
is also high man on the pole, as in their wires are mounted higher than the
others; also, they use a combination of their own employees and independent
contractors as service techs, and the guy they'd sent this time was a
contractor. His ladder wouldn't reach as high as the Astound cable, so he had
to call a real Astound guy with a cherry-picker truck. Finally the real
Astound guy showed up, replaced the cable from my house to the main line on
the poles, and showed me that the original cable had a big gash in it, and
basically as it moved in the wind could make or entirely break the electrical
connection. And yet, with a physical connection so tenuous, it worked fine
most of the time.

After that, I didn't have any more speed or reliability problems for the next
year.

Pros: pretty fast (18mbps/2mbps down/up); pretty cheap (especially at the 1st-
year introductory rate); worked fine after the first problem was resolved;
tech support was easy to reach and pretty easy to deal with.

Cons: shoddily run. Example 1: the original broken wire they gave me, and the
service tech they sent who couldn't reach the wire. Example 2: they forgot to
bill me for 3 months, then noticed and reacted by just turning off my account,
which got my attention to call them pretty quickly -- but it's not like I was
failing to pay their bills; they were failing to bill me. Example 3: they had
bogus reverse-DNS entries, so that my IP address would reverse-resolve to a
hostname that forward-resolved to some other IP address, which made it hard to
log into various remote servers by ssh as sshd looks askance at such
tomfoolery.

Anyway, I stuck with this connection for a little more than a year, until
Comcast rolled out DOCSIS 3 in this area, opening the door to faster speeds.
Faster uploads, especially.

One note is that I never saw the purported disadvantage of cable, where the
medium and associated bandwidth is shared among a whole neighborhood, and the
rated speed is high but actual speed decreases when your neighbors are doing
anything -- I got the rated speed pretty much all the time.

