---
layout: post
title: So, I sat down to watch a movie on my iPad and this happened. Or, why "just
  works" is a lie.
tags:
- apple
- gadgets
- bugs
comments: true
---
Vanessa and I went on a weekend trip to Orange County with Dominic and wanted
to relax by watching a movie when he was napping, and the easiest vehicle for
this seemed to be our iPad. What could go wrong? Lots, it turns out.

I cruised over to the increasingly inaccurately named iTunes store and found
[Safety Not Guaranteed](http://www.imdb.com/title/tt1862079/) which looked
interesting so clicked Buy, waited for it to start downloading, watched the
progress bar long enough to verify it looked like it would take about 40
minutes to download, and took Dominic out for a walk so he'd fall asleep, with
the idea that in 40 minutes we'd have a sleeping baby and a watchable movie.

Dominic behaved as I'd hoped; the iPad didn't; after about an hour I grabbed
the iPad to find absolutely no sign of the movie. The Videos app said "no
videos, but you can cruise over to the store to buy one". The iTunes store app
didn't have any downloads in progress, and going back to the Purchases tab, it
had the cloud icon next to our movie. Upon clicking that, it told me it can't
download it because there's not enough storage available.

So apparently when I first purchased the movie, there was enough storage to
download it, but then something went wrong with the download, it silently
canceled the download without showing me any error message whatsoever, and now
there's not enough space for it? That's hard to explain, but whatever, there's
nothing to do but try to clear space and download it again. I go to Settings:
General: Usage and look at the breakdown of what's using how much space, and
the individual app usage doesn't add up to anywhere close to what it says is
used, but I don't have many options here. So I deleted Infinity Blade to free
up a gigabyte, invoked the download, and waited another 40 minutes while it
downloaded the movie again. At the end of the download, the iPad spent another
5 minutes saying "processing", then gave me a generic error message, and
kicked me back to the state where the movie is not available for playback but
is available for download. And again trying to download it says there's no
space available, and going back to Settings: General: Usage, there's 2.7GB
(the size of the movie) less than there had been when I started the download.
Something very weird is going on. I can't fix this problem on the iPad itself
(so much for the post-PC era: you need a PC to configure or troubleshoot your
post-PC device!) and now it's been 2 hours and we don't have time to watch a
movie anyway.

When I got back home from the trip, I plugged the iPad into my Mac and
launched iTunes and iTunes told me that there's 10GB of "other" content. Given
that this is the 16GB model (whose actual capacity is 13.8GB; go figure), that
doesn't leave room for very many 2.7GB movie downloads. That also explains why
the total usage was so much higher than the sum of the space used by each app.
But it doesn't at all help explain what "other" actually means;
[the Internet isn't much help here either](https://www.google.com/search?q=itunes+capacity+other). Trying to get
this to go away or at least explain itself, I tried syncing the iPad with the
Mac a couple times. The first thing I got for my trouble was that iTunes
decided I had 7.1GB of video on the iPad, and now I'm over capacity by 6GB
(this without me having added any additional content to the iPad, actually).
The second thing I got for my trouble was that iTunes decided to sync that
video content back to the Mac, which took all night, and resulted in 70GB of
corrupt data: it created 3 .m4v files which were actually directories
containing what looks like the entire iPad filesystem, 2 of which were named
after the movie that caused/revealed all this trouble (Safety Not Guaranteed)
and the 3rd of which was an episode of Breaking Bad which I didn't realize was
on the iPad in the first place. I'll repeat: what got synced back to my
computer in each case was not a valid .m4v file, but an entire directory
structure whose top level ended in ".m4v"; one of these was 10GB, one was
20GB, and one was 40GB. Clearly, these weren't actually on the iPad, and no,
my Mac didn't really like the resulting 70GB of garbage data either.
(Something created what should have been .m4v files on the iPad as symbolic
links to /, maybe? [The entire directory listing is here](http://metamatt.com/static/2012/10/crazy-ipad-movie-sync.txt) if anyone finds this edifying.)

Back to reality. Apparently the fix for this [runaway "Other" usage](https://discussions.apple.com/thread/2562027?start=90&tstart=0) is to
back up the iPad, then restore it from backup. So I did this, and after half
an hour, I had a working iPad with 2.2GB of apps, 3.3GB of "other", and 7.3GB
free. That's still not very satisfying, though -- what is this 3.3GB and how
do I get it back?

So then I tried completely erasing and restoring the iPad (restoring the
firmware, not just the user data, which is a similarly named but differently
implemented operation in iTunes). This worked a little too well — the iPad
came back with only 0.62GB of "other" and 13.2GB free, because it has no apps
installed. Um, that's partially my fault, because I'd turned off syncing of
apps in iTunes (in my experience, leaving app syncing enabled makes syncing
take much longer and sometimes forever, and it shouldn't be necessary in the
post-PC mode where you manage the device on the device itself); I don't find
it obvious, but apparently if you disable the syncing of apps in iTunes, that
also means that local restores via iTunes don't restore apps either.

But oh whatever, I have a recent iCloud backup which should have all the apps
backed up. I do another complete erase of the iPad, and this time when it
boots up, instead of driving the restore from iTunes on the Mac, I walk
through the on-device setup and select my iCloud backup. It chews for a while,
reboots, and then gets stuck forever at the boot screen (Apple logo with
progress bar). [Apparently I'm not the only one with this problem either](https://discussions.apple.com/thread/4372003?start=0&tstart=0). I tried again and got the same result.

So apparently the iCloud backup is corrupt and can't be used; the local backup
works but leaves me with extra work to do.

In the big picture, this is just another internet rant about a bug which
happened to one person and probably isn't generally applicable, and while I
can describe it as 6 separate problems (iPad aborts my download without
showing an error message, iPad downloads movie to bit bucket and won't play it
back, iPad runs out of space, iTunes can't sanely describe space usage, iTunes
syncs garbage from iPad back to my computer, iCloud backup is corrupt) it's
likely all one root cause, where some data structure got corrupted and caused
the rest of the failures downstream from there. And computers are complicated,
and not that expensive given the complexity, and hard and expensive to get
right.

But what's frustrating about this is that Apple's moved the openness needle
pretty far back toward walled garden, in the name of preventing problems.
Problems like malware, yes, but also problems due to misconfigurations, and
problems due to third party software that causes finger-pointing instead of
solutions. This was all first-party software; Apple content in Apple software
on an Apple device synced and controlled from another Apple device. No
jailbreaking, and I didn't even commit the minor sin of trying to run iTunes
on Windows. This is the case that we should be getting right; that's the
benefit that we're paying the walled-garden cost for.

Apple is often applauded for bringing us technology that "just works", but
I've been having more and more experiences lately that are pretty far from
"just works". The moral of the story is that Apple's devices are computers
just like other computers; they're still a stack of fiendishly complex
hardware and software components; also with iOS in version 6 and
[iTunes in version 10.7](http://en.wikipedia.org/wiki/ITunes_version_history#Version_history)
there's a lot of untestable legacy cruft. "Just works" sounds nice, but we're
not really there yet, or maybe we've been there but don't know how to stay
there for long.
