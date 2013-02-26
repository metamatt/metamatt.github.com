---
layout: post
title: ! 'How long can bugs survive in Windows Notepad? '
tags:
- software
- windows
- bugs
---
Damn the Windows Notepad bug that makes the cursor move away from the end of
the document when you add lines and press save.  How many years and they
haven't fixed that?

(I haven't figured out the exact behavior that triggers this, but it's
something like: open a new or existing file, and add a paragraph or so at the
end; leave the cursor at the end of the document; invoke the Save command,
using mouse or keyboard shortcuts, and the cursor will move back a few
characters. The amount it moves seems to be proportional to the amount of text
you've added since the last save; I suspect some confusion over the 2-byte
CRLF ( ) sequence.)

  
This is annoying because if you've trained yourself to press ctrl-s to save
your document every once in a while, and you type, press ctrl-s, then keep
typing, the later burst of typing won't append like you expect it to, it'll be
in the middle of one of the words from the first burst of typing. Kind of like
if your trackpad detects a false click from your palm and moves the cursor,
except Notepad doesn't need a trackpad's help for this.

I've noticed this bug at least since Windows 2000, and each time there's a new
version of Windows I wonder if they'll have noticed and fixed this, but as of
Windows 7 it's still there, and still annoying me.

Also, Notepad tends to add fake hard line breaks at the window width when you
save with word wrap on.  It doesn't really add line break, but it appears to;
after you open a file (with word wrap on and necessary), edit it, save it,
then widen the window, the lines don't rewrap (until you exit and relauch
Notepad).

(Yeah, who really uses Notepad? That's probably why these bugs survive. Still,
it's there and the easiest thing to reach for when you want a text editor; if
they're going to ship it they should fix the bugs!)

