---
layout: post
title: "From Tumblr to Octopress, part 3: footnotes"
date: 2013-03-17 01:42
comments: true
categories: 
tags:
- jekyll
- octopress
---
Once I got Jekyll and Octopress to import my blog from Tumblr and generate it in its new format, almost everything was formatted correctly, with the marked exception of footnotes. Like a certain furious Canadian[^1], I've become a fan of footnotes for adding detail without littering my posts with parenthetical expressions. In the migrated posts, the footnotes were there at the bottom, but the links to them were all wrong — full-sized unlinked numbers, instead of superscripted hyperlinks.

It took me a while to figure out what was wrong because there were actually 3 distinct problems. And as background, while it wasn't a direct problem here, you should understand that footnotes are not a feature of the [original Markdown syntax](http://daringfireball.net/projects/markdown/syntax), but were added later by other dialects, mostly converging around [PHP Markdown Extra](http://michelf.ca/projects/php-markdown/extra/#footnotes), which is what Tumblr uses.

First: The post content generated in Markdown format from tumblr.rb, in its trip through nokogiri and html2text and maybe elsewhere, didn't actually preserve the footnote declarations I'd originally given Tumblr. Even though I had written these posts in Markdown format, and the Markdown form of my posts is presumably preserved somewhere at Tumblr[^2], tumblr.rb instead downloads HTML and then reverse-converts it back to Markdown format. This conversion doesn't preserve footnotes as Markdown footnotes; instead it leaves them as static HTML, and it renders the footnote bodies reasonably but the footnote links unreasonably.

So I had to go edit all the posts in which I used footnotes, and manually redo the footnote links using PHP Markdown Extra syntax.

Second: Having done that and told Jekyll to regenerate the blog, I found myself looking at a bunch of raw unconverted PHP Markdown Extra footnote tags. That's because Jekyll's markdown processing is done by RDiscount, and the version of RDiscount specified by Octopress's Gemfile (1.6.8) does not support footnotes at all; footnotes using PHP Markdown Extra syntax were added as a feature of RDiscount 2.0.7.

So I had to edit the Gemfile to specify RDiscount 2.0.7.

Third: Having done that and told Jekyll to regenerate the blog, some posts looked fine, but others had chunks of footnote definition content floating near the end of the post body but before the footnotes, and completely out of order. Some trial and error led me to deduce that RDiscount 2.0.7 does not actually honor the documented PHP Markdown Extra syntax, which allows you to hard-wrap the footnotes or even place the definition offset from the footnote number[^3]; RDiscount is happy only if the footnote number and entire body are on one logical line with no hard line breaks. Since I'm doing all this posting from a colocated Linux VM on which I don't run X, and thus use text editors in old-school terminal windows, I tend to hard-break my posts (and in fact, the posts I imported from Tumblr tended to be hard-wrapped at 76 columns by something somewhere along the write/post/import pipeline). RDiscount doesn't play well with these hard breaks.

So I had to edit all the footnoted posts again to comply with RDiscount's actual behavior.

Summary: you can get nice footnotes from Octopress/Jekyll if you

* Update to RDiscount 2.0.7
* Use the footnote syntax that RDiscount actually supports, which is like PHP Markdown Extra except each footnote definition must stay on one line without hard line breaks
* If importing your blog from a previous home using a script like tumblr.rb, verify that the conversion actually generates footnote markup

There's still one more bug with footnotes on the index page, which is that Jekyll generates each page independently through RDiscount, which generates in-page links between the footnotes and their bodies, using the footnote number: for the first footnote, the forward link is ```#fn:1``` and the backward link is ```#fnref:1```. This works fine on individual pages, but on the index page the footnote numbers get reused and collide, so the in-page links don't work there. Syeong Gan has a post with [a deeper description of this problem, and a possible workaround](http://syeong.jcsg.com/2012/07/07/octopress-footnote-problem/).

[^1]: [Footnotes, Footnotify and Octopress](http://canadian-fury.com/2012/04/26/footnotify-and-octopress/) has a pretty good argument in favor of footnotes, as well as a point-in-time description of how to get them to work in Octopress which I think is now outdated: he suggests switching from RDiscount to Kramdown; as mentioned above, RDiscount 2.0.7 added footnote support which mostly works. I tried Kramdown anyway and found RDiscount to do a slightly less bad job of honoring PHP Markdown Extra syntax than Kramdown does.

[^2]: MarsEdit can edit posts already posted at Tumblr, even if not originally authored with MarsEdit, in their original format: if the post was written in Markdown, MarsEdit's edit view sees Markdown. This might imply that there's a better way for Jekyll's tumblr.rb to use the Tumblr API to get the Markdown source, instead of the reverse-conversion it currently does.

[^3]: See the PHP Markdown Extra [documentation on footnotes](http://michelf.ca/projects/php-markdown/extra/#footnotes), notably the part starting with "Footnotes can contain block-level elements".
