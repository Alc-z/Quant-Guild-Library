---
title: "Can AI Learn Black-Scholes?"
source: "https://www.youtube.com/watch?v=aRr3chiwkrI"
author:
  - "[[Roman Paolucci]]"
published: 2025-04-04
created: 2026-08-04
description: "🚀 Master Quantitative Skills with Quant Guild:https://quantguild.comJoin the Quant Guild Discord server here:https://discord.com/invite/MJ4FU2c6c3Solve our Monthly Promo Question f"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=aRr3chiwkrI)

🚀 Master Quantitative Skills with Quant Guild:  
https://quantguild.com  
  
Join the Quant Guild Discord server here:  
https://discord.com/invite/MJ4FU2c6c3  
  
Solve our Monthly Promo Question for 25% Off Access to Quant Guild!  
http://youtube.com/post/Ugkx5x12aT_LSRL_tKQOxQtUNrFlcuwYp3Jv?si=hYkEZ0ajWj1rAyyI  
___________________________________________  
Jupyter Notebook:  
https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/13.%20Can%20AI%20Learn%20Black-Scholes/Can%20AI%20Learn%20Black-Scholes.ipynb  
  
Trading with the Black-Scholes Model:  
https://www.youtube.com/watch?v=0x-Pc-Z3wu4  
  
Black-Scholes Equation Derivation:  
https://www.youtube.com/watch?v=2iClLEfXuqA  
https://medium.com/swlh/deriving-the-black-scholes-model-5e518c65d0bc  
  
European Options 101:  
https://www.youtube.com/watch?v=HgjeDJVCHSo  
  
Market Implied Volatility:  
https://www.youtube.com/watch?v=VzieTIsBaHM  
___________________________________________  
Articles and code walkthroughs can be found on our blog  
https://medium.com/quant-guild  
https://romanmichaelpaolucci.medium.com/  
  
For more free tutorials and references see our GitHub  
https://github.com/RomanMichaelPaolucci  
https://github.com/Quant-Guild  

## Transcript

**00:01** · [Music] welcome back can AI learn black schs more generally can AI learn to price options this is a topic of particular interest to me because it combines data science machine learning artificial

> [音乐] 欢迎回来。AI 能学会 Black-Scholes（布莱克-斯科尔斯）吗？更一般地说，AI 能学会给期权定价吗？这个话题我特别感兴趣，因为它把数据科学、机器学习、人工智能……

**00:15** · intelligence with financial mathematics areas that I have a great affinity for and really enjoy studying this is an area or a topic that I spent a lot of time studying as a quantitative researcher so without further Ado I

> ——与金融数学结合在了一起，而这些正是我非常热爱、也特别喜欢研究的领域。作为量化研究员，这个话题我花了很多时间去研究。闲话少说，我……

**00:29** · would like to talk about the background required to understand this problem space and then I want to walk through very clear simple and easy to understand examples so that we can climb up each rung of the ladder together and

> ——想先谈谈理解这个问题域所需的背景知识，然后我会带着大家一步步走过非常清晰、简单、易懂的例子，让我们能一起沿着梯子逐级向上攀登，并……

**00:44** · understand why this stream of literature exists in the first place and talk about some very interesting Solutions proposed to solve some very intricate problems we can develop an argument for black shs prices right we can assume a geometric

> ——理解这一系列文献究竟为什么会存在，并讨论一些为解决复杂难题而提出的非常有趣的解决方案。我们可以为 Black-Scholes 定价建立论证，对吧？我们可以假设标的资产服从几何……

**00:58** · brownie emotion const volatility no Arbitrage no transaction costs continuous hedging capacity Etc and yes we can go ahead and use to Lama we can derive the black shs equation solve that partial differential equation get the

> ——布朗运动（geometric Brownian motion）、波动率恒定、无套利（no arbitrage）、无交易成本、具备连续对冲能力等等。是的，我们可以用伊藤引理（Ito's lemma）推导 Black-Scholes 方程，求解这个偏微分方程，得到……

**01:13** · black shs model prices and generate prices for European calls and puts that's all well and good however we all know that these assumptions are just not true we know in practice there are transaction costs we know that there is

> ——Black-Scholes 模型价格，并为欧式看涨期权和看跌期权生成价格。这些都很好。然而，我们也都知道这些假设在现实中根本不成立：我们知道实践中存在交易成本，我们知道存在……

**01:28** · arbitrage we know that we can't hedge continuously and of course volatility is not constant among other violations and omissions of you know the model in the the case for the real world right however there are many models that do

> ——套利，我们知道我们无法持续对冲，当然波动率也不是恒定的——这些都是模型相对于真实世界情形的各种违背与遗漏。然而，确实有很多模型……

**01:43** · aim to capture more Dynamics and sterilized facts of the market so we know that volatility is not constant so hon has his model the duper has his local volatility we we have models in that try to create volatility as either

> ——旨在捕捉市场更多动态特征和典型化事实（stylized facts）。我们知道波动率不是恒定的，所以 Heston 有他的模型，Dupire 有他的局部波动率（local volatility）模型。我们还有一些模型试图把波动率构建成——

**01:58** · a function locally or as its own process that evolves throughout time like a hon we also know for example that prices can jump there are jump diffusion models we know there are transaction costs in occasional Arbitrage and and you know so

> ——局部的函数，或者像 Heston 那样，作为一个随时间演化的独立过程。我们还知道，例如价格可能会跳变，于是有了跳扩散（jump diffusion）模型；我们知道存在交易成本和偶尔出现的套利，等等等等……

**02:13** · on and so forth but there is this this implicit tradeoff right if we have a parsimonious model that is you know efficient something like a black schs then we can get a analytically tractable solution so

> ——诸如此类。但这里存在一个隐含的权衡（tradeoff），对吧？如果我们有一个简约（parsimonious）、高效、类似 Black-Scholes 那样的模型，那我们就能得到一个解析可解（analytically tractable）的解——

**02:27** · the black shs model is actually a function you plug in a whole bunch of parameters and it spits out a price something like a hon you know if you consider fft that's that's totally fine we have the the fast 48 transform but

> ——Black-Scholes 模型实际上就是一个函数：你塞进去一大堆参数，它就吐出一个价格。像 Heston 这样的模型，如果你用 FFT，那也完全没问题，我们有快速傅里叶变换（FFT），但——

**02:39** · something that's more complicated maybe of the rough model family where you have this fractional Brown motion and and long range dependency on on volatility then you're not going to have an an analytical solution so what I what I

> ——如果是更复杂的模型，比如粗糙波动率（rough volatility）模型家族——那里有分数布朗运动（fractional Brownian motion）、波动率的长程依赖（long range dependency）——那么你就不会再有解析解了。所以我想说……

**02:53** · mean to say is the more complicated your model gets the less analytically tractable it probably will be and you will require simulation or more computationally expensive means of generating prices that isn't too far off

> ——的意思是：模型越复杂，它就越难有解析解，你就需要模拟，或者用更耗算力的方式来生成价格。这个道理并不难理解——

**03:07** · or difficult to understand and in essence what I'm saying is something like a black sches with all these assumptions it's like yeah these assumptions aren't true but the more things that we assume away the easier it

> ——也并非难以理解。本质上我想说的是，像 Black-Scholes 这样的东西带着所有这些假设——诚然，这些假设并不成立——但你假设掉的东西越多，就越是容易……

**03:19** · is to generate a price and the less things we assume away the more difficult it is to generate a price and and that shouldn't be difficult to see so something as simple as you know removing the constant volatility so consider

