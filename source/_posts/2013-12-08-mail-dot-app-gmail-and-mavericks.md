---
layout: post
title: "Mail.app and gmail in Mavericks"
date: 2013-12-08 23:47
comments: true
categories: 
tags:
- apple
- google
- mail
---
I use email pretty seriously, and like a good thick client. I like what gmail is trying to do, but I've never been able to get along with its web interface. My years-old mailstore has many folders, and emulating them with labels works fine but the gmail UI for assigning labels just isn't as good as what any decent thick client does with folders. So.

I see a lot of hate on the internet for [Mail.app](http://en.wikipedia.org/wiki/Mail_(application)), but having tried many alternatives, I really like it[^1]. Or did until [Mavericks](http://en.wikipedia.org/wiki/OS_X_Mavericks), which is the point of this post.

The Mavericks version of Mail.app made some big changes to how Mail.app talks to gimap, which I can only assume were to make things work better with gmail's "labels" system and the idea that unlike with folders, one message can be filed with multiple labels. Because it worked fine before Mavericks, at the cost of perhaps syncing multiple copies of the same message. However, immediately after the Mavericks release, [it was well documented](https://tidbits.com/article/14219) that instead of making things better, they'd made them worse.

In fact, it was bad enough that [Apple took the unusual step of releasing a Mail.app-Gmail specific update](http://support.apple.com/kb/HT6030) only a few days later.

In my experience, it made things a little better but far from good; even after the update

* server-side changes (made in another client, or in the gmail web interface, or new mail arriving) may not be noticed for minutes, hours, days, or weeks, or at all
* if I move messages between folders in Mail.app, the message disappears from the source folder, then reappears a couple seconds later, then disappears again a couple more seconds later
* the "Mailbox" column in the message list view, which should show what folder a message is in, always shows "All Mail", regardless of which more interesting folder(s) the message is actually in

The 2nd and 3rd problems are annoying but cosmetic; the 1st problem, though, renders Mail.app entirely unusable. There doesn't seem to be any workaround -- I've tried switching folders many times, triggering Synchronize, triggering Rebuild Folder, logging out and logging back in, rebooting, quitting and restarting Mail, even deleting my entire mail cache folder and all accounts and re-adding the accounts and downloading all the mail again. Nothing helped.

Hopefully Apple will fix this soon (there are [rumored to be further Mail.app/gmail bugfixes in an upcoming 10.9.1 update](http://appleinsider.com/articles/13/11/21/apple-seeds-second-os-x-1091-beta-to-developers-with-mail-improvements)). As it is, it means I either can't upgrade to Mavericks on the machine I actually care about[^2], or I need to find a different mail client.

So, in the past couple weeks I've spent some time dabbling in alternate mail clients. I haven't found one I like.

[Postbox](http://www.postbox-inc.com/):

* Works well enough from a strict functionality point of view, but has enough minor problems I still prefer the OS X 10.8 version of Mail.app, and would prefer a version of Mail.app that works into the future.
* Sluggishness: even after enabling its offline support and telling it to cache all my folders, selecting any message the first time is still sluggish, like it wasn't cached until I clicked on it. The normal flow is new mail arrives and I can see it in the message list, I click on it, then nothing happens for a second or two.
* Key bindings: Mac OS accepts Emacs keybindings (things like Ctrl-n for down arrow) systemwide, but not in Postbox.
* No springloaded autocollapse for dragging and dropping messages to nested folders.
* Aesthetically: it's just not as nice as Mail.app.

[Airmail](http://airmailapp.com/):

* Doesn't show me all my mail. This is, obviously, a dealbreaker. I clicked around a bunch of different folders, and it only showed me a small recent smattering of messages in folders other than the inbox (for my Sent folder, only stuff for the last 2 weeks; for a lower-traffic folder, it went back about 30 months but only about 20 messages; in all cases it’s far less than the number of messages actually there).
* Polarizing UI. Some people seem to love it. To me, it just looks weird (dark colors, unfamiliar icon glyphs, unlabelled icons all over the place including parts of windows that don't normally have buttons, busy menu structure).
* Weird behavior with nested folders. The toplevel folders are sorted alphabetically (as one would expect); so are first-level nested folders. But folders nested more deeply than that show in an apparently arbitrary order.

For now, I'm sticking with OS X 10.8.

[^1]: Notably, Mail.app is the only client I've ever used that makes IMAP feel perfectly natural, hiding all its design foibles. Other clients want to only download headers until I actually click on a message, or make me configure which folders get cached locally, or expose a difference between "delete" and "expunge". Mail.app's default settings just cache the whole IMAP mailstore in the background and make it feel like all the mail is local.

[^2]: I upgraded some machines I can live without, to see how well Mavericks works. I wasn't expecting any problems this big. But luckily I didn't upgrade the laptop I do use every day, which I need for my job; unluckily that machine is the one that would benefit the most from Mavericks banner features: better power management and better multi-monitor support.
