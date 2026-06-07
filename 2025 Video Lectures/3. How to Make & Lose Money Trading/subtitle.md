---
title: "How to Make & Lose Money Trading"
source: "https://www.youtube.com/watch?v=WP9fb7AMFsI"
author:
  - "[[Roman Paolucci]]"
published: 2025-01-18
created: 2026-06-05
description: "*🚀 Master Quantitative Skills with Quant Guild*https://quantguild.com*📈 Interactive Brokers for Algorithmic Trading*https://www.interactivebrokers.com/mkt/?src=quantguildY&url=%2Fen%2Fwhyib%2Fov"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=WP9fb7AMFsI)

\*🚀 Master Quantitative Skills with Quant Guild\*  
https://quantguild.com  
  
\*📈 Interactive Brokers for Algorithmic Trading\*  
https://www.interactivebrokers.com/mkt/?src=quantguildY&url=%2Fen%2Fwhyib%2Foverview.php  
  
\*👾 Join the Quant Guild Discord server here\*  
https://discord.com/invite/MJ4FU2c6c3  
  
I hope you enjoyed this lecture, please feel free to leave a comment or reach out to me with any questions.  
  
Problems with Statistics in Trading Jupyter Notebook:  
https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/3.%20How%20to%20Make%20%26%20Lose%20Money%20Trading/Problems%20with%20Statistics%20in%20Trading.ipynb  
  
Articles and code walkthroughs can be found on our blog  
https://medium.com/quant-guild  
https://romanmichaelpaolucci.medium.com/  
  
For more free tutorials and references see our GitHub  
https://github.com/RomanMichaelPaolucci  
https://github.com/Quant-Guild

## Transcript

**0:01** · \[Music\] and we are back welcome back today what I want to do is talk about problems with Statistics in trading this is the only video that you need to understand probability and statistics in the context of trading this is not going to teach you all of probability and statistics but this is going to highlight some of the major issues with the application of probability and statistics at an undergraduate grad uate level in the context of trading some

**0:33** · sort of product whether it be a derivative product equities Etc I've been doing a lot of trading recently on my own and I thought that this would be particularly relevant and interesting so without further Ado let us head on over to my Jupiter notebook and we can go ahead and get started so clearly we need to model the particular

**1:00** · product that we are trading if we had the underlying density the structure of the underlying density for the process there would be literally no reason to develop a model we would just use that density to derive all of our statistics and probabilities and all would be well in the world but instead we're left with this this open-ended issue of of modeling the Dynamics of some sort of process whether it be a stock price path or the appropriate value for a

**1:30** · derivative product whatever it is we're trying to model or whatever it is we're trying to price or or anything like that it's a a very open-ended question now what I want to do is start with a very fundamental issue in statistics and that is parameter estimation and I want to progress down to the idea of stationerity and Edge in trading and how all of these things kind of work together and by the end of this video you'll have a a really nice big picture of how statistics can be used

**2:00** · for trading and identifying profitable trading strategies and identifying if your strategy could be profitable um but also the pitfalls that you can run into in implementing your trading strategy so number one is parameter estimation so I had said that if we knew the underlying structure of the density or the Dynamics of the process we would have no reason to implement a model that's pretty fancy what does that mean well what I'm saying is I'm going to draw a parallel to a

**2:30** · coin flip process here so what I have here is I'm going to flip a coin 10 times and the parameter for each coin flip that is the probability of a heads is going to be 0.5 so each coin flip has a 50% chance of landing on a heads I'm going to constitute that as a success and then that's going to be an

**2:50** · outcome of one if I land on a taals then I'm going to get a zero and I'm going to do this 10 times and and what you'll see here is I have a list of the outcomes and I have two heads and I have eight tails now clearly this is random

**3:08** · every time I do 10 coin flips I'm going to get a different set of results it's finite that is in in the context of how many combinations and permutations of heads and tails are there there is a finite number of those but each trial

**3:24** · itself of 10 coin flips is going to be random so parameter estimation is a fundamental problem in statistics and we have a lot of tools to be able to estimate population parameters so again parameter being this 05 if we knew what this 0. five was in the context of the the stock market whether it be some sort of like I said derivative product or underlying Equity process regardless if

