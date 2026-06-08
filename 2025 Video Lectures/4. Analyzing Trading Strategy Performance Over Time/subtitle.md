---
title: "Analyzing Trading Strategy Performance Over Time"
source: "https://www.youtube.com/watch?v=boh9JkGPG9U"
author:
  - "[[Roman Paolucci]]"
published: 2025-01-25
created: 2026-06-08
description: "🚀 Master Quantitative Skills with Quant Guild:https://quantguild.comJoin the Quant Guild Discord server here:https://discord.com/invite/MJ4FU2c6c3I hope you enjoyed this lecture, please feel fr"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=boh9JkGPG9U)

🚀 Master Quantitative Skills with Quant Guild:  
https://quantguild.com  
  
Join the Quant Guild Discord server here:  
https://discord.com/invite/MJ4FU2c6c3  
  
I hope you enjoyed this lecture, please feel free to leave a comment or reach out to me with any questions.  
  
Note: The mean-reverting process is a good example of what you may face when plotting the probabilities over time if severely negative drift is an indication to one that simply "taking the opposite position" or "negating the strategy" is a viable option. In reality, this often makes no economic sense.  
  
Video's Jupyter Notebook:  
https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/4.%20Analyzing%20Trading%20Strategy%20Performance%20Over%20Time/When%20to%20Stop%20Trading%20a%20Profitable%20Strategy.ipynb  
  
Articles and code walkthroughs can be found on our blog  
https://medium.com/quant-guild  
https://romanmichaelpaolucci.medium.com/  
  
For more free tutorials and references see our GitHub  
https://github.com/RomanMichaelPaolucci  
https://github.com/Quant-Guild

## Transcript

**0:01** · \[Music\] and we are back welcome back today what I want to do is build off of the previous video where I discussed how to make and lose money trading in the previous video I Quantified this idea of trading eggs which you may have heard before floating around the trading Space by using the law of total expectation essentially what I do is I quantify a trading strategy and I derive the EXP Ed

**0:30** · value of that trading strategy on a per trade basis by taking a look at the probability of winning the probability of losing the average p&amp;l for a winner the average p&amp;l for a loser and if that is overall positive then we say we have a positive Edge or a profitable trading

**0:53** · strategy this is clearly a non-trivial task this is what Traders all around the world try to do on a daily basis but what I wanted to really emphasize today was the idea of when to stop trading

**1:08** · what would otherwise have been a profitable trading strategy and this could be for a variety of reasons there could be a regime change maybe the macro conditions have changed maybe people have caught on to this and there's there's less capacity to trade this type of strategy um I'm really talking about systematic trading strategy statistical trading strategy is a large cross-section of equities and you're doing some sort of of condition to buy and sell on a daily basis based on some

**1:39** · sort of signal that you've developed and the idea that I'm trying to emphasize here is the parameters that we estimate for our trading Edge are themselves governed by some sort of unknown density and that density has the propensity to be non-stationary so the problem is we can't continuously get a good estimate

**2:11** · for the probability of a winner the probability of a loser in fact when we start to lose more than we win we may never see the conditions for success in that system again this will become more clear when we start to look at the charts but let's go ahead and break down this idea of egg really quickly right here and then we're going to take a look at some charts and hopefully Hammer this idea home so we

**2:36** · have egge defined as the probability of a winning trade times the p&amp;l of the average win less the probability of a losing trade times the average p&amp;l of a losing trade of course if this is positive you'll make money over time if this is negative you'll lose money over time the problem is in the context of

**2:57** · parameter estimation we don't necessarily know the we absolutely don't know the density in which these originate from and that density as I said has the propensity to change over time that's this idea of non-stationarity so it's definitely a difficult problem it's not impossible to

**3:17** · deal with otherwise people wouldn't trade now whether or not the trading practices are questionable and people are citing statistics incorrectly is a whole another ball game whole another issue but here what I want to do is I want to highlight this idea of parameter estimation in the context of a

