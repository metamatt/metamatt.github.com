---
layout: post
title: Previewing Markdown files from the terminal
tags:
- software
comments: true
---
I've been wanting a way to preview
[Markdown](http://daringfireball.net/projects/markdown/)-formatted text files
from the terminal, ideally via [less](http://www.greenwoodsoftware.com/less/).
Primarily, I think, because Github encourages it, a lot of open source
projects are starting to include a
[README.md](https://www.google.com/search?q=+readme.md) instead of a plain old
[README](http://en.wikipedia.org/wiki/README)[^1],[^2]; these marked-down READMEs are
easy to view in Github's web interface but not after (or before) you clone the
repo into your own filesystem.

There's `zless` that can understand compressed files; why not `mdless` that
can understand Markdown files?

I went looking and stackoverflow came to the rescue with this question and
answer about a [less-style markdown viewer for UNIX
systems](http://stackoverflow.com/a/7603703/275581), suggesting
[pandoc](http://johnmacfarlane.net/pandoc/) as the tool to translate from
Markdown format to troff format. The suggested incantation there works for me
under Debian Linux but not under Mac OS X because it relies on `man`'s `-l`
option, which I'm guessing is a GNU addition not supported by BSD `man`. I had
to figure out how to duplicate the processing that `man -l` does, which I knew
involved `troff` (or `groff`); it turns out that `groff` understands a `-man`
flag which predefines the macros used by manpages. The version using `groff`
instead of `man -l` seems more portable (it works fine under Linux as well as
Mac OS X), so that's what I'll use.

Hence, the following incantation to view a README.md file:

`pandoc -s -f markdown -t man README.md | groff -T utf8 -man | less`

Or, a `mdless` command implemented as a tcsh alias:

`alias mdless "pandoc -s -f markdown -t man \!* | groff -T utf8 -man | less"`

[^1]: As one data point for when this became common, README.md was added to the short list of common readme file names in this Wikipedia article on [March 7, 2012](http://en.wikipedia.org/w/index.php?title=README&oldid=480712255).

[^2]: Not to be confused with [REAMDE](http://www.amazon.com/gp/product/0062191497/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=metamatt-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0062191497).