**3:50** · we knew what the parameter set was in the Dynamics then we wouldn't need to estimate anything so we don't have that5 in the context of the market so the best we could do is look at data and try to build a model using that data to parameterize some sort of model this brings us to problem one parameter estimation we have a lot of tools at our disposal confidence intervals simulation variance reduction we have a lot of tools we can use historic data whether

**4:19** · or not that's appropriate we'll talk about in problem two but here is just one example of an issue with parameter estimation well take a look at this what if these 10 trials were the only trials that I could observe I can't repeat this process think about it the previous 10 days of trading only occurs one time I can't repeat that so if I take the average number of heads here I'm going to get 20% that's going to be my estimated

**4:51** · parameter the particularly Keen among us maybe talking about variance and confidence intervals and you know I I commend you but let's go ahead and and digress from that notion for now and just take a look at a simple parameter estimation we have two of the 10 flips being heads so wouldn't it be reasonable

**5:09** · if I didn't know what the parameter was we know the population parameter is 0.5 but if I didn't know 20% might be a reasonable guess okay that brings us to the first issue of parameter estimation okay there is a lot that you can do simulation variance reduction ction

**5:30** · aiding in tightening the the bounds of a confidence interval to provide a more precise estimate as to whether or not that interval contains the parameter but again this is a a fundamental issue so that's going to be problem one parameter estimation is how do you

**5:49** · determine what that parameter should be in the context of a traing strategy you're not just looking at 0 five as the probability of heads or tails you're looking at the probability of a winning trade and the probability of a losing trade it's the same idea as a coin flip heads and tails but here you need to estimate that probability do you trade a 100 days is that enough data to estimate your

**6:21** · probability so hopefully this is starting to become a little bit more apparent as to why this is an issue you only have so much money to trade with and more often than not if you're testing a strategy you're going to lose it so what about back testing can't you just back test your strategy and then take a look at the probabilities well

**6:39** · yes and no this brings us to problem two so problem one is parameter estimation you can either trade live and try to determine your your winning probabilities and determine whether or not your strategy is going to be profitable in the long run if you have some sort of edge otherwise you can back test but what's the problem with back testing that's that's this idea of stationerity so what is the issue with

**7:02** · this idea of stationarity well in the context of our coin flip experiment you can take a look at each coin flip as an experiment you can take a look at each trade as an experiment the population parameter. 5 is not going to change that is a key underlying Assumption of our parameter estimation is that it is not a function of time if we come down here to

**7:28** · the idea of stationerity let's take a look at what happened here well in the previous 10 coin flips I have observed seven heads so I've estimated the parameter to be 7 but the true parameter is actually

**7:46** · 46 okay if we were to reiterate this experiment let's say another 10 trades go by or 10 coin flips you can use either as an example here we have a pretty reasonable estimation of the parameter the true parameter is 0.51 and our estimation was 0.5 but we repeat this again and we could see okay our estimated parameter here is .2 but the true parameter is 04

**8:09** · and all I'm saying is I'm letting this P value change with time randomly so I'm saying the parameter p is a random function of time which is very reasonable for the Dynamics that govern a stock price process or some sort of trading strategy that is a Time dependent function of a stochastic process and this is the key issue we're either underestimating or overestimating the probability because the parameter changes over time when does it change I

**8:41** · have no idea is it going to change every 30 minutes every 20 minutes every hour every 10 days we have no idea you can back test all you like but this is the same reason why historic results are not indicative of future performance is cu of this key issue with with stationary stationarity we have no idea what the parameter is going to be and when because if we did we wouldn't need to try to model anything we wouldn't need to try to estimate any parameters so this is the key issue with

**9:13** · stationerity that is the parameter of the underlying density or the parameters of the underlying density or the Dynamics of the process are going to change over time and you'll see a lot of different processes that try to emulate this behavior and what ends up happening is you have some sort of stochastic term

**9:35** · that evolves over time and that's scal by some sort of time dependent function and you know you can take a look at things like maybe a local volatility you could take a look at stochastic volatility that aim to capture that that parameterization over time but it is a a very non-trivial task and of course the Dynamics themselves are stochastic so we have this fundamental issue here so that's the second problem here we're going to transition to this idea of edge

**10:02** · but before we do I want to emphasize that these are not the only issues these are just some very prevalent issues in applying basic statistics to the idea of trading you could have violations of Independence you could have a violation

