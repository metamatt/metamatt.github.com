---
layout: post
title: Amusing traceroutes from Argentina
tags:
- web
---
This is traceroute output from a server in a datacenter in Fremont, California
to the IP address of the DSL connection in the apartment I'm staying in in
Buenos Aires:

skynet:~>traceroute 190.55.119.242

traceroute to 190.55.119.242 (190.55.119.242), 30 hops max, 40 byte packets

1 64.62.173.1 (64.62.173.1) 0.399 ms 0.302 ms 2.316 ms

2 gige-g3-15.core1.fmt1.he.net (64.62.244.109) 2.687 ms 3.670 ms 3.597 ms

3 10gigabitethernet1-2.core1.sjc2.he.net (72.52.92.110) 4.046 ms 4.094 ms
4.135 ms

4 Port-channel100.ar3.SJC2.gblx.net (64.214.174.245) 13.111 ms 13.034 ms
12.961 ms

5 INTERNATIONAL-SATELLITE-COMM.gigabitethernet2-5.ar3.EZE1.gblx.net
(208.48.250.82) 195.896 ms 195.824 ms 195.702 ms

6 * * *

7 * * *

8 * * *

9 * * *

10 * * *

Hop 5 is the interesting one. (That lands in Buenos Aires, by the name;
packets after that aren't getting a response.) So Global Crossing is routing
this over a satellite connection with ~200ms of latency?

The same trace in the other direction, from Buenos Aires to Fremont:

C:\Users\magi>tracert skynet.timespace.net

Tracing route to skynet.timespace.net [64.62.173.33]

over a maximum of 30 hops:

1 3 ms 1 ms 1 ms 192.168.1.1

2 * * * Request timed out.

3 10 ms 10 ms 10 ms cpe-200-115-195-85.telecentro-reversos.com.ar
[200.115.195.85]

4 * 32 ms 33 ms te4-4.baires3.bai.seabone.net [195.22.220.33]

5 161 ms 162 ms 162 ms te4-4.ashburn2.ash.seabone.net [89.221.40.7]

6 * * * Request timed out.

7 207 ms 213 ms 207 ms 10gigabitethernet1-4.core1.pao1.he.net [72.52.92.29]

8 213 ms 221 ms 223 ms 10gigabitethernet1-2.core1.fmt1.he.net [66.160.158.241]

9 206 ms 207 ms 207 ms lafrance-internet-
services.gigabitethernet3-15.core1.fmt1.he.net [66.220.10.126]

10 207 ms 207 ms 222 ms 64.62.173.33

That's a little better; the long hop is over
[seabone.net](http://www.seabone.net/), "the international backbone of Telecom
Italia"; hopefully a higher-capacity land link but still slow.

No wonder net access from Argentina to US sites has seemed uniformly slow.

