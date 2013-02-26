---
layout: post
title: How photo sync would be done right
tags:
- gadgets
- photography
- sync
- sharing
- backup
---
I've been wishing and waiting and watching and waiting, with an idea in my
head of what I want: from computers and the internet, regarding photos and
photo management, and connecting all the computers I use. Some of this is very
specific to photos, and some of this is general multi-computer file
management, and after years of watching and waiting, little of it is done the
way I wish it was.

I take photos with digital cameras. I want all of those photos accessible to
me wherever I go, on all the computers and smart devices I own and any I
happen to use temporarily; I want them backed up for safety; I want some of
them shared with my friends or the whole internet. In short: I want my
memories protected, accessible to me, and selectively shared with those I
choose to share them with.

There exist good file sync solutions, and there exist good backup solutions,
and there exist good photo sharing solutions, but all of them have drawbacks,
not least of which is that they're separate and don't really work together, so
I need to do more to get these combined benefits.

Ideally, I'd like all photos I take immediately uploaded to a private site in
the cloud, automatically, which acts as backup and also automatically syncs
them between all my devices, and which also offers a web interface capable of
giving me full access to the collection, and selecting some photos for sharing
in a nice way, with or without authentication.

Since upload bandwidth is generally too slow and expensive, I want the cloud
upload to happen once, automatically and asynchronously in the background, as
soon as possible; the photo is now backed up and syncable; if I choose to
share it, there's no further waiting for upload.

I want flexible organization (which should work well with as much metadata as
I want to add, or as little), to scale to my collection of thousands of photos
over many years, and grow into the future. I want the sync solution to play
promiscuously well with other apps I choose to use, and not enforce a
particular filesystem or logical organization scheme, but I want it to offer
optional organization features which help me keep a well-groomed collection if
I can use the help. And the sync part of the solution means that any
organizational changes I make, on any connected device and in any app, is
reflected everywhere.

I want this to work with full-resolution photos, and raw photos, and I want it
to work with arbitrary metadata. And I want it to be promiscuously
crossplatform: on Mac and Windows and Linux desktops, and iOS and Android and
whichever other mobile platforms manage to prove their relevance.

I want the mobile device version to realize and revel in the constraints of
the platform, acknowledging that connectivity is ubiquitous but not always
fast or reliable, that memory is limited, and that snappy touch interactions
feel good. Thus, if I'm using a device that combines a camera and a network
interface (any smartphone) I want every photo I take immediately sent to the
cloud for backup and syncability. I also want my entire collection synced down
to my device as a photo wallet, but, acknowledging local storage limits, I
want this to automatically downscale to an appropriate resolution, and I want
to be able to select per-device subsets of the entire collection to subscribe
to.

It would be great if the sync/backup/share features work with non-photo files
-- the solution I envision would be file-based, and have a bunch of special
sugar for image files, but would be useful even for other files -- but that's
not necessary. Non-photo files are already handled pretty well by services
like DropBox.

In fact, my continuing desire for the magic super photo cloud service is
driven by noting that by and large, photos are the only remaining file type I
have to really care about on my computer, meaning data I create that isn't
already well handled by cloud services. Examples that are already well
handled: Email (tons of cloud services including Gmail);  office documents
(Google Docs); unstructured notes and clippings (Evernote); miscellaneous
files that don't fall into the above buckets but are small (Dropbox): what's
left? Well, photos, music and video. But music is a special beast, which like
photos also involves largish files but unlike photos is something I buy
instead of create, meaning any individual file I want already exists in some
canonical form I can get from lots of other sources; anyway it's well handled:
Amazon, Apple, and Google have cloud sync; the file-based approach is somewhat
displaced by subscription services like Rhapsody and Spotify. Video is a
combination of photos and music which, in the case of video we record
ourselves, I think will end up having the same properties as photos: large
files we create, embodying our memories, that we want to sync and backup and
share. So it's the photos we take (and by extension I include video we take)
that we care about managing with computers, better than it's currently done.