**3:36** · stochastic function or a Time dependent function of a stochastic process that is this Edge right here so what I have here is the probability of a win being 0.55 the average winner is 10 the average loser is eight clearly this is going to develop some sort of positive Edge and this is what our Equity curve would look like if we were to trade this particular strategy over you know a thousand trades or so now this is of course stochastic

**4:05** · so if I reran this I would get a different Equity curve but notice on average we're accumulating p&amp;l I believe I random seed it here yes so I random seed it here so let me get rid of the seed but due to the positive Edge even

**4:23** · though this curve looks a little bit different every time we run it we still see that up into the right behavior and that's exactly what we would want to see we don't want to see you know very choppy activity we don't want to see large draw downs we want to see a very nice smooth Equity curve in fact the smoother that it gets the less supposed

**4:44** · or the less risk we have in deploying this this type of strategy now you know this does not necessarily mean that this is going to hold up in the next thousand trades and that's that's what I'm about to get to here now of course the actual p&amp;l is arbitrary right you can just it's

**5:03** · linear you can just add leverage and you can multiply this entire curve by four to to increase the profit so we're we're not talking about any form of you know optimal risk reward here there's no sharp there's no sortino there's we're not looking at ratios we're not looking at you know the you know performance metrics associated with the strategy per se we're just analyzing it from a statistical point of view whether or not this is a good Equity curve is you know depends on a lot of different things it depends on the macro environment the

**5:36** · current risk- free rates it depends what did the S&amp;P return what did you know all these all these other things so we're not going to talk about the performance metrics of the strategy but like I said we're going to analyze the statistics so clearly there's a positive edge here if I reran this I would continue to get different Equity curves trading the strategy is productive it would appear okay now the parameters are 0.55 the the average winner is 10 the average loser is minus 8 if you use a

**6:05** · limit so let's say you have a limit stop for taking profit and for a stop loss then these could be fixed values and really you would just be looking at the probability of of wins and losses over time which does simplify the the space quite a bit but you're still going to deal with these same issues so just keep that in mind even even if you don't have some sort of trailing stop and your take profit is going to be scaled by you know

**6:33** · however much of a run it goes up you're still going to face this issue so the average winner average loser could be simplified to fixed values but nevertheless we still have this probability of winning and losing we have to deal with so what do I mean by the probability of winning and losing being nonstationary changing over time well probability of winning and losing and perhaps even the average win and average loss depending on how you enter and exit trades can change so what I

**7:04** · mean by this is here I'm going to add some some sort of Decay to the win rate so as you can see with this particular Equity curve the edge decays over time now this could be due to a variety of things as I had mentioned earlier it could be the the macro environment is completely different it could be rates being higher rates being lower it could be due to regulatory issues it could be due to this or that or whatever ever you know that's that's kind of the the job

**7:33** · of the the trader to figure out what is going on with their strategy but here you can see this is not the up and to the right behavior that we were looking for prior so if we look at the previous Equity curve we see this growth all the way to the thousandth trade but when we look at the thousandth trade here it starts to plateau and this is what I've seen in quite a few systematic strategies I've seen sentiment based strategies they work really really well and then 2021 2022 hits and it starts to

**8:06** · plateau and you know the the key question is why why would that be the case and that's when you go to your Quant researchers and you say fix this and your Quant researchers go well it's not that easy the entire regime for sentiment based strategies has changed because of this because of that maybe different type of sentiment signals work better in this new regime maybe they don't work at all but you can quantify

**8:31** · what's going on prior to understanding why very easily by just taking a look at your trading profitability over time in this context so here what we have is we start with 0.55 and I have a linear Decay so I'm going 0.55 to 04 over the Thousand trades so you can see my profitability goes from 55% wins so

**8:55** · that's the probability of winning to 40% and the average winner is not big enough to outweigh the decrease in probability thus we start to Plateau here we don't get that up into the right Behavior okay so what we're looking at here is the change in the probability of winning or losing a trade over time we

