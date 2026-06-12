---
title: "How to Trade Options with the Black-Scholes Model"
source: "https://www.youtube.com/watch?v=1OByexsEJXc"
author:
  - "[[Roman Paolucci]]"
published: 2026-05-02
created: 2026-06-11
description: "*🚀 Master Quantitative Skills with Quant Guild*https://quantguild.com*📈 Interactive Brokers for Algorithmic Trading*https://www.interactivebrokers.com/mkt/?src=quantguildY&url=%2Fen%2Fwhyib%2Fov"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=1OByexsEJXc)

\*🚀 Master Quantitative Skills with Quant Guild\*  
https://quantguild.com  
  
\*📈 Interactive Brokers for Algorithmic Trading\*  
https://www.interactivebrokers.com/mkt/?src=quantguildY&url=%2Fen%2Fwhyib%2Foverview.php  
  
\*👾 Join the Quant Guild Discord server here\*  
https://discord.com/invite/MJ4FU2c6c3  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
\*🪐 Free Jupyter Notebook Access 👇\*  
https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2026%20Video%20Lectures/107.%20How%20to%20Trade%20Options%20with%20the%20Black-Scholes%20Model/htobs.ipynb  
  
\*📜 How to Trade the Covered Call 👇\*  
https://youtu.be/iPsPRQlDeTA  
  
\*🔗 How to Read Options Chains 👇\*  
https://youtu.be/RrRbz6oXwxE  
  
TL;DW Executive Summary:  
\- We explored the Black-Scholes model to build intuition about its applications and limitations in the real world, emphasizing that it is not intended as a forecasting or prediction model for asset prices or option outcomes  
\- A key takeaway is that Black-Scholes option prices between different contexts are not always apples-to-apples; differences in inputs, market assumptions, and volatility surfaces mean prices can't be universally compared, unlike implied volatility (iVol), which offers a consistent, relative scale for comparing options across strikes and maturities  
\- We clarified that while the Black-Scholes “delta” is often associated with probability, in reality it is a hedge ratio—it does not represent the actual chance of finishing in-the-money, but instead indicates how much the option price changes with small moves in the underlying  
\- Through practical examples and visualizations, we highlighted why it's crucial for traders to interpret model outputs with caution and always consider the assumptions, including market dynamics and model risk, when applying Black-Scholes-based insights to real-world option trading  
  
I hope you enjoyed, and I hope you learned something!  
  
\- Roman  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
\*📖 Chapters:\*  
00:00 - Model Informed Decision Making  
01:44 - Relative European Option Pricing  
03:30 - Implied Volatility: Apples-to-Apples  
05:56 - The Most Important Idea to Understand  
07:03 - Delta: Probability of Expiring in the Money  
09:50 - Relative Contract Pricing in the Live Markets  
12:54 - Delta in the Live Markets  
16:38 - Trading Options with the Black-Scholes Model  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
\*🗣️ Shout Outs\*  
  
A special thank you to my members on YouTube for supporting my channel and enabling me to continue to create videos just like this one!  
  
\*⭐ Quant Guild Directors\*  
Dr. Jason Pirozzolo  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
\*▶️ Related Videos\*  
  
\*Quant Builds 🔨\*  
How to Build a Live Volatility Surface in Python (Interactive Brokers)  
https://youtu.be/5JEeAsQqlro  
  
\*Statistics and Trading Profitability Over Time (Edge) 📈\*  
  
Time Series Analysis for Quant Finance  
https://youtu.be/JwqjuUnR8OY  
  
Quant Trader on Retail vs Institutional Trading  
https://youtu.be/j1XAcdEHzbU  
  
Quant on Trading and Investing  
https://youtu.be/CKXp\_sMwPuY  
  
