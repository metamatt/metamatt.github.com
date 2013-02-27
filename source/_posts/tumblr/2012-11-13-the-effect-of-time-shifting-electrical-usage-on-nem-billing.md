---
layout: post
title: The effect of time-shifting electrical usage on NEM billing
tags:
- solar
- energy
comments: true
---
One more post on the topic of PG&E bills for solar (NEM) customers.

PGE's NEM billing scheme [blends usage across
seasons](http://blog.metamatt.com/blog/2012/11/09/one-year-of-solar-power/) to
allow for seasonal variation in generated power, and their E-6 billing scheme
[separates usage into 5 time-of-use
periods](http://blog.metamatt.com/blog/2012/11/11/e-1-vs-e-6-for-residential-
solar-customers/) to encourage customers to shift usage away from peak
periods.

A question that just occurred to me is whether you can game their billing
results by time-shifting usage around inside the same true-up period, between
TOU zones, months, or even seasons.

It's pretty easy to move usage between TOU zones of the same day (say between
summer on-peak and summer off-peak) by delaying energy-hungry activities like
baking pies until night; that's both tractable for a home customer and exactly
the kind of behavior the E-6 TOU billing rates are designed to encourage.
Moving usage between TOU zones of different seasons (say between summer on-
peak and winter off-peak), or even from one monthly billing cycle to another,
would be more difficult (it's possible in theory but doesn't really match
human activity patterns to delay all your energy-hungry activities for months
and then execute them in a big batch months later; alternatively you'd need a
really big battery which is exactly what grid tie-in lets you avoid), but I'm
still curious if it would be advantageous in some circumstances.

Again drawing on the example of my last year's experience, the answer turns
out to be yes for both forms of time-shifting. Say you're going to bake a
bunch of pies, and need to run the oven at 3KW for a little over 3 hours,
consuming 10 KWh of electricity. (The 3 KW figure is realistic for an electric
oven; the heating element running continuously is not; ignore that in the
service of an example.) If you're going to consume that 10 KWh, does it matter
_when_ you consume it; what's the effect on your final true-up bill of adding
10 KWh at various different times?

If you can move that 10 KWh from a higher-value TOU period to a lower-value
TOU period in the same day, you win; this turns out to be independent of
tiering, consumption, or which month or season you're in, which is a nice
property. It won't change your overall consumption for that day or month, so
it won't change your tiering calculation. If you had a surplus in the higher-
value TOU period, you'll now have a bigger surplus, which at the higher rate
is more than enough to buy the same electricity back from PG&E later in the
day, even if the solar cells aren't producing at that time. (Basically, it
wasn't immediately obvious to me what the credit/charge calculations do in
this case, because my intuition keeps wanting to tell me it's better to
consume energy when I'm getting it free from my solar panels than when I'm
buying it from PG&E. That turns out not to be true; the NEM system means if
you buy and sell the same amount of electricity at a given rate, it's a wash,
and the TOU system actually rewards you for selling it at a higher rate and
buying it back at a lower rate.) So yes, you can "game" the E-6 billing system
by moving usage from peak times to off-peak times, which use of "game" gets
scare quotes because it's actually the behavior they want to encourage.

Meanwhile, if you could move that same 10 KWh across months, the story is a
lot more complicated. Due to tiering, you may be paying more than the baseline
rate for some of your electricity, and since PG&E applies the tiering
calculations entirely inside each month, based on that month's usage, you can
actually get crossover between "high-value" and "low-value" TOU periods. More
concretely: as a solar generator, you may be paying more for winter off-peak
electricity at 3rd-tier rates than you are for summer part-peak electricity
where you never exceed the first tier. This is exactly what happened to me
over the last year (note in the [E-6
schedule](http://www.pge.com/tariffs/tm2/pdf/ELEC_SCHEDS_E-6.pdf) that winter
off-peak and part-peak above 130% of baseline cost about what summer on-peak
baseline usage does, and winter off-peak and part-peak above 200% of baseline
cost more than the summer on-peak baseline). While from the previous example
you'd expect the result of time-shifting your usage to depend on the TOU rates
(and you would win by shifting from a high-rate TOU to a low-rate TOU, and
lose by doing the reverse), in fact it also depends on the tiering
calculations, and you can also win by shifting usage out of a month where you
had higher-tier usage into a month where you didn't, and this can even be true
if it involves shifting that usage from a low-rate TOU to a higher-rate TOU.
So, surprisingly, you could see a net benefit from moving usage from winter to
summer; it's pretty easy to make the numbers work out if moving from winter
part-peak to summer part-peak, and in extreme cases, you could even win by
moving from winter off-peak to summer on-peak. This is decidedly not the
result they want to encourage, so I'd call it gaming the system. (Of course,
you'd need a way to actually buffer your usage across months; a better way to
lower your winter bills is to simply use less electricity, without
compensating in the opposite direction in the summer.)

I'll note again that this perverse result derives from the fact that PG&E
calculates and finalizes the tiering calculations entirely inside each month,
instead of smoothing them across the true-up period, so it's actually possible
for a big energy user with an even bigger solar array to generate a net
surplus for the year but be paying 4th-tier rates for winter electricity when
the array is underperforming.