**9:20** · don't know the Dynamics of that specific probability if we did it would serve us quite well and there would be no need to develop any sort of model for it so what could the Dynamics of that process that parameter process look like if you will

**9:38** · well it could be mean reverting there could be a drift or Trend or there could be a regime shift and there could be jumps and and shifts and parameters uh all about the the process's space so what could this look like well this is the linear Decay that I had just displayed in the previous curve that had plateaued here I have the probability of winning on the left y AIS here and the

**10:07** · equity value on the right Axis here the right y AIS now the parameter starts at .55 and this is just a linear Decay this is quite unlikely as to what the actual dynamics of the probability of your winning or losing a particular trade in a strategy set would be but it's quite a

**10:30** · trivial example to see what's going on so what you can see here is we start at 0.55 and after each trade you know we're doing pretty well we're doing pretty well and then the parameter continues to degrade until it gets to 0 4 and now we're seeing some plateau in the equity curve itself we're still winning we still have our average winner is to be greater than the average loser otherwise we would begin to lose Equity value here

**10:58** · but this is Hope hopefully a very interesting diagram to see what could be going on in your trading strategy you can see the probability of your win the probability of winning in your trading strategy is decreasing over time and the probability of losing is just the complement one minus the probability of a win and that's increasing over

**11:21** · time so this is very this is very informative as to what's going on here and this is nothing that you can't do yourself if you had an Excel of your trades and your Equity over time then you could develop this plot on a a cumulative basis you would just accumulate the probability over time and see what happens to this this probability of winning and the corresponding probability of losing now clearly it's not going to tell the entire story um but you know if

**11:51** · you see your Equity curve increasing increasing increasing and then plateauing or decreasing then you can take a look at the probability of winning probability of losing maybe that doesn't change maybe it's still you know 6040 and you're winning uh a good fraction of the time but maybe your winners are now smaller than your losers

**12:10** · and your losers are too big and that's what's dragging your Equity curve down so you can do this sort of analysis to see kind of like which lever you need to pull to hopefully you know get your strategy back in order you could see oh well you know my winners are are still winning so I have a good probability of win probability of loss but my average winner is decreasing because that's a whole another Dynamic that we're not even looking at you could plot that as well on a different Y axis but you know

**12:39** · these two that we're looking at here the probability of win probability of loss you can swap that with average p&amp;l because if you're not using fixed stop loss and profit takes then that itself to could also be again based on your entry and exit conditions could be uh a stochastic process as as well so here

**13:01** · we're taking a look at the probability of win probability of loss over time this is just a linear decay in performance if we scroll on down here we're taking a look at a completely different possible process to explain the Dynamics of the probability of winning probability of losing so here what I have is I actually have a mean reverting process and what I'm trying to show you here is we don't know the density the underlying density the underlying Dynamics of the change in probability over time if we did then we

**13:34** · would know to continue to trade our our strategy or to not trade our strategy um but we're going to try to model it and by modeling it you know we can graph this using using live trading data but what I'm doing here is I'm simulating Poss possible Dynamics so previously I showed you the this is just a linear decay in

**13:57** · probability here this this is a mean reverting process the probability of winning probability of losing now what you can see is the probability of winning kind of has this negative Drift But then it gets drawn back to a mean value of 51 so there is still that edge

**14:18** · but it changes over time now we we're still up and to the right here but not nearly as much as when we had our fixed Edge in the beginning right here we go from 0 to 1750 of course that's random but we come down here and we are 0 to 800 and this is going to have a completely different sharp ratio if you want to talk about performance metrics I'm sorry 0 to roughly 800 and this is

**14:47** · going to have a completely different sharp ratio um compared to the previous Equity curve of course it's going to be much worse because we're simulating the true dynamics of this probability of win probability of loss you could fit like an orl back process the immune reverting process to your data and stimulate it forward to see what it could look like um but again there there really is no cut and dry answer as to what you should do now here what I'm trying to show you is this could be the case you could have

