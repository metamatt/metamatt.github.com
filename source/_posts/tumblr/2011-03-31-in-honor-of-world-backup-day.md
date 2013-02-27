---
layout: post
title: In honor of World Backup Day
tags:
- backup
- software
- iusethis
comments: true
---
In honor of [World Backup Day](http://arstechnica.com/gadgets/news/2011/03
/world-backup-day-what-are-you-doing-to-make-sure-youre-covered.ars), here's a
description of my current backup strategy:

My desktop computer backs up to:

  * Time Machine to local drive
  * [CrashPlan](http://www.crashplan.com/) to a separate server in my house which hosts a Promise DS4600 RAID array
  * CrashPlan to a friend's house in another state, where I stashed another Promise NS4300 RAID array

My laptop backs up to CrashPlan to the server in my house, only.

I don't really like Time Machine for local use, had even worse experiences
with it on my LAN (my Mac Pro would frequently kernel panic on resume from
sleep, and it hasn't done that since I moved the TM drive local), and it
doesn't even try to work across the WAN. And TM is slow: even for local use,
it seems like TM is almost always running or "cleaning" even if few files have
changed since the last run -- it will often take > 10 minutes to back up what
it reports as 3MB of data (I haven't used the trick described in the article
above to dial back Time Machine from its default hourly backups, and intend to
try that now).

CrashPlan has a lot of advantages over Time Machine (in addition to working
with computers other than Macs) -- it mostly works across the WAN, across
networks and firewalls, and it doesn't take nearly as long to run.

I don't see the objections to offsite networked backup these days, assuming
you have a decent Internet connection. Several different services have
unlimited storage for $5/month, CrashPlan among them, but CP one-ups the
others by also offering a free option if you host the storage yourself (or a
friend does it for you). As for speeds, I have a 5mbps upstream connection and
was able to back up about 300GB from scratch in about 10 days. The incremental
backups for whatever I change in a day have no trouble running overnight. This
is a DOCSIS 3 cable connection; if you have DSL your upload speeds are
probably 3x to 10x slower and that could be painful; if you're lucky enough to
have fiber your upload speeds are probably 10x faster and this is a no-
brainer; anyway I wasn't wholly expecting 5mbps to be fast enough to make
backups painless but was pleasantly surprised. I look forward to the day when
we can take that level of speed for granted.