Here's a smattering of things that exist now, attacking some of the above
problems and illustrating a variety of different approaches. I'll call out
what they do right, and what I find lacking:

  * [Dropbox](https://www.dropbox.com/) (file sync and then some): can do most of what I'm asking for, but it's not photo-specific (which could be bug or feature or both). The price is high (compared to photo sharing and backup services which usually offer unlimited storage). They have a sharing UI which has been somewhat customized for photo albums, but it's pretty bare bones compared to full-blown photo sharing sites. The syncing is good but not perfect; p2p sync first requires an upload to the cloud (so it makes you wait for the slow hop then skips the fast hop); it enforces a certain filesystem layout on computer clients; it doesn't have an appropriate mode for syncing all photos to/from smart devices at suitable resolution. All this said, Dropbox is probably the closest existing thing to what I want, and it offers good 3rd party APIs allowing others to extend it -- I think they see themselves more as storage infrastructure for the web than any specific application -- so if the interoperability and pricing concerns don't bother you, maybe it's already the right answer.
  * [Photo Stream](http://www.apple.com/icloud/features/photo-stream.html) (photo sync): gets the sync right (the first I've seen that automatically adds photos as they're taken). However, it has very strict and arbitrary limits: no deletion, no organization, and includes only the last 1000 photos or 30 days, so it's basically this write-only temporary repository that syncs across devices but which you need to manually fish the things you care about out of, and manage separately. It does have the magic auto-upload feature for network-connected cameras, and it does deal with RAW images. I see this as a promising demo of one aspect of what I'm looking for, but it doesn't even touch the others (organization, backup, or sharing).
  * [Adobe Carousel](http://www.adobe.com/products/carousel.html) (photo sync and sharing): haven't tried it yet, and it looks promising but with limited platform support and doesn't handle raw files. Pricing may be a turnoff (monthly fee and limited number of carousels). Should handle sharing, both public and private. But not suitable for my entire photo library, as far as I can tell.
  * [CrashPlan](http://www.crashplan.com/) (online backup, also see Mozy, Carbonite, BackBlaze): cheap unlimited-size cloud backup, which can also let you retrieve individual files from the cloud via a web interface, which in a pinch means you can get at your files from anywhere. The web interface isn't optimized for this case though, nor is it optimized for photo display, and there are no suitable features for sharing (albums, delegatable access control).
  * [Flickr](http://www.flickr.com/) (photo sharing): Flickr is great for photo hosting and sharing; it has great organizational features and a good community. The pro version offers effectively unlimited storage and has neat tracking features so you can see the popularity of what you post. However, Flickr doesn't itself handle uploads or, really, client software in general, so it doesn't handle sync (it does have an API with good 3rd party adoption, addressing this somewhat). It doesn't handle RAW files, and it's not suitable for backup. The sharing features allow flexible public and private sharing, but with not a lot of flexibility for album display. In general, the evolution of the site has been slow since Yahoo! bought them out. I think the site was originally designed with a forward-looking vision that in the near future, nobody would need any local photo software, and you could just upload everything to Flickr, edit and organize it there, share it there, and you wouldn't need sync or backup. And maybe if the site had continued on its original trajectory and pace, this would have happened by now -- but I find it's anything but true in the real world.
  * [Facebook](https://www.facebook.com/) (photo sharing): Facebook has huge adoption, and I've found that photos I post there get seen (and "liked" and commented on) more than anywhere else, including Flickr. But, Facebook is a walled garden (it may be possible to use it for public photo sharing but I don't see people doing that in practice); content hosted there is not search engine friendly; you as the photographer also get zero control over photo presentation, zero insight into who's viewing your photos, and only very limited organizational features (albums with a size limit which can't be nested hierarchically). Person tagging and automatic face recognition make up for some of this; general ease of use and speed and reach make Facebook a good solution for sharing your photos as long as your needs are simple; however on my list of big top-level wishes (handle sync, backup, and sharing) it only touches sharing, and honestly, given the limited control over organization and presentation, I'd prefer to use Flickr if I could get the same reach. Given the name of the site (it's the book of faces, after all) and the mandate implied therein, I feel like they could take this feature much much farther, but it also seems like the backup/syncing aspect I want is not part of this "book of faces" mandate and cries out for a dedicated solution. Note that Facebook is free and offers unlimited storage (as far as I know); the platform scales well (and is, I believe, by far the world's largest-volume photo server); it doesn't handle RAW files, or even particularly high-resolution images.
  * [Google's photo suite](https://picasaweb.google.com/) (photo organization and sharing): Google has nice desktop client software for photo organization and editing (Picasa), which they eventually built an online companion for with sharing and automatic sync features (Picasaweb), and then integrated into their new social network, Google+. Taken together, this provides a pretty good start-to-finish solution for taking, editing, uploading, and sharing photos. However the upload/sync solution based on Picasa is not flexible or pervasive enough to serve as backup or sync files managed outside Picasa, and the website is certainly not designed to serve as a central hub for managing and syncing my entire photo library. I'm not even sure if the sync is bidirectional; it may be upload-only.
  * [Evernote](http://evernote.com/) (generic unstructured data sync): Evernote has a good web service, with client apps and a web app for access, automatic syncing for offline access, and attractive pricing. However it doesn't offer any of the organization or sharing features you'd really want for photo management, nor does it integrate with other apps via the filesystem (stuff stored in and synced via Evernote is available via the Evernote API, but not via older integration points, namely local filesystems).
  * File sync in general: Beyond Dropbox, described above, I haven't seen anything that really scratches this itch in the way I'm envisioning.
  * Photo sharing in general: there are tons more photo sharing services, but by and large, they have the same properties I ascribed to Flickr above, but are less good at it. You might have a favorite that you think I'm giving short shrift to here; fine; let me know if you know of any that are qualitatively better than Flickr on the list of things I'm wishing for in this post.
  * Other things not mentioned here: This list is intended to show examples, not be exhaustive, so I've collapsed whole categories onto one exemplar; for example, while I'm aware of SpiderOak and see it having certain advantages over Dropbox, for my purposes here it's essentially the same. There are probably many other sync, backup and photo sharing services that have their own advantages but don't break new ground on the aspects I care about; if you know about something I missed that does address my wish list, please let me know.

How I'd build this: I'd want the following pieces:

  1. The central cloud service which stores files securely for backup, and handles sync to any clients I've authorized.
  2. Client software for every platform which matters, which handles sync, automatically in the background: new files appearing first on this device are uploaded to the cloud service; new files announced from the cloud service are synced (at an appropriate resolution) down to this device's local library; changes to existing files (including filesystem metadata like name and location, picture-specific metadata like that encoded in EXIF and IPTC mechanisms, and image data itself) are also automatically synced in both directions.
  3. Web app atop the first cloud service which handles organization and management -- letting me move files between folders or albums, apply tags, and designate what to share with whom.
  4. Web app for sharing, pulling authorized files from the cloud service, and displaying them with nice presentation and according to whatever organization (individual file, album, by tag, etc) I've chosen.
  5. Client local versions of #3 (optional and lower priority, since I should be able to use the web version or any local software I want to most things this could do).

(I think Evernote, top to bottom, service to applications, is a great example
of this architecture -- handling what they call "notes", which basically means
document snippets with attachments -- but, as described above, it doesn't
solve my photo sync problem, since the client local apps don't integrate my
local filesystem and provide an integration point for other local apps, and
the web interface doesn't have theorganization and display features I'd want
for photos.)

I don't know what this should cost or what I'd be willing to pay for it --
more than free (Google and Facebook); probably more than Flickr's $25/year and
more than the unlimited backup companies' $5/month; probably less than
Dropbox's per-GB-per-month fees. For this to be done right, the storage and
bandwidth would probably have significant cost, and most of the data is
private so can't be de-duped.

Clearly this isn't easy -- the inherent challenges of handling and
transporting and scaling to this much data, and designing good interfaces for
all the services and applications, are real, and for anyone but the
incumbents, there are also the additional challenges of integrating with 3rd
party software and OS platforms, especially less open and less flexible mobile
platforms (given the sandboxing and multitasking restrictions in iOS, for
example, I'm not sure anyone but Apple is in a position to implement Photo
Stream for iOS right now).

But it would be nice.