> ——生成一个价格；而你假设掉的东西越少，生成价格就越困难。这一点应该不难看出来。就拿去掉恒定波动率这种简单改动来说，考虑一下……

**03:32** · something like a hon it becomes very difficult to develop a Hing argument because you don't just have stock but you need another option in that portfolio so I'm going to digress but the there's this tradeoff essentially

> ——像 Heston 这样的模型，就很难再建立对冲（hedging）论证，因为你的组合里不只是有股票，还需要另一个期权。我有点跑题了，但本质上就是存在这样一个权衡……

**03:44** · between model complexity and model efficiency now when we have more complicated models that you know fair enough they are you know less efficient and they may not have analytically tractable Solutions so you may need to

> ——在模型复杂度和模型效率之间。当我们有更复杂的模型——好吧，它们确实效率更低，而且可能没有解析可解的解——所以你可能需要……

**04:02** · do some sort of simulation to generate prices we very quickly lose capacity to use these models in practice because in real time we need to price a very large number of these financial instruments and what I mean is you know generating a

> ——通过某种模拟来生成价格。这样我们就很快失去了在实践中使用这些模型的能力，因为在实时场景下我们需要给大量的金融工具定价。我的意思是，生成——

**04:21** · whole bunch of of paths and discounting payoffs is is great and you can you know approximate prices in that capacity but when you're trying trying to actually price or extrapolate prices based on some sort of Mark Market volatility

> ——一大堆路径并贴现收益，这很好，你可以用那种方式近似出价格。但当你想根据某个市场波动率（market volatility）曲面来实际定价或外推价格时——

**04:34** · surface you need to calibrate your model first to this volatility surface and this is what makes it computationally intractable that is it's not that oh I need to generate a whole bunch of paths and you know if that doesn't mean too

> ——你就得先把你的模型校准（calibrate）到这个波动率曲面上，而正是这一点让计算变得不可行（computationally intractable）。也就是说，并不是"哦，我只需要生成一大堆路径"那么简单，如果你还不大明白这一点——

**04:48** · much to you yet we'll go over what this means in a moment but in in order to let's say we can't just plug in our parameters into a function and get a price like black sches we have a more complicated model and we need to

> ——我们待会儿会再详细讲这是什么意思。但是，为了……比如说我们不能再像 Black-Scholes 那样，把参数直接塞进一个函数就能得到价格。我们有一个更复杂的模型，我们需要……

**05:00** · simulate a price simulating a price is not as simple as just okay let's run like 10,000 simulations and get a price it's like no no no you need to fit that model to a surface first and all of the different points on that surface in

> ——去模拟一个价格。而模拟价格并不像"好吧，我们跑一万次模拟就得到价格"那么简单。不、不、不，你得先把那个模型拟合（fit）到一个曲面上，以及该曲面上的所有不同点。为此……

**05:14** · order to do that you need to use some sort of optimization scheme and generate prices each step of the way now when you do that you're going to have relative error across obviously all of your prices because you're simulating them

> ——你需要使用某种优化方案（optimization scheme），并在每一步中都生成价格。当你这样做的时候，显然你所有价格都会有相对误差（relative error），因为价格是模拟出来的——

**05:27** · but moreover you're going to have to run that Sim imulation a large number of times cuz you're not going to fit the surface on your first simulation you're not going to fit it on your second simulation nor your third so fitting the

> ——而且你还得把那个模拟运行很多很多次，因为你不会在第一次模拟时就拟合好曲面，第二次、第三次也都不行。所以，把——

**05:40** · current model that you're using to a market surface is a difficult problem especially if your model is computationally expensive you're going to have to simulate a lot of paths you're going to have to simulate a lot

> ——你当前使用的模型拟合到市场曲面是一个困难的问题，尤其是当你的模型计算代价很高的时候。你得模拟很多路径，你得模拟大量……

**05:54** · of paths to generate prices and this is going to take way too long so the stream of literature that I'm discussing today is aiming to do the heavy work this kind of heavy lifting of simulating a lot of paths offline when efficiency and timing

> ——的路径来生成价格，而这会花上太长的时间。所以今天我要讨论的这一系列文献，目标就是做这些重活——这种"离线"（offline）模拟大量路径的繁重工作，在效率和时效性……

**06:12** · is not important and then once you train AI or a neural network on the data that you've generated then in real time you can just implement the neural network and what you have is some sort of function like a black sches so it it

> ——并不重要的时候去做。然后，一旦你用生成好的数据训练了 AI 或神经网络，实时阶段你只需部署这个神经网络，你所拥有的就是某种类似 Black-Scholes 的函数。所以它——

**06:25** · operates like a black sches in an analytical way where you give it parameters and spits out a price and this tends to be very very quick so essentially what we have is something like a black chols that assumes away all

> ——以解析的方式运作，就像 Black-Scholes 一样：你给它参数，它就吐出价格，而且往往非常非常快。所以本质上，我们拥有的是一种类似 Black-Scholes、把所有——

**06:38** · of these difficult Dynamics and then we can generate a price but that price doesn't really reflect all the Dynamics we would like then we have something that's a more complicated model maybe some sort of rough volatility model or

> ——困难的动态特性都假设掉的东西，然后我们可以生成一个价格，但那个价格并不能真正反映我们想要的全部动态。然后我们有更复杂的模型，也许是某种粗糙波动率（rough volatility）模型，或是——

**06:51** · some sort of jump diffusion model and we simulate a whole bunch of prices and then we take a neural network and we say hey look at these prices learn the map from the parameters that generated these paths to the

> ——某种跳扩散（jump diffusion）模型。我们模拟出一大堆价格，然后拿一个神经网络，对它说：嘿，看看这些价格，学习从"生成这些路径的参数"到"价格"的映射——

**07:07** · prices and then once that neural network learns it we have the same input output that we had with the black shes of course this is an approximation we'll talk about all the implications of this but that is at a high level what's going

> ——一旦那个神经网络学会了这个映射，我们就有了与 Black-Scholes 相同的输入-输出关系。当然，这是一种近似，我们会讨论它的所有含义。但概括地讲，正在发生的事就是——

**07:19** · on is we're trying to use neural networks to get that same input output that we get with a black schs but with more complicated models that may capture more dynamic that we are interested in capturing in our prices let's start at

> ——我们试图用神经网络来获得与 Black-Scholes 相同的输入-输出，只不过底层是更复杂的模型，可能捕捉更多我们希望在价格中体现的动态特征。让我们一起从——

**07:33** · the first rung and the ladder together this idea of an input and an output to get a price the black shs model is the solution to the black shs equation and if you give me five things I can give you an option price and of course we're

> ——梯子的第一级开始。这个"输入-输出得到价格"的想法：Black-Scholes 模型是 Black-Scholes 方程的解。如果你给我五样东西，我就能给你一个期权价格。当然，我们——

**07:47** · assuming everything that's required to derive this model the original equation and of course the solution which is this model so everything that I talked about before geometric Brown motion constant volatility no Arbitrage all of those

> ——是在假设推导这个模型所需的一切都成立的前提下：最初的方程，当然还有解（也就是这个模型本身）。所以，我之前谈到的所有东西——几何布朗运动、恒定波动率、无套利——所有这些……

**08:01** · things we are assuming is the case and we know this isn't the case but to get this map of parameters to price we're assuming all of that is true so you give me the current price of the stock you give me a strike price of the option you

> ——我们都假设是成立的，尽管我们知道事实并非如此。但为了得到"参数到价格"的这个映射，我们假设这一切都是真的。所以，你给我当前股票价格，你给我期权的执行价，你——

