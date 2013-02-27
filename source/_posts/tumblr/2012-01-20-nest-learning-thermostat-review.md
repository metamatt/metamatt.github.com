---
layout: post
title: Nest learning thermostat review
tags:
- nest
- gadgets
- thermostats
comments: true
---
I bought two [Nest Learning Thermostats](http://www.nest.com/living-with-
nest/) for my house, which has two furnaces. Here's how they're working out
for me.

**Ordering**

I almost bought them on the day they were announced back in November, but
dithered, and the initial batch sold out; I got on the waiting list and
waited. In early January they sent me an email allowing me to place an order
(for up to 5 units); I ordered two; they arrived Friday and I've spent the
weekend playing (er, working) with them.

One thing that happened between when I didn't order them the first day and
when my turn to order came around was [Marco Arment's post on Nest
incompatibility with his existing wiring](http://www.marco.org/2011/12/17
/nest-incompatibility-without-c-wire). Having read that, I semi-carefully
checked my own wiring against Nest's online compatibility wizard before
ordering (which I might not have bothered doing if I hadn't read Marco's post,
given that my furnaces and wiring are only 3 years old, so I assumed they're
modern). When I say "semi-carefully", I mean I looked at my wires and verified
them against Nest's tool (which says I'm fine), and I considered Marco's
problem (2 wires, red and white, are enough for a basic thermostat to control
heating, but not to power or recharge the thermostat without activating said
heating) and made sure I had a 3rd wire and figured I wouldn't have that
problem.

In fact, when my thermostats arrived and I installed them, I also uttered a
[triumphant but premature
tweet](https://twitter.com/#!/metamatt/status/157882839508062209) about having
modern wiring. If only. If you're reading carefully — more carefully than I
had read Marco's post — you'll note I said I had 3 wires, but not which 3
wires. And, as it turns out, I had it wrong. No, I didn't have a C (common)
wire; my third wire was a G (fan) wire.

**Unboxing and setup**

The packaging is nice; the actual thermostat unit is nice; the base which you
attach to the wall has a built-in level, and pressure-fit connectors for the
wires instead of screw terminals. It's obvious the device was carefully
designed and built without taking shortcuts — which had better be true, given
the price.

It was fairly easy to take my old thermostat off the wall, note how it was
using the wires, reconnect the same wires (Rh, W and G, again) in the same
capacity to the Nest base, attach the Nest base to the wall, and then press
the Nest device onto the base. It didn't take long to do this twice, in fact —
once upstairs and once downstairs.

The next step is to connect the thermostat my Wi-Fi network — entering Wi-Fi
passwords on small devices without keyboards is usually no fun, but entering
text on the Nest's rotating dial is surprisingly satisfying. Kind of like
using a combination lock from high school again, but less confusing. As soon
as it connected to the network, the Nest found itself a software update,
invoking the download-and-reboot cycle that's the bane of many modern smart
devices. In fact, it seemed to reboot twice. The downstairs device survived
this fine and next wanted me to join it to a cloud management account; the
upstairs device asked me what time it was, which is a bad sign for something
that's supposed to be connected to the internet. It turns out it had forgotten
how to connect to the network, so I had to enter my Wi-Fi password again.

After this setup phase — which took a little longer than I'd expected due to
all that rebooting — the thermostats were active, ready to use manually, and,
ostensibly, learning my habits so I don't need to tell them what to do.

**Use**

These thermostats are easy on the eyes and easy to use; you just turn the dial
to change the temperature, or push in on the dial to bring up the onscreen UI
with easy-to-understand options for setting home/away, turning the whole thing
off, or invoking manual scheduling settings I haven't bothered playing with.

If you create a Nest account and install the smartphone app or use their
website, you can monitor and change the temperature from anywhere, which is
pretty darn space age if you ask me.

One minor glitch is that the just-approach-to-wake-screen feature seems to
only sometimes work; the Nest is supposed to recognize when you approach and
greet you by turning on the screen, but sometimes it doesn't turn on until I
actually touch it, sometimes it only turns in when I stick my hand within
inches, and sometimes it turns on when I just walk by. This would be a minor
annoyance, but it also makes me wonder how well the auto-away feature will
work, since that's also based on a proximity sensor (maybe the same one, maybe
a different one, I don't know).

Two simple things my old, not-worth-blogging-about thermostat did that the
Nest doesn't: show you the time on the main screen (my wife and I are used to
using the thermostat as a clock on our way out the door, as it's conveniently
located for that) and remind you to change the furnace filters. Oh well, not a
dealbreaker, and maybe these features will appear in a future software update.

One design deficiency that wouldn't be worth complaining about with any other
thermostat, but is noteworthy with the Nest now that they're trying to apply
good design to elevate thermostats to the level of art object: off-angle
viewing of the display is terrible. It looks great from straight on, but
thermostats are usually mounted at chest level, not at eye level, and used
from fairly close by, so in normal use I'm looking down at the display at a
fairly steep angle. Part of the problem is the LCD display itself, and part of
the problem is the convex lens sitting over it; it's really not putting its
best face forward in actual use.

**Problems**

The second day after I installed the two Nests, I heard a clicking sound
coming from the heating ducts. Upon inspection, the downstairs furnace was
working fine, but the upstairs furnace was making the clicking noises, which
were resonating through the ducts. I fiddled with the thermostat; it wanted
the furnace on but it wouldn't come on. I turned the thermostat off; the
clicking stopped. I turned the thermostat back on, and it turned on the
furnace for about a minute, then the furnace turned off and went back to
clicking. I fiddled with the thermostat for a while longer, and was able to
provoke various permutations of this behavior, but not a working upstairs
furnace.

