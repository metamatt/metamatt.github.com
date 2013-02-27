---
layout: post
title: Configuring iOS for Google's cloud data services
tags:
- iOS
- apple
- google
- gmail
- sync
comments: true
---
If you're a Gmail user, you've already got cloud email, a contact list or
address book, and a calendar (actually a set of calendars) hosted by Google.
And if you have an iPhone, you want to connect the built-in email, contacts
and calendar applications to those Google data sources.

It's possible, but it's not as easy as it should be.

"Not easy", you're thinking? Go to Settings, "Mail, Contacts, Calendars", "Add
Account", and there's Gmail — enter your credentials, the account is set up,
what could be easier than that?

Well, that isn't hard, but it also doesn't work very well. If you use the
"Gmail" account type, it doesn't sync contacts at all. Email is there, via
IMAP, but Gmail via IMAP has some notable deficiencies: push email doesn't
work (so the iPhone doesn't see new mail or other changes right away), the
delete behavior is weird, and there's this extra "All Mail" folder which might
sync an extra copy of all your messages. Your calendars are there -- well, by
default, only the main calendar, and not any others you may have created, or
calendars others have shared with you, or delegated/published calendars like
the one TripIt can automatically publish your travel plans to. ([You can fix
this with an extra
step](http://www.google.com/support/mobile/bin/answer.py?answer=151674), after
which multiple calendars work normally.)

There's another way: add your Google account using the "Microsoft Exchange"
account type. (If this seems confusing, note that what this really means is to
access Google's data services using the Exchange ActiveSync, or EAS, protocol,
[which Microsoft has licensed to both Apple and Google among
others](http://en.wikipedia.org/wiki/ActiveSync). Even more confusing, Google
brands this method of access to its services not as Exchange or EAS, but as
"[Google Sync](http://www.google.com/mobile/sync/)". Whatever.)

If you do this, things get quite a bit better: contacts sync to the phone;
email gains push (and in my opinion, the folder list and delete button work
better). This is actually t[he method Google recommends for use with
iOS](http://www.google.com/support/mobile/bin/answer.py?answer=138740). Again,
only the main calendar syncs to the phone, but again, [there's a way to enable
the other
calendars](http://www.google.com/support/mobile/bin/answer.py?answer=139206),
which is even more of a pain than the CalDAV method.

(Aside: I think the ability to get multiple calendars via Google Sync and EAS
was recently added, because when I first set up my iPhone I couldn't find this
method, and resorted to adding my Gmail account twice: once using the
"Exchange" account type for email and contacts with calendars disabled, and
once using the "Gmail" account type for calendars with email disabled. This no
longer seems necessary, but it may be a useful tip for anyone who wants Google
contacts synced to their phone but for whatever reason don't like the
EAS/Google Sync behavior for email or calendars.)

You may also run into some problems with contact sync, documented on the
"[Google Sync known issues with
iOS](http://www.google.com/support/mobile/bin/answer.py?answer=139635)" page,
under "Limited Contact Information": "Phone number synchronization is limited
to 2 Home numbers, 1 Home Fax, 1 Mobile, 1 Pager, 3 Work (one will be labeled
'Company Main') and one Work Fax number." Another problem **not** described
here is that phone numbers not exactly matching the expected labels (which are
case sensitive) will not sync: I had dozens of friends who in in my Google
contacts list had their mobile phone number labeled as "Mobile" instead of
"mobile", and these people showed up on my iPhone with no phone number at all.

The end result is that it's possible to make iOS and Google accounts play
nicely together, but it requires some up front knowledge, some extra steps in
account step on the iOS device, and some extra massaging of, potentially,
every entry in your address book to make sure the expected phone numbers sync.

Is it possible to do better than this? Sure. The late
[webOS](http://en.wikipedia.org/wiki/WebOS) synced all my Google data (email,
calendars and contacts) easily with no extra setup beyond choosing the Gmail
account type and adding my credentials. Presumably Android is capable of
similarly smooth integration. Apple may not be interested in smoothing the
process in iOS because they're wary of Google's dominance and want to push
[their own cloud data services](http://www.apple.com/icloud/), but given the
number of people who use both Gmail and iOS, I think they do their users a
disservice.