**08:17** · give me the time until maturity risk-free rate and a volatility and I will be able to give you a black schs price we can implement this in Python and of course we get an output for the black shols price based on a series of

> ——给我到期时间、无风险利率和一个波动率，我就能给你一个 Black-Scholes 价格。我们可以用 Python 实现这个。当然，基于一系列输入，我们得到 Black-Scholes 价格的输出——

**08:32** · five inputs so these are five example inputs this is the underlying asset price the strike price the time to maturity this is the risk-free rate and this is the volatility term so what's happening here is we go

> ——那就是五个输入。这些就是五个示例输入：这是标的资产价格、执行价、到期时间、这是无风险利率，这是波动率项。所以这里发生的是，我们走——

**08:45** · through the entire hedging argument we find the partial differential equation we solve the partial differential equation we get this function that prices options according to the black shols model that is the black Sholes

> ——完整个对冲（hedging）论证，得到偏微分方程，求解这个偏微分方程，得到这个根据 Black-Scholes 模型给期权定价的函数。这就是 Black-Scholes——

**08:58** · assumptions everything that we talked about before what's the problem with this well we know these assumptions are all violated in practice okay so let's say we want to use a more complicated model

> ——假设：我们之前讨论过的所有东西。这有什么问题呢？嗯，我们知道这些假设在实践中都被违反了。好吧，假设我们想用一个更复杂的模型——

**09:10** · to price our options well in order to use a more complicated model to price our options then you know we are no longer assuming that the underlying follows a geometric Baran motion we're no longer assuming constant volatility

> ——来给期权定价。那么，为了用更复杂的模型给期权定价，你明白，我们不再假设标的资产服从几何布朗运动，我们不再假设波动率恒定——

**09:23** · for example no longer assuming that the there are no jumps in underlying asset prices we we're no longer making those assumptions now what is the consequence the consequence is we don't get this nice close form solution I can't just

> ——比如说，我们不再假设标的资产价格没有跳变。我们不再做这些假设。那后果是什么？后果是我们得不到这个漂亮的闭式解（closed-form solution）。我不能只是——

**09:39** · Define a function you give me five inputs and I spit out an option price it no longer works like that we don't have any assumptions now we're going to need a different tool to generate prices so

> ——定义一个函数，你给我五个输入，我就吐出一个期权价格。它不再是这样运作的了。现在我们什么假设都没有了，我们需要一种不同的工具来生成价格。所以——

**09:50** · originally you gave me five inputs I plug those five inputs into my black shs function and I get a price that's very nice but of course of course you know everyone's screaming that these assumptions are all violated in practice

> ——原本你给我五个输入，我把这五个输入塞进我的 Black-Scholes 函数，得到一个价格，那非常好。但当然，当然，你也知道，大家都在喊：这些假设在实践中全都被违反了——

**10:03** · and fair enough so how do we generate prices what's another way to do that well what we can do is we can go ahead and simulate the Dynamics of the underlying asset and then we can discount the payoffs to the present and

> ——而且说得有道理。那我们怎么生成价格呢？还有别的方法吗？嗯，我们能做的，就是去模拟标的资产的动态过程，然后把收益贴现到当前时刻，然后——

**10:18** · we can generate prices in that capacity and that's going to take the risk neutral payoff and it's going to take the average of the risk neutral payoff at time T equals z and if we do that we're going to find also the fair value

> ——用这种方式生成价格。那就是取风险中性收益（risk-neutral payoff），取时间 T 时刻风险中性收益的平均值。如果我们这样做，我们同样能得到期权的——

**10:30** · of the option so here what I'm doing is I'm simulating a whole bunch of paths according to the geometric branum motion and this is what's being assumed in a black trolls model now if I use the same parameter set as before you'll see that

> ——公允价值。所以在这里，我按照几何布朗运动模拟了一大堆路径——这正是 Black-Scholes 模型所假设的。现在如果我使用和之前相同的参数集，你会看到——

**10:43** · I get a very similar price and that folks is not a coincidence okay this is another way that we can generate option prices is via simulation now simulation in this sense is kind of useless because if

> ——我得到了一个非常相似的价格。各位，这可不是巧合。好吧，这是另一种生成期权价格的方式，即通过模拟。不过在这个意义上，模拟有点"没用"，因为——

**10:59** · we're simulating geometric Brown motion to get black trolls prices for a European call or put option why would we do that we can just go ahead and plug them directly into the equation so hopefully that makes sense you're like

> ——如果我们模拟几何布朗运动只是为了得到欧式看涨或看跌期权的 Black-Scholes 价格，那我们何必这么做呢？我们完全可以直接把参数塞进公式里。所以希望这个道理讲得通，你会想——

**11:12** · well wait a second if I have these parameters why would I try to simulate all of these price paths find the payoff and discount it to the present and take the average and then I get some sort of approximate price when I could just plug

> ——等等，如果我有这些参数，我为什么还要模拟所有这些价格路径、求收益、贴现到当前、再取平均，然后得到一个近似价格呢？我明明可以直接把——

**11:26** · in all these parameters into this equation and get the exact price okay that is the fundamental basis for this problem all right we have a function that generates a precise price under the assumptions of the model and

> ——所有这些参数塞进这个公式，得到精确价格。好，这就是这个问题的根本基础。没错，我们有一个函数，能在模型假设下生成精确价格；同时——

**11:44** · we also have this tool available via simulation to generate prices by essentially simulating different states of the world computing the payoff of that option discounting it back to the present and then taking the average of

> ——我们也有模拟这个工具来生成价格：本质上就是模拟世界的不同状态、计算该期权的收益、把它贴现回当前时刻，然后取所有——

**11:57** · all of those payoffs so these are our two tools available to us to generate prices now I would say in more complicated models it should be very clear we don't have this first analytical option available to us we

> ——收益的平均值。所以，这就是我们可用于生成价格的两大工具。我要说的是，在更复杂的模型中，应该很清楚：第一个解析选项我们是用不了的，我们——

**12:10** · can't just take the parameters plug it in and end up with a price we would have no reason to use simulation if that was the case we would have no reason to even consider a black sches right we would be talking about some crazy maybe modified

> ——不能只是把参数塞进去就得到一个价格。如果真能那样，我们就没有理由用模拟，也没有理由考虑 Black-Scholes 了，对吧？我们早就去讨论什么疯狂的、也许改良过的——

**12:24** · rough burgamy model if you know we could just plug in parameters and get a price with no computational cost at all those types of models those more advanced more intricate models that capture more market dynamics are more computationally

> ——粗糙伯格曼（rough Bergomi）模型之类的了。如果我们能零计算成本地把参数塞进去就得到价格，那类更先进、更复杂、捕捉更多市场动态的模型，在计算上就会——

**12:40** · expensive and that's because they require simulation we need to simulate all of these price paths going forward and then we compute some sort of payoff discount that payoff to the present take the average and then we get an

> ——更昂贵，而这正是因为它们需要模拟。我们需要向前模拟所有这些价格路径，然后计算某种收益、把收益贴现到当前、取平均，然后得到一个——

**12:51** · approximate price clearly the as the number of paths increases the accuracy will increase and you could use some sort of an analysis on the error and bound the error and so on but you know nevertheless this is the fundamental

> ——近似价格。显然，随着路径数量增加，精度会提高，你还可以做某种误差分析、给误差定界等等。但你知道，无论如何，这就是根本——

**13:04** · idea we have two ways of generating prices we can do it analytically or numerically analytically via a function and numerically via simulation now let's pivot to the AI talk about some neural networks if we have a very simple

