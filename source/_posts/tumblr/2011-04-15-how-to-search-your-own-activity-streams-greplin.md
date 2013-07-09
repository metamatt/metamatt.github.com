---
layout: post
title: How to search your own activity streams? greplin!
tags:
- facebook
- greplin
- lifestream
- software
comments: true
---
I recently wrote a post, [On searching one's own activity streams](http://blog.metamatt.com/blog/2011/04/13/on-searching-ones-own-activity-streams/), lamenting the difficulty of finding stuff I myself had
posted on Facebook and Twitter. In response to that post, a friend pointed
out: "You may be looking for [Greplin](https://www.greplin.com/)".

Intrigued, I gave Greplin a try, and overall I'm impressed. It's a new service
that indexes data you create, on other sites and services like Facebook,
Twitter, Gmail and associated Google services like Calendar, and Evernote.
(Note that most of these involve indexing data that's not publicly available,
so Greplin needs access to your account data -- it uses OAuth to request this
access without needing to know your password.)

This goes well beyond what I was asking for in the stream-search post, and
actually nicely answers something else I'd been wanting recently, and overall
I'm impressed (and slightly jealous I didn't get to it first).

But, back to the specific "find my own Facebook" posts case that led me to
Greplin in the first place: I tried searching for a few of my own posts, and
it didn't find them. It seems pretty good about finding tweets, mail messages,
appointments, and pretty much everything else it's supposed to including
Facebook messages, but not Facebook wall posts. I went looking for answers in
Greplin's help system. From the ["which sites does Greplin index" article in their FAQ](http://help.greplin.com/customer/portal/articles/4766-which-sites-does-greplin-index-):

> Please note that for news feed and wall posts, Facebook only allows us to
collect data from a few days before you began your index on Greplin. However,
we will collect all your data from that point forward. This means that you may
not find Facebook news feed or wall post items that were created up to 4 days
prior to your initial signup for Greplin.

Ouch. I don't know whether that's a policy or technical limitation. I don't
believe it's a technical limitation, because I wrote my own little Python
script to download my own status messages since the beginning of time, and
comments on those status messages, and they're all available via the API.

That seems to leave policy as the limitation. I sure hope that Facebook isn't
preventing 3rd party sites, with my permission, from looking at my own data. I
can't see any consistency in letting Greplin access my very recent posts and
my future posts but not my past posts. Especially because if they're not
allowed to index old content, and they want to index content going forward
(and the ability to rebuild the index as necessary), that pretty much requires
them to keep a separate copy of my data, whereas if they had reasonable access
to past data, they could rely on Facebook to store it and provide it as
necessary and they would need only the index on their side.
