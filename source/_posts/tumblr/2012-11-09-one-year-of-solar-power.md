---
layout: post
title: One year of solar power
tags:
- energy
comments: true
---
When I got solar panels installed on the roof of our house last fall, friends
immediately started asking how well they were working out, and my answer had
to be that while they're [generating a nice amount of
power](https://enlighten.enphaseenergy.com/public/systems/g8ah32261), I
wouldn't know how well they were doing on the actual goal of zeroing our
electric bill until a year had passed. That year has now passed, and it's time
to answer the question.

If you add solar power to your grid energy, at least the way it's done in
California, two things will happen:

  1. Your electric bills will be lower, but
  2. You won't understand them.

## The problem:

California electric rates are confusing because they're complicated and
variable. You pay a different rate depending on how much you use (tiering)[^1].
You can opt into time-of-use (TOU) billing[^2], which makes electricity more
expensive at peak times and cheaper the rest of the time to encourage you to
shift usage away from peak times. The normal residential billing schedule is
called [E-1 ("residential
services")](http://www.pge.com/tariffs/tm2/pdf/ELEC_SCHEDS_E-1.pdf) and shows
5 different rates according to tier; the TOU residential schedule is called
[E-6 ("residential time-of-use
service")](http://www.pge.com/tariffs/tm2/pdf/ELEC_SCHEDS_E-6.pdf) and shows
25 different rates according to tier and time.

Once you introduce solar (or other generation capabilities) into the mix,
there's another wrinkle. Assuming you stay connected to the grid, PG&E will
convert your billing to what they call [NEM](http://www.pge.com/standardnem/)
(Net Energy Metering), which means your electric meter will measure the flow
of power in both directions — from the grid into your house when you're using
more than you're generating, and from your house back to the grid when you're
generating more than you're using. But solar panel output varies by season and
with weather, in addition to the obvious day/night cycle. To account for this
seasonal variation, PG&E bills NEM customers on a yearly cycle called the
[true-up period](http://www.pge.com/myhome/myaccount/explanationofbill/nem/).
Your monthly bills are only an approximation, and at the end of the year they
calculate the actual balance owed compared to what you already paid, and have
you "true up" to that amount, hence the name.

For NEM customers, that's 3 different axes of variation[^3]: tiered rates based
on total consumption, variable rates due to time-of-use, and true-up billing
to account for seasonal variation of generated output.

## Before adding solar generation

You have to calculate how much electricity you want to generate to produce the
desired effect (economically or ecologically or both[^4]), and then you need to
calculate the size of a PV solar array that will produce that effect.

Both of these calculations actually turn out to involve a fair amount of
prediction. Companies that specialize in solar installations (for example,
[Luminalt](http://www.luminalt.com/meet-luminalt/about-us), who installed
ours) can help you with these predictions and calculations.

But even after you've done the calculations, decided to go solar, and had the
array installed and it's live, you still won't know if you were right, at
least for a while. That's what this post is about. I wanted to know if we'd
predicted correctly, and I also wanted to know if PG&E's billing methods
fairly account for the seasonal variation. (If I have a large surplus in
summer on-peak in July, and a big deficit in winter off-peak in January, do
these cancel out, and how?)

## After adding solar generation

I said that after activating a solar array and switching over to PG&E's NEM
program, you'll get lower bills that you won't understand. Here's what I mean.
Each month with my electric bill[^5], I get a separate "Net energy metering
electric statement". It includes three amounts:

  1. "total current month's billed amount", which is always in the neighborhood of $12.
  2. "current month energy charge or credit", which is the actual charge for electricity I used, or credit for electricity I produced, after accounting for tiered TOU rates.
  3. "cumulative energy charges or credits for the current true-up period", which is the sum of the #2 values.

This is hard to interpret month by month, partly because there's no
relationship between what I'm asked to pay (#1) and what I used (#2), and #3
will swing wildly one direction[^6] and then correct over the course of the year.
All of this evens out at the end of the year, which is the reason for the
1-year true-up method of billing.

But when the 1-year anniversary arrives, and with it the final true-up
payment, there's a new confusing quantity: "total current month's billed
amount" is replaced with "total true-up billed amount". This amount, which is
your actual bill for the 12th month, is not the usual $12, bears no obvious
relationship to the cumulative energy charge, and isn't explained or derived
by PG&E on the bill or elsewhere that I could find[^7]. (In my case: my
cumulative energy charge after 12 months was $60.22, and the "total true-up
billed amount" was $22.02.) Why?

There's a method to their madness, but I had to dig deep into PG&E's rate
documentation and then spend a few hours messing with a spreadsheet to try to
derive the calculations that would map my usage to my bills.

## Understanding true-up billing

First, the monthly bill. Where does this $12 come from? It turns out PG&E
charges E-6 (TOU) customers a "meter charge" of approximately $0.25 per day.
E6 and E-1 both also have a "minimum charge" of approximately $0.15 per day;
they don't explain what this means, but if my reverse engineering of my bills
is correct, for NEM customers it's essentially a placeholder for your usage
before they know what your usage is. These fees added together and multiplied
by the number of days in a billing cycle yield the approximately $12 amount
that I was billed for each month (billing cycles ranged from 28 to 32 days, so
the monthly bill ranged from $11.22 to $12.83, with the most common bill being
$12.02 for a 30-day billing cycle).

Second, the usage charges. These are not simple (since they involve both the
tiering and TOU calculations), but they are actually decently explained on the
monthly NEM statement itself, and with one nitpicky exception[^8], they're the
same as what you had before you added NEM, and the true-up calculation doesn't
affect them.

Third, the cumulative usage charge. This one is completely straightforward:
add the usage charges for the current true-up period, to date. Each NEM
statement shows the current cumulative charge (this amount) and the amount by
which it changed (the month's usage charge), and you can verify that the
current cumulative balance is equal to the previous month's balance plus/minus
the current month's usage charge/credit. However, as mentioned above, this
amount will swing one direction and then correct due to seasonal variation,

Fourth, the true-up amount. This is a simple calculation if you know where it
comes from, but PG&E doesn't explain it, so I had to reverse engineer it,
learning to understand the daily meter and minimum charges. What it boils down
to is that the $0.15 "minimum charge" is not a real charge once the true-up
period is over, but a provisional placeholder: you pay this with each month's
$12 bill, but at the end of the year, when your real usage is known, you get
back the provisional amount and pay the real amount. At the end of the year,
you take your usage charge/credit, and add the meter charge ($0.25 per day or
about $7.50 per monthly bill or $92.33 in a full year[^9]), and that's what you
owe for the year. Except you've already paid that meter charge, plus you've
paid the "minimum" usage charge as a provisional placeholder. So subtract the
provisional usage charge ($0.15 per day or about $4.50 per monthly bill or
$53.96 in a full year), and you have the amount that's unpaid, that you must
still pay in order to True Up. So, your first 11 bills are for 30-ish days of
meter charges and minimum charges, totaling about $12; your 12th bill is for
30-ish days of meter charges, minus 335-ish days of minimum charges, plus your
cumulative usage charge for the whole year. In my case, actual usage at the
end of the year was $60.22, of which $46.27 had already been paid monthly as
that "minimum" charge, so what I'd call the actual true-up component was
$13.95; add in $8.07 in meter fees (32 days at $0.25/day) for the final
billing period and we have what PG&E calls my true-up bill of $22.02.

## Cancelation across TOU periods

I was curious whether a surplus in one TOU period (for example, summer on-
peak, which is likely the best case for residential solar customers) can
partially or wholly cancel a deficit in another TOU period (for example,
winter off-peak, which is pretty much entirely dark, and thus worst-case for
solar customers). As it turns out, PG&E doesn't directly add and subtract
usage across TOU periods; they convert usage to a dollar amount every month
(based on TOU periods and tiering), then add and subtract the monthly dollar
amounts. This is a clever way of accounting, since it's pretty easy to
understand, and does a pretty fair job of reconciling the amounts from
different TOU periods. (In fact, it works out pretty well for residential
solar customers, since your summer on-peak surplus is credited at a higher
rate than that winter off-peak deficit.) My only complaint here is again that
the tiering calculations are done per month and only affect you on the
downside.

## Raw facts

Here are the actual numbers from my house over the last year, which may be
helpful in understanding the derivations here, making the descriptions more
concrete, and/or planning your own PV solar system.

  * Generated by solar: 7195 KWh
  * Bought from PG&E: 1601 KWh
  * Total consumed: 8796 KWh
  * Months with positive grid usage, resulting in PGE charge: 6 (Oct-Mar)
  * Months with negative grid usage, resulting in PG&E credit: 6 (Apr-Sept)
  * Whole-year usage charge: $60.22
  * Value of electricity consumed if I had to buy it all from PG&E: $2052.34 (assuming E-1 and not E-6 billing, since I don't have the generated KWh broken out by TOU period)
  * Prior-year electric bill: $1403.77
  * Granular usage (from PG&E's point of view), broken down by month and TOU billing period:

## Sum-up

The true-up billing method mostly but not entirely allows you to smooth out
the seasonal variation, canceling bad performance one month against good
performance in another month.

You can understand your monthly bills if you think of them like this: $12 a
month, $7.50 of which is just for the privilege of being connected to the
grid, and $4.50 of which is a deposit against your actual usage. Meanwhile,
the actual usage bill accrues in the background, and at the end of the year,
you pay this balance minus a $49.50 refund for those eleven $4.50 deposits.

Due to the low NCS reimbursement it still seems to me that the optimal array
size is what brings you very close to even for the year, offsetting your usage
without generating much of a surplus. However, due to the way usage tiers are
finalized each month instead of across the true-up period, sizing your array
slightly larger than this may pay off by reducing higher-tier winter bills,
even though the net surplus KWh aren't themselves valuable in the NCS
calculation.

[^1]: The baseline usage, which determines the details of the tiering calculation, further varies by where you live in California and whether your home has a gas or electric primary heat source.

[^2]: You can opt into TOU billing regardless of whether you have solar or other generation facilities, but in general, it makes a lot of sense if you have generation capabilities and less sense if you don't, plus most people not planning on adding solar won't have the TOU option waved in their face and probably don't even know about it. I don't know the exact numbers, but I presume most NEM customers opt for TOU billing, and most grid-only customers do not.

[^3]: There's another confusing way they split things up, but I'm not denoting it as an axis because it's not orthogonal to the others. PG&E separates the rate into separate quantities for "generation", "transmission", "distribution", and "the funding of public purpose programs". We'll come back to the reason for this bookkeeping sleight-of-hand later; it doesn't really matter unless you generate a surplus, but if you do, look for this to raise its head in the Net Surplus Compensation calculation.

[^4]: If you believe solar power is cleaner than grid power, the ecologically optimal size for your home array is "as large as possible", though of course there's some ecological cost to PV panel manufacturing too. But if you're trying to make your solar array economically viable, you'll want to compare actual costs and benefits; the costs depend on the cost and output of the array and how long you plan to keep it and whether you buy or lease and the details of the financing, all things you can find [companies or calculators](http://www.gosolarnow.com/NetMetering.html) to help with. The benefits depend on what you're actually paying for grid electricity, which follows the complicated calculations already described. If you're a light user paying baseline $0.12/KWh rates, you'll save less than a heavy user paying 4th-tier $0.34/KWh rates. While the specifics vary, it's probably easy to generate solar power for less than $0.34/KWh and somewhat hard to generate solar power for less than $0.12/KWh. What this means is most solar customers try to offset most but not all of their own usage, to get back down in the baseline tier. It's often not cost-effective to compete with PG&E's baseline rates. It's especially cost-ineffective to operate at a net surplus, because of the way PG&E values the surplus: read their [Net Surplus Compensation](http://www.pge.com/myhome/saveenergymoney/solarenergy/afterinstalling/ab920/) rules, paying special attention to the last section, "Why is NSC less than the credit on my NEM statement?". In short, PG&E splits the "retail" rates that you're used to seeing into separate components for generation, transmission, distribution, and the funding of public programs like nuclear plant decommissioning; your NEM credits come back at the retail rate until you hit break-even; however if you operate at a surplus, PG&E pays only a "wholesale-type rate for generation". You can see the actual breakdown on the E-1 or E-6 billing schedules; I don't actually know how to calculate the breakdown for E-6 since your surplus is for the year and it's not clear which TOU rate to apply; in any case generation is less than half of the total.

[^5]: Actually not _with_ my electric bill, because I've opted for paperless billing and told PG&E to stop sending me paperless bills, and I can look at the details on the website. But none of the NEM details are available on their website, nor is there an option to go paperless for the NEM data. So what actually happens is the NEM data shows up on paper in my mailbox a few days after I get the bill itself electronically.

[^6]: Which direction it swings will depend on when your true-up period starts. Mine starts in October and so the first few months are fall and winter, and I accumulated quite a large charge before April when I started getting credits. By the following October, it was nearly back to 0. If your true-up period starts in April, you'd presumably see the reverse, amassing a series of credits and a large negative balance over the summer before winter charges start to eat away at the credit balance.

[^7]: PG&E's explanation of how to read this is split into four pages on their website, for the [monthly statement](http://www.pge.com/myhome/myaccount/explanationofbill/nem/), [monthly bill](http://www.pge.com/myhome/myaccount/explanationofbill/nem/monthlybill/), [true-up-statement](http://www.pge.com/myhome/myaccount/explanationofbill/nem/trueupstatement/), and [true-up bill](http://www.pge.com/myhome/myaccount/explanationofbill/nem/trueupstatement/). These pages explain the meaning of each item on the bill, but don't explain how the amounts are calculated, or why you owe what you owe.

[^8]: The true-up calculation doesn't affect the monthly usage charge calculation, but arguably it should, because the rates depend on tiering, the tiering depends on usage, and usage is supposed to be smoothed over the entire true-up period. But actually, the tiering calculations are done entirely inside each month. What this means is that in the winter when your solar array is underperforming, higher usage might push you into the upper tiers, and you'll pay more for your grid electricity because of this, and no amount of summer credits can offset these higher rates. Again using my first-year numbers as an example, my assigned baseline value for the year sums to 2878 units, and my actual cumulative usage was 1601 KWh. (Or: the average of the monthly baselines was 240, and my average monthly usage was 133.) I'd argue that this means I should be paying only first-tier rates. However, because of the seasonal variation expected with solar generation, my usage from PG&E's point of view is skewed heavily toward winter, and in fact I had above-baseline usage in only the 4 shortest months: November through February. Because PG&E applies the baseline-to-tier calculation on each month's usage individually, instead of across the true-up period, I paid substantially more for electricity in those 4 months. In my case, I was charged $60.22 for my electricity usage, but if it had all been at baseline rates, I would have been owed a $5 credit.

[^9]: I'm writing this after my first year of NEM, and the PGE switched me over to NEM billing in the middle of a billing month without changing the billing cycle, so my first month's NEM bill only included 9 days, and so my first true-up period of 12 bills is only 11 1/3 months or 345 days. Presumably, future true-up periods will be a full year.

