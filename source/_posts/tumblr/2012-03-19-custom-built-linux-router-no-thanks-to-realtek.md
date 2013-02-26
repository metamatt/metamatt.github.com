---
layout: post
title: Custom-built Linux router, (no) thanks to Realtek
tags:
- linux
- networking
- gadgets
---
In my last post, I spelled out my requirements for a home router: dependable
and not requiring babysitting or monthly rebooting, but flexible enough to let
me run and control dnsmasq, tcpdump, and VLANs.

When I realized I was seeing so much weirdness at once from my OpenWrt router
as to be circumstantial evidence against OpenWrt itself, I mentioned this to
my officemate and he said "why don't you stop screwing around and install
full-blown Linux?" Sure, I thought, but that brings up two problems: it
sounded like a huge time suck, and where am I going to find appropriate
hardware to use as a router?

With help from friends I eventually solved the second one, not without paying
a heavy tax in terms of the first (and not in the way I expected): this is
that story.

On the time suck question, it seemed like I would have to learn a lot of new
things to set up and, possibly, maintain a lot of tasks that I was accustomed
to having OpenWrt do for me. I already knew how to install and administer
Linux for standard desktop or server use, but I'd never myself configured any
advanced networking topologies and my few interactions with iptables had been
painful, so configuring NAT and firewalling and routing and dealing with
multiple network interfaces was daunting (and this box is by definition going
to be exposed to the Internet, so I'd better get the firewall right). I poked
around and found [shorewall](http://www.shorewall.net/), which exists
basically to configure the parts that I didn't already know how to do, and the
more I read about it, the more it seemed a good match for what I was trying to
do.

On the hardware question, I wanted something small and quiet and low-power,
which would fit in my server rack and stay on all the time without running up
my power bill or generating so much heat that it either fails or needs a leaf
blower of a fan. (That basically describes most consumer routers, for which,
generally, the closest thing you can find to a standard Linux distribution
supporting them is OpenWrt. Ahem.)

I also wanted it to have multiple network interfaces, as a router should.
(This may or may not be relevant to the hardware decision, though; read on.) A
router needs a minimum of two interfaces by definition: one for each network
it routes between, so at the minimum, one for the LAN and one for the WAN. The
scenario I had in mind was more complicated, with two separate LANs (one for
my family and one for guests who just want to get their tablet on the
internet), and leaving room for the possibility of multiple internet
providers, so I'd need at least 3 interfaces, with the option to expand to 4
or more in the future. Now, these don't all have to be physical interfaces
built into the router. If the router has USB ports, you can add more that way;
also if you have other physical infrastructure supporting VLANs, you can
multiplex several networks over one physical port. (Again as a comparison to
OpenWrt: standard consumer routers that OpenWrt runs on tend to have 5 ports
and 2 network interfaces; one network interface is connected directly to one
port labeled WAN, and the other interface is connected through a switch chip
to the other 4 ports, which by default are bridged onto a single VLAN but
which can be configured for 4 separate VLANs if that floats your boat.)

After getting some advice from friends and discussing it ad nauseum, I ended
up buying a [fit-pc2i](http://www.fit-pc.com/web/fit-pc/fit-pc2i-
specifications/), notable because it's a standard x86 PC (so I can choose
really any standard Linux distribution or even Windows to run on it), in a
tiny passively cooled case, drawing 6W, and with 2 physical network
interfaces. (I didn't like the idea of depending on a bunch of USB network
adapters, and I wasn't sure I could rely only on VLAN support to get extra
ports, so I wanted a 2nd port for insurance. Now that I've used it, I think a
single reliable physical network interface + VLAN support would work out
fine.) Those 2 network ports are not enough for my scenario, so I also bought
a [Cisco SG200-08](http://www.cisco.com/en/US/products/ps11229/index.html)
switch, which I use solely to add ports, turning 1 into 8.

Having made these decisions, I bought the fit-pc2i and SG200, installed Linux
(Ubuntu 11.10 Server) and dnsmasq and shorewall, configured VLANs between the
router and switch so that various switch ports acted like they were connected
to additional eth1.x interfaces in the router, and started testing things. It
worked fine until I tried a speed test (from a client connected through the
new router which was connected behind my old router); the speed test promptly
hung from the client's point of view, and I couldn't access the new router
over the network at all. I power cycled the new router, tried again, same
result. I poked around log files, tried to enable the Linux NMI watchdog, and
generally looked for clues without finding anything until I visited the fit-pc
forums and read ["solution for freezes when scp/ftp/nfs with most Linux
dist"](http://www.fit-pc.com/forum/viewtopic.php?f=9&t=2383). This pointed the
blame squarely at the Realtek network interfaces, and suggested an alternate
driver as a solution. Once I started investigating fixes for this, I got
really pessimistic at first: [a Google query for "r8169
freeze"](https://www.google.com/search?q=r8169+freeze) shows a dismaying
number of hits, many in distribution-specific bug reports going back years and
years. I'd been under the assumption that networking is Linux's lifeblood and
that wired networking has long been a solved problem — wireless network
hardware flaky under Linux, sure, any network hardware flaky under Windows,
sure, but wired network hardware flaky under Linux? That was a rude surprise.

Long story shorter, the in-tree driver (open source and provided with Linux
kernels) for this class of Realtek hardware is named r8169. It actually
supports a family of Realtek chips named RTL8111/RTL8168, of which there are
apparently many variants with important programming differences even inside
the same PCI ID, so using lspci won't necessarily tell you enough about which
one you have. Realtek also has their own driver, also ostensibly open source
but not included in the standard Linux kernel, called r8168. For years now,
you can find blog posts saying "I had such and such a problem with r8169 and I
switched to r8168 and it worked better." So naturally, I tried r8168, and
found it didn't work at all. Upon further investigation, it has completely
broken VLAN support (at least on my hardware, in the 8.027 driver that was
current at the time, in the phase of the moon that obtained at the time): on a
non-virtual interface it worked fine (and without freezing the kernel); frames
that should have an 802.1Q tag added or removed had it done incorrectly, and
would either (outgoing) get ignored by the switch, or (incoming) get ignored
by the kernel. After spending hours running 3 instances of tcpdump (on the
fitpc on the raw interface, on the fitpc on the virtual interface, and on a
separate machine plugged into a switch port on the SG200 mapped to the same
VLAN), I could characterize the problem: outgoing frames were transmitted with
no tag, and get dropped by the switch. Incoming frames with a tag actually had
it stripped and were dispatched properly. I found out about "ethtool -K" to
control hardware acceleration of VLAN tagging (does this really benefit from
hardware acceleration? More than it loses from the possibility of someone
screwing it up?), disabled VLAN tag hardware acceleration in both directions,
and found the opposite problem. Just by luck, at this point I re-enabled
hardware acceleration for VLAN tagging only on the RX path, and things started
working. But only on certain ports.

As a recap of what I found to be broken with r8169 and 802.1Q: as the driver
loads by default, it improperly tags packets on the TX path. If I use "ethtool
-K txvlan off", TX works but RX packets are ignored. If I use "ethtool -K
txvlan off rxvlan off" followed by "ethtool -K txvlan off rxvlan on", TX and
RX both work, but flakily — some ports and protocols work, some don't, and I
don't know why but I've spent too much time staring at packet traces and I
don't care any more. The driver is broken out of the box, can be made to
almost work by enabling and disabling VLAN tag acceleration in the right order
through an order-dependent set of transitions reminiscent of port knocking,
but still doesn't entirely work, and I'm not going to trust it.

Then, back in r8169-land, I found an Ubuntu bug report, [Network problem with
the r8169 driver and RTL8111/8168B](https://bugs.launchpad.net/ubuntu/+source
/linux-backports-modules-3.0.0/+bug/839393?comments=all), in response to which
people said the 3.1 kernel driver seems to work better than the 3.0 kernel
driver, and Leann Ogasawara produced a 3.0 kernel with the 3.1 r8169 driver
grafted in for people to try. So I tried it, and: lo and behold, while my
repro scenario would still provoke a nasty warning and stack trace in
system.log, there was no freeze.

At this point, I reported my findings to both the r8168 maintainers (Realtek)
and the r8169 drivers (Linux netdev mailing list and Francois Romieu). Realtek
didn't respond at all. Francois did reply, saying he'd been fixing a bunch of
problems in this area recently, and the 3.2 driver should work even better
(this was last December, in the final throes of the 3.2 kernel release). I
grabbed a 3.2RC7 kernel, installed it under the Ubuntu 11.10 install I was
using, and it worked fine. No warnings, no backtraces, no freezes.

I haven't touched the configuration since; after another week or so of testing
I installed the fitpc + Ubuntu 11.10 + the 3.2RC7 kernel as our main router,
and we haven't had any problems with it. Hopefully, the Ubuntu 12.04 release
(which already uses a 3.2 kernel) will install and run fine, and I won't have
to worry about this for another another 5 years since 12.04 is an LTS release.

Lessons learned here:

  * VLANs are cool, and I don't really need more than one physical interface on the router the way I'm using it. I recommend the VLAN + separate switch as port splitter technique. But you do want a gigabit network interface if you're going to do that.
  * Realtek was the bane of my existence for a few weeks in December. It looks like I just had bad timing, and if I'd done the same setup in April using Ubuntu 12.04 with a Linux 3.2 kernel I wouldn't have had to learn any of this r8168/r8169 business. But given the history, I wouldn't recommend their products. I went so far as to reconsider the whole fitpc choice. But in this form factor, it seems all the alternatives (including other fitpc products) use Realtec NICs.
  * shorewall makes configuration of NAT routing, firewalling, and traffic shaping much easier, in my opinion, than raw iptables and tc.
  * Aside from dealing with the Realtek issue, this was less of a time suck than I was expecting.
  * Including dealing with the Realtek issue, this was more of a time suck than I was expecting.
  * I'm happy with the result, though. Treating the fitpc-2i and SG200 as one unit, I have something that's about the size and power consumption of the OpenWrt router, except now it's got a 1 GHz x86 CPU, 1GB of RAM, 32GB of flash storage, 9 individually addressable network ports, and is still entirely solid state. Those hardware specs only matter inasmuchas they give me plenty of breathing room for future expansion (I don't think my actual usage was taxing the much-lower-speced OpenWrt router), but the real bonus is it's stable: OpenVPN, dnsmasq and miniupnpd are all behaving as they ought to.

