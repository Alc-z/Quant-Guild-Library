---
title: "Control Variates for Variance Reduction"
source: "https://www.youtube.com/watch?v=Iu_gCD74Y70&t=107s"
author:
  - "[[Roman Paolucci]]"
published: 2025-01-11
created: 2026-05-30
description: "🚀 Master Quantitative Skills with Quant Guild:https://quantguild.comJoin the Quant Guild Discord server here:https://discord.com/invite/MJ4FU2c6c3I hope you enjoyed this lecture, please feel fr"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Iu_gCD74Y70)

🚀 Master Quantitative Skills with Quant Guild:  
https://quantguild.com  
  
Join the Quant Guild Discord server here:  
https://discord.com/invite/MJ4FU2c6c3  
  
I hope you enjoyed this lecture, please feel free to leave a comment or reach out to me with any questions.  
  
Control Variates Jupyter Notebook:  
https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/2.%20Control%20Variates%20for%20Variance%20Reduction/Control%20Variates%20for%20Variance%20Reduction.ipynb  
  
Articles and code walkthroughs can be found on our blog  
https://medium.com/quant-guild  
https://romanmichaelpaolucci.medium.com/  
  
For more free tutorials and references see our GitHub  
https://github.com/RomanMichaelPaolucci  
https://github.com/Quant-Guild

## Transcript

**0:01** · \[Music\] and we are back welcome back today we're going to talk about control variates for variance reduction in simulation variance reduction is a a very interesting topic right off the bat you may say Hey you know if we have something we're trying to estimate using

**0:22** · simulation then clearly if we're trying to discern some sort of confidence interval for how confident we are in our estimation you know that the standard error is somewhat proportional to the number of simulations that we run so why don't we just jack up the simulation number we go

**0:41** · from 1,000 10,000 100,000 why not a million simulations decrease the variance that way well that's not always practical due to the cost computationally of that which we are trying to simulate in fact it may take way too long to reduce the variance that way but there are other ways for example control variant to reduce the variance in whatever you were trying to estimate now control variance are not the only way to reduce variance

**1:13** · in some sort of estimation of a parameter however it is a good way to get started with variance reduction we're going to go over a toy example using an arithmetic brownia motion I'm going to connect it to some current literature in quantitative finance and

**1:31** · we'll talk a little bit about the implications of that may not be directly through control varats but I think it is a reasonable introduction to the topic and I think it's you know moderately interesting to connect it to a current stream of literature that aims to improve pricing efficiency so let's go ahead and get started with this idea of control varats what the heck is a control variant well

**1:55** · at a high level what's going on here is we we have some sort of simulation so let's say we're trying to figure out an option price classically we pick some sort of model to model the underlying dynamics of our stock price process maybe we choose an arithmetic Brown Mission geometric maybe we do some sort of jump diffusion model you you have your pick some sort of stochastic volatility model whatever it may be well we simulate

**2:21** · those price paths forward Compu a payoff and then discount them back to the present average off that payoff and we get our risk neutral price if you will will okay in generating those price paths we

**2:37** · have a lot of other information available to us we have the average price we have the Min price the max price so on and so forth and that can be used as auxiliary information to Aid in informing the final price of the option now this will be a

**2:57** · little more clear in a moment when we get to the actual applied example option pricing under arithmetic Brown motion but at a high level what we're doing is we're using other variables other information that we have any anyway within a simulation to Aid in that final

**3:15** · estimation and it turns out when you use other information that happens to be highly correlated with the quantity of interest you can achieve significant variance reduction and what that does is it leads to more precise were precise estimation so let's take a look at this equation for a control variant here

**3:38** · this is actually a linear regression and what we have here is we have this control variant and it's important to know the control variant is not the quantity itself but the expectation matches the quantity of Interest so let's take a look at what's going on here why is the quantity of Interest so you can say that that may be a European option price for example what have you and then X is some sort of auxiliary variable that you're going to have that's highly correlated with the target quantity of

**4:12** · Interest all right now what you'll notice happens here is we we have the expectation of X so if we have some sort of model whose Dynamics enable us to have in close form the expectation of say the stocks price at the maturity

**4:32** · then this is going to be extremely correlated with the target quantity of interest and we're going to achieve variance reduction if that's a little too complicated then let's just take a look at what happens when we take the expectation of this top equation here that's what's going on down here so remember why is the target quantity at interest I'm going to take the expectation of both sides so when I take the expectation of both sides I'm going to substitute C in for this Y and you can see that the expectation of the control variant is going to be equal to

**5:05** · the expectation of the target quantity of interest and why is that well when you take the expectation of the right hand side what happens is due to the linearity of expectation you can distribute the expectation through C is just a constant we select that value and

