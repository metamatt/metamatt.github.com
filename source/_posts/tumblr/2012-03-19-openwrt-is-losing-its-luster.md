---
layout: post
title: OpenWrt is losing its luster
tags:
- openwrt
- linux
- networking
- gadgets
---
Ever since I discovered it in 2006, I've used, and been a huge fan of,
[OpenWrt](https://openwrt.org/) for my home network router. I started running
the venerable Whiterussian release on a genuine WRT54G, at a time when I
wanted to tweak some configuration options that the stock firmware didn't give
me control over; I dabbled in alternate firmware like Tomato and HyperWRT but
quickly found that their filesystem layout made them too hard to customize;
then I discovered OpenWRT and found the design far saner.

While my original purpose in looking past the factory firmware (power boosting
to increase range) didn't work out well (it boosted the signal and the noise,
with little effect on range — go figure — replacing the antenna worked far
better), I soon found myself addicted to several features of a fully
configurable router. Probably at least half of what I loved about OpenWRT can
be attributed directly to
[dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html), a wonderfully clever
piece of software that acts as both DHCP and DNS servers, and coordinates
across the two protocols, so that in general, all DHCP clients get entered in
the DNS with reasonable hostnames. (This solves the same problem that
Microsoft tried to solve with NetBIOS and WINS, and that Apple tried to solve
with Rendezvous/Bonjour, but the dnsmasq approach doesn't require any new
protocols or software on any of the clients — DNS just works.) Beyond dnsmasq,
here is a short list of things I ended up configuring my OpenWrt router to do,
which I hadn't realized I needed, but once available proved to be very useful:

  * OpenVPN server: set up an offsite file server at a friend's house for offsite backup 
  * avahi: to forward mDNS across the OpenVPN link as appropriate
  * VLAN support: in addition to my private LAN, I ran a separate semi-public network with wireless access points using a separate SSID bridged onto a separate VLAN which had access to the internet but not my LAN
  * tcpdump: whenever having network problems, the ability to sniff traffic on the router is invaluable in troubleshooting them

This worked great for years, but as time passed eventually the WRT54G got
flaky and started rebooting every few days. When it came time to replace it, I
wanted newer and faster hardware — compared to 2002-era hardware, I wanted
more RAM, more flash storage, gigabit wired networking, and N-speed wireless
networking. This was 2010, and such hardware was readily available. I picked a
suitable-looking model with good hardware (Netgear WNDR3700), installed the
current OpenWrt release (10.03, Backfire), and at first things were great1.

Then, what's the problem, you may ask? Well, over time I started experiencing
a raft of weird problems, to be detailed below, and slowly but surely I
started associating them with the current version of OpenWRT. I tried newer
versions, filing bug reports and asking for help in the forums, and even
switching to different hardware, but eventually these problems piled up to the
point I decided to switch away. I still have a lot of respect for the project
and its volunteer developers, but it just wasn't working out for me. My
unprovable hypothesis is this: Openwrt originally started as a fork of the
GPL-mandated open source drop of Linksys' own WRT54G firmware, and thanks to
Linksys' own engineering and binary drivers for the specific hardware they
used, the result wasn't particularly clean but worked great. Over time, as
OpenWrt started running on more and more hardware, and started tracking closer
to stock Linux instead of vendor-provided customizations, and using open
source drivers instead of opaque vendor binary drivers, it has to deal with
more configuration sprawl and gets less benefit from the vendor QA and the
result, while much cleaner, is also flakier. I don't know that this is true,
but in terms of pure stability, I never had a problem with Whiterussian on
2002-era hardware (Linksys WRT54G and Asus WL500G-P), whereas I saw all sorts
of weirdness with Backfire on 2010-era hardware (Netgear WNDR3700 and Buffalo
WZR-HP-300N).

