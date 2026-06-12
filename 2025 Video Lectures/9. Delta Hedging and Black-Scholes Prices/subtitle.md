---
title: "Delta Hedging and Black-Scholes Prices"
source: "https://www.youtube.com/watch?v=jDoLost28tE"
author:
  - "[[Roman Paolucci]]"
published: 2025-03-08
created: 2026-06-13
description: "🚀 Master Quantitative Skills with Quant Guild:https://quantguild.comMarch 2025 Promo Question for Quant Guild Lifetime Access:https://www.youtube.com/channel/UCW1svfGxG4ADnbc1HCH6dqA/community?lb"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=jDoLost28tE)

🚀 Master Quantitative Skills with Quant Guild:  
https://quantguild.com  
  
March 2025 Promo Question for Quant Guild Lifetime Access:  
https://www.youtube.com/channel/UCW1svfGxG4ADnbc1HCH6dqA/community?lb=UgkxIAhQCKcI8GHGE-T\_V0JIIZ4FB9nbkeLQ  
  
Join the Quant Guild Discord server here:  
https://discord.com/invite/MJ4FU2c6c3  
  
Jupyter Notebook:  
https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/9.%20Delta%20Hedging%20and%20Black-Scholes%20Prices/Delta%20Hedging%20Trading%20Strategy.ipynb  
  
Black-Scholes Equation Derivation:  
https://www.youtube.com/watch?v=2iClLEfXuqA  
https://medium.com/swlh/deriving-the-black-scholes-model-5e518c65d0bc  
  
Market Implied Volatility:  
https://www.youtube.com/watch?v=VzieTIsBaHM  
  
Check out my new free open-source market-making game:  
https://practicemarketmaking.com  
  
Articles and code walkthroughs can be found on our blog  
https://medium.com/quant-guild  
https://romanmichaelpaolucci.medium.com/  
  
For more free tutorials and references see our GitHub  
https://github.com/RomanMichaelPaolucci  
https://github.com/Quant-Guild

## Transcript

**0:01** · \[Music\] welcome back today what I'd like to do is talk about Delta hedging an option if you haven't seen my previous video on the black sches model where I actually derive the partial differential equation that is the black shols equation the argument itself for that

**0:21** · equation is based on a continuous time Delta hedge in this video what we're going to do is we're going to take a look at the Delta hedging Strat stry itself and hopefully by the end of the video you'll have a better idea of what a Delta hedge actually is and the intuition behind the price that gets generated from the black shes model now

**0:44** · regardless of if you understand the derivation itself of the black chols equation and solution which yields the black shols model this right here is going to give you the price of a European call according to their assumptions and arguments that is of the the black model I've implemented this equation in Python to generate prices based on a specific parameter set and I've also created this nice chart to help us visualize the price of an option based

**1:15** · on the underlying asset price and the corresponding Delta of the option now what is Delta Delta is the first order sensitivity of the options price with respect to to the underlying assets price now in layman's terms what does this mean this means as the underlying

**1:37** · asset or the stock that our option contract is written with respect to changes we can expect a subsequent change in the option price of approximately Delta it is a linear approximation of the change in an options price based on a unit change in

**1:55** · the underlying asset price long story short it is how we can expect the options price to change when the stock price changes this red line here represents Delta itself and it's also sometimes used as an approximation for the probability that an option expires in the money so you can read into Delta in a variety of different ways and you can see that as we change some of the parameters the pricing function for the

**2:25** · option along with the Delta function changes so as are time to maturity increases you can see the subsequent change in the option pricing function and the Delta function with respect to of course the underlying asset price if we narrow this time window this starts to look like a classic hockey stick diagram and we get this almost sigmoid looking function situation for our Delta

**2:52** · that is there are more significant changes when we have fluctuation around the strike price when we are very very close to expiration and this is relatively intuitive because you will see that if you are hovering around the strike price expiration then there is going to be a lot of variation in the

**3:14** · option price depending on whether or not it is changing towards in the money or towards out of the money status let's look at a quick example of the two interpretations of Delta so suppose I have the this option contract and this option contract currently has an underlying asset price of $100 that means I will pay roughly 10 bucks for this option the Delta of this option

