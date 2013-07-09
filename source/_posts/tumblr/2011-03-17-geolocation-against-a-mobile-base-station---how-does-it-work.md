---
layout: post
title: Geolocation against a mobile base station - how does it work?
tags:
- mobile
- apple
- location
comments: true
---
I just saw these [two](http://blog.urbanape.com/post/3798485232/show-me-the-way) [posts](http://www.tabletmonsters.com/news/video-wi-fi-only-ipad-2-gps-navigation) describing how an iPad tethered to an iPhone still gets accurate and up-to-date location information without GPS (via DF, citing this ability as "[another reason to consider a Wi-Fi-only iPad](http://daringfireball.net/linked/2011/03/16/gps-tethering)").

(As background, location information on mobile devices generally comes from
some combination of 3 sources, each of which may or may not be available: (1)
triangulation against GPS satellites, (2) triangulation against the cellular
network towers, (3) triangulation against Wi-Fi base stations. On cell phones,
GPS is often implemented as A-GPS, which means "assisted GPS" and is often
confused with #2, but is actually a combination of #1 and #2 -- that is, A-GPS
is a superset of standard GPS. The reason for having 3 different methods is
partly that each one requires a separate radio, and partly that different
methods work better in different situations -- GPS is most accurate and covers
the whole globe but is slow and only works outdoors; the other two only work
in areas with cellular or Wi-Fi coverage and are less accurate.)

Recent smartphones generally support all 3 of these methods (the original
iPhone lacked a GPS chip, and used #2 and #3). An iPod Touch has only a Wi-Fi
radio, no cellular radio and no GPS radio, so it can do only #3; this is also
true of most current laptops. The iPad is sold in two versions, branded as Wi-
Fi and 3G; Apple also adds a GPS chip only in the 3G models, so the Wi-Fi iPad
can do only #3, and the 3G iPad can do all 3 methods (this is true of both the
original iPad and iPad 2).

So. Clearly the 3G iPad is better equipped to know its location -- the
question is how well the Wi-Fi only iPad can know its location, especially,
say, if you're driving around using it for navigation, and its data connection
is coming from Wi-Fi tethering to a mobile hotspot (in the examples above an
iPhone 4, but in theory this could also be another cell phone with mobile
hotspot feature, or dedicated mobile hotspot device -- I wonder if that works
too).

This is a Wi-Fi only iPad, so clearly it can't use techniques #1 or #2. It can
use #3, but the standard query -- "I can see the base station with this MAC
address; where am I?" doesn't work in a straightforward way when the base
station is a mobile hotspot with no fixed location. That's why the fact that
it does work is news.

After brainstorming with friends we came up with 4 possible ways this could
work:

1. Collusion between the iPad and the hotspot: Some new protocol/secret
channel between the iPad and the mobile hotspot, where without using any of
the standard techniques listed above, the iPad can just ask the mobile hotspot
where it is. (The mobile hotspot has access at least to technique #2, and
probably #1, so it knows where it is.) This would be easy for Apple to do, but
somebody would probably have noticed if there was a new network service on the
iPhone whereby you could query its location. (NB 1: this might have privacy
concerns, though if all you can do is ask an iPhone where it is when you're
already right next to it, these concerns are minimal. NB 2: this would only
work with Apple hotspots, not, say, a Mi-Fi.)

2. Collusion between the hotspot and the service that implements base station
-> location lookups: This would make modify technique #3 to cooperate with
base stations that move around frequently, i.e. mobile hotspots. This is
believable, since Apple originally licensed said service from Skyhook and then
later moved to their own implementation. Maybe the iPhone in personal hotspot
mode is constantly updating Apple with its location, and the iPad can then do
the normal "where is base station with this MAC address" query and actually
get up-to-date results. (NB 1: this might also have privacy concerns, if
anybody can query the database by MAC address and follow your iPhone around.
NB 2: this would also work only with Apple hotspots, at least initially.)

3. Collusion between the location service and the cellular network: the cell
network knows where your mobile hotspot is (using technique #2), and it knows
what IP address it's assigned to your mobile hotspot. All of the data from
your tethered iPad is being routed through that IP address. Thus, it's
theoretically possible for the cell network to implement a service that
answers the question "I sent you a data packet, look at its IP source and map
that to a mobile hotspot and tell me where I am". This doesn't seem to have
any privacy issues, and doesn't require any changes to the hotspot so would
work with all hotspots, and would be a neat service for the cell networks to
offer, but you'd have to get every cell network to offer it, and I'm not aware
of any such thing.

4. None of the above; the iPads in the posts above aren't getting location
information from the iPhone they're tethered to; they're also seeing other
(fixed) base stations in range as they drive by, and are using those MAC
addresses to implement technique #3 the normal way; that is, nothing new is
happening here, and this works as long as you're in range of fixed base
stations (i.e. in a city) but not otherwise (i.e. on the open road, hiking
trails, etc).

Without going out somewhere where there are no other Wi-Fi signals available,
it's impossible to distinguish case #4 from the others. We tried this in San
Francisco today with an iPad tethered to a Palm Pre on Sprint, and its
location updated in real time as we walked around. I also tried tethering my
MacBook Pro to a Palm Pre on Sprint, then using Google Maps inside Chrome
(which supports geolocation services for web apps), and Google Maps was able
to correctly determine my location -- but again, it's impossible to tell
whether this was case #4 or one of the others.

Further research needed: does the iPad get up-to-date location from all
personal hotspots, or only an iPhone 4? And does this work in the boonies, or
only in range of fixed Wi-Fi base stations whose location is already known?
