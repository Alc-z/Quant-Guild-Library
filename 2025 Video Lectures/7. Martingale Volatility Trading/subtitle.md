---
title: "Martingale Volatility Trading"
source: "https://www.youtube.com/watch?v=Q1lxVrLHrYE"
author:
  - "[[Roman Paolucci]]"
published: 2025-02-22
created: 2026-06-13
description: "*🚀 Master Quantitative Skills with Quant Guild*https://quantguild.com*📈 Interactive Brokers for Algorithmic Trading*https://www.interactivebrokers.com/mkt/?src=quantguildY&url=%2Fen%2Fwhyib%2Fov"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Q1lxVrLHrYE)

\*🚀 Master Quantitative Skills with Quant Guild\*  
https://quantguild.com  
  
\*📈 Interactive Brokers for Algorithmic Trading\*  
https://www.interactivebrokers.com/mkt/?src=quantguildY&url=%2Fen%2Fwhyib%2Foverview.php  
  
\*👾 Join the Quant Guild Discord server here\*  
https://discord.com/invite/MJ4FU2c6c3  
  
Check out my new free open-source market-making game:  
https://practicemarketmaking.com  
  
Jupyter Notebook:  
https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/7.%20Martingale%20Volatility%20Trading/Martingale%20Volatility%20Trading.ipynb  
  
Black-Scholes Equation Derivation:  
https://www.youtube.com/watch?v=2iClLEfXuqA  
https://medium.com/swlh/deriving-the-black-scholes-model-5e518c65d0bc  
  
European Options 101:  
https://www.youtube.com/watch?v=HgjeDJVCHSo  
  
Market Implied Volatility:  
https://www.youtube.com/watch?v=VzieTIsBaHM  
  
Articles and code walkthroughs can be found on our blog  
https://medium.com/quant-guild  
https://romanmichaelpaolucci.medium.com/  
  
For more free tutorials and references see our GitHub  
https://github.com/RomanMichaelPaolucci  
https://github.com/Quant-Guild

## Transcript

**0:01** · \[Music\] welcome back today what I want to do is talk about Martin Gail betting Theory we'll use a casino as an example it's kind of the canonical example for any sort of betting strategy we'll take a look at meanor version and or lback process and how that's typically used to model volatility you may have seen an extension of the black schs model maybe like a hon model where volatility is treated as a stochastic process then

**0:29** · what we're going to do is we're going to try to apply the Martin Gill betting Theory to volatility trading we'll see if we can continue to take a short position in say the vix and then double down on that short position every day or week to try to cover our losses and gain

**0:46** · some money some p&amp;l and that's what it's all about at the end of the day so for starters let's take a look at roulette we're going to simplify roulette no zeros no greens we're just going to talk about black and red here and we're going to take a look at what happens every time you lose and then double down so suppose that you have an initial bet size B after n losses the total amount wagered is going to be B plus 2 B plus 4B plus so on until you

**1:18** · get 2 to the NB where n is your total number of losses so if I bet 100 bucks and my first loss is going to yield you know a loss of 100 bucks I'm going to go ahead and bet 200 the next time around and then my total amount wagered is going to be T of 1 which is going to go ahead and

**1:40** · be 2 to the first Power \* B which is 100 and then we have our initial bet of 100 so 300 total wagered and you can go ahead and do this recursively you can continue to compute the total amount wagered it's not super difficult really all we're doing is every time we lose we Double Down Double Down Double Down you know depending on how how much Capital you got this may or may not be a good idea regardless at the n+ one bet

**2:11** · your total profit is going to be B minus t subn + 2 to the NB and this strategy assumes that you have some sort of infinite Capital capacity of course maybe unrealistic in practice but some people do have quite a bit of money maybe close to infinite money so this may be even somewhat practical for them now why is this an issue for casinos well the expected value of the Mart Gale strategy so this particular betting strategy is actually your initial bet size so after one round

**2:44** · of Martingale the EV is going to be B which is positive and if you've seen any of my previous videos I talk about you know making decisions that yield positive expected value to accumulate profit over time we don't know what's going to happen in the short run but if you can make decision ision that contribute to positive EV over time that's how you accumulate p&amp;l that's how you generate wealth well this is a problem for cassin because if I could walk in and I could do this Martin Gale strategy continue to double down on my