**3:42** · according to these parameters if we go up to this red line is roughly 60% 6 what this means is if the underlying asset price was to move from 100 to 101 we would expect a option price change of 6 in other words we would expect the option price to increase by approximately 6 moreover the other interpretation is that the option has roughly a 60% chance of expiring in

**4:13** · the money this model of course assumes that the Dynamics of the stock follow a geometric brownia motion that is characterized by this stochastic differential equation and this stochastic differential equation is parameterized by a volatility term by a drift term and a Wier process that is

**4:34** · the brownia motion itself I have written a function here to simulate a geometric Brown Motion in my python Library qfin I also have this capability so you can just import the process itself and simulate it if you would like to do it that way and every time we run this we will get a different path according to that process according

**4:58** · to the process that is assumed by a black schs model let's pause right here and talk about Delta hent the argument for the black choles equation revolves around a continuous time Delta hge that is if we hold a portfolio of stock and option and we hold a particular quantity of stock we can

**5:24** · ensure that a instantaneous change in our portfolio value is essentially risk neutral that is we remove the randomness from our portfolio in turn we must earn a risk-free rate and that establishes the black shols equation whose solution yields the black shols model now that

**5:43** · Delta hedge is clearly impossible to do because we can't continuously h a portfolio we would accumulate way too many transaction costs we can you know dive into all of the assumptions that are violated by the model but if you have a model that doesn't make any assumptions and you have the true density then we wouldn't need to develop a model in the first place if you had the true density function for the price of all options I would ask you what are you doing here you should be making money with that true density that you have access to nevertheless this Delta

**6:16** · hedging argument is what allows us to establish the black schs model price what we're going to do is we're going to cont conduct a Delta hedge but not in continuous time we're going to conduct it on a daily basis so what's going to happen is we are going to sell an option

**6:34** · and then we are going to Delta hedge that position which means we're going to buy stock to ensure that our portfolio is delta neutral we have that risk neutral portfolio in other words an instantaneous change in our portfolio value is not going to yield a change in our portfolio value therefore we must earn the risk-free rate what we will see

**6:57** · is throughout the life of this Delta hedge we are going to accumulate p&amp;l now we could accumulate p&amp;l in a positive sense we could accumulate pnl in a negative sense we could end up making money we could end up losing money but the amazing thing about the numerical argument which we are about to conduct for a Delta hedge is as you approach

**7:20** · continuous time hedging that is as you approach this idea of continuously hedging your portfolio which is of course only theoretical before I get a thousand comments about transaction costs I know there are transaction costs I trade myself I understand how this works the theory itself suggests that as we approach The Continuous time we will approach the expected value of the

**7:49** · option which is the black schs model price in other words if we do a continuous time Delta hedge on average if we take a look at p&amp;l we should see that we get approximately the black shs model price and that is the the incredible thing about this numerical argument that we're about to take a look at and then the subsequent idea of taking a position based on violations of

**8:13** · these assumptions is how we can in turn make some money so let's take a look at these different arguments here let's take a look at Delta hedging in the context of a short European call position I'm going to sell a European call option which means my net Delta

**8:30** · position is going to be negative in other words if the option price increases this is good for the guy who holds the option he wants the option price to go up I don't necessarily want the option price to go up if it does go up that means the value of my option is going to decrease now what can I do if I know that if the option was to go down in value when there's an increase in the underlying price well I can go ahead and and buy stock if I buy stock then if the

**9:03** · underlying asset increases I'll make money on my stock even though I lose money on my option so how much stock should I buy well I'm going to buy Delta shares of stock this is going to ensure that they perfectly offset so if I buy Delta shares of stock my option price is going to go down by Delta my stock price will go up by Delta and vice versa now of course of course we

**9:37** · see that Delta and the option price are nonlinear functions which means our linear approximation is going to get worse and worse as we move away from our initial point in which we are hedging about therefore we must continue to rebalance the Hedge throughout the life of the option this is the continuous time or The Continuous hedging argument made for the black shs equation which we cannot do so we will do it on a daily basis then what we will

**10:08** · do is we will calculate the p&amp;l from our stock position and then take a look at the ending p&amp;l in a variety of different situations so I have this function to simulate a Delta hedge I'm going to run it I'm going to run it under this parameter set here so I have a spot price of 100 strike of 100 time to to maturity of a year 5% risk free rate 20% V and then an 8% drift our option price