**15:16** · a a profitable strategy and over time that that probability of winning is going to be mean reverting and it's going to come back up maybe to maintain that positive Edge and the profitability of your strategy that's one instance you could have linear Decay or somewhat linear Decay very unlikely it's going to be as you know straight line as this but more

**15:42** · likely it'll have some sort of negative drift if there is any at all so here what you can see is the probability of winning has this negative drift and it starts at like 6 and then it starts to come down and again it's just a stochastic process so it's going to continue down and then maybe it stabilizes maybe it has some mean reverting Tendencies maybe it has some jumps who knows but these are the

**16:06** · possible dynamics of the change in the probability of your wins and your losses in your trading strategy okay so what can you do to combat this well there's a lot of different things you can do the simplest thing to start with if you have been trading for a while and you're trading the same strategy maybe this is systematic Maybe you have a specific you know type of of day trading strategy that you use however you choose to trade

**16:35** · what you can do is you can just plot your Equity curve over time and you can plot your wins and losses your cumulative probability of wins and losses over time and you can see how the they evolve throughout time you could see oh well you know my probability of winning was significantly larger here the probability of losing was significantly larger here uh and you can you can kind of check out the Dynamics of of what your strategies p&amp;l and

**17:02** · probability of win and loss looks like if it looks something like this it may be time to retire the strategy this is a good indication something like this that unless there is a drastic change in the probability of

**17:22** · winning which is reasonable to even monitor over time so don't actually trade this strategy I would never trade this strategy if you know the probability of winning was degrading like this and the probability of losing was increasing and we assume some sort of fixed average win average loser for for our p&amp;l I would never trade something like this and you shouldn't either but what is reasonable to do is to track this over time and to see hey

**17:50** · like now it's starting to win again right if this blue line starts to revert heavily back to the mean of a positive Edge that then it might be reasonable to trade this strategy again okay you may choose to use moving averages you may choose to use you know a lot of different things to quantify a window perhaps of the probability of of

**18:13** · winning probability of losing but we're not going to kind of dive into that into this video it kind of opens a whole separate can of vums of TSA and I'm not really interested and diving into that in the uh the remainder of this this video here um this is another good examp example here if you know you have some sort of mean reverting esque process like this then you know here this is even kind of a tossup should we trade this strategy well we went from 0.51 all

**18:42** · the way down to 0 42 and we plateaued pretty aggressively in all reality with transaction costs we probably would have lost money here and then we started to come back up here to 0.5 1.5 2ish and you know even this is not enough to to trade this is has a negative drift even though it's mean reverting this would not be reasonable to trade now it could

**19:05** · eventually have a positive drift and the probability of winning may even be greater than 50% then it might be reasonable to begin trading again so this is what I'm trying to say is when should you stop trading a profitable strategy well when it stops becoming profitable is a an acceptable answer but more quantitatively it's like well you can look at your Edge and you can see the degradation in your performance over time based on your actual trading data

**19:33** · or simulation with fitted parameters if you want to assume some sort of model and Dynamics for your parameters so I hope this video was helpful I hope this video was interesting in explaining how and when to stop trading a profitable strategy uh again really what we're looking at is we're just looking at this idea of Ed over time this is just one way to determine whether or not you should trade a strategy right if we have

**20:04** · negative EV we probably shouldn't trade it if we have positive EV then I think it's reasonable to trade but you know that is something that you're going to have to determine for yourself based on your own strategies so I hope this was an enjoyable video I hope these charts were interesting and helped explain the idea visually of what Edge is as we're looking at it with respect to a strategy's win and lose rate and the

**20:33** · equity that we are generating by traing that strategy if you have any questions please feel free to leave them in the comments below if you want to ask me a question directly I tend to be more responsive on Discord that'll be in the description below as well other than that thank you so much for watching and I will see you in the next video