Why Poker Pros Make the Best Traders (It's NOT Luck)  
https://youtu.be/wZChBKDFFeU  
  
Quant vs. Discretionary Trading  
https://youtu.be/3gblERSSHXI  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
\*🗂️ Resources\*  
  
\*📚 Quant Guild Library:\*  
https://github.com/romanmichaelpaolucci/Quant-Guild-Library  
  
\*🌎 GitHub:\*  
https://github.com/RomanMichaelPaolucci  
https://github.com/Quant-Guild  
  
\*📝 Medium (Blog):\*  
https://quantguild.medium.com/  
https://medium.com/quant-guild  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
\*🛠️ Projects\*  
  
\*The Gaussian Cookbook:\*  
https://gaussiancookbook.com  
  
\*Recipes for simulating stochastic processes:\*  
https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=5332011  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
\*💬 Socials\*  
  
\*TikTok:\* https://www.tiktok.com/@quantguild  
  
\*Instagram:\* https://www.instagram.com/quantguild/  
  
\*X/Twitter:\* https://x.com/quantguild/  
  
\*LinkedIn (personal):\* https://www.linkedin.com/in/rmp99/  
  
\*LinkedIn (company):\* https://www.linkedin.com/company/quant-guild  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Transcript

### Model Informed Decision Making

**0:00** · \[music\] By the end of this video, you will fully understand the Black-Scholes model and its place in modern options trading, whether as a market maker, a retail trader, the list goes on.

**0:15** · Trading is about positioning and survival. There is no crystal ball.

**0:22** · There is no price prediction. It is about positioning and survival.

**0:29** · I find that nobody understands how to implement models in practice because they treat it like a crystal ball, rather than a basis for decision-making.

**0:41** · The entire purpose of this video is to combat the dozens of comments that I see all over a whole bunch of videos that I have on the Black-Scholes model. The fact that it's useless, it doesn't predict anything. Yeah, no kidding. It does not predict anything. It is a model used to explain and understand, effectively as a filter for decision-making, relative pricing, and probability based on what the market is currently thinking.

**1:12** · That's what we're going to talk about in this video. I'm Roman, founder of QuantGuild. Check out QuantGuild to master your quantitative skills and learn real math, probability, and statistics for the financial markets.

**1:25** · We're going to use Interactive Brokers for this video. We're going to bridge the gap between theory and practice.

**1:29** · We'll talk first about the model in the classroom to understand exactly what's going on and why it seems to fall apart in practice. And then we'll head on over to the Trader Workstation, take a look at some real options contracts, and talk about what's going on there. We'll first start with this idea of relative pricing. I'm going to assume that you understand European call and put options. If you're unfamiliar, I just put out a video this week on how to trade the covered call, and I cover all of those fundamentals within that video.

### Relative European Option Pricing

**1:58** · I'll leave a link to it in the description below. If you'd like to check it out, I highly recommend you look at that video first if you don't understand the dynamics of these contracts. If you do, I'm going to ask you this question.

**2:08** · What sense can we make of a market price for these contracts if they are apples to oranges?

**2:15** · What do I mean by this?

**2:16** · If the price of an at-the-money 15-day Google call is 11 bucks, and the price of an at-the-money 15-day Nvidia call is also 11 bucks, I'm going to ask you, which one is more expensive?

**2:32** · You might be saying, "Wait a second, they're the same price. What do you mean which one is more expensive?" Well, we're not dealing with the same underlying here. What I have is a simulation. We're going to take a look at Nvidia. It's currently trading roughly 214, Google roughly 340. If I play the simulation for you, you're going to see, sure, the dynamics of the call option itself will remain the same for each underlying, right? Pretty much the exact same contract specification, but the underlying itself, they are not the same. Nvidia is trading at 214, Google at 340.

**3:05** · And they are completely different companies.

**3:08** · And the size of the spot is completely different. Yet the at-the-money contract price is the same.

**3:17** · So, this is really apples to oranges.

**3:19** · What sense can we make of these prices without some sort of way to turn this into apples to apples or oranges to oranges?

**3:29** · This is exactly where the Black-Scholes model comes into play. I'm not talking about risk-neutral pricing. I spent my entire professional life focusing on the risk-neutral pricing argument, pricing financial derivatives, coming up with the implied volatility surface, calibrating to that surface, extrapolating exotic prices. I have dozens of videos on this channel and more formal courses and bizarre items on QuantGuild if you'd like to cover the more formal mathematics, but we're going to talk about the practical implications within this video.

### Implied Volatility: Apples-to-Apples

**3:59** · And that is that supply and demand is going to create that price.

**4:03** · The $11 that we see on our terminal.

**4:07** · The Black-Scholes model is going to allow us to back out what is known as the implied volatility within the framework of that model, that is assuming that the underlying is following a geometric Brownian motion.

**4:20** · And that is going to allow us to compare these contracts, that is the prices, relatively speaking in terms of apples to apples, oranges to oranges. So, what I have here is a simulation of the underlying based on what the market is currently pricing those at-the-money options at. And what you'll see here is the implied volatility for Google is much lower than the implied volatility for Nvidia. So, the implications of this in a forward-looking sense are that the market is expecting more turbulence for Nvidia than it is for Google.

**4:51** · So, even though they have the same prices, that is the same prices for the at-the-money contracts, which one is currently more expensive? Well, that is going to be Nvidia. It has a higher implied volatility, and that is going to raise the contract's price relative to Google.

**5:14** · So, when we just had the prices, we really didn't know which one the market was considering to be more expensive, more volatile in terms of the volatility that that contract was worth. But now, with the Black-Scholes model, we have a measure of apples to apples, oranges to oranges. Is it wrong? Yes, you're a scholar. Congratulations. The market does not follow a geometric Brownian motion. We all understand this.

**5:39** · But now, we can see in the market on our terminal screen which contract is relatively more expensive in terms of volatility.

**5:53** · Without a model, we don't have that information. Understanding this idea of apples to apples or oranges to oranges pricing, what is the most important thing to understand? Well, that is this implied volatility. You know when it's good for? It's good for right now. It is not good for an hour from now. It's not good for a day from now or a week from now.

### The Most Important Idea to Understand

**6:17** · This is something that everybody seems to misunderstand about the market trading these types of contracts, especially in a retail capacity. This implied volatility is subject to change whenever it wants.

**6:32** · The other day, Nvidia went from 208 to 216 to 218.

**6:36** · And now it's back down to 208 to 213.

**6:40** · The implied volatility is going to swing wildly alongside the price intraday.

**6:46** · Everything gets repriced every second.

**6:51** · That is the misconception with these models is that there's some sort of predictability.

**6:56** · No. It is telling you what is going on in the market right now.

### Delta: Probability of Expiring in the Money

**7:03** · This leads us to probably the most misunderstood idea coming from the Black-Scholes model, and that is this idea of delta.

**7:12** · And delta being the probability roughly of an option expiring in the money.

**7:18** · We're going to hop on the Trader Workstation in a moment and actually take a look at some real options and talk about what this interpretation means, but I want you to see it in the classroom.

**7:28** · This is what should happen, but in reality does not.

**7:33** · What I have here is a simulation of that option \[snorts\] contract, a 15-day Nvidia call at-the-money.

**7:42** · We're going to compute the delta. The delta is .53.

**7:47** · What does that mean? Well, according to the Black-Scholes framework, it's the cumulative normal distribution. It is roughly the probability that this contract expires in the money.

**7:57** · So, if I was to play this contract out a very large number of times, right? This is what we're seeing in the simulation.

**8:04** · Each path is just going to be a contract outcome. You're going to see, oh, take a take a look over here at these these bar charts, right? You can see the ones that expire in the money, the ones that expire out of the money. It's not it's not 53/47.

**8:18** · That's because this is a sample.

**8:21** · By the law of large numbers, when we have a large enough sample size, it's going to converge to that 53%. And all the way at the end of this simulation, you can see it's really starting to get there, 52.4%, 47.6%.

**8:35** · By the law of large numbers, asymptotic convergence is guaranteed.

**8:39** · You know what that means for real life?

**8:42** · Literally nothing. The central limit theorem, the law of large numbers, none of that holds in real life. So, when you take a look at an option that has a delta of .53, if it's an at-the-money call and the stock plummets 3% over the next couple hours, that delta is going to be like .1. There's going to be no chance of it, relatively speaking, of it expiring within the money. That's because the market is going to reprice that contract. This is what everybody thinks is going to happen.

**9:12** · Why wouldn't I buy a 30 delta call? 30% of the time, it doesn't expire in the money. That's because the probabilities are amorphous.

**9:22** · It's explaining what's going on in the market. It is not a prediction model. It is a filter at best. You're playing poker, whether you like it or not. Some people are far better at playing poker than others.

**9:37** · These models are used as a basis for decision-making in a discretionary or systematic capacity.

**9:45** · They are not to be used with the intent of achieving classroom asymptotic convergence. Understanding these ideas, we're ready to approach the live markets. I've cracked open my Trader Workstation here. I'll leave a link in the description below if you'd like to get started with Interactive Brokers. They're the only broker I use.

### Relative Contract Pricing in the Live Markets

**10:01** · I've been with them for over 10 years in a trading and investing capacity and we use them for all of my quant builds on this channel. Once you crack open the Trader Workstation here, it's going to launch you into Mosaic View, but I am a fan of the classic view, so we're going to click on that guy and you can see I have Nvidia and Google ready to go.

**10:21** · These are the underlying, but we want to take a look at the options contracts.

**10:25** · So, I'm going to open up the option trader on this top bar here and I've already selected Google as my underlying. If you go to the upper left-hand corner here, you can type in Google and you will pull up the options chain for that particular underlying. If you're unfamiliar with how an options chain is structured or what it is exactly you are looking at, I'll leave a link to a dedicated video on reading the options chain in the description below.

**10:49** · So, if we take a look at Google here, I'm going to select an expiration of roughly the contract that I had in the classroom. This is going to be 16 days and if we take a look at the at-the-money call, we're going to look at 345 1145, roughly 12 bucks for this contract sold in lots of 100, so that's going to be 1,200 dollars.

**11:10** · Okay.

**11:11** · If we go on over to Nvidia now, going to type Nvidia, head on over to the at-the-money call. This is trading for roughly what's that? 690 700 bucks for the at-the-money call.

**11:27** · Same expiration, roughly the same contract parameters, both are trading at-the-money. Which one is more expensive?

**11:35** · Well, that question we know is not one of price necessarily. It can be one of volatility.

**11:44** · And what we have here, if you take a look at the upper right-hand corner of the options chain, is a measure of that at-the-money implied volatility. So, we are comparing apples to oranges if we just take a look at the price arbitrarily of the at-the-money contracts for different underlying, but what can we compare to make it apples to apples? That's going to be this implied volatility. So, for the 16-day at-the-money call, we can see 40.8%.

**12:12** · We can see Nvidia is 40.3%, so the Google contract relatively speaking is more expensive in terms of volatility forward-looking variance.

**12:24** · Okay. That's one facet of the Black-Scholes model, but we know that that is subject to change whenever it likes.

**12:31** · If this price decides to gap up, gap down, this is going to adjust. And what was more expensive may be cheaper and what was cheaper may be more expensive.

**12:44** · It is a relative measure for your positioning, for your intent on survival. That is what makes for effective trading.

### Delta in the Live Markets

**12:54** · Okay. That's one facet of the Black-Scholes model that is this apples to apples, oranges to oranges comparison. We're not just going to look at necessarily raw price, we're going to look at something like implied volatility.

**13:06** · Great.

**13:08** · What about delta? Delta is roughly the probability of an option expiring in the money, is it not? Well, certainly and this is also going to give us a relative measure because over time the underlying price is going to change. Right now it's trading at 210. If you watch this video a year from now, I guarantee you it's going to be at 250, 260, whatever the price target is for this particular equity.

**13:30** · That's not me predicting anything, just by the nature of growth stocks and the accumulation of risk premium over time, it would not shock me to see 250, 260 one year from now, but the points of this is not my arbitrary prediction. The point of this is understanding that the at-the-money contract is going to change over time.

**13:54** · So, if you are trying to buy and sell options in a consistent way to at least understand your strategy, then what are you going to do? Are you going to look at price? Well, we just said price is really not apples to apples. If we go five points up and five points down in terms of this options chain, then that is not necessarily going to yield the same option dynamics as five points up and five points down on something like Google.

**14:25** · This turns into that same pricing problem. It's not just about the price of the option itself, but also the relative price of the underlying. So, what can we do? We can use delta as a relative measure because the delta of all of these options contracts is going to be priced consistency consistently relative to the at-the-money contract. What do I mean by this? Well, let's go back to Nvidia.

**14:52** · If we go back to Nvidia, we take a look at the delta. Come on down here, we see this is a roughly 30 delta call.

**15:00** · That means the market is currently pricing it in a Black-Scholes framework of having a 30% probability of expiring in the money. Is it actually 30%? No.

**15:09** · This is going to jump up to 40%, 50% as the underlying approaches 220 222.5 or it's going to decrease as the underlying moves down. These are going to constantly be repriced just like that animation I showed you. If you treat this as something that is going to converge in reality, you're going to lose a tremendous amount of money. This is for relative pricing.

**15:34** · Relative pricing. What do I mean by that? If you take a look at the current price, what is this? Roughly 211? We'll just use 210 as an anchor. This is 12 and 1/2 points up. Okay? So, we have roughly a 30 delta call, right? This just moved down to 29, right? Roughly a 30 delta call 12 and 1/2 points up.

**15:54** · What does a 30 delta call look like for Google? Is it 12 and 1/2 points up? Let's go to Google.

**16:02** · And if we take a look at a 30 delta call for Google, right? We're going from Look at this. We go from 346, which is current. We go 12 points up, that would be 58. That is not a 30 delta call. That is a 38 delta call.

**16:21** · If you go to a 30 delta call, that's 365.

**16:25** · That is completely different in terms of price.

**16:30** · It is not 12 points up.

**16:32** · It is What is this going to be? Roughly 20 points up from 346.

### Trading Options with the Black-Scholes Model

**16:38** · This is how you use the model in practice for relative selection, relative pricing, filtering your discretionary decision-making. It is not a prediction model. This is not something where you can just pull up this options chain and go, "Oh, I'm going to sell all of these 30 delta calls and I know 30% of all those calls are going to expire in the money. I'm going to do a little bit of arithmetic and I'm good to go. That's my edge and and we're we're off to the races." No.

**17:06** · This is poker at best. This is a filter for your discretionary systematic decision-making.

**17:13** · This is how the model is used in practice. All models are wrong, some are useful. They are useful for decision-making under uncertainty.

**17:22** · Without this model, right? You can kick and scream all you like that the market don't follow a geometric Brownian motion, it's not predictive, your delta hedge isn't perfect, you need a back-of-the-napkin adjustment like every trading desk in the entire world. Yes, we all understand this. We all understand this, but without this model, you do not have any relative basis, any concrete relative basis for your decision-making.

**17:47** · That is the purpose of the Black-Scholes model and that is how you trade options with the Black-Scholes model. That's going to do it for this video. I hope you enjoyed I hope you learned something. This video certainly took a tremendous effort to put together, so if you liked it and you want to see more like it in the future, please like, comment, subscribe, share. It helps me out tremendously. It's always greatly appreciated. I'll leave a link to this Jupiter notebook in the description below if you would like to check it out alongside all of my other Jupiter notebooks and open source quant builds available on the Quant Kill Library on GitHub.

**18:19** · Check out quantkill.com to master your quantitative skills. Check out Interactive Brokers if you would like to get started with the Trader Workstation and engage with the live markets. Other than that, I want to thank you so much for watching and I'll see you in the next video.