On to the problem list:

  1. On the WNDR3700, internet connectivity would occasionally just stop. My LAN would be fine, except no contact with the outside world. I first blamed this on my cable modem and provider (hence [this](http://blog.metamatt.com/blog/2011/04/07/state-of-the-last-mile-internet-connection-year-2009/) [series](http://blog.metamatt.com/blog/2011/04/09/state-of-the-last-mile-internet-connection-year-2011/) [of](http://blog.metamatt.com/blog/2011/06/13/update-on-comcast-last-mile-isp-connection/) [articles](http://blog.metamatt.com/blog/2011/06/23/not-the-modem-after-all/)), and at the time I'd had such a good experience with OpenWrt that it was a long time before I thought to blame the router, but eventually I looked in that direction, and found eth1 would get into a stuck state that I could reset either by replugging the cable or using mii-tool to reset the media interface. [I posted about this on the OpenWrt forum](https://forum.openwrt.org/viewtopic.php?id=30655), without hearing much.

  2. Because of that problem, and because I couldn't tell whether it was hardware or software at fault, I did the extremely scientific thing of changing two variables at once, and bought a different router (Buffalo WZR-HP-300N) and installed a newer Backfire (10.03.1) on it. I didn't have the eth1 problem any more. But I did have a different and equally annoying problem at approximately the same frequency: dnsmasq would stop serving requests. Since it's responsible for both DHCP and DNS, this was fairly crippling. I'm loathe to blame dnsmasq itself since I've never seen this behavior from it in any other install, and also because this was accompanied by weird system level behavior: when it got into this state, I was unable to kill -9 the dnsmasq process, nslookup processes on the router would also become unkillable, and the router would fail to soft-reboot — I had to hard power cycle it. [I posted about this on the OpenWrt forum](http://blog.metamatt.com/blog/2011/04/09/state-of-the-last-mile-internet-connection-year-2011/) as well, to deafening silence.

  3. I'd see a low but present rate of DNS lookup request failures — a valid request would return NXDOMAIN, and repeated immediately would succeed. This caused a small amount of application-layer collateral damage and general flakiness. Of course, I don't know whether to blame Backfire or dnsmasq or something else. But I saw this problem during the 2 years I used Backfire as my main router, and not before or since.

  4. The OpenVPN link would eventually stop carrying traffic. Traffic that should be routed over the VPN link would just disappear. At this point, I'd try troubleshooting first with tcpdump, then by adding verbose logging like echo-a-character-for-each-packet in OpenVPN (which requires restarting the server), then restarting the firewall a few times, and none of these changes would make a difference immediately, but after restarting both OpenVPN and the firewall a few times each (without making any configuration changes other than enabling logging), suddenly I'd start seeing the echo characters and packets would flow; then I'd disable the logging and restart OpenVPN and it would work fine for a few more weeks. Again, I have no proof that Backfire was to blame here. But as in #3, I saw this problem during the 2 years I used Backfire as my main router, and not before or since.

  5. My Xbox 360 suddenly found itself unable to sign into Xbox Live. I noticed this in January 2011 and while it's hard to know exactly when it started or what changed, I hadn't changed anything in the router configuration recently, so I suspect the Xbox dashboard update shortly before that made the critical change. But I blame OpenWrt, not the Xbox software, because I sniffed the traffic it was sending, and found weirdness. Specifically, the Xbox likes to use UPnP to open network ports, and I had miniupnpd enabled on the router to allow this, and in the broken state, the Xbox would make a UPnP request to forward UDP port 3074 to itself, then it would send outgoing UDP packets to something.xboxlive.com:3074, and the router would see that as eligible for the forwarding rule it just set up, and immediately reflect the Xbox's own packet back to it. (It would also get NATted and go out on the WAN, and a few hundred milliseconds later a response would arrive from the real Xbox Live service, but by then the Xbox was already confused.) Meanwhile, the port forwarding wasn't actually necessary because of the OpenWrt NAT implementation. So if I stopped miniupnpd, the Xbox would be able to sign into Live, but other things I run that want UPnP or NAT-PMP would break. I was able to have it both ways by blacklisting the Xbox from talking to miniupnpd, but this didn't inspire confidence.

Once I mentally assembled this list into one place, I realized there was
enough general weirdness here that I was no longer happy with OpenWRT, and I
wanted something that would be completely stable and dependable. That made it
tempting to buy a router with the right capabilities as advertised features
out of the box, and stick with the stock firmware, but I didn't want to give
up on the flexibility I'd become accustomed to (especially, dnsmasq, ability
to run tcpdump, and ability to install extra services). What I actually did
about this is a story for another time. Here, I'll just say that after
replacing the OpenWrt router 3 months ago, I haven't seen any of the above
problems recur.

Note 1: Actually things took a little hacking before they were great, speaking
of Backfire on WNDR3700 — I initially started setting this up before the final
Backfire release, so I had to compile from source, which was fine because then
and even now, 5GHz radio support doesn't work in the precompiled releases. Too
bad, since dual radio support was my reason for choosing the WNDR3700 in the
first place.