I called Nest support, and got a really helpful and knowledgeable guy who
suggested I swap the upstairs and downstairs units, to help rule out a problem
with the thermostat itself. After the swap, I still had problems upstairs and
not downstairs — apparently the problem is with the furnace, and not the
specific Nest unit. His hypothesis was that my furnace was so sensitive to
voltage that it would work fine if the thermostat just bridges the Rh and W
wires, but if the thermostat pulls any power at all from those wires, the
furnace relays get confused and start toggling instead of staying on. Just for
fun, I measured the wiring at both thermostats with a multimeter and couldn't
detect much difference between upstairs and downstairs (in both cases, the
multimeter saw 28 V across Rh and W with the thermostat detached and the
furnace not running, and 0.485 A across Rh and W with the furnace running),
but the Nest's built-in technical details monitoring report claimed voltage
dropped from 29 V upstairs when not running the furnace to 7.77 V when running
the furnace (and compared to 9.19 V downstairs). Is that 1.4 V difference
enough to explain why one would work and the other wouldn't? I don't know.

When I called back to Nest support with these results, the tech support guy
said this sounds like a power stealing problem and the probable solution is to
run a C wire. I asked why two nearly identical (same model, different size)
furnaces that are only 3 years old would be different in this regard, and he
didn't really know.

Note this isn't the same problem Marco wrote about, though I'd likely have
that problem over time too; his problem happens if the furnace doesn't run
very often and the Nest needs to charge itself without running the furnace; in
my case the fully charged Nest couldn't even run the furnace when it should be
on.

**Gripes**

Beyond the fact that the thermostat can't run one of my furnaces, it's
annoying that the [Nest compatibility
tool](http://store.nest.com/#compatibility) doesn't even warn of this problem.

A few other things that came up with I was on the support call: first, when I
was first describing the problem and giving information on how I'd connected
the Nest et cetera, I asked if they were already collecting diagnostic
information in the cloud since the thermostat is smart and internet-connected,
and was told no. I find that surprising and disappointing — a missed
opportunity. (There's maybe a privacy concern, and I don't want them selling
data on how often I run my furnace or how often I'm home vs away, but I
certainly wouldn't mind them collecting diagnostics to improve their product.)

Also while chatting with the support tech, I asked if there was a way to get
the Nest to display a clock on the main screen, and to remind me when to
change the furnace filter, and was told no on both accounts; then I asked if I
could file a feature request for those and was told that not only do they not
take feature requests from customers, but that the support techs are
prohibited from talking to the product designers, both for legal/intellectual
property reasons. I joked that this must be because Nest was founded by people
from Apple — famous for not being persnickety about taking ideas from people
who might then claim ownership of said ideas; what can you say about a company
with an official "[unsolicited idea submission
policy](http://www.apple.com/legal/policies/ideas.html)"? — and he said yeah,
if you read our privacy policy it has a lot in common with Apple's. But come
on. It's not like there's any intellectual property in the idea of a
thermostat displaying the time of day. And more than that: a policy that says
a company can't listen to its customers is a customer-hostile policy.

**Solution**

Basically, to get the Nest working with my upstairs furnace, I need to give it
a C wire. I did consider running new thermostat control wiring, but when I
looked at where the wires run, it's not worth the trouble — there's no way to
rerun the wires without opening walls.

But. What's this G wire for, anyway? Following the [Transtronics wiki](http://
wiki.xtronics.com/index.php/Thermostat_signals_and_wiring#Heating) Marco
linked to, and confirmed by observation, the thermostat doesn't need to tell
the fan when to run while heating — I have gas heating and the furnace itself
controls the fan. Now, the thermostat can also tell the fan to run without the
heat, and it turns out that's all the G wire is good for. After checking with
my wife, I confirmed we almost never use that feature (and it was relatively
easy to access before, with a switch on our old thermostats, whereas with the
Nest it requires digging through the settings menu a bit, so we're even less
likely to do it).

Thus, the solution: repurpose the G wire as a C wire. We don't really need
direct control over the fan, and if I do, I can run new wiring for that, to
locations that aren't as hard to get to as the thermostat locations. (Note
that this works for me because we have gas heat; electric heaters don't
control the fan themselves, so removing the G wire would not be a good idea.)
So, I had to turn off the furnace and reconnect the green wire on that end
too, moving it from the G terminal to the C terminal. This quick-and-dirty
solution satisfies my hacker instincts, and after a couple days of use, the
Nest is much happier: the Nest's voltage monitoring reports 36 V at 100 mA,
instead of 8 V at 20 mA without the C wire, and the furnace runs when it
should.

**Summary**

I like it; I'll keep mine.

But based on my experience, I can't recommend the Nest thermostat unless you
can give it a C wire. And I'm disappointed that all the information Nest will
give you before buying doesn't point out even a whiff of such problems.

**Update**: Nest support [tweeted me back](https://twitter.com/#!/nest/status/160464579711877120) to say they've updated the compatibility tool with a note about the C wire, but in my opinion [it's still buried where it's too easy to miss](http://blog.metamatt.com/blog/2012/01/20/nest-c-wire-update/).

