---
layout: post
title: Windows wi-fi connection sharing annoyances
tags:
- software
- windows
---
Windows has this "internet connection sharing" feature which lets you share an
existing network connection over one network adapter by turning on NAT,
forwarding and DHCP services on additional network adapters.

[This is really useful](http://blog.metamatt.com/blog/2010/11/24/windows-
connection-sharing-for-travel-network-access/), but Windows' UI for
enabling/disabling it is really lacking compared to, say, Mac OS X.

When I want to share the ethernet connection over wi-fi: I have to both set
the wifi adapter to connect to a private ad-hoc network, and set the wired
adapter to shared. This requires 2 separate steps in two completely different
places in the network configuration UI.

Then, when I want to use the computer as a wi-fi client, I have to turn both
of these off, again requiring 2 separate steps in 2 separate places.  If you
just associate to a real wifi network but leave sharing enabled for the
Ethernet connection, then Windows acts as dhcp server and not client on the
wi-fi connection.  (And if you don't know what's wrong, the symptom is pretty
non-obvious -- Windows will let you join wireless networks and report it's
connected, but no traffic will flow.)  So you have to dig around in 2
different places and remember to change both or you get a broken config.

The Mac OS way of saying, all in one place, "share this [wired] through that
[wifi]", and if "that" is "wifi", asking the name to share it under and
setting up an AP, works far better.

Another wart in Windows' ICS:: the result is an ad-hoc network which not
everything is compatible with (my iPhone works until it sleeps, but loses its
DHCP address on wake; Pre doesn't even show it).

