---
layout: post
title: Update on Comcast last-mile ISP connection
tags:
- network
- cable
- last-mile
---
After [months of woe with my Comcast cable
connection](http://blog.metamatt.com/blog/2011/04/07/state-of-the-last-mile-
internet-connection-year-2009/), and a couple months of [flirtation with indie
DSL](http://blog.metamatt.com/blog/2011/04/21/dsl-disappointments-too-bad-
that-didnt-work/), I called Comcast out for a third service visit to focus on
the external wiring. (Aside: This took some convincing from the service rep on
the phone; more on this later.)

I realized that our house had a bunch of old exterior cable wiring including a
dodgy splitter, left over from when we bought it, and entirely unused now.
Comcast hadn't decided to look at this before, and it hadn't occurred to me
that it would be related since I have no idea how things are wired downstream
of their lock box except inside my part of the house, but this time I decided
to be more careful. When the tech arrived, I asked him to open the lock box
and disconnect everything in there that I'm not using.

Also, the tech took a look at the wire from the pole to the lock box and said
it doesn't meet their current standards and offered to replace it.

Other than some hilarity involving division of labor (one guy calls in the
order for new wiring, a separate guy shows up a day later and strings it, then
the first guy comes back a day later and actually connects it inside the lock
box, because the first guy doesn't have the cherry picker truck to string the
cable and the second guy doesn't have the key to the lock box?), this went
pretty smoothly.

So now I have shiny new wire from the pole to my house, we disconnected all
the other old wiring so from the lock box the only connected wiring is my own
new indoor wiring, and, knock on wood. one of these things was the problem and
the problem is no more.

(This was a month ago, and I hesitated to write about it immediately for fear
of jinxing it, but now that it's been a month with none of the same old
problem, I'm feeling better about it.)

The promised aside: the service rep I spoke with on the phone was either a
genius or knew just enough about networking to be dangerous; I'm not sure
which. He asked how I knew it was Comcast's problem and I said I'd tried
replacing the modem already so what else could it be. He said what if it's my
router; I should try connecting my computer directly to the router and see if
the problem still happens. I explained how the problem only happens an average
of once every two weeks and there's no way I'm disconnecting all but one
computer in the house for weeks on end, and why should I suspect my router
anyway? Then we got in an argument about 192.168.100.1 and whether it is
indeed the address of the cable modem, as I believe, or, as he said, "the
address my computer uses to get online" (whatever that means). I was convinced
he was stonewalling me and he was convinced I was being difficult and this was
going nowhere so finally I said just send a tech out and he said OK but we'll
have to charge you if it's not our fault and I said fine, you've already done
that twice and I'll just have all the charges reversed once it does turn out
to be your fault. (And I did call back later and Comcast was happy to refund
the earlier service charges once they saw they'd had 3 calls for the same
issue.)

So anyway. I didn't find any of his facts or arguments highly convincing but
it did get me thinking -- how do I know my router's not acting up? It doesn't
seem to be, but maybe. It is bleeding-edge [OpenWRT](https://openwrt.org/),
after all, totally awesome in its power but not the most mainstream and tested
thing. So the next time the usual problem happened (conveniently, before the
wiring repairs mentioned above were finished), instead of power cycling the
modem I disconnected and reconnected the ethernet cable between modem and
router, thus toggling the ethernet link state. After that, connectivity was
restored -- I could ping both the router and external sites -- and the modem
reported no downtime.

That seemed like a smoking gun, but it doesn't explain why each Comcast wiring
repair changed the frequency of the problem. At this point I'm pretty sure I'm
dealing with multiple problems, interacting or at least masking each other in
complicated ways, and making troubleshooting that much harder. It really seems
like the wiring repairs helped materially, but if I do see more "modem
crashes", I'll be looking hard at the router first.

(And to make things even more confusing, I'll note I've also seen a handful of
"T4 timeout" problems where the modem complains to its logfile and then
reboots itself; that's definitely a Comcast-side problem; it's also wholly
distinct from the one I've been calling "the problem" and easily identifiable
since the modem clearly identifies it as such; it's also a lot less annoying
because it only seems to happen in the middle of the night and it fixes itself
within minutes.)

