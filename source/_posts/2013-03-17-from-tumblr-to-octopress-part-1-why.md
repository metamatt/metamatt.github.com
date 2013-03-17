---
layout: post
title: "From Tumblr to Octopress, part 1: why"
date: 2013-03-17 01:37
comments: true
categories: 
tags:
- blog
- tumblr
- octopress
---
When I first started this blog, I set it up at Tumblr so I wouldn't have to think about hosting it and could concentrate on writing.

I've since realized that Tumblr is a bad match. Among things that I prioritize higher than Tumblr evidently does, reliability ranks high on the list[^1], as do control over site structure and appearance. Tumblr themes allow some control over appearance — and there are some very nice ones — but not the structure[^2].

Among things that they care about that I do not are their web posting interface, iOS native clients, a plethora of post types designed to be slightly quicker if you want to post audio/picture/video/quote content[^3], and a follower system[^4].

So. On to Octopress. I get a lot more control over site structure, a more usable form of control over visual layout, and I can host it somewhere reliable (github for now, myself if I want to, and I can move hosting providers without having to do any deeper conversion).

[^1]: Reliability problems with Tumblr have been intermittent; sometimes it works fine, sometimes I get "the server returned no content" errors 10 times in a row before I can load a single page.

[^2]: Tumblr's main navigational construct is a list of all posts sorted in descending order by posting date. Individual posts get permalinks, and there's a very slow-loading calendar view which gives some semblance of an overall table of contents, but there's no really usable way to do monthly archives or next/previous links to stitch time back together.

[^3]: All Tumblr posts have a URL, a title, and a body; what goes into the body can include really anything you can embed in a webpage, including audio and video. Presumably in an attempt to move beyond text-heavy blogging, in addition to letting you embed pictures/audio/video in a normal "text" post, Tumblr added these separate post types that special-case the body (the "link" post type makes the title into a navigable link; the "quote" type puts quotes around the body, etc). All of these are less general than the "text" type; they are also poorly represented in the API and, as I've found out, commensurately poorly handled by export tools. I dabbled in the special post types a few times, and am mostly sorry I did.

[^4]: Readers are unlikely to be Tumblr users; that's what RSS is for.
