---
layout: post
title: OS X has a builtin Wi-Fi network scanner
tags:
- apple
---
Here's a bonus on top of a bonus: OS X 10.8 (Mountain Lion) adds a really
useful "Wi-Fi" scan feature, buried inside a utility I didn't know existed.

I wanted a Wi-Fi scan tool to show me a list of nearby wireless networks and
strengths, so I could avoid interference from existing networks when placing
and choosing a channel for a new access point, and verify the new access point
is operating properly. A few years ago I did this with KisMAC, MacStumbler or
iStumbler, but these utilities seem to have stopped working over time, either
as a result of newer hardware or newer OSes.

Googling for new alternatives to these utilities, I found that [Mountain Lion
actually has this functionality built in](http://osxdaily.com/2012/07/31/wi-
fi-scanner-mac-os-x-mountain-lion/). There's a "Wi-Fi Diagnostics" app buried
in /System/Library/CoreServices (where, annoyingly, Spotlight can't find it
and the Finder by default won't show it); at launch it presents a very
limited-looking wizard interface, but in the menubar the File:New command and
command-N keyboard shortcut have been replaced by an unassuming "Network
Utilities" command.

This brings up a "Network Utilities" window, not to be confused with
/Applications/Utilities/Network Utility.app, with a bunch of really useful
utilities (which look like a strict superset of the old Network Utility, have
a more modern UI and additional functionality, and except for the "Wi-Fi Scan"
tab, have no reason to be restricted to Wi-Fi networks).

I only wish this thing were easier to find; it should probably replace the old
Network Utility app. I don't remember seeing it mentioned in most what's-new-
and-why-to-upgrade articles about Mountain Lion. For me, it's a pretty nice
bonus to having upgraded and deserves wider mention.

