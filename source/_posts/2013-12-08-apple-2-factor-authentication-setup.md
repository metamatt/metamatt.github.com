---
layout: post
title: "2-factor authentication setup for AppleID"
date: 2013-12-08 23:16
comments: true
categories: 
tags:
- apple
- usability
---
As part of setting up my new iPad, I got tired of telling Apple I didn't want to add weak security questions to allow me (or would-be hackers) to reset my password, and decided to set up 2-factor authentication (which is a good idea in any case).

This should be pretty straightforward -- and it is, at other sites where I've set this up (Google, Facebook, Twitter). Apple's setup process was a lot more complicated. Judging from the questions and admonishments during this setup process, Apple is a lot more worried than these others about people losing access to the "thing you have" and locking themselves out of their accounts. Which is a legitimate concern, but I think they can make the UI around this process a lot better.

The first place this went awry is the list of devices where they can deliver authentication codes. The AppleID website shows a list of known iOS devices (those enrolled in "Find my iPhone"), and allows you to select any/all of these, plus optionally one or more SMS-enabled phone numbers, to receive login verification codes. The problem is, all of these devices were listed as "offline", even though at least 3 of them were actually online. I spent some time trying to figure out which parts of the description was clickable (spoiler: none, though there is one part that triggers an inaccurate explanatory popup if you mouse over it and hold still) before I eventually discovered a Refresh button at the very bottom of the list (far enough down I had to scroll to see it).

So beef #1: this page always loads stale information, and doesn't show you correct information until you click a Refresh button that's initially offscreen.

After selecting a couple notification methods here (which involves additional careful confirmation to make sure they actually work) and clicking Next, Apple showed me a "recovery key" with instructions to write it down or print it, but not to store it on any computer (and to enforce that, they make it impossible to copy it to the clipboard). OK guys, I get what you're saying about the whole point being not exposing my keys to hackers, but if I write it on paper I'm going to lose it. Plus the computer I'm on doesn't have a printer. I'm going to store this on my computer, thanks; I'll just encrypt it. So I pull out my iPhone and open an encrypted note-taking program and type in this long alphanumeric code and check it carefully to make sure I transcribed it correctly. Then back to the computer and I click Next and it starts to ask me to retype the code, when suddenly... Session Timeout! Back to the very beginning. Time to start over (and this has taken about 10 minutes so far[^1]).

So beef #2: aggressively short[^2] session timeouts are user-hostile, plus why not give me a chance to confirm I'm still there before just kicking me out of the session, plus the website was willing to let me sit there at the first "recovery key" page indefinitely long, and let me keep doing the work to copy down the useless recovery key[^3], and only when I click Next does it tell me the session had already expired.

This whole process would work a lot better if the 2 pages in question would dynamically update. AJAX in 2006 was pretty hot stuff. In late 2013, it's table stakes.

[^1]: OK, it won't take me 10 minutes the second time, now that I know what I'm doing, notably with respect to the magic refresh button. But still, there was a lot of clicking done so far and a lot of clicking to repeat, and it's pretty annoying.

[^2]: The session timeout wasn't actually so short that I couldn't transcribe the recovery key, annoying as it is to type arbitrary hyphenated alphanumeric strings into the iOS keyboard. What actually happened was the AppleID website was slow and the page load between the "configure devices" and "recovery key" page took long enough I went to go do something else for a few minutes, then came back to the "recovery key" page, at which point the session had probably already expired before I even started dealing with transcribing the key.

[^3]: Useless, because the second time through, the randomly generated recovery key was of course different.
