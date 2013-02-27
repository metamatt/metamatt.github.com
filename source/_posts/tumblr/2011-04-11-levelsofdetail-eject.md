---
layout: post
title: ! 'LevelsOfDetail: eject'
tags:
- software
- windows
- mac os x
comments: true
---
[LevelsOfDetail: eject](http://puntium.tumblr.com/post/4517405510)

[puntium](http://puntium.tumblr.com/post/4517405510):

> I shouldn’t have to ask this, but what is the fastest way to eject a
removable disk in Windows 7? So far I’ve been finding an explorer window, then
right clicking on the drive, and picking eject. Why is this three difficult
clicks? What’s the one thing that you know is going to happen with…

I use the systray icon. I don't think it's that bad. Except when it breaks…
yeah, that shouldn't be a concern but it is; even under Win7 I've seen quite a
few occurrences where right-clicking that Unplug/Eject systray icon does
nothing. Then you have to double-click said icon, and navigate through the
resulting dialog box, which is too many clicks. Also, even when the systray
icon isn't broken, sometimes the autohide logic decides to hide it (and I
understand the sad state of affairs that led MS to implement autohide for
systray icons, but I don't think it should choose transient status icons like
this one). I just set it to always show.

I'm not 100% with you on "what's the one thing you know is going to happen
with" removable disks. Just because it's connected to a bus that technically
supports hotplug doesn't mean you're going to remove it. On my Mac, I have a
couple drives connected via Firewire that I never unplug, and I actively
dislike that there's always an eject button staring me in the face and
tempting me to press it, or waiting for errant clicks. I've only ever
accidentally ejected one of these drives once, but that's still once too many.
And in no case should the guest user be able to eject the Time Machine drive.
([I complained about this
before](http://www.facebook.com/metamatt/posts/10150099468713843);
unfortunately that was on Facebook and links from the public web won't work
well so apologies if you're reading this and can't see that.) And even for
disks you do unplug sometimes, the OS gets no guarantees as to when.

I'm fine with how Windows exposes this (though it should actually always
work). And I wish that Mac OS had a way to say "treat this drive as
nonremovable", or at least require admin abilities and a confirmation dialog
before ejecting it.