> ——的思想：我们有两种生成价格的方式，可以解析地做，也可以数值地做——解析地通过一个函数，数值地通过模拟。现在让我们转向 AI，谈一谈神经网络。如果我们有一个非常简单的——

**13:18** · function f ofx = x^2 this fundamentally is no different than this we have several inputs and one output here we have one input and one output it's very important that you understand that this

> ——函数 f(x) = x²，这在本质上和刚才那个没什么区别：那里我们有多个输入、一个输出；这里我们有一个输入、一个输出。非常重要的是，你要理解这一点——

**13:35** · functionally is exactly the same as the analytical function that is the black shs model that being said this is obviously very easy to visualized because it's just two Dimensions we have an X and Y F ofx is equal to x^2 and

> ——在功能上和作为解析函数的 Black-Scholes 模型完全相同。话说回来，这个函数显然非常容易可视化，因为它只是二维的：我们有 X 和 Y，f(x) = x²。然后——

**13:51** · what I'm going to actually do is I'm going to build a neural network that aims to learn this function so what I'm going to do is I'm going to generate a whole bunch of inputs and outputs we've all seen a parabola before what I'm

> ——我实际上要做的是，构建一个旨在学习这个函数的神经网络。所以我要做的，就是生成一大堆输入和输出。我们都见过抛物线，我——

**14:03** · going to do is I'm going to take all of the inputs that is in our domain the X AIS in a specific range -2 to 2 and I'm going to generate outputs according to this function that is squaring all of those

> ——要做的是，取我们定义域内的所有输入，即 X 轴在特定范围（-2 到 2）内的点，然后根据这个函数生成输出——也就是把所有那些值——

**14:20** · values then what I'm going to do is I'm going to give the neural network all of the inputs I'm going to tell it to learn from the inputs the output and that output is the input squared okay so the neural network is

> ——平方。然后我要做的，是把所有输入都给神经网络，告诉它从输入学习输出，而这个输出就是输入的平方。好吧，所以神经网络在——

**14:34** · trying to learn this Parabola that is the setup for this problem now if I look only in Sample after I train this neural network it performs quite well this should not be a surprise as neural networks are Universal function

> ——试图学习这条抛物线。这就是这个问题的设定。现在，如果我只看样本内（in-sample），训练完这个神经网络后，它表现相当不错。这不该让人惊讶，因为神经网络是通用函数——

**14:48** · approximators so here what we have is in Sample this error is very very small and I haven't trained it very much -2 to2 given what we've seen AI is capable of and and these large neural networks large deep neural networks are capable

> ——逼近器（universal function approximators）。所以我们这里看到的是：在样本内，这个误差非常非常小，而且我也没怎么训练它，范围只有 -2 到 2。考虑到我们已经见过的 AI 的能力，以及这些大型神经网络、大型深度神经网络能做到的事——

**15:02** · of you should not be surprised that this can perfectly approximate a you know pretty much the most trivial quadratic this is all in Sample let's take a look at the out of sample performance when it starts to

> ——你就不该惊讶它能完美逼近一个几乎最普通的二次函数。这都是样本内的表现。让我们来看看样本外（out-of-sample）的表现——当它开始——

**15:15** · extrapolate well how does it do does it do amazing no clearly it doesn't do amazing right so the verticals here are the cut offs for the training data and once I use the neural network out of sample doesn't extrapolate quite well

> ——外推（extrapolate）时，它表现如何？它表现得惊人吗？不，显然不惊人，对吧？所以这里的竖线是训练数据的分界点，而一旦我在样本外使用神经网络，它外推得并不太好——

**15:29** · but isn't this what we've seen in the case for AI in general anyway it doesn't tend to extrapolate very well and that shouldn't be too much of a surprise okay and there there are techniques and different things you can do to improve

> ——但这难道不正是我们在 AI 身上普遍看到的情况吗？反正它往往不太擅长外推，这不该太让人意外。好吧，也有一些技术和不同的手段可以用来改进——

**15:42** · its ability to extrapolate and whatnot we're not going to talk about you know more of the the inner mechan of the neural network itself but I just want you to be aware of them so clearly we can train a neural network to learn a

> ——它外推的能力之类的东西。我们不会过多讨论神经网络内部机制本身，但我只是想让你知道它们存在。所以很明显，我们可以训练一个神经网络去学习一个——

**15:57** · function it doesn't NE necessarily extrapolate well so we have to consider that and be careful and you know the different ways that we can structure our neural network we can improve or you know make this extrapolation better and

> ——函数，但它不一定会外推得很好。所以我们必须考虑到这一点并保持谨慎。而且，你知道，用不同的方式来构建我们的神经网络，我们可以改进、或者让这种外推变得更好或——

**16:08** · worse why is this important well if we are trying to use neural networks to price options we know that we have two options we can price them analytically or we can price them numerically what do we know about these

> ——更差。为什么这很重要？嗯，如果我们试图用神经网络给期权定价，我们知道我们有两种选择：可以解析地定价，也可以数值地定价。关于这些价格我们知道什么？——

**16:26** · prices we know that a function C so let's say this is our black schs function we give five inputs we get a black shs price we know C is approximately equal to the simulated or numerical

> ——我们知道一个函数 C——假设这就是我们的 Black-Scholes 函数，我们给五个输入，得到一个 Black-Scholes 价格——我们知道 C 约等于模拟出来的、也就是数值的——

**16:39** · price what is this C Tilda Tilda well clda Tilda is the neural network learning the approximate price so pause that's very intricate this is very complicated what's going on here well five parameter input will give me a

> ——价格。那这个 C 波浪波浪（C-tilde-tilde）是什么？嗯，C-tilde-tilde 就是神经网络学习到的近似价格。先停一下，这非常精妙、非常复杂——这里到底发生了什么？嗯，五个参数的输入会给我一个——

**16:58** · price output here a one parameter input is going to give me one output so you give me an X I give you x squared here I'm saying with the black sches model you give me five parameters I'll give you a price well is

> ——价格输出；而这里一个参数的输入会给出一个输出。所以你给我一个 X，我给你 x 的平方；这里我说的是：用 Black-Scholes 模型，你给我五个参数，我给你一个价格。那么——

**17:15** · that not true for the simulation too you just have to run the simulation a large number of times you give me five parameters all of these paths are parameterized in the same way it would not make sense if they were not

> ——对模拟而言不也是一样的吗？你只需要把模拟运行很多很多次。你给我五个参数——所有这些路径都以同样的方式参数化，如果不是这样那就不合理了——

**17:29** · parameterized in the same way so you give me five inputs for the numerical solution and I can still give you a price now what if I tell the neural network just like I told it here to learn the inputs that is the parameters

> ——所以数值解那边，你给我五个输入，我仍然可以给你一个价格。现在，如果我像在这里告诉神经网络那样告诉它：去学习输入（也就是模型的参数）——

**17:45** · of the model and learn that map of the parameters to the model to the subsequent price that is this C Tilda Tilda here this is the fundament Al basis for

> ——并学习"从参数到随后价格"的映射——也就是这里的这个 C-tilde-tilde——这就是——

**18:00** · this entire stream of literature now we know that this isn't always possible clearly this is not always possible but we know that we can numerically simulate and we can numerically simulate Offline that means we can generate a very very

> ——整个这一系列文献的根本基础。现在我们知道这并不总是可行，显然并非总是可行。但我们知道，我们可以数值模拟，而且可以离线（offline）数值模拟，那意味着我们可以生成非常非常——

