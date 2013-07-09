---
layout: post
title: State of the last-mile internet connection, year 2000
tags:
- dsl
- last-mile
- network
- squirrels
comments: true
---
In the fall of 2000, my last year at Stanford, I lived with a group of friends in one of [Rob Levitsky's Dead Houses](http://www.paloaltoonline.com/weekly/morgue/news/1996_Sep_11.DEAD.html). While most of the Dead Houses already had shared DSL connections, this specific house was new to this capacity and didn't. We called up PacBell and asked for a DSL line; they said it would take 3 months.

(Seriously, here we are in residential Palo Alto -- in the heart of Silicon
Valley during the tech boom -- and the fastest last-mile Internet connection
available is 1.5 megabit DSL and even that has a 3 month waiting period.)

One of the friends moving into the new house had previously been living in
another Dead House right across the street, and it turned out that the DSL
line for that house was in his name and attached to his phone number. He
wanted to keep the phone number, and PacBell was happy to move the line to the
new house immediately, but then neither house would have Internet for 3
months.

So, like any self-sufficient group of tech-savvy geeks, we took matters into
our own hands. We strung an Ethernet cable across the street, connecting the
houses (there was enough tree cover that you could barely see the cable). One
cat5 cable has 4 twisted pairs of wire, and the slower variants of Ethernet
only need 2 pairs. So we connected one pair from this cable to the incoming
phone line at the old house, moved the DSL modem across the street to the new
house and connected it to the other end of that pair, then set up a NAT router
at the new house, put an Ethernet plug on 4 of the remaining wires in the long
cable, and used 2 of the remaining pairs to share the NAT router back across
the street so the old house didn't lose Internet access.

The cable crossing the street in the trees was probably illegal, and running
both phone and Ethernet on different pairs in the same cat5 cable is not
exactly encouraged by the Ethernet spec, but it all worked fine.

For about 6 months. Until a squirrel chewed through the cable.

Oh well. It was fun while it lasted. I don't remember what we did after that,
but I think the severe backlog at PacBell had eased and we were able to get
each house its own DSL line relatively quickly.