**3:14** · losses then I have positive EV and I can continue to do that and continue to take money from the casino in the long run again it's not about the short run it's about the long run so let's take a look at the expected value here what we do is we are going to wait each outcome by the associated probability that is each profit gets a probability weight by the likelihood of the outcome and this turns into some sort of geometric series which will eventually

**3:42** · converge to B okay so what is the issue with this well clearly The Profit has a positive expectation for the player the casino is going to lose money over time therefore we really don't want that we really don't want that as the house we really don't want that as a casino we don't want to give the players the now some games you may consider fair you know others you know there's an edge towards the casino and that's how they generate money in the long run and you know we talk a lot about probability statistics we talk about casinos in the

**4:14** · realm of of Finance because that is a very canonical example of you know just odds in general it's not necessarily saying that Finance itself is gambling depending on what you do it may may be gambling but you know there's a very big difference between just arbitrarily gambling investing and you know we we

**4:34** · got to try to draw a line somewhere there but nevertheless let's continue to look at this so through this strategy we get positive expected value casinos don't want this the house doesn't want this we're going to throw limits on roulette for example so that they can't double down at some point and you know those short-term losses are just going to accumulate and and you're not going to be able to recover this so if I lose $10,000 and I can't double down then how

**4:58** · can I possibly hope to have positive expected value if I do 10,000 again that's not going to yield the positive expected value that I'm looking for so that's an important idea right just because it's capped at 10,000 doesn't mean if I keep betting 10,000 I'll eventually regain those losses you need that doubling down that's the process itself that yields the positive expected

**5:19** · value now we talked about getting to the long run and that's true positive EV to get to the long run but what does the short run look like what is the probability of surviving the short run with some sort of Martin Gale strategy well if you just take a look the total amount wagered is going to be proportional to 2 to the N which is exponential so that can be a problem because after 10 losses you take your initial bet b and you have a a coefficient of 2,47 then after 20 losses you have a coefficient of 2 million so your bet

**5:52** · size blows up right and that's really the issue with this strategy is if you don't survive the short run you blow out your account account and now there's no more recovering losses there's no more positive expected value and that's really the game that we play right whether you're a market maker a Cino a player in a casino or a market participant you need to figure out what it is you're trying to do what your strategy is what your expected value is

**6:17** · and how you can survive the short run to get to the long long run to to kind of reap the reward of that expected value over time what I have here is a simulation of the Martin Gale strategy with roulette so every time I run this

**6:33** · we're going to essentially try to win win money from roulette and we are going to play until we win so if we lose we'll double down if we lose again we'll double down and every time I run this so we won we won we won I run it again we

**6:50** · win here we lost the first round so we double down we win the second round as you can see eventually you always end up at this 1,0 right so my you know initial bet is 10 my Max rounds is 10 here just for the sake of the simulation and then the bank roll is 1,000 so you can see as I keep running this here's a very good example is we keep doubling down we keep doubling down so 990 970 930 850 very

**7:17** · quickly we're starting to increase you know this is this is not going linearly right this is going 30 then it's 40 and then it's going down all the way to 80 so that is that 2 to the n and here we can see eventually we do hit that win and we get back to the 1010 but this is the problem right eventually this is going to hit really really big loss streak maybe 20 losses and we're

**7:42** · going to completely blow out the account in fact with a bank roll of a th000 it's not going to take 20 losses it's going to take roughly what is that close to 10 maybe 10 losses or something like that so it's very important to understand that idea now here's the deal if you do

**7:58** · survive the short run you don't blow out your account or you have infinite money which you know you wouldn't be doing this but you can go ahead and actually simulate the outcome of this Martin Gale strategy and roulette over time so as you can see you kind of have these manic highs and lows locally but over time you still have this cumulative wealth that is positive and this is really what it means to have a positive expected value

**8:22** · now this is all well and good but what does the actual bet sizing look like here's the issue right take a look at this bet sizing So based on all these game numbers you have a th games eventually the BET size spikes up look at this we're betting you know over $1,200 here a variety of different times

**8:41** · so you're risking a significant amount of capital cumul cumulatively to attempt to recoup your losses but also regain that you know initial wager back you know that's how you accumulate the wealth is you bet 100 or you bet 10 and then you know you get that that 10 back plus 10 here you know in this case scenario you could see that it's it's not a a nice low constant stable bet