**18:15** · large number of these paths and generate a lot a lot a lot of prices once we do that we end up with a very large data set that we can train our neural network on so essentially what I'm saying is our neural network

> ——大量的路径，生成很多很多很多的价格。一旦我们这样做，我们就得到非常大的数据集，可以用来训练神经网络。所以本质上我说的是，我们的神经网络——

**18:29** · just like it learns this quadratic between -2 and 2 we can generate a very very large parameter space and we can have our neural network learn the approximate prices for any model don't believe me let's give this a

> ——就像它学习 -2 到 2 之间的二次函数一样，我们可以生成一个非常非常大的参数空间，然后让我们的神经网络去学习任何模型的近似价格。不信的话，让我们来试——

**18:47** · shot with the black shes model and see if our neural network can in fact learn the black shs prices this is some math notation for you now we we have the five parameters of the black shes model in this Vector X being in

> ——试 Black-Scholes 模型，看看我们的神经网络是否真的能学会 Black-Scholes 价格。这里给你一些数学记号。现在，我们把这五个 Black-Scholes 模型参数放在向量 X 中，X 属于——

**19:03** · R5 the analytical mapping is R5 to r that is we have these parameters that output to the price given by the black shes model that's what this F function represents and that is exactly what this x Arrow represents here is you give me

> ——R⁵。解析映射是从 R⁵ 到 R，也就是说，这些参数输出到由 Black-Scholes 模型给出的价格。这就是 F 函数所代表的，也正是这个 X 箭头所代表的：你给我——

**19:21** · this input Vector I give you the price that should not be confusing in any shape way or form this is literally the same as a parabola the only difference is we don't have one input we have five harder to visualize yes functionally the

> ——这个输入向量，我给你价格。这不应该以任何形式让你困惑。这literally和抛物线完全一样，唯一的区别是我们不是有一个输入而是有五个，更难可视化。是的，功能上——

**19:36** · same yes this is an analytical solution we also have our man Carlo approximation our simulation our numerical prices okay it is the exact same thing R5 to R that's exactly what I had said here you give me parameters I output

> ——相同。是的，这是一个解析解。我们还有蒙特卡洛近似（Monte Carlo approximation）、我们的模拟、我们的数值价格。好吧，它完全是同一件事：R⁵ 到 R。这正是我之前说过的：你给我参数，我输出——

**19:54** · real price you give me parameters I output approximate price that's EX exactly what I'm saying here in the Monte Carlo approximation you give me five parameters I output price but why is it f Tilda because it maps to the

> ——真实价格；你给我参数，我输出近似价格。这正是我在蒙特卡洛近似里所说的：你给我五个参数，我输出价格。但为什么它是 f-tilde？因为它映射到——

**20:06** · expectation of the discounted Max that's exactly what I said we were doing in the numerical setting we were simulating all of these prices we were simulating all of these underlying asset prices generating a

> ——贴现后的 Max 的期望（expectation）。这正是我说我们在数值设置里所做的事情：我们模拟所有这些价格，模拟所有这些标的资产价格，生成一个——

**20:21** · payoff discounting it to the present and then taking the average that is exactly what this expectation is is right here this Vector maps to this expectation which generates approximate prices so what's happening here well now

> ——收益，把它贴现到当前，然后取平均——这正是那个期望。这个向量映射到那个期望，进而生成近似价格。那么这里发生的是什么呢？嗯，现在——

**20:38** · we have a narrow Network approximating this relationship so instead of f Tilda I called it C Tilda Tilda here here we have this F of theta where Theta is an arbitrary parameter set and the reason why we use Theta for an arbitrary

> ——我们有一个神经网络在近似这个关系。所以，不是 f-tilde，我在这里把它叫做 C-tilde-tilde。这里我们有这个 F(θ)，其中 θ 是任意参数集。我们用 θ 来表示任意——

**20:53** · parameter set is because we don't necessarily know what model we're going to assume but this is true for every model because it doesn't matter what parameter set we use we can take this parameter set though it may not be an R5

> ——参数集，是因为我们不一定要知道我们假设的是哪个模型，但这适用于每一个模型，因为无论我们使用什么参数集都不重要。我们可以取这个参数集，虽然它可能不是 R⁵——

**21:06** · it's going to be in the dimensionality of theta and it's going to map to a single price and that's exactly what we have here all of these are consistent they're all saying the exact same thing and if the approximation error goes to

> ——它会是 θ 的维度，并且映射到一个单一价格。这正是我们这里所拥有的。所有这些都是一致的，说的都是完全同一件事。如果近似误差趋于——

**21:21** · zero and maybe there are some theorems we can apply such that this is the case that would be very nice then all of these are equivalent that being said quick recap we have two tools to generate prices

> ——零——也许我们可以应用一些定理使得这种情况成立，那就非常好了——那么所有这些就都是等价的。话虽如此，快速回顾一下：我们有两个生成价格的工具——

**21:35** · given a parameter set for a model we have analytical Solutions and we have numerical Solutions available via mon Carlo simulation the Monte Carlo simulation takes far too long Analytical in real time is efficient it's

> ——给定一个模型的参数集，我们有解析解，也有通过蒙特卡洛模拟得到的数值解。蒙特卡洛模拟花的时间太长；解析地在实时环境下是高效的，它是——

**21:50** · practically instant numerical in real time is not efficient and it's not instant so what can we do well given the second ability to generate prices for any model that is models that don't even have analytical Solutions we can do this

> ——几乎是瞬间的；数值地在实时环境下则不高效率，也不即时。那我们能做什么？嗯，既然有了第二种能力，可以为任何模型生成价格——即使是那些根本没有解析解的模型——我们就可以做这件事：

**22:06** · a large number of times offline Generate random parameter sets simulate generate a price Generate random parameter set simulate generate price do this a large number of times this is the exact same thing as generating inputs and outputs

> ——离线地做很多很多次：生成随机参数集、模拟、生成一个价格；再生成随机参数集、模拟、生成价格，这样重复很多很多次。这和为二次函数生成输入和输出是完全一样的事——

**22:23** · for a quadratic which was learned here it is the exact same thing the only difference is the neural network is not learning a quadratic it's trying to learn the map of those parameters in the complicated model to the price given in

> ——而那个二次函数就是在这里被学到的。这是完全一样的事，唯一的区别在于，神经网络学习的不是二次函数，而是试图学习那个复杂模型中"参数到价格"的映射，这个价格是——

**22:39** · the setting of that model and that is going to be the goal of implementing a neural network is once it learns that relationship because remember this isn't necessarily analytically tractable we don't necessarily know how to solve this

> ——在该模型的设定下给出的。而实现神经网络的目标就是：一旦它学会了这种关系——因为记住，这不一定能解析求解，我们不一定要知道如何——

**22:52** · in closed form but that doesn't mean that we can't get a solution that is going to develop price under a specific model that is analytically intractable so what we're doing is we're using the neural network

> ——用闭式（closed form）求解，但这不意味着我们得不到解——即在解析上不可解的特定模型下得到价格。所以我们所做的，就是利用神经网络——

**23:05** · to learn the map of the parameters to the price just as you give me the five inputs to Black tools I get a price we generate a whole bunch of parameters for a difficult model generate a whole bunch of prices and we say hey neural network

> ——去学习"参数到价格"的映射，正如你给我 Black-Scholes 的五个输入、我得到一个价格一样。我们为一个困难的模型生成一大堆参数、生成一大堆价格，然后我们说：嘿，神经网络——

**23:18** · you figure out this relationship and then what we can do is once that neural network learns the relationship we can use it in real time that curvefitting process fitting your model to the market volatility curve is very very quick

