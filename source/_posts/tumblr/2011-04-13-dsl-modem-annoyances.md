---
layout: post
title: DSL modem annoyances
tags:
- dsl
- last-mile
- network
comments: true
---
For [my dual-line Fusion setup](http://blog.metamatt.com/blog/2011/04/09
/state-of-the-last-mile-internet-connection-year-2011/), Sonic.net sent me a
Comtrend Nexuslink 5361.

It's an ADSL2+ modem that works with one line, or two lines bonded together,
and also includes normal home wireless router functionality (NAT firewall, 4
ethernet ports, and Wi-Fi).

My specific complaint here is that the way they wired it to accept 2 DSL lines
is annoying. It's got a single [RJ14 jack](http://en.wikipedia.org/wiki/Regist
ered_jack#RJ11.2C_RJ14.2C_RJ25_wiring_details), so both lines enter it there,
on the inner and outer pair of the same jack. The problem is that it considers
the outer pair to be line 1 (primary/master) and the inner pair to be line 2
(slave). And if you connect only the slave line, it will establish ADSL sync
but will not carry IP traffic (it looks like it never even acquires an IP
address and gateway via DHCP).

If you connect only the master line, or both master and slave, then it works
fine and carries IP traffic. But the way they wired it, it's much easier to
connect only the slave. (In fact, some Sonic.net support personnel told me
they thought this modem doesn't support single-line operation, which is
probably because they'd tried plugging it in the straightforward way and
found, indeed, it didn't work.)

The reason this is a problem is that any single-line (RJ11) phone jack you
have will only have the inner pair active. If you connect that to this modem
with a standard phone cord (with either 1 or 2 pairs), you've connected the
active pair to the inner pair on the modem, which is the slave line which will
sync but will not alone carry traffic.

And the way AT&T's wires [terminate at the
MPOE](http://en.wikipedia.org/wiki/Demarcation_point), each line goes to a
separate test jack (an RJ11 jack, so on the inner pair), and a separate set of
terminals, and it's up to the customer how it's wired from there. I connected
an RJ14 jack to both lines, the inner pair connected to one phone line and the
outer pair connected to the other phone line, which is the standard way of
wiring a 2-line setup, and I can patch that jack directly to the modem with a
standard 2-line phone cable to activate both lines. This setup is fine for
actual use, but if I'm having problems, it's unnecessarily difficult to
troubleshoot.

The problem is that no standard phone cable gives you an easy way of
connecting just the outer pair. A standard 1-line phone cable will connect the
inner pair to the inner pair. A standard 2-line phone cable will connect both
the inner and outer pairs to the matching pair on the other end. Sonic even
gave me a fancy Y cable, which on one end has an RJ14 plug with both lines
(inner and outer pair) active, and the other end has 2 separate RJ11 plugs
each with only the inner pair. Using this Y cable, I can plug the modem
directly into the MPOE, and connect both modem lines for bonded operation, or
test single-line operation by connecting either single line to either the
modem's master or slave (in practice, since slave-only operation isn't useful,
it's only useful to use the side of the Y cable that connects as the other
end's outer pair, thus goes to the modem's master side). And also, I can hack
the Y cable to work at my 2-line RJ14 jack to (in one direction) connect the
inner pair on the line to either the inner or outer pair on the modem, or (in
the other direction) connect the inner pair on the modem to either the inner
or outer pair on the line (and if you've followed me so far, you'll see that
these 4 configurations are really just 3, and 2 of them connect only the slave
line, so the only useful one is connecting the modem's master line to the
inner incoming pair, and there's no way to test the modem's master line on
only the outer incoming pair, unless I build myself a cable that connects
outer pair to outer pair while not connecting the inner pair).

The reason I'm complaining: this would all have been strictly better had
Comtrend made the modem treat its inner pair as the master line. As it is now,
you get the right result when connecting with a standard 2-pair phone cable to
a 2-line jack, or using the fancy Y cable to connect to 2 separate 1-line
jacks. But if you use a 1-line cable (to either a 1 or 2 line jack), or a
2-line cable to a 1-line jack, you'll end up in the broken configuration, and
this easily made mistake could have been easily avoided if they'd just
configured the modem the more obvious way.

Why do I care so much about connecting this modem one line at a time, when
it's designed for bonded operation, you might ask? That's a story for another
time.

Update 4/16/2011: Sonic.net noticed this post, and called me to say that the
various problems reported here have been fixed in updates by Comtrend to both
the hardware and software. They were surprised I'd gotten one of the old
modems, and are sending me a replacement (and even though most of the problems
mentioned in this post only affect troubleshooting and won't matter for real
usage, I accepted the offer to see if the newer modem will help with any of
the other problems I'm experiencing). +1 to Sonic.net for noticing this and
being proactive.

