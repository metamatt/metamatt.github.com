---
layout: post
title: Google account access from an iPhone
tags:
- apple
- google
- mobile
- cloud
- gadgets
---
Google recently announced that after January 2013, they'll be [deprecating EAS
access to
Gmail](http://support.google.com/a/bin/answer.py?hl=en&answer=2716936) (and
calendar, and address book) for free customers (addresses ending in
@gmail.com, and free Google Apps accounts). It'll still be available for paid
Google Apps customers, and it'll keep working for normal customers who are
already using it, but only on their existing devices.

This is bad news because EAS (aka Google Sync) has been and continues to be
the best way to get Google services on an iOS device. In my opinion, iOS +
Google Sync continues to be the best combination of mobile device and cloud
services, but this change makes them work a little less well together.

Google Sync (EAS) is the best way to connect iOS to Google services because

  * One "account" (setup step in iOS) handles mail, contacts and calendars.
  * Until September 2012, this was the only way to sync contacts between iOS and Google.
  * Mail works better: Push works, and the delete button works the way you'd expect. (Supposedly both iOS mail client and Gimap mail server support IMAP IDLE, but they disagree on how, or something, because the result doesn't work.)
  * Also, if you enable Google's 2-factor authentication, you need to generate fallback "app-specific" passwords for all your devices1, and for EAS this is one per device, and without EAS it's at least two2.

For these reasons, especially the second one, I've been using — and
recommending to friends and family — EAS as the preferred way of connecting to
Google accounts. In fact, I didn't even realize that contact sync was now
possible without it (Google just added CardDAV support in September 2012).

Similarly, I've been using — and recommending to friends and family — Google
Apps (Gmail and friends) as my preferred provider for cloud
mail/contacts/calendars. Apple's track record for cloud mail services is
spotty; even if iCloud is improving, I just don't see the advantage over
Google, especially if you don't want to tie yourself to Apple devices
forever3.

That leaves us trying to connect iOS to Google's services as best we can.
Which to be fair is pretty good, but losing EAS is a step back4. This speaks
to [something my friend Ken wrote months
ago](http://levelsofdetail.kendeeter.com/post/31926718063/maps) (in the
context of the maps kerfuffle):

> Why is it that two tech giants with best-of-breed tech in different areas
rarely seem to be able to cooperate to produce an awesome product for the
user?

This has been a bright spot in this regard, which is getting a little less
bright at the end of January.

Google probably doesn't care about keeping free EAS working because, in order
of preference, they'd like to see

  * You using an Android device to connect to Gmail+friends
  * You using a (paid) Google Apps for Business account
  * And for anyone else, using a non-Google device to connect to a free Google account, there are still the open protocols (IMAP for mail, CardDAV and CalDAV for calendar and contacts).

Apple may not care about optimizing the Gmail experience for iOS users because

  * They'd like to see you using iCloud for mail+contacts+calendars
  * Plus they've already connected you to Google services using EAS, so why should they have to do it again differently.

In fairness to Apple, adding a "Gmail" account to iOS adds both mail and
calendars (IMAP + CalDAV), and Google only added CardDAV support on the server
side in September 2012 (i.e. after the current iOS release). Maybe, hopefully,
Apple will make iOS "Gmail" accounts start supporting calendars via CardDAV in
the next release. In the meantime, you have to do it manually.

I don't see any reason why the open-protocol support from iOS to Google
services couldn't work just as well as EAS — if one setup step added all 3
protocols, and if push were made to work — but it's not the case now.

* * *

  1. It's too bad that native device clients basically negate the advantage of 2-factor authentication, since they aren't compatible and force you to use the fallback mechanism. ↩

  2. One for the "Gmail" account supporting IMAP and CalDAV, and one for the separate CardDAV account you have to add. And I don't know whether/how "app-specific" password authentication actually works for the Gmail account type, given that it's a hybrid of two protocols; it's possible that doesn't work in which case you would have to avoid the Gmail account type, generate 3 fallback passwords, and set up IMAP and CardDAV and CalDav separately. ↩

  3. I'm complaining here about the flaws in the relatively good iOS support for Google services; I suspect that anyone trying to connect to iCloud from Android or Windows apps has it far worse. ↩

  4. There's some irony here in that the best way to connect some Apple software to some Google software is using protocols designed by Microsoft. ↩

