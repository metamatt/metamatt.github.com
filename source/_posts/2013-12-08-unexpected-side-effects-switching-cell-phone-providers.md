---
layout: post
title: "Unexpected side effects switching cell phone providers"
date: 2013-12-08 22:14
comments: true
categories: 
tags:
- wireless
- cell
- messaging
---
I wanted to note that when switching cell phone providers, one source of trouble I had not expected was the non-portable email address associated with my phone number for email-to-SMS forwarding.

Sprint has an email-to-SMS gateway that forwards messages sent to yournumber@messaging.sprintpcs.com. Verizon does the same thing using yournumber@vtext.com.

I was using this mechanism for a smattering of services that know how to send notifications by email but either don't know how or charge extra for sending SMSes:

* [Pingdom](https://www.pingdom.com/) web service monitoring
* [Eyez-on Envisalink](http://www.eyezon.com/?page_id=176) alarm monitoring
* [Custom software I wrote](https://github.com/metamatt/stargate) that generates more interesting alerts from the alarm system data (like, it messages me if I leave the garage door open)

All of these alerts stopped happening when I switched providers, and I only noticed when I realized I wasn't getting the alerts any more. Then I had to go back and try to remember everywhere I'd used that messaging.sprintpcs.com address (hint: this took a couple iterations).

A different case that ended up working out the same way is [Twitter's SMS integration](https://support.twitter.com/articles/14014-twitter-via-sms-faqs). Here, they have real support for SMS (not cheaping out and using a per-carrier email forwarding gateway). But it still broke, with the same symptoms, when I switched carriers: over time, I realized I was no longer getting SMS notifications I used to get. I don't know how Twitter's SMS integration is implemented, and whether they do it themselves or use some service like Twilio; unlike a lot of sites I've seen that ask you for a phone number to SMS, they just ask for a phone number and not which carrier. Anyway, it broke and there was no obvious setting to change to fix it; I ended up deleting my phone number and re-adding it and that fixed things.