**10:18** · of the density assumption that you're assuming your returns are distributed as you could say that they're normally distributed or log normally distributed when in reality they have uh excess curtosis and they leptokurtic and all the moments don't match and you have all of these different issues there's uh volatility clusters leverage effect so on and so forth so there are a variety of issues baked into the actual empirics

**10:42** · of the financial markets but for now let's just take a look at these in the context of a simple trading strategy and see why we have an issue with parameter estimation and stationarity by looking at a trading strategy so what is Edge Let's Start with this idea of egge I think in simple terms we can just say egge is the idea that if you were to reiterate this experiment whether it be playing roulette or trading a particular

**11:13** · strategy in the long run you're going to make money and that can constitute what's known as a positive drift in other words supposing that you don't go bankrupt first which is more of like a gambler's fallacy sort of of problem you will make money in the long run assuming this expectation is strictly positive and is going to maintain its positive nature over time keyw maintain positive nature over time

**11:45** · time okay let's break down this this expectation here and talk about the implication so for any trading strategy s we could say that that's Buy on close sell on open Buy on open sell on close Buy on open sell midday buy when there's an imbalance sell when there's momentum whatever it may be we can define a trading strategy s and the expected p&amp;l

**12:11** · will always be as follows the expectation of s is equal to the expected p&amp;l when you win times the probability of a win plus the expected pnl when you lose times the probability you lose and that is going to be the same as the unconditional average of your overall pnl but this is going to give you more information why because it tells you how your win and loss ratio plays into your overall trading eggs your expectation of your p&amp;l over

**12:43** · time okay but what are these values clearly we do not know we can get these values one of two ways we can back test obviously there's a whole set of issues with back testing you can have look ahead bias you can fit a curve you can do 10 ,01 things wrong in estimating these probabilities even more issues and

**13:04** · bias than I've already discussed or you could trade live you could trade live with your own money and then try to estimate these probabilities so this takes us to that first issue of parameter estimation how much is enough what is a reasonable amount of data to use and when do you change these values maybe you change them on a rolling basis every week maybe every two weeks so on and so forth it's important to keep that in mind is they are not not stationary so these two issues immediately play into the expected p&amp;l of our trading

**13:35** · strategy so what do I do well I'm going to take data that I have here from trades and I'm going to compute the expectation of my trading strategy the expected pnl so here's my data I have p&amp;l of 150 120 90 100- 300 - andus 50 I

**13:55** · have four wins and three losses so what can I do well I can derive of each piece of this equation and then glue it together to get the overall expectation so the expected p&amp;l when I win is 115 the expected p&amp;l when I lose is minus 150 the probability of a win is .57 roughly and the probability of a loss this should be a loss is 43 roughly so when I multiply

**14:27** · the probability of a win times the expected p&amp;l of a win plus the probability of a loss times the expected p&amp;l of a loss then I'm going to get the overall expected p&amp;l and that's exactly what this equation here is telling us it's saying if I take the average winner multiplied by the probability of winning plus the average loser times the probability of losing then I get the unconditional average

**14:55** · p&amp;l okay this is great so my unconditional average pnl is 1.42 what I'm going to do is I'm actually going to simulate this trading strategy over time so here I'm going to simulate it for 252 days I'm going to assume that on each day I'm either going to have a win or a loss according to this estimated

**15:16** · parameter set here and after a year of trading this is my outcome well that's not good I'm down 3,000 bucks that's terrible well if I rerun this look I'm up $750 so where's my Edge why am I not

**15:33** · seeing my Edge well if I keep running this I'm going to get different charts it's stochastic but if I increase the days to say 2,000 now we're starting to see some drift if I make it 100,000 now we're starting to see some drift if I make this a million now we're starting to see what I mean by this this drift right we're seeing this this Edge that's exactly

**16:02** · what we have here is even though it's stochastic we have this Edge we're going to have losses we may have big losses we're going to have wins we may have big wins over time everything's going to average out such that we will generate

**16:22** · money over time we will be profitable in the long run you just have to survive the short run here we survive the short run here we survive the short run here we do as well here maybe we would have gone bankrupt first again more of a gamblers fallacy problem from a stochastic processes class but you catch my drift

