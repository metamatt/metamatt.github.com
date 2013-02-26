---
layout: post
title: Don't override keys that already have a meaning in your scope
tags:
- mac os x
- software
- adobe
---
Two keyboard shortcuts I use very frequently under Mac OS X are:

  * Command-H: hide the current application
  * Command-L: jump to the browser address bar (this isn't a systemwide shortcut, but it's the same for Safari, Chrome and Firefox, so it may as well be).

These, along with Command-Tab to switch between applications, and Command-
curly brace to switch between tabs of the current application, are basically
how I navigate the system from the keyboard, and I get very annoyed when
something interferes with them and they don't work as intended.

(A special note on Command-H, for hide: I've never liked the OS X minimize
behavior. You just get a pile of tiny icons at the end of the dock, in
addition to the app icon at the beginning of the dock. For a plethora of
reasons intertwined with the dock/taskbar/task switching behavior, minimized
windows are more useful under Windows and Linux than they are under Mac OS X.
Now, you do want a "get out of my face until I need you again" action, and
under Windows and Linux minimize is that action, but under OS X minimize is
not that action. Hide is that action.)

Since Command-H is bound to an important systemwide command, no apps should
override it, at least by default. It should be available for app use in
special cases (remote control or virtual machine environment where you may
need access to every possible key and there's a predefined bypass mechanism;
kiosk apps that are designed not to be hidden), but if apps get a way to turn
this into an arms race, I wish the system gave me a way to escalate by
removing that ability from naughty ones (Adobe CreativeSuite apps are the ones
I remember being frustrating in this regard).

Likewise, for sites and plugins that are designed to be hosted inside a web
browser, you do realize that that browser already has dibs on certain
keystrokes, right? Again it's Adobe that breaks conventions -- Flash applets
in particular often like to hook all keystrokes, including those with meaning
to the browser like Command-L to jump to the address bar, Command-T to open a
new tab, and Command-} to go to to the next tab. Again, I'm glad this is
technically possible for those few special cases where the applet knows best,
but I can't see a good argument for acting this way by default, and again I
wish the outer scope (in this case the browser) provided me a big hammer to
say "always interpret your own keyboard shortcuts first".

This is especially annoying because not only is behavior that I depend on and
have committed to muscle memory getting blocked, but it's not even for any
good reason -- the feature that Illustrator CS3 bound to Command-H wasn't
anything I ever used (at least it let me unmap the keyboard shortcut and
return it to the OS). And most Flash applets that steal Command-L don't do
anything at all when I press it (nor is there, to the best of my knowledge, a
way to tell them to stop hooking keystrokes I care about, at either the Flash
Player or browser level -- it's up to the applet).

