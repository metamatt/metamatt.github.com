---
layout: post
title: Wi-fi password request UI suggestion
tags:
- gadgets
- software
comments: true
---
Say you're at a friend's house, or in a hotel or cafe, and they have a wi-fi
network you haven't used before, and you try to connect, and it's password
protected so you get asked for the password.

If you already know the password, great, you enter it and join the network and
go about your business. Let's say you don't know the password, so you ask your
friend or a clerk or waiter; they give you the answer a minute later, and you
enter it, and your computer fails to join. What happened?

If you wait too long between when the wi-fi network asks for the password and
when you provide it, the join request always fails, tells you an error
occurred, and doesn't ask again.  I think there's a challenge in the initial
association response that expires so a client isn't allowed to take that long
to associate, but your computer could know it's been that long, and
reassociate before using the credential you provide.  Or at least just tell
you you've taken too long and dismiss the auth dialog.  Or at least show a
useful error message and bring back the auth dialog when it fails.  But no, it
just acts like you gave the wrong credentials, and leaves you to figure out
the problem. (OK, even if you don't figure out the underlying problem, the
natural thing is to just try again and that will work, but it's a waste of
human effort.)

(As far as I know, Windows, iOS and Mac OS all act like this.)

