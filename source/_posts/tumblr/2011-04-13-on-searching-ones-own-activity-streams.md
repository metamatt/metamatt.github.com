---
layout: post
title: On searching one's own activity streams
tags:
- software
- lifestream
- search
- facebook
- twitter
- chrome
---
One of the potential upsides to posting stuff on Twitter or Facebook ought to
be that you can find it later when you want to know what you were
doing/thinking/saying at a given time.

Too bad neither site has a good way of searching your own contributions.

Twitter does have a search feature and you can restrict it to your own tweets
by adding your username but it only returns very recent tweets (like maybe the
last week); Twitter is also indexed by the major web search engines and if you
add "site:twitter.com username" to your queries you may or may not find what
you're looking for with minimal additional cruft; there's also [Snap
Bird](http://snapbird.org/) which is a 3rd party site designed to do this but
it's clunky and I've never seen it actually work (maybe the fault of Twitter's
API, who knows).

Facebook does have a search feature but it inexplicably doesn't search your
own updates (it finds people and pages and if you click the "See more results
for…" link then a tantalizing "posts from friends" link appears which doesn't
seem to find content in posts by me or my friends); Facebook is a walled
garden and its content is generally not indexable by external search engines;
it does have a pretty good API and so somebody could probably go build this as
a 3rd party app but I'm not aware of one, and arguably it would be better done
as part of the core site anyway.

So, on those occasions I do want to go track down one of my own updates on
either of these sites, I resort to viewing my own profile, then scrolling
down, and clicking the "show older posts" link as necessary, and scrolling
down, and repeating until I've gone back a couple months, and using my
browser's find-in-page feature to find what I'm looking for, eventually after
way too much clicking and scrolling.

Not only is this ridiculous, it's made even worse by an interaction with
Google Chrome (and maybe other browsers, but Chrome's what I'm using lately).
Apparently the AJAXy way these sites use DOM writes or whatever they do to
append content to the current page without reloading triggers this behavior in
Chrome where "Find Again" (ctrl-G or Command-G) doesn't find text in newly
added parts of the page. So often, I'll load the page and scroll back a month
or so and then use the browser Find command to search for "widgets" and not
find it, then scroll another month or so and then hit Command-G and not find
it, then scroll back another month or so and so on… and after going back 6 or
7 months, I'll remember that Command-G doesn't work, and cancel the search and
repeat the search with Command-F and *then* command-G and then it will find it
halfway up the page, which I would have found a lot easier if Command-G had
worked the first applicable time. (This was a pattern I learned with earlier
versions of Chrome; using Chrome 10, it's a little different -- the first
Command-G may actually scroll the search hit into view, but it won't highlight
it and you won't notice it on a busy page, and it will keep reporting "0 of 0"
in the search status pane; you still need to do the 3-step deselect, Find,
Find Again dance to get it to highlight.)

(Side note on Facebook: there's a [metafilter question asking how to search
your own Facebook profile](http://ask.metafilter.com/128906/How-to-search-
through-your-own-Facebook-profile); not only do the answers there not have a
solution, but the overall feeling is highly negative on it even being
possible. That's not quite true; I've confirmed that using the Facebook API
from a simple Python script I can get back anything I ever posted. They do
keep it, and they or someone else could write an indexer and search tool.)

Update: [Greplin](https://greplin.com) does a pretty good job of this, though
[not as good a job as it could with Facebook
posts](http://blog.metamatt.com/blog/2011/04/15/how-to-search-your-own-
activity-streams-greplin/).

