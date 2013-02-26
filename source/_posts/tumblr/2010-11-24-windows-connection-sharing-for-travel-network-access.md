---
layout: post
title: Windows connection sharing for travel network access
tags:
- windows
- travel
---
While traveling the world, Vanessa and I have been sharing a single netbook
for internet access.  In addition to the netbook, we each have one of my old
unlocked iPhones, which are useful for voice calls and even 3G data access in
countries where that's available cheap to travelers, and also come in handy as
wi-fi devices for checking email/facebook/web/whatever when the netbook is
already in use.

One thing we found is that in some countries (India, Argentina, Turkey) wi-fi
is widely available and the iPhones (or even an iPod Touch) can get online
almost anywhere; in other places (especially Japan) there's widespread wired
ethernet but no wi-fi. In these cases, it's handy to use the netbook as a wi-
fi base station, repeating the internet access from ethernet over a private
wi-fi network so the iPhones can see it. (Another use for this technique is
business hotels where they charge per device; if we get the netbook online we
can use the iPhones simultaneously for free.)

To do this using Windows 7's internet connection sharing, you need to do 2
things:

- set up a computer-to-computer network (in "Network and Sharing Center" control panel, go to "Manage Wireless Networks", click Add, then choose "Create an Ad Hoc Network"; after you create this once, it will remain available in the list of available wi-fi networks)

- enable connection sharing (in "Network and Sharing Center" control panel, click "Change adapter settings", get properties for the wired connection (probably called "Local Area Connection"), go to the Sharing tab, and enable "Allow other network users to connect through this computer's internet connection".

Note that you have to turn off internet connection sharing before you can join
any other wireless networks. (If you don't, Windows won't give you any errors
but traffic over the wireless network will just silently not work; this can be
frustrating if you don't know what's going on.)

Also of note:

- internet connection sharing isn't available in Windows 7 Home Basic that came with our netbook; we had to upgrade to Home Premium  
- the wi-fi network that Windows creates isn't perfect; one iPhone is perfectly happy to see it, another loses the DHCP settings every time it goes to sleep, and my Palm Pre can't see it at all. Still, much better than nothing.

