---
layout: post
title: "Death by dueling modal dialog"
date: 2013-12-08 23:35
comments: true
categories: 
tags:
- apple
- usability
---
Setting up a new iPad from a backup of a previous one -- which, I think, is the method de rigeur for a few million people in this season -- I noticed a really annoying problem.

When you first turn on the new device, runs a fullscreen setup program that is not the normal iOS user experience starting at the home screen (Springboard). It wants to connect to a Wi-Fi network and then it asks you if you want to set it up as a new device or from a backup (and if the latter, whether to restore from iCloud or iTunes). If you elect to restore from an iCloud backup, it chews away for a few minutes restoring your user account, then reboots, and asks you a few further questions in the fullscreen setup program before jumping to the home screen.

As soon as the setup program exits and Springboard runs, normal background services and apps start launching and doing their thing, plus there's still some first-use setup stuff to take care of, which means that all of the following try to happen simultaneously:

- email accounts try to sync, realize they don't have the server credentials, and ask you for a password (for each of several email accounts)
- iOS wants you to set a device PIN for the unlock screen, and asks you to provide one
- Facebook account tries to sync, realizes it doesn't have the server credentials, and asks you for a password
- if you managed to supply a device PIN without that dialog getting clobbered by one of the other ones, it comes back and wants you to confirm it
- if you managed to supply your Facebook password, Facebook's 2-factor authentication says "that's nice but we just texted you a code which you now need to provide"

All of these happen in modal dialogs that pop to the foreground over the active app... or over one of the other aforementioned modal dialogs. This isn't supposed to happen with modal dialogs. But it does, here, in the default out-of-box experience for pretty much any iOS device where the owner is upgrading from a previous one that was used for anything serious.

In fact, these password dialogs continue to pop up even when you're in the middle of typing in an existing one (and if you manage to fill out and confirm one before another one takes its place, it seems like the previous ones may still be there with your previous partial input, or they may start empty when they reappear). The resultant focus stealing issues are worse than anything I've seen since the late 90s versions of Windows.