**16:44** · pun intended so what we have here is we have the equity curve of our strategy and we can see that edge over time as I increase the number of time steps we get this curve going up and to the right that is our income over time that's what we want to see from trading strategy okay but very easily these parameters

**17:05** · just as we saw up here in the context of stationarity and parameter estimation they could be wrong first of all there's no reason why the probability of a win should be 057 and the probability of a loss should be 043 what if in reality we estimated wrong we estimated the coin flip wrong here we said 20% so why is this data to estimate the

**17:31** · probability of a win right if I run this Equity curve look at that that's terrible that is terrible what if we don't include transaction costs this could be even worse okay so in the context of parameter estimation and stationerity there's no reason for this curve to maintain the same parameter set

**17:54** · or the parameter set that we've estimated in the first place is already wrong so those are two potential issues in this idea here okay why is the law of total expectation helpful well if you keep re-evaluating this on a weekly basis maybe you stay current maybe every 30 days so you know

**18:13** · it's completely arbitrary you can determine whether or not you're gaining losing eggs or you know you can take a look at your egge over time and and even plot that and see if in the long run you will have a reasonable strategy that is capable of of generating money so what I have here is a little app I mean I could barely call this an app I would say but if I change this slider I'm going to compute the edge of the trading strategy s so

**18:40** · this is my win probability here and you'll notice that the loss probability is just going to be the complement one minus whatever this value is so if I make the win probability lower let's take a look at what happens to my Edge goes away minus 70 well that

**18:56** · makes sense right because the probability of a loss is much greater than the probability of a win and the expected value of a loss is much greater than a win so this is a terrible strategy this is a terrible strategy but if my win percentage is like 80 then let's take a look at my Edge 67.2 N9 that's that's fantastic here

**19:18** · that's fantastic let's take a look at the equity curve under this condition look at that that's one year if I have 80% wins and my win expectation my my average winner is 115 bucks and my average loser is 150 That's My Equity curve trading that for a year assuming that I can get one trade in a day but what if my win is 10 bucks and

**19:42** · my loss is 150 yeah I have an 80% win rate but what's my Edge minus 17 What's My Equity curve look like that's a terrible Equity curve that is a terrible terrible Equity curve so this is just something to keep in mind that you know when you are trading a particular strategy these things are objective these things exist whether you like it or not you have a win probability that is a Time dependent stochastic function and you also have a

**20:12** · expectation and a you have a win expectation and a loss expectation that is the average winner your average winning trade and your average loser your average losing trade whether you like it or not those things are present and they're always evolving through time so you're going to have to do your best to estimate these values there's a lot of different techniques in the literature I'm not saying these are impossible problems to solve but they are problems that you are going to have to deal with you have to determine whether or not you're using enough data to estimate your parameters are you using too much old data should you wait

**20:43** · new data more how are you looking at your average winner and loser has there been a regime change is it different postco is there a new regulation that impacted your over so do you see how there's so much that goes into determining the actual parameters is associated with the trading strategy trading strategies don't always work sometimes they work for a couple years then they stop working you just got to survive a bonus cycle or two and you'll

**21:10** · get rich and then you'll get fired or the firm will go bankrupt you know so these are kind of the ideas that I wanted to cover in today's video to shed some light on what's actually going on in trading it's not that necessarily people know more than other people or

**21:27** · they have some sort of Mag crystal ball unless they're insider trading which is you know always going to happen anyway but in the context of edge this is exactly what it means is like look at this we have Negative Edge over time we're just losing money versus here if the loss is only 27 bucks what

**21:45** · kind of edge do we have five bucks of edge that's a great Equity curve so I hope you found this this video informative if nothing else maybe maybe slightly entertaining but these are practical statistical tools you can add to your toolbox right now to evaluate

**22:04** · how you're trading you can take a look at your expected loss expected win look at the probability and see hey like you have a negative age over time you're just going to keep losing money or you're going to keep making money maybe depending on how the parameters evolve over time so I'm going to put a link to this Jupiter notebook in the description

**22:24** · box below if you'd like to check it out I'll post it on my GitHub and you can play around with these charts if you have any questions you can leave them in the comment section join Discord tend to be a little more responsive there um but I hope you've enjoyed this video talking about some problems with Statistics in trading and I will see you in the next one if you'd like to see more content like this please let me know other than that thanks for watching