**10:38** · is going to be 10.45 our initial Delta is roughly 64% and here is one possible outcome this is one possible outcome our final p&amp;l from Delta hedging is 44.05 if I was to run this again this is going to be another one of 44.05

**11:03** · 44.3 here we have accumulated negative P we have Nega 55.94 you get the gist so every time we conduct a Delta hedge what we're doing is we are going to say on this day today let us purchase Delta shares of stock

**11:20** · tomorrow I'm going to buy or sell stock to ensure that I hold Delta shares on that day and I'm going to continue to do that throughout the life of the option and then at the end of the option's life I'm going to accumulate a p&amp;l from the stock and the option position and that may be positive or

**11:42** · negative okay so knowing that each time we simulate a stock price path according to the geometric browny motion and conducted Delta hedge we accumulate a p&amp;l what happens if we repeat the simulation a large number of times say 10,000 times and then take the average p&amp; L well it turns out depending on how

**12:03** · frequently we Delta hedge that is on a daily basis twice a day so on and so forth we are going to get a price that closer and closer reflects that of the black schols model price in other words the model price is 1045 if I was to repeat this daily Delta hedge in this case I get a mean pnl of

**12:25** · 5.72 if that was to increase the frequency of H you can see that the meme p&amp;l is going to start to approach that black shs option price in other words the expected p&amp;l should we be hedging in a continuous sense is going to be the black shols model price in general so we can expect to be just collecting the premium for the option price we are not going to earn any excess pnl should we

**12:55** · be selling that option short in essence this is connecting all the dots for it to be the risk neutral price so how can we use this idea to actually trade well we have to have an opinion on the parameter set that we're assuming to be constant so in our current simulation we

**13:16** · have the spot price the strike price the time to maturity the risk-free rate and the volatility term so if I had an opinion on volatility let's say that right now Nvidia is trading at 40% implied V and I think that the realized V is going to be substantially less than

**13:38** · the current market implied volatility which is quite probable there are papers on the idea of the volatility risk premium I think aqr wrote one of the first on those so clearly there's a way that we can capitalize on this idea to make money should we have an opinion that the volatility realized is going to be less there's going to be some sort of theoretical statistical whatever you want to call it Edge so how can we simulate to reflect this well essentially what I'm going to do is I am going to fix the parameter set for the

**14:12** · geometric brownie emission under the condition of my opinion in other words I'm going to simulate the stock price with the idea that we are going to achieve a lower implied volatility or I'm sorry a lower realized volatility throughout the life of the option

**14:29** · however I will price the black schols option with the current market implied volatility so in other words I'm going to collect a premium based on that 40% implied V today and then I'm going to realize stock price paths that actually follow something with less V maybe 10 20% V and on average what you'll see is

**14:50** · there's going to be some sort of discrepancy that we can capitalize on to make money so in other words we should be seeing a theoretical price that is the expected p&amp;l at the end of the simulations that is larger than the original option price that we collected a premium for so let's go ahead and check this out if I was to run this simulation

**15:24** · here 23.50 that seems like it's significantly more than what I had going on back over here so in essence what we're doing is we are selling a European call option for more than it's actually worth and we are collecting a pretty penny based on the alternative that is we're realizing a price path or series of price paths that have the same parameter set as the black schs model which was used to price

**15:55** · the premium that we collected in this case we're saying hey those price paths are not going to be realized according to the parameter set that the model is pricing the options at so in other words we can collect more money right now than we should be allowed to do theoretically

**16:14** · because when the option expires we are not going to realize as much volatility as the market thinks and that is how you can capitalize on an opinion on volatility using the idea of Delta hedging and the black shs

**16:33** · model so what's the big picture key takeaway of this video it's that anytime that you think that the realization of a path or series of paths is going to have a different parameter set that is your opinion is the parameters should be higher they should be lower they will be higher they will be lower then according to this argument you can capitalize on those opinions by conducting a hedge

**17:01** · that is you can sell an option today for more than you think it's worth or buy an option today for less than you think it's worth and should you do this a large quantity of times over time you will accumulate a positive expected value and p&amp;l for your firm I hope you enjoyed this video thank you so much for watching and I will see you in the next one