> ——你来搞明白这个关系。然后，一旦神经网络学会了这个关系，我们就可以在实时环境中使用它。那个曲线拟合（curve fitting）过程——把你的模型拟合到市场波动率曲线——会非常非常快——

**23:34** · because neural networks are very very fast so how do I teach a neural network the black schs price well we don't need to simulate anything here because we have an analytical solution this is obviously just an

> ——因为神经网络非常非常快。那么，我怎么教神经网络学会 Black-Scholes 价格呢？嗯，在这里我们不需要模拟任何东西，因为我们有解析解。这显然只是——

**23:50** · exercise but if we can understand it here then we can understand it in the case it's actually useful so what do I do I generate a whole bunch of parameters for black TRS prices I'm generating

> ——一个练习。但如果我们能在这里理解它，那么我们就能在它真正有用的场景下理解它。所以我做的是：我为 Black-Scholes 价格生成一大堆参数，我生成——

**24:03** · 5,000 different prices all right so I have these five parameters but I have them 5,000 times which means when I plug each five into the black trols model I'm going to get 5,000 different option prices what I do then is I say hey given

> ——5,000 个不同的价格。好吧，我有这五个参数，但同样五个参数我有了 5,000 组，这意味着我把每一组五个参数塞进 Black-Scholes 模型，就会得到 5,000 个不同的期权价格。然后我做的事是，我说：嘿，给定——

**24:20** · this five here's the option price also given this five here's the option price and so on and so on and so on and so on and I say hey neural network learn the relationship between the five inputs and the price then what I can do is if the

> ——这一组五个参数，这里是期权价格；给定这一组五个参数，这里是期权价格；如此反复、反复。然后我说：嘿，神经网络，学习这五个输入与价格之间的关系。那么我能做的就是，如果——

**24:36** · neural network learns effectively I can give it a set of parameters that is within the bounds of that which I've generated for it to train with but I can generate approximate prices under that model and that model's assumptions this

> ——神经网络学习得有效，我就可以给它一组参数——只要这组参数落在我生成给它训练的范围内——然后我就能在那个模型及其假设下生成近似价格。这件事——

**24:52** · is extremely useful in the case of the black shols right now no not useful at all we have the analytical solution why would I ever do this again you understand this you understand the useful case so here I generate all of my

> ——在 Black-Scholes 的情形下极其有用吗？现在，不——完全没用，因为我们有解析解，我何必再这样做呢？你理解了这个，你也就理解了有用的场景。所以在这里，我生成我所有的——

**25:04** · parameter sets those are my inputs but now it's a series of inputs I have 5,000 inputs that is I have parameter set of five inputs parameter set of five inputs parameter set of five inputs 5,000 times then I have via the black shows call

> ——参数集，那些就是我的输入，但现在是输入的序列：我有 5,000 个输入，也就是一组五个参数、一组五个参数、一组五个参数，共 5,000 组。然后我通过之前创建的 Black-Scholes 看涨——

**25:23** · function that I created earlier I have 5,000 option prices then I create a very basic neural network and what I'm saying is I want you to learn by a th000 Epoch the relationship of those five parameters to the option prices and we

> ——函数，得到 5,000 个期权价格。然后我创建一个非常基础的神经网络，我说的是：我要你在 1,000 个 epoch 内学习这五个参数与期权价格之间的关系。而我们——

**25:38** · do this of course by minimizing the error but more specifically we're going to talk about neural networks machine learning and optimization another day this is going to be with respect to the video that I did on why the definition

> ——这样做当然是通过最小化误差（minimizing the error）。但更具体地说，关于神经网络、机器学习、优化，我们改天再谈——这将与我做的另一期"为什么导数的定义是有用的"视频有关——

**25:52** · of the derivative is useful so stay tuned for that until then this neural network once it learns the relationship we can go ahead and see I'm going to run this one more time so that I get the output because I forgot the F in that FR

> ——敬请期待。在那之前，这个神经网络一旦学会了这个关系，我们就可以去看——我要再运行一次以获得输出，因为我漏了那个 print 里的 f——

**26:09** · print there we can see that hey check this out given the parameter set this is parameter set number 3,817 the true price is 30449 4 and the approximate price is 30679 okay given the parameter set 425

> ——你看，我们可以看到了：嘿，看看这个，给定参数集（这是第 3,817 组参数集），真实价格是 3.04494，近似价格是 3.0679。好，给定参数集 425——

**26:29** · the crew price is 0142 and the prediction is negative clearly we would have to bound this because the intrinsic price of the option in this case can't be negative nevertheless we can see that all of

> ——真实价格是 0.142，而预测值是负的。显然我们必须对这个做约束（bound），因为在这种情况下期权的内在价值不能为负。尽管如此，我们可以看出所有——

**26:44** · these are approximations and they aren't too far off so I think it's reasonable to say that the neural network is learning black shs and as we increase obviously the training capacity maybe we'll make it 5,000 here for example you

> ——这些都是近似，而且相差不算太远。所以我认为可以合理地说，神经网络正在学习 Black-Scholes。而且，显然随着我们增加训练容量——比如这里把它改成 5,000——你——

**26:59** · can see that it is going to generate more and more accurate prices so here you can see 26.97 27.1 11.89

> ——可以看到它将生成越来越精确的价格。所以在这里你可以看到 26.97、27.1、11.89……

**27:27** · 11.79% most effective neural network structure or optim optimization scheme but short answer yes it can learn black shs more generally can it learn option prices that is a more important question because it's more General let's talk

> ——11.79……最有效的神经网络结构或优化方案。但简短的回答是：是的，它能学会 Black-Scholes。更一般地说，它能学会期权价格吗？这才是一个更重要的问题，因为它更普适。让我们谈谈——

**27:42** · about what that could look like again we're generating this parameter set and this is a pretty constrained parameter set I just want you to keep that in mind as well like I'm fixing the strike price here I'm fixing the risk-free rate so

> ——那会是什么样子。同样，我们正在生成这个参数集，而这是一个相当受限的参数集——我想让你也记住这一点。比如我在这里固定了执行价，我固定了无风险利率，所以——

**27:54** · you would want to generate a large number of permutations of these param as well okay but again this is for an analytical solution this is the useless case let's talk about the useful case what we've done here is we've generated

> ——你也应该生成这些参数的大量排列组合。好吧，但再说一遍，这是针对解析解的情形——这是"没用的情形"。让我们谈谈"有用的情形"。我们在这里做的是，我们生成了——

**28:08** · this neural network has learned the black shs model this is C Tilda Tilda so if we go back up here we have the analytical solution we have the simulated solution and this is the neural network approximation of the

> ——这个神经网络已经学会了 Black-Scholes 模型，这就是 C-tilde-tilde。所以如果我们回到上面那里，我们有解析解、我们有模拟解，而这是对——

**28:23** · simulated solution so C Tilda Tilda right now we are saying that that is approximating the analytical Solution that's what we have here the analytical solution to the five inputs but what if we don't have the analytical solution

> ——模拟解的神经网络近似。所以 C-tilde-tilde 现在，我们说它是在近似解析解——这就是我们这里的：五个输入的解析解。但如果我们没有解析解呢？——

**28:38** · we're going to have to replace this with simulation and that is really what the C Tilda Tilda is it's an approximation of the simulated price a h model could be an example of where we need to use simulation to get prices don't want to

> ——我们就必须用模拟来替换它。而这才是 C-tilde-tilde 真正的含义：它是对模拟价格的近似。Heston 模型可以作为一个需要我们用模拟来得到价格的例子。如果你不想——

