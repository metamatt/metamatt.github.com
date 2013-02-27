---
layout: post
title: OAuth and localization fixes for Palm-Evernote importer
tags:
- software
- palm
- evernote
comments: true
---
I’ve updated my [utility for importing notes from Palm Desktop into
Evernote](http://www.maddogsw.com/evernote-utilities/evernote-palm-importer/)
again.

The big change is that it now uses [OAuth for authentication to the Evernote s
ervice](http://dev.evernote.com/documentation/cloud/chapters/Authentication.ph
p), instead of asking you for Evernote account credentials directly. This is a
step forward in general; utilities like this one shouldn't have unrestricted
access to your entire account, nor should they know your actual password in
case you use the same password for other services1. [Evernote has disabled
username/password logins for third party
apps](http://blog.evernote.com/tech/2012/11/01/third-party-authentication-
transition-to-oauth-complete/) to force them to use OAuth, a move which I
think more services should make2.

I also made some smaller changes to further improve the chance of success for
people outside the USA, using nondefault character encoding or locale
settings.

Finally, I added the [public source repository](https://github.com/metamatt
/evernote-palmimport) to my github account. (I've always made the source code
for the current version available, but now the complete repository with
history is public.)

Download here: [[http://www.maddogsw.com/evernote-utilities/evernote-palm-
importer/](http://www.maddogsw.com/evernote-utilities/evernote-palm-
importer/)](http://www.maddogsw.com/evernote-utilities/evernote-palm-
importer/).

* * *

  1. Which you shouldn't do, but lots of people do anyway. ↩

  2. I'm looking at you, Google Reader clients. ↩

