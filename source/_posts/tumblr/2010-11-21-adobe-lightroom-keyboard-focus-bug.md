---
layout: post
title: Adobe Lightroom keyboard focus bug
tags:
- software
- bug
- lightroom
comments: true
---
Lightroom loves to lose keyboard focus when you're typing in iptc fields in
the metadata editor in the right panel, especially on slow netbook -- select a
bunch of images, change one field for all of them, press Tab, keep typing in
the 2nd field, a second or two later it'll decide to commit the first edits
and yank focus away from the text field and then apply the rest of your
keypresses as LR keyboard shortcuts.

I've noticed this bug in LR 2.x and 3.x, and again, it's especially easy to
trigger on a slow Windows netbook.