**28:54** · use a h model want to use a more advanced model then do the exact same thing we're about to do with the hesta model with your more advanced model everyone's screaming at me that volatility is not constant well use this

> ——用 Heston 模型，而想用更先进的模型，那就把你即将与 Heston 模型一起做的事情，套用到你的更先进模型上。大家都冲我嚷嚷说波动率不是恒定的，那好，就用这个——

**29:06** · model instead volatility here is a stochastic differential equation governed by an orstein back process and it's going to be mean reverting that captures the Dynamics of volatility pretty well in the market take a look at

> ——模型代替。这里的波动率是一个由 Ornstein-Uhlenbeck 过程支配的随机微分方程，它是均值回归（mean reverting）的，能相当好地捕捉市场中的波动率动态。看看——

**29:16** · the vix look at my video on vix Marill volatility trading for example we look at the vix we look at the mean reverting nature of the vix I think this is a pretty reasonable model but what parameters should this model follow for

> ——VIX，看看我做的关于 VIX 均值回归波动率交易的那期视频。我们观察 VIX，我们观察 VIX 的均值回归特性。我认为这是一个相当合理的模型。但是，对于——

**29:28** · our given underlying that is going to depend on the current volatility surface we are trying to extrapolate prices for okay well how do we do that we're going to calibrate our surface to the market surface but we don't have a analytical

> ——给定的标的资产，这个模型应该采用什么参数呢？这将取决于我们试图外推价格时所面对的当前波动率曲面。好吧，我们怎么做呢？我们要把我们的曲面校准到市场曲面，但我们没有解析——

**29:44** · price I'm dismissing fft for now if everyone is saying that we can do some sort of characteristic function transformation I don't want to talk about that I'm saying again we can use the H model as an example for needing

> ——价格。我暂时不采用 FFT。如果大家都说我们可以做某种特征函数变换，我不想谈那个。我要说的是，我们可以用 Heston 模型作为"需要模拟"的例子——

**29:54** · simulation and that's what we're going to do so here our parameter set Theta and I'm not talking about just the Theta that is the long run variance I'm saying if we go back and we look at what the neural network approximation is doing

> ——而这就是我们要做的。所以这里我们的参数集是 θ——我说的不只是那个代表长期方差的 θ。我是说，如果我们回过头看神经网络近似在做什么——

**30:06** · it's saying hey given an arbitrary parameter set Theta you give me inputs you give me a price then I can learn that relationship using a neural network okay well I have a Theta Theta is my

> ——它说的是：嘿，给定任意参数集 θ，你给我输入，你给我价格，那我就可以用神经网络学习这种关系。好，我有一组 θ，θ 是我的——

**30:19** · parameter set for the hon model smt vft Capa Theta Kai WFT WFT smv those are correlated Brown emotions we have this parameter set but how do we generate prices for that parameter set we can't use an

> ——Heston 模型的参数集：S₀、V₀、T、r、κappa、θ、ξ、Wᵗ、Wᵗ 的 ρ——那些是相关的布朗运动。我们有这个参数集，但我们如何为该参数集生成价格呢？我们无法使用——

**30:36** · analytical solution I mean there is no analytical solution so we need to simulate so I have this discretization scheme and I simulate the hessen model forward for a parameter set just like I did with the black shs model but here we

> ——解析解。我的意思是，这里没有解析解，所以我们需要模拟。所以我有这个离散化（discretization）方案，我像对 Black-Scholes 模型那样，为一个参数集向前模拟 Heston 模型，但在这里我们——

**30:50** · don't have an analytical solution and what is the upshot we don't have this Assumption of constant volatility that's pretty nice okay well I can generate all these paths for this parameter set and discount back

> ——没有解析解。结果是什么呢？我们没有了恒定波动率这个假设，那相当不错。好吧，我可以为该参数集生成所有这些路径，贴现回——

**31:02** · the payoff and I can get the average of those payoffs find this you know this price of the option under this model framework today but if I wanted to do this live and I wanted to fit that that volatility

> ——收益，然后得到那些收益的平均值，从而求得在今天这个模型框架下的期权价格。但如果我想实时做这件事，想把这个波动率——

**31:16** · surface again iteratively through an optimization scheme to the market surface that is way too expensive I need to simulate way too many paths so what should I do well I'm going to do exct exactly what I'm about to do offline and

> ——曲面再次通过优化方案迭代地拟合到市场曲面，那就太昂贵了，我需要模拟太多太多的路径。那我该怎么办呢？嗯，我要做的正是接下来要离线做的事，并且——

**31:31** · I'm going to do it for a large number of parameters and then I can implement the neural network in real time and I can accept some error to be able to implement the model that captures the Dynamics that I'm interested in

> ——我要为大量的参数来做。然后我可以在实时环境中部署神经网络，并接受一定的误差，以便能够部署那个捕捉了我感兴趣的动态的模型——

**31:41** · capturing relative to the Dynamics that are assumed away that is in something like a black sches so what do I have here well if you take a look at this this scheme here what I'm doing is I'm taking these

> ——相对于像 Black-Scholes 那样被假设掉的动态。那么我这里有什么呢？嗯，如果你看一下这个方案，我在这里做的是，我取这些——

**31:55** · inputs and again this is no longer a five-dimensional input right this Vector remember this Theta Vector here is relative to our model so Theta here we have s0 v0 t r Capa Theta Kai and row these are going to be the parameters

> ——输入。再说一次，这不再是五维输入，对吧？记住，这个 θ 向量相对于我们的模型。所以这里的 θ 有：S₀、V₀、T、r、κappa、θ、ξ 和 ρ，这些将成为——

**32:13** · of the hon model so this is not a five-dimensional input like a black scholes but this is a 1 2 3 4 5 6 7 e Dimension eight dimensional vector or Nate Dimension vector and that is

> ——Heston 模型的参数。所以这不是像 Black-Scholes 那样的五维输入，而是 1、2、3、4、5、6、7——8 维的向量，八维向量。而那就是——

**32:31** · going to be our input okay so black shes five parameter input price hon eight parameter input price but that middle thing that we're inputting these parameters to we need to make that and that's what we're doing with this neural

> ——我们的输入。好吧，所以 Black-Scholes 是五个参数输入得到价格，Heston 是八个参数输入得到价格。但中间那个我们把这些参数输入进去的东西，我们需要把它造出来——而这正是我们用这个神经——

**32:43** · network so here I'm going to actually generate a whole bunch of possible parameter sets that's exactly what I'm doing here is I'm generating a whole bunch of possible parameter sets all right my stock prices my you know

> ——网络在做的事。所以在这里，我实际上要生成一大堆可能的参数集——这正是我在这里所做的：我生成一大堆可能的参数集，包括我的股票价格、我的，你知道——

**32:57** · variance and all of this I'm generating a whole bunch of possible parameter sets then I'm actually going to simulate okay I'm simulating these parameters going forward just like I did here and then

> ——方差以及所有这些，我生成一大堆可能的参数集。然后我实际上去模拟：好吧，我像刚才在这里做的那样，把这些参数向前模拟，然后——

**33:10** · I'm going to back out the price by finding some sort of payoff and discounting it back to the present then taking the average that's how I'm generating the prices that's the numerical simulation the Monte Carlo

> ——我要反推（back out）出价格：找到某种收益，把它贴现回当前时刻，然后取平均。我就是这样生成价格的——这就是数值模拟、蒙特卡洛——

**33:21** · simulation that's our second option but remember in real time that's slow that's why we're doing this offline we're doing this when we have a lot of time and it doesn't matter so that when we do require efficiency our network has