**9:08** · size but rather you know over the significant number of games that we play here it does tend to blow up so you can see the positive expected value but if you blow out your account in the short run due to this bet size and you can't double down or there's limits then you can't use this strategy and it's it's not productive okay so that's the idea of Martin Gale at least in a nutshell what about applied to the financial markets well we don't really have just a way to

**9:35** · 50/50 the the financial markets of course there's you know different types of contracts you might be able to engage in and you may argue that they're 50/50 I I would argue that more likely not the implication is that they're 50/50 or there's some sort of implied probability that they're 50/50 but let's take a look at this this sort of example in the context of volatility trading mean

**9:57** · reversions so the on sign L back process models uh meanor version so it could be used for rates it could be used for volatility here I'm I'm kind of just showing the process itself it's a stochastic differential equation and you can simulate this stochastic differential equation and it's going to give you a path over time now this red line represents the mean level and what you'll notice is as I continue to generate paths the path tends towards

**10:24** · the mean and if it goes too low it starts to tend back if it goes too high it starts to the 10 back and there are processes in the financial markets that emulate this Behavior specifically volatility if you take a look at the vix right the vix based off of the implied volatility of the S&amp;P 500 options we

**10:46** · take a look here and this is the mean level here typically it's below 20 this is the mean level you can see that as there are these spikes it does revert back to this mean level here so one one strategy perhaps to you know apply what we had just talked about in roulette to the financial markets is realizing hey well if volatility tends you know tends towards the mean and the mean tends to be around 20 then if we deviate from the

**11:14** · mean so if we go up shouldn't we just take a short position and if it continues to go up double down on that short position and continue to do that until you know we start to ride the Vault down and we just collect essentially the the cash for borrowing those shares then we can buy back the shares cover the shares in the Market at a lower level and you know we'll we'll make out with that profit that is one theoretical

**11:41** · implementation of Martin Gale and I actually have a simulation of it here so what I'm going to do is I'm going to go ahead and I'm going to apply that Martingale strategy to the the vix this historical data and I'm going to enter a short position every day if there's a loss I'll double down if there's not a loss I'm going to collect that premium and you can take a look at what this Equity looks like over time it's like wow you know this is this is tremendous we're we're certainly gaining a lot of equity value here and what you'll have

**12:09** · to notice is the the final Capital may be you know roughly what is this 700,000 or something but your exposure is significantly higher than your final Capital so if you took a look at the sharp ratio this would just be absolutely exous for the amount of capital that you risk to acquire this Equity curve moreover another issue is you may not have the capital to continue to short the the vix itself so you're on

**12:38** · margin when you go ahead and and short the vix here you're eventually going to run out of capital right so if I continue to try to double down then eventually I might get a margin call and I'll have to liquidate the position at a at a losser or I'll blow out my account I'll be bankrupt or I might ow money so

**12:58** · that's an important idea as well to remember so even though going short collecting that you know collecting the cash for going short eventually you could buy back those shares at a lower level theoretically yeah that works great if you could do that survive the short run get to the long run yeah fantastic however you know with events like 2020 if you go all the way back to events like 2008 2001 even these spikes here to like 40

**13:24** · and 50 they can completely blow out your account so when you're taking a short position let's say you start doubling down at at you know 25 if we ride all the way up to 40 there's no way that you're going to be above water you're going to have to liquidate at a pretty massive loss so important to keep that in mind that is just uh I think this is a this was a fun video to make I wanted to kind of talk a little bit about you know an application of probability

**13:52** · to not just like not just casinos and and trading but I wanted to kind of go from from Theory to practice theory to practice so you know the idea here was we started with the Martin Gil betting Theory we talked about it theoretically in roulette positive EV we talked about it in practice how eventually you're going to have a bet size that kind of just blows up and it's not practical similarly we talked about theoretically with mean reversion how well hey if you know we have this process that reverts to a level over time then we can take a

**14:24** · position and maybe double down on our losses when it goes against us to apply that theoretical betting strategy to the process that is mean reverting but of course in practice you're going to have a crazy amount of exposure and margin to answer to and that is no good that is no good for getting to the long getting to the long run so I hope you enjoyed this video this was a fun one to make and I'll see you in the next one