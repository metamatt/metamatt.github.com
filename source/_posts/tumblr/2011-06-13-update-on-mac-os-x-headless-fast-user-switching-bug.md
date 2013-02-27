---
layout: post
title: Update on Mac OS X headless Fast User Switching bug
tags:
- apple
- bugs
- mac os x
comments: true
---
I [complained](http://blog.metamatt.com/blog/2011/02/15/mac-os-x-bugs-apples-
never-gonna-fix/) that Fast User Switching over a Screen Sharing connection is
a bag of hurt, and that it seems like something Apple's never going to fix (#4
on the list at that link).

(Fingers crossed), maybe I was wrong: the [what's-new page for
Lion](http://www.apple.com/macosx/whats-new/features.html#screensharing)*
advertises per-user screen sharing, which sounds more like the Microsoft
Windows Terminal Server approach: a combination of fast user switching and
remote access, so that multiple sessions can be active simultaneously, and
remote sessions aren't onscreen on the local console.

I can only hope that this new feature will make the old bug go away; I have a
hard time imagining how they'd implement detached remote sessions that still
result in the buggy behavior I described. Though, from the bug I described and
earlier incarnations that seemed related, it seems that headless isn't a
primary/supported use case in Apple's eyes.

Here's hoping it gets better.

*: I wonder how long that URL will last; probably until the next major version is announced, since there's no versioning in the URL. I hate linking to links that are going to break, but I don't know of a stable equivalent.