> ——模拟，那是我们的第二个选项。但要记住，在实时环境中那很慢，这就是为什么我们要离线做这件事——我们在有大量时间、时效性不重要的时侯做，这样当我们确实需要效率时，我们的网络已经——

**33:35** · already done the heavy lifting offline again when time didn't matter and then in real time it's very very quick and and accurate and that's exactly the point here is what we're doing is we're training this neural network through all

> ——在时间不重要的离线阶段做完了繁重的工作。然后在实时环境中它非常非常快，而且准确。这正是重点所在：我们所做的，就是通过所有这些——

**33:48** · of these hon parameters now these are not black schols parameters and we end up with check this out here's a set of inputs here's the true price and here's the neural network prediction that's pretty darn good here's the true price

> ——Heston 参数来训练这个神经网络。注意，这些不是 Black-Scholes 参数。结果我们得到——看看这个：这是一组输入，这是真实价格，这是神经网络预测——相当不错。这是真实价格——

**34:00** · here's the neural network prediction and so on and so on you're like hey these these predictions are not that great well I did not train this for very long I only used 1,000 Epoch and moreover I only simulated 500 paths so this is

> ——这是神经网络预测，如此这般。你会说：嘿，这些预测不怎么样啊。嗯，我并没有训练它很久，我只用了 1,000 个 epoch，而且我只模拟了 500 条路径。所以这是——

**34:14** · awful this is awful if I really cared about the Precision of this of this model that remember I have eight parameters going into my neural network out comes the price that's the C Tilda Tilda if I really cared about the

> ——糟糕的，这很糟糕。如果我真的很在意这个模型的精确度——记住，我有八个参数进入我的神经网络，出来的是价格，也就是 C-tilde-tilde——如果我真的很在意——

**34:29** · Precision then or not even just the Precision but the accuracy then I would need to jack these numbers up right I would need to jack these numbers up and that's exactly the point and this error is very well studied this error is very

> ——精确度，甚至不只是精确度，还有准确性，那我就需要把这些数字往上调，对吧？我需要把这些数字往上调。而这正是重点。而且这个误差被研究得很透彻，这个误差非常——

**34:41** · well studied so if you required a certain amount of prision you can run the statistics very easily you can run some sort of confidence interval very easily but this right here this is the main point of the Lit Literature and

> ——非常地有研究。所以如果你需要一定程度的精度，你可以很容易地做统计，很容易地运行某种置信区间。但这里，这才是这篇文献的核心要点。而且——

**34:53** · this of course is some fancy crazy looking chart that shows you know how the neural network prediction fits relative to the cre fit and the error evolving um and and this is you know due to the idea of some sort of

> ——这当然是一些花哨的、看起来有点疯狂的图，它展示神经网络预测相对于真实拟合的贴合程度，以及误差的演变。嗯，而且这是出于某种——

**35:04** · extrapolation error as well if you you know come back up to the quadratic example you can see that out of a range of parameters we start to perform poorly and this particular scheme is generating some kind of crazy looking error it

> ——外推误差的想法。如果你回到二次函数的例子，你可以看到在参数范围之外，我们开始表现不佳。而这个特定方案正在生成某种看起来疯狂的误差，它——

**35:18** · doesn't look as linear as as it does in the black shols setting um but that's not the point of this video the point of this video is not to optimize the network to you know learn the approximate pricing function via

> ——看起来不像 Black-Scholes 情形里那样线性。嗯，但这并不是本期视频的重点。本期视频的重点不是去优化网络，去通过模拟学习近似的定价函数——

**35:31** · simulation that's not the point of this video we can talk about that another time if if you guys actually care about the optimal schemes for this stuff we we can talk about it but this is just about as Quant of a topic as it can get we're

> ——那不是本期视频的重点。我们可以在另一个时间再谈这个，如果你们真的在乎这些东西的最优方案，我们可以谈。但这就是一个再"量化"不过的话题了。我们——

**35:44** · combining neural networks with financial mathematics and the hope is that we can improve efficiency we're kind of double dipping you know can we improve efficiency while keeping these you know dynamics that we're capturing intact of

> ——把神经网络与金融数学结合起来，希望我们能提高效率。我们有点像"一鱼两吃"：我们能不能在保持所捕捉的那些动态特性的同时提高效率？当然——

**35:58** · course you're not going to get something for nothing you're paying some sort of you know relative error but this is an incredibly interesting topic because you're you're kind of getting something for nothing because you're doing all the

> ——你不可能不劳而获，你是在付出某种相对误差。但这是一个极其有趣的话题，因为你有点像是"空手套白狼"：你是在离线阶段做所有——

**36:09** · heavy lifting offline and if you can constrain that error then this is going to be very very good so moral of the story moral of the story is you know we have the ability to price in a given model's framework analytically or

> ——繁重的工作，而且如果你能约束住那个误差，那这就会非常非常好。所以，故事的寓意，故事的寓意是：我们有能力在给定模型的框架下，解析地或——

**36:24** · numerically most of the time we can't do it analytically so we do numerically but in real time if we have any hope of implementing more complicated models that capture more Dynamics we can't just simulate in real time that's going to

> ——数值地定价。大多数时候我们无法解析地做，所以我们数值地做。但在实时环境中，如果我们有任何希望部署那些捕捉更多动态的复杂模型，我们不能就在实时中去模拟，那会——

**36:36** · take far too long so what can we do well we can generate all of these parameter sets and prices via simulation offline and then we can train a neural network that is essentially a deterministic function that's trying to act like that

> ——花上太长时间。那我们能做什么？嗯，我们可以离线地通过模拟生成所有这些参数集和价格，然后训练一个神经网络——它本质上是一个确定性的函数，试图扮演那个——

**36:51** · analytical function that is that black shs example and once we do that offline and we get a reasonably precise and accurate model we can Implement that in real time because the naral networks are extremely extremely fast it's just a

> ——解析函数，也就是那个 Black-Scholes 例子。一旦我们离线做完这些，得到一个相当精确且准确的模型，我们就可以在实时环境中部署它，因为神经网络极其极其快。它只是一系列——

**37:06** · series of linear transformation and and nonlinear activations it's it's a very very fast operation so if the weights that it learns are correct then it is an extremely powerful tool especially applied in this

> ——线性变换和非线性激活（nonlinear activations），这是一种非常非常快的运算。所以如果它学到的权重是正确的，那它就是极其强大的工具，尤其是在这个——

**37:20** · setting with that being said this is probably the most involved Quant topic we've discussed on this channel so so I hope you enjoyed this is not trivial subject matter so if you have any questions please feel free to leave a

> ——场景下应用时。话虽如此，这可能是我们频道讨论过的最深入的量化话题了。所以我希望你们喜欢。这不是一个浅显的课题。所以如果你有任何问题，请随时——

**37:35** · comment below check out Discord you can join our Discord discuss this idea among others we have a very active Discord community and I'm very happy to answer any questions on on there or on YouTube or you can always reach out to me if you

> ——在下方留言。看看 Discord，你可以加入我们的 Discord，讨论这个想法以及其他话题。我们有一个非常活跃的 Discord 社区，我很乐意在上面或 YouTube 上回答任何问题。或者，如果你——

**37:49** · have any questions directly but other than that I want to thank you so much for watching this is one of my favorite topics I hope you enjoyed and I'll see you in the next one

> ——有任何问题，也随时可以私下联系我。除此之外，非常感谢你们的观看。这是我最喜欢的话题之一，希望你们喜欢，我们下期再见。