**5:22** · you distribute the expectation through it gets assigned to this x it gets assigned to this expectation of X clearly expectation of X is just a constant as well and they end up canceling each other out this is what allows us to use the information from that auxiliary variable to inform the estimation of the target

**5:42** · quantity of interest because the control variant itself that that value is not the quantity of interest but the expectation of that control varant is the same as the expectation of the target quantity of interest in other words C C sub CV is not C but the

**6:04** · expectation of C sub CV is the expectation of C okay how is C chosen well we minimize the variance of the estimator through very simple optimization you can go ahead and take the derivative set it equal to zero if you like turns out C is going to be Co variance of YX / the variance of X and of course just a linear regression here but if we had the coari of y and x

**6:36** · and the variance of X we would not need to do this because we would have the target quantities expectation so we're going to need to use the sample covariance and the sample variance to estimate this constant C and that's what we do after simulation how does does this reduce the

**7:01** · variance well if we take the variance of both sides here we can see that the variance of the control variant is going to be equal to the variance of y l c^ 2 times the variance of X but you'll notice here that if you substitute this quantity in here that the more that the

**7:24** · co variance this is going to be I believe this is going to be just the Yeah the more that the two quantities are related turns out that the more variance reduction you will achieve so in other words the more valuable the information is of X within each run of your simulation the fewer simulations you have to run to achieve similar precision

**7:59** · that's exactly what we have here if you take the variance of both sides you can see that you end up actually with a correlation term here and this correlation term says that you know maximum variance reduction is achieved when correlation is one clearly correlation can't be one because you would have the target quantity of Interest expectation anyway but if they are highly correlated you're going to achieve significant variance

**8:26** · reduction so that is the gist of control variat for variance reduction we have this linear regression here you're not limited to just one auxiliary variable you could do a multi- regression as well so you could you know add uh a z as well if you like you could do you know more than one auxiliary variable to decrease the the variance as well but this is just a a very simple hopefully simple uh

**8:52** · example here in the context of pricing and this is the general gist here is you can see that since variance is going to be uh positive you know variance is going to be the expected deviation away from the mean you will go ahead and see that if you subtract some sort of constant times the variance you're going to have less variance than the variance of the original Target quantity of Interest anyway okay so how does this relate to a

**9:24** · practical example that was a lot of theory for those of you interested in the theory now we can go ahead and talk talk about a practical application uh in pricing options so here we're choosing an arithmetic Bry motion this is unnecessary right like we have a close form solution actually we don't need to

**9:41** · we don't need to use control variates here but this is a very intuitive example and I think it's a it's more fun than just seeing it applied to something random like some sort of q a continuous time markof chain or something like that so let's just take a look at it in the context of option pricing under ABM so we know that the call option at

**10:04** · maturity has a payoff function of S Sub T minus K and zero whichever one is larger our hockey stick diagrams if you will and we know that the Dynamics for the underlying asset are given under arithmetic Barum motion by this equation here where we have an initial asset price we add some sort of drift scaled by time and we add some some sort of volatility scaled by

**10:35** · Sigma the volatility is just a standard brown motion what we can do is we can add a control VAR control varant to Aid in the estimation of this European call simulation so we're trying to simulate the price of a European option we are going to simulate a whole bunch of ABM price paths to maturity calculate the payoff discounted to the present we're going to get the average of that set of

**11:02** · values and that'll be the approximate price of the call now there's going to be variance and what we want to do is reduce that variance so we don't have to simulate as many price paths what we can do is we can use the arithmetic average of the simulated prices because we know under arithmetic Brown and motion that the expected price at maturity is going to be the initial Price Plus mu time the

**11:28** · maturity / two that is going to be our control variant notice how the Dynamics of the model that we've chosen arithmetic Brine and motion enable us to have this known value for the expectation at time cap T okay that's very important now is this kind of redundant if we know this do we

**11:51** · really need to simulate price paths probably not but bear with me it's it's a a toy example here cuz clearly if we have the the expectation at time cap T then this is this is completely redundant right but let's just take a look at what happens here so what we're going to do is we're going to run this simulation so I'm going to have the initial price our strike price time to maturity a drift a volatility certain number of simulations and time steps so

**12:20** · initial stock price of 100 a strike of 100 time to maturity of 252 we have 252 days we're going to do daily time steps 252 steps we have a a 10% drift a 30% volatility and we're going to do this 10,000 times I'm going to go ahead and run this guy here and we get this this interesting output so let's go ahead and take a look at what's going on here so we have our original payoff distribution that's this blue distribution here and this is the

**12:52** · average payoff of the simulated prices or these are the payoffs I should say of the simulated prices you'll notice that the adjusted payoffs with the control variant has a tighter distribution now that doesn't necessarily specify the payoffs remember the control varant is not the payoff if we go back up to this equation here we can see that CCV that value CCV is the target

