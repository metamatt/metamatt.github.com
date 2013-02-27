---
layout: post
title: Mac OS X bugs Apple's never gonna fix
tags:
- apple
- mac os x
- bugs
comments: true
---
Mostly the OS X user experience is really good and getting better, and Apple's
famous for fit and finish and general polish and avoiding dreary annoyances
that other platforms make users put up with.

That said, here are a couple problems which I experience sporadically, and
have been seeing for years, and at this point don't really expect to ever see
fixed:

  1. Sleep Mac, do something else, later wake it up. Usually this works great (Mac OS on Apple hardware has by far the fastest and most reliable suspend/resume code of any general-purpose OS I've ever used). However, on resume sometimes I'll be unable to dismiss the screen saver after entering my password. The OS itself is healthy at most levels (compare with Windows which used to frequently BSOD on suspend/resume, or Linux which seems to like to resume most of the hardware but leave the graphics hardware in a useless state): processes are running, input devices work, the rendering stack works. It's just that there's this all-black topmost window which won't go away. I can ssh in and use the Mac like any other Unix machine, but that's small comfort. Reproducible: randomly, occasionally. Fix: reboot.
  2. Leave Mail.app running on two different Macs connected to the same IMAP account served by courier-imap. Sleep one Mac, use the other, wake first the first one, return to Mail.app, and it it won't see changes that happened (new messages that arrived, old messages moved to another folder, etc.) while it was asleep. This bug showed up in Snow Leopard and persists in 10.6.7. Reproducible: always. Fix: quit/relaunch mail.
  3. My desktop background sometimes disappears (and is replaced by the configured background color instead of the configured background image). Reproducible: randomly, frequently. Fix: launch "Desktop & Screen Saver" prefpane and toggle any setting.
  4. Log into headless Mac mini via Screen Sharing.app (VNC), try to use Fast User Switching to switch to another user account. Display stack gets completely screwed up; I can still ssh into the Mac and use terminal-based processes, but can't use the GUI either remotely via VNC or locally if I attach a screen. Reproducible: always. Fix: reboot.

I've reported most of these to Apple, to see them either languish for years or
get resolved as a dupe of some older bug that's been languishing for even more
years. Oh well.

