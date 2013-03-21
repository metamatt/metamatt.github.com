---
layout: post
title: Google default account for multiple sign in
tags:
- google
- accounts
comments: true
---
Google Accounts allow you to [stay signed into multiple accounts at once](http://support.google.com/accounts/bin/answer.py?hl=en&answer=1721977), which is hugely helpful for those of us who have multiple account, but there's one thing that's been frustrating me here.

I use the browser address bar (relying heavily on its autocomplete feature) to do most of my navigation directly from the keyboard. If I want my document files in Google Docs, I open a new browser tab from the keyboard shortcut, then type "docs" and by that time, autocomplete has already filled in docs.google.com[^1],[^2].

However, I have 3 different Google Accounts that I'm usually signed into: one standard personal account (ending in @gmail.com), one GAFYD[^3] account for my personal email[^4], and one GAFYD account for work. If I navigate to docs.google.com, Google automatically chooses one of the accounts to redirect to, and at different times on different computers I end up with a different (seemingly arbitrary) account selected, and if it wasn't the right one, it's 3 extra clicks in the account switcher to get to the right account.

What's controlling its choice? It turns out it's the order you sign into the accounts. If you look closely at the URLs, either by mousing over the links in the account switcher or by looking at the URL you end up at for gmail but not for docs[^5], you'll see an "authuser" or "u" parameter which is a low-valued integer. It starts at 0 for the first account you sign into, and counts up from there as you sign into additional accounts.

If you navigate directly to docs.google.com (or mail.google.com, etc), you'll get the account currently associated as authuser 0, which is the first account you signed into.

For the GAFYD case, Google lets you [set up convenient forwarding addresses](http://support.google.com/a/bin/answer.py?hl=en&answer=53340) for domains you control, and I've used this to map mail.mydomain.foo and docs.mydomain.foo to redirect automatically to mail.google.com/a/mydomain.foo and docs.google.com/a/mydomain.foo. This means that for the two GAFYD domains, if I want the mail or docs view associated with that account, I go to docs.mydomain.foo, which in turn means that if I navigate to docs.google.com, I always want my personal account selected by default.

For me, the solution to get the behavior I wanted boils down to:

* Sign out (which signs you out of all acocunts)
* Sign into the primary account which I want as default (the one ending in gmail.com) first, then sign into the others.
* Always use this same signin order in the future.

Thanks go to [Ramesh](http://www.linkedin.com/pub/ramesh-dharan/1/13b/8a2) for helping me figure this out.

[^1]: Google has rebranded Google Docs as Google Drive, and docs.google.com redirects to drive.google.com. I haven't retrained my fingers, so I always type "docs", so I'll keep using the old name. Both names work fine as described in this post.

[^2]: (Everything in this post is true for other Google Accounts services like gmail, as well, but docs is the one I navigate directly to the most frequently, so I'll stick with it for the example.)

[^3]: Google Apps for Your Domain, back when that was a thing; since rebranded as [Google Apps for Business](http://www.google.com/intl/en/enterprise/apps/business/) once they removed the free option.

[^4]: Why a separate gmail.com and personal GAFYD account? I've long used the same personal email address at a domain I control, predating Gmail. When Google created Gmail and started tacking many other services onto your Gmail account, becoming Google Accounts, I signed up with a gmail address but didn't use it for email, just for Google Accounts. At some point I got tired of running my own email server and dealing with reliability and spam, so I decided to let Google host it via the then-free GAFYD. I could have just forwarded mail from the vanity address to the gmail address without setting up another mailbox, but it seemed simpler to keep them separate. That may have been a mistake.

[^5]: The URLs vary by service, so this isn't as obvious as it could be. Docs/Drive uses URLs like drive.google.com/?authuser=N in the account switcher, but for a GAFYD account, you actually end up at drive.google.com/a/mydomain.foo. Gmail uses URLs like mail.google.com/u/N, both in the account switcher and where you actually end up, though for a GAFYD account you can also navigate to mail.google.com/a/mydomain.foo (and you'll be redirected to mail.google.com/u/N for the correct value of N if you're already signed into that account, and to the login page if you're not).
