---
layout: post
title: Storytlr/Tumblr import failures, and fix
tags:
- software
- bugs
- patch
comments: true
---
I installed [Storytlr](http://storytlr.org/) on my own server for personal
use, and then started adding the sources where I have accounts -- Flickr,
Twitter, Delicious, and a few others worked right away, but I couldn't get it
to add Tumblr at all. Every attempt yielded an error message that just said to
try again later; looking in Storytlr's messages.log, I saw more detailed
errors like

2010-12-24T03:50:55+01:00 ERR (3): Exception updating tumblr (21): Tumblr API
returned http status 503 for url: [http://metamatt.tumblr.com/api/read/json?ca
llback=wrap&num=50&start=0](http://metamatt.tumblr.com/api/read/json?callback=
wrap&num=50&start=0)

2010-12-24T20:07:38+01:00 ERR (3): Exception updating tumblr (22): Tumblr API
returned http status 503 for url: [http://metamatt.tumblr.com/api/read/json?ca
llback=wrap&num=50&start=550](http://metamatt.tumblr.com/api/read/json?callbac
k=wrap&num=50&start=550)

2010-12-24T20:08:10+01:00 ERR (3): Exception updating tumblr (23): Tumblr API
returned http status 503 for url: [http://metamatt.tumblr.com/api/read/json?ca
llback=wrap&num=50&start=0](http://metamatt.tumblr.com/api/read/json?callback=
wrap&num=50&start=0)

2010-12-24T20:09:28+01:00 ERR (3): Exception updating tumblr (24): Tumblr API
returned http status 503 for url: [http://metamatt.tumblr.com/api/read/json?ca
llback=wrap&num=50&start=50](http://metamatt.tumblr.com/api/read/json?callback
=wrap&num=50&start=50)

2010-12-24T20:27:05+01:00 ERR (3): Exception updating tumblr (25): Tumblr API
returned http status 503 for url: [http://metamatt.tumblr.com/api/read/json?ca
llback=wrap&num=50&start=1150](http://metamatt.tumblr.com/api/read/json?callba
ck=wrap&num=50&start=1150)

Note that the "start" parameter in the request varies each time, and sometimes
got quite large -- Obviously it's looking for too many posts and doesn't know
where to stop, since my Tumblr blog has < 100 posts. My theory is that Tumblr
rate-throttles requests, so when Storytlr makes a few or a few dozen requests
at once, Tumblr returns 503 (temporary failure, try again later) and Storytlr
treats that as a more serious error.

Looking at the Storytlr source, I quickly found the code that imports from
Tumblr, and the problem. Here's the answer:

    
    --- protected/application/plugins/tumblr/models/TumblrModel-orig.php     2010-12-24 11:39:38.000000000 -0800
    +++ protected/application/plugins/tumblr/models/TumblrModel.php     2010-12-24 11:40:05.000000000 -0800
    @@ -53,9 +53,9 @@
          }
     
          public function updateData($full=false) {
    -          // Fetch the data from twitter
    +          // Fetch the data from Tumblr
               $username   = $this->getProperty(username);
    -          $pages          = $full ? 50 : 1;
    +          $pages          = $full ? 2 : 1;
               $count          = 50;
               $result      = array();
               $curl = curl_init();
    

So it's hardcoded to always ask for 50 pages of data (2500 posts); hardcoded
is probably not the way to go here. (It would be wasteful, but not inherently
wrong, as long as the Tumblr API were happy to return 50 pages of empty posts,
or if the Storytlr import code would understand 503 status codes and retry;
however since the Tumblr API is currently unreliable enough that you're lucky
to get a couple consecutive reads to succeed, and Storytlr doesn't know to
retry, it's important to only ask for what you really need.)

I just hacked it to ask for 2 pages since I knew that would account for my
posts; a better fix would query Tumblr for the actual number of posts, and
stop there, and/or just recognize an empty response and stop there.

(Note: I tried posting this to the [Storytlr-discuss mailing
list](http://groups.google.com/group/storytlr-discuss), which is backed by a
Google Group, but the group is broken or a moderator is eating the post,
because it will temporarily show up and then disappear, with commensurate bugs
in the unread-post count. So I'm posting it here.)

