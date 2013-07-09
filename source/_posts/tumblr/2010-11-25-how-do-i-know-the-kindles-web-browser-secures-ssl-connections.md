---
layout: post
title: How do I know the Kindle's web browser secures SSL connections?
tags:
- amazon
- kindle
- web
- security
- ssl
comments: true
---
It's possible to [hijack an SSL connection that's forwarded through a network you control](http://www.thoughtcrime.org/software/sslstrip/), if the user and
browser combination aren't extra vigilant to verify they ended up at the
requested domain. (Actually, sslstrip can generally hijack traffic on adjacent
networks by pretending to be the router, but it's even easier and more
reliable if it runs on the router.)

This hijacking is possible even using best-available off-the-shelf browsers.
If you control the browser, of course it's even easier to hijack SSL; you just
fake the padlock icon and send the traffic wherever you want.

I'm not saying Amazon does anything like this with the Kindle, but I am
curious how to verify that SSL traffic originating in the Kindle browser is
actually secure end-to-end like SSL is supposed to be.

I got curious about this and used my Kindle's 3G connection to retrieve some
pages from an HTTPS server I control, and looked at the access log to see
where the access came from.

Using the Kindle 3G connection (from Argentina!), the requesting IP address
was 8.18.145.245, which back-resolves as kindle-user.whispernet.com according
to nslookup. (That name doesn't forward-resolve to anything, which is
suspicious network management on Amazon's part.) Running a traceroute to this
address shows packets entering Amazon's network and doesn't show details past
that.

Setting the Kindle to use Wi-Fi instead of 3G and then requesting the page
again, the requesting IP address was 190.55.119.242, which back-resolves as
cpe-190-55-119-242.telecentro-reversos.com.ar -- clearly in Argentina.

As another comparison point: Using my cell phone on 3G, with Wi-Fi disabled,
to request the same page yielded an access from IP address 170.51.255.253,
which doesn't have a reverse DNS entry; traceroute shows this address as
clearly in Argentina, however. (The cell phone was on Claro's network; I don't
know what 3G network the Kindle was using, and it's not necessarily the same.)

What this means is that not only does Amazon control the Kindle hardware and
software, but for 3G (Whispernet) connections, they apparently route all the
traffic through Amazon's network and datacenter. It's probably cheaper for
them to negotiate bulk data contracts with a bunch of 3G networks that way,
but it would make me feel better if I saw a direct route from where I'm
sitting to where I'm going, like I do with the cell phone.

(Note 1: this is all moot since again, if you control the browsing software
and hardware as Amazon does, there are easier ways to cheat, and I do trust
Amazon not to do any of this cheating.)

(Note 2: proxying all wireless traffic, regardless of where your device is,
through the home datacenter is also essentially how all Blackberry network
access works, and also how Opera Mini works, right?)
