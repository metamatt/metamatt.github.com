---
layout: post
title: "From Tumblr to Octopress, part 2: how"
date: 2013-03-17 01:40
comments: true
categories: 
tags:
- blog
- tumblr
- octopress
- jekyll
---
Having decided to move this blog from Tumblr to Octopress, there remained the matter of migrating it[^1].

Octopress is basically a convenience framework around Jekyll, adding a nice-by-default theme and some convenience wrappers for starting new posts, invoking Jekyll to generate the site, and deploying the site. You could probably use Octopress quite happily without touching Jekyll directly, unless you want to import an existing blog; then you end up at [Jekyll's Blog Migrations tool](https://github.com/mojombo/jekyll/wiki/blog-migrations), which has options for a number of popular blog engines, including Tumblr.

The instructions for [setting up Octopress](http://octopress.org/docs/setup/) are pretty simple and [well documented](http://octopress.org/docs/setup/):
* git and ruby (and probably rvm or rbenv) are prerequisites
* obtain octopress itself via "git clone"
* install dependencies via "gem install bundler; bundle install"
* install the default Octopress theme (which also generates the skeleton site layout) via "rake install"

At this point, you've got a working Octopress installation and you could use its rake task-based interface to write and publish posts. However, if you want to migrate an existing blog, you have more setup steps which are also [well documented](https://github.com/mojombo/jekyll/wiki/blog-migrations):
* assuming you want to keep your raw posts in markdown format instead of raw HTML, Jekyll's Tumblr migrator needs nokogiri: ```gem install nokogiri```
* invoke the Tumblr migrator (```ruby -rubygems -e 'require "jekyll/migrators/tumblr"; Jekyll::Tumblr.process("http://www.your_blog_url.com", "md")'```). Note that this doesn't require any account information or credentials, because the Tumblr API will provide enough information to do this anonymously. Heck, if you're evil, you could convert someone else's blog (don't do that). On the topic of Tumblr reliability, I ran this step a few dozen times while I was figuring out how it works and fixing some bugs in tumblr.rb, and ~90% of the time, it downloaded my ~165 posts almost instantly, but palpably often, it would get stuck halfway as the Tumblr API stopped sending it network traffic. Oh well. Ctrl-C and restart if this happens to you.

What neither the Jekyll nor Octopress documentation tells you is what happens next. Assuming you run all the above commands from the octopress directory: Octopress setup (the ```rake install``` step) created a directory called "source", under which the (initially empty) "\_posts" directory is where Jekyll will look for posts. Meanwhile, Jekyll's tumblr.rb will create and populate a "_\posts/tumblr" directory with your posts, and a "posts" directory with redirects from the old Tumblr-style post URLs to new Octopress-style URLs[^2],[^3]. Neither the "_\posts" nor "posts" directory spit out by tumblr.rb are under "source" where Jekyll will look for them. What this means is that without additional effort on your part, Jekyll as invoked by Octopress won't see the files you just imported.

Again: your blog posts go in "octopress/source/_posts". The Tumblr migrator will create "octopress/posts" and "octopress/_posts". Just move these two directories under "octopress/source" once you've verified they look OK. (NB: the migrator actually dumped all its files under "octopress/_posts/tumblr"; it's fine to leave them there, so they end up in "octopress/source/_posts/tumblr"; Octopress doesn't seem to care about the organization of your files inside the source/_posts directory.)

Now, you can tell Octopress to generate the site: "rake generate".

If you're reading this at the right point of relative stability, lucky you; you win. I ran into several more issues, due to the fact that Jekyll and Octopress are prerelease open source software intended for an audience of hackers; some assembly definitely required:

* At the point I was performing this migration (January 2013), Jekyll was at version 0.12 and the tumblr.rb migrator script was broken in a [couple](https://github.com/mojombo/jekyll/commit/863643c7e8080c73a7968caabfc9c7e9b18c6b95) [respects](https://github.com/mojombo/jekyll/commit/fbc9d0c66397234ab85e03a55955602e0ce40356) which I submitted patches for.
* After my patches were merged upstream, I tried running with Jekyll's head version in mid-February, to find that tumblr.rb had been deleted from the Jekyll repository entirely, and moved to a separate [jekyll-import](https://github.com/jekyll/jekyll-import) project, which at the time had no documentation and appeared to have little chance of running.
* Meanwhile, using any version of Jekyll newer than 0.12 broke Octopress in a trivial way; the :generate rule in Octopress's Rakefile finishes by invoking Jekyll as ```system 'jekyll'```, with no arguments, and newer versions of Jekyll expect a ```build``` argument. Octopress will fix this when Jekyll actually releases a new version (which may have already happened between me finding this and posting this); it makes no sense to fix it sooner.

This last list of foibles is probably all related to Jekyll being in the throes of the 1.0 release process and will probably be a historical footnote afterwards.

[^1]: Many others have done this before; one post I found helpful was [Goodbye Tumblr. Hello, Octopress Powered by Jekyll and Markdown!](http://blog.assimov.net/blog/2012/03/24/tumblr-to-octopress-powered-by-jekyll-and-markdown/).

[^2]: The redirects spit out by tumblr.rb are under "posts" because Tumblr URLs are of the form example.com/posts/12341234/post-title-slug; Octopress URLs are by default of the form example.com/blog/year/month/post-title-slug; tumblr.rb creates redirects from the former to the latter, without requiring any special interaction with the webserver, by just creating a file for each post, named for the Tumblr relative URL (in this case, posts/12341234/post-title-slug/index.html) containing a browser-side meta refresh redirect to the new URL.

[^3]: I found the redirects created by tumblr.rb to be not quite enough. Tumblr indexes posts by number, then creates a nice search-engine-friendly SLUG such as post-title-slug, yielding a post URL like example.com/posts/12341234/post-title-slug. But actually, when receiving a request, Tumblr ignores everything after the number, and you could also load that post as example.com/posts/12341234/foobar, or just example.com/posts/12341234, and in fact the latter is the canonical URL used by Disqus. If you are running a webserver with rewrite rules, you might do well to redirect the entire URL namespace under posts/12341234 to the new URL, as Tumblr would have; I settled for copying posts/12341234/post-title-slug/index.html to posts/12341234/index.html for each post, so both number alone and number+SLUG will redirect correctly.
