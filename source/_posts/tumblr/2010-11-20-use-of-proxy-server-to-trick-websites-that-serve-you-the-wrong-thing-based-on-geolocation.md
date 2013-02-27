---
layout: post
title: Use of proxy server to trick websites that serve you the wrong thing based
  on geolocation
tags:
- web
comments: true
---
There are a few US-centric websites that I want to use while traveling, which
work suboptimally from outside the US.

Obvious examples are Netflix (watch instantly) and Rhapsody, which probably
have license agreements restricting their use to inside the US. If you try to
browse these sites from a non-US IP address, they'll just tell you to go away.

A less obvious example is PayPal; they work from outside the US but tend to
paranoia about dirty foreign hackers stealing access to your account. At
least, when I logged into my own account from Turkey, I found it locked into
"limited" mode, and after I jumped through the hoops to prove I was the real
owner and get the limitations removed, then went to Argentina, I immediately
found the account limited again the first time I logged in. All in all, it
seems easiest to let PayPal think I'm always in the US.

I understand why these sites have these behaviors based on location, but it's
not what I want for me -- I'm paying the same fees for the use of these sites
regardless of where I am; it seems silly to enforce artificial geographic
boundaries on the Internet.

So, I run an http proxy (tinyproxy) on a computer I control in the US, and
when I'm out of the US, I proxy use of these sites through that computer.

In practice there are a couple steps to this:

1) install tinyproxy somewhere

2) lock it down so only you can use it; you don't want random people using it
(you might be paying for bandwidth, it might slow down your connection, and if
Netflix/Rhapsody/PayPal see too much traffic from it they might figure out
what you're up to and block it). You could try to lock it down by IP but if
you're traveling your IP address will change all the time; you could try to
set up authentication but I haven't bothered to look what authentication
mechanisms are available to both tinyproxy and the browsers I care about and
whether they're secure. Instead, I already have an all-purpose authentication
mechanism I like, openssh -- so I set up an ssh tunnel with a local port
forwarded to the proxy port, and I just set tinyproxy to accept connections
only from localhost.

3) set your browser to use the proxy. Since proxied browsing relies on me
starting the ssh tunnel, might be slightly slower, and in some cases I do want
sites to be able to correctly geolocate me, I don't want this to be the
default. I could turn the proxy on and off depending on what I'm browsing, but
that's a pain. Instead, since I have multiple browsers installed, I just leave
one set without a proxy for normal use, and another one configured with the
proxy for the sites that need it. (I wonder if there are extensions for Chrome
or Firefox that allow you to configure per-site proxies?)