**13:21** · quantity of Interest less the information added by our auxiliary variable so CV is not the the value of the payoff itself it is our control variant and we know that if we take the expectation of our control variant then we get the expectation the estimated Target quantity that's that's what we're looking for so when we come down here that orange density is not the same it's not the same as the blue

**13:49** · density in the sense that that is our control variant distribution okay the original payoffs is the blue distribution but you'll notice that the expectation is the same but variance reduction is achieved so how can we see this well the original call price is going to be 25.1147000

**14:29** · is to take a look at the confidence interval under the same Alpha value and in that sense you just take a look at the standard error and you can see the original standard error is 05 and the adjusted standard error after introducing the control varant is 02

**14:45** · which gives us approximately 75% variance reduction so under the same Alpha value in other words we are 99% confident that the price or the interval contains the true price that interval is Tighter and it costs us the same amount of computational power now that's a

**15:09** · little that that kind of ties this whole thing together here I should say is fixing all of those things we have a tighter confidence interval so using the same amount of compute using the same amount of price paths uh in addition to this control Vara estimator here we are going to get a tighter confidence interval and we didn't have to increase the number of simul ations all we're doing is we're using the fact that there's this auxiliary variable that can contribute information to the Target quantity of

**15:37** · interest and that is exactly what's going on here so this is with an arithmetic barem motion but how do we connect this to what's going on in the the current body of literature you know recent literature I should say uh rough volatility model is a good example of you know when this might be useful may not be explicitly in the same

**15:59** · context here because if there was a closed form solution then again we wouldn't need to do this the the actual auxiliary variable you you may use or the technique for variance reduction is probably different but I wanted to connect it to something that is practical as well so a rough volatility model for example it introduces a long

**16:19** · range dependency um it's it's notarian instructure it is going to depend on the entire price path so it's very expensive to simulate a a sing a single path of a a rough volatility model so the idea here is if you wanted to use a rough model to approximate some sort of option price whether it be some sort of vanilla or exotic product you're going to need some sort of variance reduction technique because simulation

**16:51** · is computationally expensive it's very expensive and if you wanted to I mean think of about how many options on are on books every single day that need pricing efficiency is a a big deal in this line of work so something that has a closed form solution even though it may be you know less accurate if you will uh definitely has more value in

**17:16** · that context so you know a rough volatility model May better characterize the Dynamics of the markets but if you can't do it efficiently you know if you're pricing things that needed repricing last week today then then it's not helpful um but you know if you have

**17:32** · some way to maybe increase the efficiency of your estimations by doing variance reduction then it can be particularly helpful um you know connection to the current literature is approximation of these models these pricing functionals using neural networks so you know one way to do that is to essentially map you know you're going to create a parameter set map of the model's inputs fit to a surface and

**17:58** · then you're going to have some sort of surface as an output and you're going to try to learn that relationship as a essentially just a a map um and then you know since a neural network is just a function you can actually use that to you know efficiently price your options um and then you're actually using some sort of optimization routine to try to maybe even fit that to a volatility surface to reprice um so on and so forth so

**18:29** · I have other videos discussing that in more depth if you're interested but that is just uh the general gist of what's going on here is the the overarching theme is it is computationally expensive to simulate these models so what can we do well you know the there are current streams of literature that aim to try to approximate these Maps approximate these pricing functionals using volatility surfaces and the model parameter set and the whole goal there is efficiency but efficiency is in the same

**19:02** · context if we simulate a whole bunch of paths then we need to simulate a lot of paths because we need good estimation of of parameters and in this sense we need a good estimation of the option price what is good well why do we simulate a lot of paths simulate a lot of paths to hope to reduce the variance and find what that true price actually is under a specific model framework and that is why you would need variance reduction specifically due to efficiency so

**19:34** · efficiency is a very big problem there's kind of this inverse relationship where as complexity increases efficiency decreases and vice versa Simplicity can be you know it can be very useful can be very useful especially if you have a close form solution so that's kind of like the gist at a high level of variance reduction hopefully that's an interesting link to the current streams of literature and Fin um and I I think that's going to do it

**20:02** · for this video on control variance and variance reduction I hope you enjoyed if you have any questions or comments please feel free to leave them in the comment section below join Discord if you have anything you'd like me to address directly I tend to be more responsive there but I hope you found this interesting I hope this was a fun toy example to illustrate variance reduction

**20:27** · clearly it's a toy example because if you have the if you have the average stock price at maturity under a specific model then why on Earth would you need the simulation in the first place nevertheless toy example hope you enjoyed it and I will catch you in the next video thanks for watching