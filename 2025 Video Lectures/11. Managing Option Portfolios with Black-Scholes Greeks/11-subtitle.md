---
title: "Managing Option Portfolios with Black-Scholes Greeks"
source: "https://www.youtube.com/watch?v=Augr2c-PMc4"
author:
  - "[[Roman Paolucci]]"
published: 2025-03-21
created: 2026-08-04
description: "🚀 Master Quantitative Skills with Quant Guild:https://quantguild.comMarch 2025 Promo Question for Quant Guild Lifetime Access:https://www.youtube.com/channel/UCW1svfGxG4ADnbc1HCH6dqA/community?lb"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Augr2c-PMc4)

🚀 Master Quantitative Skills with Quant Guild:  
https://quantguild.com  
  
March 2025 Promo Question for Quant Guild Lifetime Access:  
https://www.youtube.com/channel/UCW1svfGxG4ADnbc1HCH6dqA/community?lb=UgkxIAhQCKcI8GHGE-T\_V0JIIZ4FB9nbkeLQ  
  
Join the Quant Guild Discord server here:  
https://discord.com/invite/MJ4FU2c6c3  
  
Jupyter Notebook:  
https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/11.%20Managing%20Option%20Portfolios%20with%20Black-Scholes%20Greeks/Managing%20Option%20Portfolios.ipynb  
  
Approximating Derivatives:  
https://www.youtube.com/watch?v=CD8XYP4lq4g  
  
Black-Scholes Equation Derivation:  
https://www.youtube.com/watch?v=2iClLEfXuqA  
https://medium.com/swlh/deriving-the-black-scholes-model-5e518c65d0bc  
  
European Options 101:  
https://www.youtube.com/watch?v=HgjeDJVCHSo  
  
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

**00:01** · [Music] welcome back today we're going to talk about managing option portfolios specifically we're going to talk about different exposures you may have when you hold a portfolio of options we're

> 欢迎回来。今天我们要谈论如何管理期权组合（option portfolio），具体来说，是讨论当你持有一个期权组合时可能面临的各种风险敞口（exposure）。我们将——

**00:13** · going to talk about the so-called Greeks going to develop some mathematical intuition behind what each Greek actually represents starting from the basic idea of a linear approximation if you have no mathematical background then

> ——谈谈所谓的"希腊字母"（Greeks）。我们将从线性近似（linear approximation）这一基本概念入手，建立起对每个希腊字母实际含义的数学直觉。如果你没有数学背景，也别担心，——

**00:27** · we're going to do this visually so it makes sense then we will apply it to the idea of an option contract priced via the black shols model and we'll talk about hedging and the idea of hedging our different risk exposures using a

> ——我们会用直观的可视化方式来讲解，让你看得明白。然后我们会把它应用到用 Black-Scholes 模型定价的期权合约上，并讨论对冲（hedging）的概念，以及如何用——

**00:41** · portfolio of options and or stock let's begin by discussing this idea of a linear approximation we're going to talk about a first order tailor series approximation of this polinomial

> ——一个由期权和/或股票组成的组合来对冲我们不同的风险敞口。让我们从讨论"线性近似"这个想法开始。我们要讨论这个多项式函数的——

**00:54** · function f ofx and though the mathematics may sound difficult to comprehend and may sound relatively rigorous it's actually quite easy to interpret once we get to the visual component of this so bear with me here

> ——一阶泰勒级数近似（first-order Taylor series approximation）。虽然这些数学听起来可能难以理解、也比较严谨，但一旦我们看到它的可视化部分，就会发现它其实非常容易解读。请耐心听我讲下去。

**01:08** · what we have is this idea of an approximation of a function now this function could be an option pricing function it could be a profit function a cost function the actual interpretation of the function doesn't matter you can

> 我们这里要讲的是对某个函数的近似。这个函数可以是期权定价函数，也可以是利润函数、成本函数。函数的具体含义并不重要，你都可以——

**01:21** · still apply this Taylor series expansion approximation so what we have here is we have this function is approximately equal to the function evaluated at a point of Interest this point of Interest could be the current market prices the

> ——对它应用这种泰勒级数展开近似。所以我们有：这个函数近似等于函数在某个兴趣点（point of interest）处的取值。这个兴趣点可以是当前的市场价格，——

**01:36** · current market parameter set it could be the parameter set yielding the profit of last year it could be the parameter set yielding the cost of last year you can use any point of interest to develop this idea of a linear approximation so

> ——当前的市场参数集合；也可以是去年产生利润的那组参数，或去年产生成本的那组参数。你可以用任意兴趣点来建立这种线性近似的概念。所以——

**01:54** · it's going to be the function evaluated at that point of interest plus the first derivative ative of the function again that function is the pricing function the profit or cost function whatever it may be the first derivative of that

> ——它就是：函数在兴趣点处的取值，加上函数的一阶导数。再说一遍，这个函数就是定价函数、利润函数或成本函数，无论它是什么。这个函数在兴趣点处的一阶导数，——

**02:08** · function evaluated that at that point of Interest times a new point of Interest less the point of Interest so we have this idea of x0 being the initial point the starting point that could be the current market parameter set could be a

> ——乘以（新的兴趣点减去原兴趣点）。所以我们有这样一个概念：x0 是初始点、起点，它可以是当前的市场参数集合，也可以是——

**02:25** · parameter set from last year then we are trying to figure out hey what does it look like at this new point of interest that is this x okay so what about this derivative here what if we don't know how to compute the derivative of this

> ——去年的参数集合。然后我们想弄清楚：在这个新的兴趣点，也就是这个 x 处，函数会是什么样子。那么这里的导数呢？如果我们不知道怎么计算这个函数的导数怎么办？

**02:40** · function what if it's got an intractable analytical solution well check out my video on why the definition of a derivative is useful and you can actually develop an approximation for this overall approximation so you can

> 如果这个函数没有易于求解的解析解怎么办？请去看我那个关于"为什么导数的定义很有用"的视频，你实际上可以为这整个近似构造出一个近似。这样你就可以——

**02:54** · approximate this derivative then you can approximate this overall functional approxim o imation so that's enough mathematics let's talk about the intuition behind a linear approximation all this fancy terminology aside a

> ——先近似这个导数，然后再近似整个函数的近似值。好了，数学部分就到这里。让我们来谈谈线性近似背后的直觉。抛开所有这些花哨的术语，其实——

**03:09** · linear approximation linear means line we are using a line to approximate a function we have a nonlinear function here in blue that is this polinomial X2 and as you can see the nonlinear function is being approximated at a

> 线性近似——"线性"意味着"直线"，我们用一条直线去近似一个函数。这里我们有一个非线性函数，就是蓝色的这个多项式 x²。你可以看到，这个非线性函数在某个兴趣点处被近似——

**03:26** · point of interest and that point of interest in this case is 10 and I've cre this slider to show you what happens as you change the point of interest and what you'll notice is the approximation tends to be very good

> ——而这个兴趣点在这里是 10。我做了这个滑块，用来向你展示当你改变兴趣点时会发生什么。你会注意到，近似在兴趣点附近往往非常准确。

**03:39** · about the point of Interest so we're actually using a linear function to approximate a nonlinear function that's this idea of a linear approximation and this is only a first order approximation so the

> 也就是说，我们实际上是在用一个线性函数去近似一个非线性函数——这就是线性近似的概念。而且这只是一阶近似，所以——

**03:52** · approximation can get better but let's just focus on this idea of a first order approximation as you can see if I go a little bit to the right of the 10 or a little bit to the left of the 10 that is our point of Interest that's our x0 as I

> ——近似还可以做得更好，但我们先专注于"一阶近似"这个概念。你可以看到，如果我往 10 的右边稍微移一点，或往 10 的左边稍微移一点——10 就是我们的兴趣点、我们的 x0，正如我——

**04:10** · said it could be the market parameter set or a parameter set for profit or cost last year the line the linear approximation does a very good job approximating the nonlinear function that is this x squ

> ——所说，它可以是市场参数集合，也可以是去年利润或成本的参数集合。这条直线——这条线性近似——在近似这个非线性函数（即 x²）方面表现得非常好。

**04:23** · but what you'll notice is because it is a linear approximation it doesn't capture the growth of the polom that is as we move further away in either direction the approximation gets worse and worse and this makes sense right if

> 但你会注意到，因为它是线性近似，它无法捕捉到多项式的增长。也就是说，无论我们往哪个方向走得越远，近似就变得越来越差。这很有道理，对吧？如果——

**04:38** · I gave you information about this 10 and I'm saying hey we're going to reduce the order of this polinomial the further we get away this distance between the red line the linear approximation and the nonlinear function is going to increase

> ——我只给你关于这个 10 的信息，而我正在降低这个多项式的阶数，那么离得越远，红色直线（线性近似）与非线性函数之间的距离就会越大。

**04:53** · this distance is the error so as we get further away from the point of Interest the error is going to increase that is the idea of a linear approximation we can use this idea to very simply interpret how we can expect the

> 这个距离就是误差（error）。所以我们离兴趣点越远，误差就会越大——这就是线性近似的概念。我们可以用这个想法非常简单地解读：当输入发生变化时，我们预期——

**05:12** · nonlinear function to change when there is a change in the input so a unit change in the input what can we expect the overall function to change so for example if I have a unit change in the input of a price in function how can I

> ——这个非线性函数会如何变化。比如输入有一个单位的变化，我们可以预期整体函数会改变多少？例如，如果价格函数（price function）的输入有一个单位的变化，我该如何——

**05:31** · expect the price to change if I have a unit change in the input of a profit function how can I expect the profit to change if I have a unit change in the function or a cost function how can I expect the costs to change so that's why

> ——预期价格会怎么变？如果利润函数的输入有一个单位的变化，我该如何预期利润的变化？如果成本函数的输入有一个单位的变化，我该如何预期成本的变化？这正是——

**05:49** · this idea of a linear approximation is so useful it's very very easy to interpret essentially I'm saying is hey we have all these inputs we have a function that describes price cost profit when I have a very small change

> 线性近似这个概念如此有用的原因。它非常非常容易解读。本质上我想说的是：我们有所有这些输入，有一个描述价格、成本、利润的函数。当输入有非常微小的变化——

**06:02** · or a unit change in the input what happens to the overall function does the price increase does the profit increase does the cost increase do they decrease that is the idea of a linear approximation so you can see here if we

> ——或一个单位的变化时，整体函数会发生什么？价格会上升吗？利润会增加吗？成本会上升还是下降？这就是线性近似的概念。所以你可以看到，如果我们——

**06:17** · move to the right the line is increasing and so is our nonlinear function so we expect a unit change in X to yield an increase in this polinomial function same thing if we step to the other direction we expect this polinomial

> ——向右移动，这条直线在上升，我们的非线性函数也在上升。所以我们预期 x 的一个单位变化会带来这个多项式函数的上升。如果我们朝另一个方向走，同样，我们预期这个多项式——

**06:35** · function to decrease and that's exactly what happens now what about when we get to this new point we're going to want to do another linear approximation so let's say we start at 10 what happens if I step to the left one well we're going to

> ——函数会下降，实际情况正是如此。那么当我们到达这个新点时，我们想再做一次线性近似。假设我们从 10 开始，如果我向左移一步会怎样？我们会——

**06:50** · expect the polinomial to decrease now I'm going to recompute this linear approximation for 9 and we can continue and do this in a iterative fashion so we're going to continue to recompute this linear

> ——预期这个多项式下降。现在我要为 9 重新计算这次线性近似。我们可以以迭代的方式继续这样做——我们会持续重新计算这条线性——

**07:04** · approximation so as we move about the space of this function our linear approximation is going to be centered about the point of interest that could reflect the current market conditions could reflect the current inputs into

> ——近似。所以当我们在这个函数的空间里移动时，我们的线性近似将始终围绕兴趣点展开。这个兴趣点可以反映当前的市场状况，可以反映输入到我们利润函数或成本函数——

**07:18** · our profit function or cost function so on and so forth so the idea of this linear approximation is it's very easy to interpret in the sense that we can say what happens to the overall function based on a unit change in a particular

> ——中的当前输入，诸如此类。所以线性近似的理念在于它非常容易解读：我们可以说，基于某个特定输入的一个单位变化，整体函数会发生什么。

**07:34** · input and it turns out if you have a variety of inputs this makes it very easy to determine hey if I change this one variable a little bit and I hold everything else constant what can I expect that function to do so if profit

> 而且事实证明，如果你有各种各样的输入，这就变得非常容易判断：嘿，如果我把这一个变量稍微改一点，其它一切保持不变，我可以预期这个函数会怎样？所以如果利润——

**07:49** · is a function of let's say overall labor and overall materials then what happens if I increase materials what happens when I increase labor we can see what happens to the corresponding profit function taking a look at actual numbers

> ——是总劳动力和总原材料（假设如此）的函数，那么如果我增加原材料会怎样？增加劳动力会怎样？我们可以看到相应的利润函数会发生什么。来看一些实际数字。

**08:05** · we have this linear approximation about the point 10 how good is this approximation well we're going to start at this point of Interest 10 let's move 0.1 to the right what I'm going to do is I'm going to use this linear

> 我们以 10 为中心做线性近似，这个近似有多好呢？我们从兴趣点 10 出发，向右移动 0.1。我要做的是：使用这个线性——

**08:18** · approximation and I'm going to use the actual function so I'm going to use both the actual functional change which is represented by a change in the nonlinear function this polinomial function and I'm going to represent the change in

> ——近似，同时使用实际函数。我会同时计算实际的函数变化——也就是非线性函数、这个多项式函数的变化——以及线性近似的——

**08:32** · the linear approximation then we're going to take a look at the error so what I do here is I have the actual function change and I have the approximate function change and as you can see the actual function change is 2.

> ——变化，然后我们来观察误差。我这里做的是：既有实际函数变化，也有近似函数变化。正如你所看到的，实际函数变化大约是——

**08:45** · or 2.01 approximately and the approximate function change is 2.0 that is a very good approximation now you can do a whole bunch of analysis that's going to tell you the actual interpretation and

> ——2.01，而近似函数变化是 2.0。这是一个非常好的近似。当然，你可以做一大堆分析，来告诉你这个误差的实际解释和——

**08:59** · Bounds of this error but for what we're trying to use it for this is a phenomenal approximation based on the intuition that hey when there's a small change in this variable X how do we expect the overall function x^2 to

> ——边界。但就我们想用它来达到的目的而言，这是一个非常出色的近似。它的依据是这样的直觉：嘿，当变量 x 发生一个小变化时，我们预期整个函数 x² 会——

**09:15** · change clearly when we move away from this point too much this error is going to be significantly larger let's give an example as you can see we're moving 0.1 to the right what happens if we move five to the right

> ——如何变化？显然，当我们离这个点太远时，误差会显著变大。举个例子：如你所见，我们向右移动 0.1；如果我们向右移动 5 呢？

**09:31** · we have quite a significant difference in the actual function change and the approximate function change moreover if I move 10 you can see that this error is going to continue to increase and that makes sense because

> 我们会看到实际函数变化与近似函数变化之间有相当大的差异。此外，如果我移动 10，你可以看到这个误差会继续增大。这说得通，因为——

**09:45** · this polinomial is growing at a much faster rate again this is x^2 versus just a linear approximation of that function as we move away from this initial point this distance you can already see it here locally as this

> ——这个多项式以更快的速度增长。再说一遍，这是 x²，而它只是一个对该函数的线性近似。当我们离开这个初始点时，这个距离——你已经可以在这里局部地看到它——

**09:58** · distance As you move away from the point of Interest x0 the distance between the red line and the blue line is going to continue to increase and that's what we can see here you can see that if the change is 10 and we're centered at 10

> 当你离兴趣点 x0 越来越远时，红线与蓝线之间的距离会持续增大——这就是我们在这里看到的情况。你可以看到，如果变化量是 10，而我们以 10 为中心，——

**10:15** · then the approximate change is starting to get significantly worse if I make this now 20 it's getting even worse if I make this now 50 it's getting even worse and that's exactly what we see in our chart here

> ——那么近似的效果就开始明显变差。如果我把它设为 20，就更差了；如果设为 50，就更差。这正是我们在这张图表中看到的。

**10:28** · locally we can see as we deviate too much away from this point of Interest x0 the linear approximation gets worse so what can we do well just like with this slider we can just compute a new linear approximation at the next point

> 局部来看，当我们偏离兴趣点 x0 太远时，线性近似就变差了。那我们能做什么呢？就像用这个滑块一样，我们可以简单地在下一个兴趣点处计算一次新的线性近似，——

**10:43** · of interest and that's going to give us the same intuition and interpretation of what happens to the polom function again that could be the pricing function profit or cost function when there is a unit change in one of the inputs in this

> ——这样我们就能得到同样的直觉和解读：当某个输入（在这里是 x）有一个单位的变化时，这个多项式函数——同样，它可以是定价函数、利润函数或成本函数——会发生什么。

**10:58** · case X all right now that's a lot of calculus but why are we talking about linear approximations anyway remember we're trying to get at this idea of managing an option portfolio and in order to

> 好了，那是很多微积分了。但我们到底为什么谈论线性近似呢？记住，我们是想理解"管理期权组合"这件事，而为了——

**11:09** · manage an option portfolio we need to understand the exposures that accompany an option contract and in this case we typically refer to them as the Greeks that is a European call or put option based on the black schs model is going

> ——管理一个期权组合，我们需要理解伴随期权合约的风险敞口。在这里，我们通常把它们称为"希腊字母"（Greeks）。也就是说，基于 Black-Scholes 模型的欧式看涨或看跌期权，将——

**11:25** · to have a variety of inputs that affect its price we have the idea of the underlying stock price and the underlying stock price changing the time to maturity and time to maturity changing volatility and the

> ——会有各种各样的输入影响它的价格。我们有基础股票价格（underlying stock price）以及它的变化，到期时间（time to maturity）及其变化，波动率（volatility）及其变化，还有——

**11:41** · volatility changing the idea of row and interest rates and interest rates changing and there are a whole bunch of not just first order sensitivities but also second order sensitivities that you can compute but you'll notice that there

> 波动率的变化、利率（interest rates）与 Rho 的概念以及它们的变化。而且有一大堆敏感性可以计算——不仅有各一阶敏感性（first-order sensitivities），还有二阶敏感性（second-order sensitivities）。但你会注意到——

**11:55** · is no sensitivity to the strike price and that's because it is fixed throughout the life of the option contract so here we have our black sches pricing model this is a nonlinear function just like our x s so if we have

> 对行权价（strike price）却没有敏感性，那是因为行权价在整个期权合约存续期内是固定的。所以我们这里有 Black-Scholes 定价模型，它和我们的 x² 一样是一个非线性函数。所以如果我们有——

**12:13** · a nonlinear function just like our x s we can apply the same idea of a first order tailor series expansion in this case we're just going to compute the partial derivative relative to the function that is the BL

> ——一个像 x² 一样的非线性函数，我们就可以应用相同的一阶泰勒级数展开思想。在这种情况下，我们只需要针对 Black-Scholes 定价模型这个函数，对每一个输入——

**12:27** · shs pricing model for each of the inputs and then we're going to have a linear approximation essentially the way that you can think about it is we're going to have this pricing function and a red line for each of the inputs so we'll

> ——分别计算偏导数（partial derivative），然后我们就有了一个线性近似。本质上，你可以这样想：我们有这个定价函数，以及对应每个输入的一条红线。所以我们会——

**12:41** · have a linear approximation for the change in the underlying stock price a linear approximation for the change in time linear approximation for the change in volatility linear approximation for the change in interest rates and what

> ——有一个针对基础股票价格变化的线性近似、一个针对时间变化的线性近似、一个针对波动率变化的线性近似、一个针对利率变化的线性近似。而我们——

**12:54** · we're going to be able to do then is analyze how we can expect our option value to change when there's a unit change in each of these inputs so Delta these are the Greeks now that is this idea of a linear approximation of the

> ——接下来能做的就是分析：当每个输入发生一个单位的变化时，我们预期期权价值会如何变化。所以，Delta 等——这些就是希腊字母。现在，这正是一个对期权价格变化的线性近似的概念。

**13:11** · change in option price we have Delta which is the Greek representing the first order sensitivity of the underlying asset price we have Theta which is the same thing for the time to maturity Vega which is the same

> 我们有 Delta，它是代表对基础资产价格一阶敏感性的希腊字母；我们有 Theta，它是对到期时间的同样敏感性；Vega 则是——

**13:26** · thing for volatility row which is the the sensitivity to interest rates and then gamma is a second order sensitivity but we're not going to focus too much on that that is the rate in which Delta changes that's going to be a video for

> 对波动率的同样敏感性；Rho 是对利率的敏感性。而 Gamma 是一个二阶敏感性，我们不会太关注它——它衡量的是 Delta 变化的速率，这会是——

**13:39** · another day but essentially all of these Greeks are just using this idea of a linear approximation what we're essentially doing is we are doing this linear approximation for each input into the

> 另一期视频的主题。但本质上，所有这些希腊字母都只是在利用线性近似这个想法。我们实际上做的事情是：对输入 Black-Scholes 模型的每个输入变量——

**13:56** · black shes model so there are four four inputs into this blacks model to determine a price of course there's the strike price but that's fixed okay so I know there are five inputs but bear with me the

> 分别做一次线性近似。所以这个 Black-Scholes 模型有四个、四个输入来决定价格——当然还有行权价，但它是固定的。好了，我知道实际上有五个输入，但请听我说完——

**14:10** · strike price is fixed these four inputs can change throughout the life of the option contract so what we're going to do is we're going to compute a linear approximation for each of these inputs and then we're going to be able to see

> 行权价是固定的，而这四个输入在期权合约的存续期内都可以变化。所以我们要做的是：对这每一个输入分别计算线性近似，然后我们就能够看到——

**14:22** · at any point in time how we can expect our option contract or our portfolio of options to change when there is a change in one of these input variables and keep in mind the underlying asset price changes all the time the time to

> 在任意时间点，当其中一个输入变量发生变化时，我们预期我们的期权合约或期权组合会如何变化。而且请记住：基础资产价格一直在变，到期时间——

**14:39** · maturity changes every day volatility changes every day it's a it's a continuous process right implied volatility even though the model assumes it's fixed it's not in reality right volatility and the implied volatility of

> 每天都变，波动率每天都变——这是一个持续不断的过程，对吧？隐含波动率（implied volatility）即使模型假定它是固定的，实际上也并非如此。波动率，以及期权的隐含波动率，——

**14:55** · an option is determined by an equilibrium price and backing out the volatility to produce that market price so these linear approximations are going to give us insight into how we can expect our option portfolio to

> 是由均衡价格决定的：通过反解出能产生那个市场价格的波动率。所以这些线性近似将给我们带来洞察：当这些变量中的任何一个变化时，我们预期我们的期权组合会——

**15:09** · change when any one of these variables change how is this useful well if we have no idea how our option portfolio is going to change when there's a change in the underlying asset price or or there's a change in time or change in volatility

> 如何变化。这有什么用呢？如果我们完全不知道当基础资产价格变化、或时间变化、或波动率变化时，我们的期权组合会如何变化，——

**15:25** · then how can we possibly understand our exposure if all of a sudden there's a massive amount of uncertainty due to tariffs or macro changes or whatever this is maybe fear starts to increase and volatility

> 那我们怎么可能理解自己的敞口呢？如果突然之间，由于关税、宏观变化或诸如此类的事情出现了巨大的不确定性——也许恐慌情绪开始上升，波动率——

**15:40** · increases you should know what happens to your option portfolio if you're net positive or negative Vega if your portfolio value is going to increase or decrease that's exactly what this linear approximation is going to tell you

> 上升——你应该知道你的期权组合会发生什么：你的 Vega 是净正还是净负？你的组合价值会上升还是下降？这正是这个线性近似要告诉你的，——

**15:54** · that's exactly what the Greeks are going to tell you so I've built functions here for each of the Greeks that we are going to analyze that is these four Delta Theta Vega and row and I've also developed a pricing function for the

> 这正是希腊字母要告诉你的。所以我这里为我们要分析的每个希腊字母编写了函数——也就是这四个：Delta、Theta、Vega 和 Rho——我还写了一个 Black-Scholes 看涨期权——

**16:08** · black schs call I'm going to post this I'm going to link it in the description below I'll post it on GitHub if you want to check out this Jupiter notebook what I have here now is an example of Delta Theta Vega row relative to a parameter

> 的定价函数。我会把这个发布出来，在下方简介中给出链接，也会上传到 GitHub，如果你想查看这个 Jupyter Notebook 的话。我现在展示的是相对于一组参数的 Delta、Theta、Vega、Rho 的例子——

**16:22** · set for one European call option so what I have here is I have the current market parameters I have the current underlying asset price the current strike price remember this is fixed throughout the life of the contract so there is no

> 即针对一份欧式看涨期权的参数集合。所以我这里有的是当前的市场参数：当前的基础资产价格、当前的行权价（记住它在合约存续期内是固定的，所以没有——

**16:35** · sensitivity to the strike price time to maturity the risk-free rate and the volatility I have now Delta Theta Vega and row that is representing a unit change in the underlying asset price time to maturity volatility and the

> 对行权价的敏感性）、到期时间、无风险利率和波动率。我现在有了 Delta、Theta、Vega 和 Rho，它们代表的分别是基础资产价格、到期时间、波动率和——

**16:53** · interest rates and each of these represents what's going to happen to our approximately of course option price so that is if we are long a European call option and there is a unit change in the underlying asset price then we would

> 利率发生一个单位的变化。而每一个都代表我们的期权价格（近似地，当然）会发生什么。也就是说，如果我们做多一份欧式看涨期权，而基础资产价格有一个单位的变化，那么我们预期——

**17:10** · expect the call option to increase by roughly 64 well let's test this out would you look at that that increases by roughly 64 now why didn't it increase by precisely 64 well again it's a

> 这个看涨期权会大约上涨 0.64。好，让我们来验证一下。你看，它确实上涨了大约 0.64。那为什么没有精确地上涨 0.64 呢？因为再说一遍，它是一个——

**17:29** · approximation just as we had here we had that even though we're moving very slightly away from this initial point of interest there is still a little bit of error now this error is negligible for the interpretation and understanding

> ——近似。就像我们之前遇到的那样：即使我们只是非常轻微地离开了初始兴趣点，仍然会有一点点误差。不过对于我们从实现这个希腊字母中获得的解读和理解来说，这个误差是可以忽略不计的。

**17:43** · that we get from implementing this Greek one of the things that you will notice is the Delta is also a nonlinear function so we're using a linear approximation to determine what happens

> 你会注意到的另一件事是：Delta 本身也是一个非线性函数。所以我们用线性近似来确定在这个整体定价函数中会发生什么——

**17:58** · in in this overall pricing function but these functions themselves are also nonlinear so it jumps from 64 to 66 so we're going to expect another change of 66 roughly now it goes to 67 and all of the

> ——但这些函数本身也是非线性的。所以它从 0.64 跳到 0.66——我们预期下一次变化大约是 0.66；现在它又变成 0.67。而且所有——

**18:17** · other functions change as well so there's a lot going on here but at a high level all I want you to understand is each of these Greeks represent what happens when there's a unit change in the underlying parameter now of course

> 其它函数也都在变化，所以这里有很多事情在同时发生。但从高层次来说，我只想让你理解：每个希腊字母都代表当基础参数发生一个单位的变化时会发生什么。当然，——

**18:32** · Vega and row having a unit change that is a significant significant change most likely it's going to be in percentages so there's going to be like a 0.1% increase in Vol or a 0.5% increase in Vol that's going to scale down these

> 对 Vega 和 Rho 来说，一个单位的变化是非常、非常显著的变化——很可能它们是以百分比计的，比如波动率上升 0.1%，或波动率上升 0.5%。那会把上面这些——

**18:47** · linear approximations but we're just going to use the underlying asset price because it's so easy to see you can see now Delta is 67 the option price is 1176 what happens if the price decreases by one well we would expect that this call

> 线性近似按比例缩小。但我们只使用基础资产价格，因为它最容易观察。你可以看到，现在 Delta 是 0.67，期权价格是 11.76。如果价格下降 1，会发生什么？我们预期这个看涨——

**19:03** · option price would be roughly 11.10 so 11 1110 and that's exactly what we get so all we're doing here is we're applying this idea of a linear approximation to the change in our option value

> ——期权价格会大约变成 11.10——而实际情况正是如此。所以这里我们做的全部事情，就是把线性近似这个想法应用到期权价值的变化上，——

**19:20** · to an option price via the black schs model and that's exactly what we're doing here for each of the inputs remember this is the underlying asset this this is the time to maturity this is the volatility and this is the

> 即通过 Black-Scholes 模型对期权价格的变化做线性近似。这正是我们这里对每个输入所做的事情。记住：这是基础资产，这是到期时间，这是波动率，而这是——

**19:32** · interest rate this is precisely how the Greeks work and the upside to this sort of linear approximation is that it is linear so if I'm trading a whole bunch of different option contracts on say apple then I'm going to have a whole

> ——利率。这正是希腊字母的运作方式。而这类线性近似的一个好处是：它是线性的。所以如果我在交易一大批不同的期权合约，比如说苹果（Apple）的期权，那么我会有一大批——

**19:47** · bunch of different Deltas but the net Delta of my portfolio I can just sum together all of the Deltas of all those option contracts and that's going to tell me approximately how much I can expect my portfolio value to change when

> 不同的 Delta，但我组合的净 Delta（net Delta）可以直接把所有这些期权合约的 Delta 加总起来得到。而它会告诉我，当——

**20:00** · there's a unit change in either direction of say the underlying asset price or time to maturity Vaga row Etc so what this means is I get a very high level view for almost nothing of My overall option portfolio if I am net

> 基础资产价格或到期时间、Vega、Rho 等朝任一方向发生一个单位的变化时，我预期组合价值大约会改变多少。所以这意味着：我几乎不费吹灰之力就能对我的整个期权组合有一个非常高层级的视图。如果我净——

**20:17** · long Delta then my portfolio value will increase when the underlying asset increases if I'm net negative Delta then my portfolio value is going to decrease when the underlying asset increases that's why this idea is so useful

> 多头 Delta（net long Delta），那么当基础资产上涨时，我的组合价值就会上升；如果我是净空头 Delta（net negative Delta），那么当基础资产上涨时，我的组合价值就会下降。这就是为什么这个想法如此有用。

**20:35** · because even if I'm trading a hundred different option contracts on the same underlying then I get a summary of what's going to happen to my portfolio value in the form of Delta Theta Vega and row I could just take a look at the

> 因为即使我在同一标的上交易一百份不同的期权合约，我仍然能以 Delta、Theta、Vega 和 Rho 的形式，得到一个关于我的组合价值将会发生什么的汇总。我可以只看——

**20:50** · net exposure now if you wanted to take it a step further you could even look at the second order sensitivities to see how quickly your Delta changing how quickly your Vega is changing so on and so forth but again that's more of a

> 净敞口（net exposure）。现在，如果你想更进一步，你甚至可以看看二阶敏感性，看看你的 Delta 变化有多快、你的 Vega 变化有多快，等等。但再说一遍，那更多是——

**21:03** · video for another day this is going to tell you relatively speaking and in kind of plain old English what you want the market to do to make more money so if you're net positive Delta then you want the underlying asset to keep going up if

> 另一期视频的内容。相对而言，这个会告诉你——用大白话讲——你希望市场怎么做才能赚更多的钱。所以如果你是净正 Delta，你就希望基础资产继续上涨；如果——

**21:20** · you're net negative Delta you want that thing to keep going down because the value of your portfolio is going to increase now what if you don't necessarily want to speculate what if you're a market maker well if you're

> 你是净负 Delta，你就希望那东西继续下跌，因为那样你的组合价值会增加。那如果你不一定想投机呢？如果你是一个做市商（market maker）呢？如果你——

**21:34** · a market maker you're trying to collect this bit ass spread and you know you can argue that spreads are so tight now there's nothing left whatever you know that's that's not the point of this this video you can take that that elsewhere

> 是做市商，你试图赚取这个买卖价差（bid-ask spread）。你可以说现在价差太紧、已经没什么可赚的了，随便吧——你知道的，那不是这期视频的重点，你可以到别处去讨论那个问题。

**21:46** · the whole point of this video is suggesting that if you wanted to collect that bit ask spread then you don't want this exposure you don't want this Delta Theta Vega row exposure what you do want is you want

> 这期视频的全部重点是：如果你想赚取买卖价差，那么你就不想要这些敞口——你不想有这种 Delta、Theta、Vega、Rho 敞口。你真正想要的是——

**21:59** · net neutral exposure you don't want your portfolio value changing at all when there's a change in these the underlying asset or or time progresses or or volatility changes so what you can do then is you can try to enter offsetting

> 净中性的敞口（net neutral exposure）。你不希望当基础资产变化、或时间流逝、或波动率变化时，你的组合价值发生任何改变。那么你能做的是：尝试建立对冲（offsetting）的——

**22:17** · positions to make your Delta zero to make your Theta Zer to make your Vega zero and what that's going to do is it's it's going to neutralize that exposure meaning you're going to have almost a net zero change in your portfolio

> ——头寸，使你的 Delta 为零、Theta 为零、Vega 为零。这样做的效果是：它会中和掉那些敞口，意味着当市场中的这些变量变化时，你的组合价值几乎——

**22:34** · value when these variables in the market change and then the idea is you would try to collect that bit ass spread so that is the idea from a market Maker's perspective that's the idea of implementing this linear approximation

> 是净零变化。然后你的想法就是去赚取那个买卖价差。所以这就是从做市商角度的思路——这就是实现这个线性近似作为做市商的意义。

**22:47** · as a market maker um this is again a very crude um interpretation explanation there's a lot of other stuff going on in that setting but just at a high level to understand why these linear approximations are so useful in any

> 嗯，这又是一个非常粗略的解读和解释，在那个场景下还有很多其它事情在发生。但只是在高层面上理解为什么这些线性近似在任意——

**23:01** · context whether you're managing your own option portfolio or you are a market maker that is the highle gist of what's going on excuse the breaching continuity it is quite cold out the last thing I'd like to do is discuss this idea of a

> ——情境中都如此有用——无论你是在管理自己的期权组合，还是身为做市商。以上就是这期内容的大要。请原谅我打断了连贯性，外面真的很冷。最后我想做的是讨论这个想法：——

**23:17** · linear approximation relative to the other inputs in our function of interest in this case the function of interest is our black shs model our pricing function and we have all of these different parameters that can change now you'll

> 线性近似相对于我们关注函数中其它输入的情况。在这里，我们关注的函数就是 Black-Scholes 模型，我们的定价函数。我们有所有这些可能变化的参数。现在你——

**23:31** · notice if we take a look at something like Delta what happens when we change the time to maturity well you can see that Delta does change when the time to maturity also changes moreover if the strike price changes then our Delta is

> 会注意到：如果我们看看 Delta 之类的东西，当我们改变到期时间时会发生什么？你可以看到，当到期时间变化时，Delta 确实会变化。此外，如果行权价改变，那么我们的 Delta 就会——

**23:46** · going to change because that's going to affect the moneyness of our option now I'm not saying the strike price will change throughout the life of the option but when it's initially set you can see that's going to determine our Delta the

> 改变，因为那会影响我们期权的实值程度（moneyness）。我并不是说行权价在期权存续期内会改变，但你可以看到，当它最初被设定时，它就会决定我们的 Delta。这个——

**23:57** · moneyness of the option is going to have an impact on that linear approximation so what are the implications of this well we also have the ability to look at second order sensitivities that is we don't just have

> 期权的实值程度会对那条线性近似产生影响。那么这意味着什么呢？我们还能够考察二阶敏感性——也就是说，我们不只是——

**24:11** · to look at the change in option price relative to the underlying asset but we can also look at the change in the underlying asset and the change in time or the underlying asset and volatility or interest rates so you can compute

> 看期权价格相对于基础资产的变化，我们还可以看基础资产与时间的变化、或基础资产与波动率/利率的变化。所以你可以计算——

**24:28** · these cross cross partials if you will and you get a similar effect and that's a second order sensitivity what I want to do is I want to kind of give you the gist of this idea of how the parameters influence one

> 这些交叉偏导数（cross partials，如果你愿意这么叫的话），你会得到类似的效果，那就是二阶敏感性。我想做的是：给你一些这个想法的要义，即这些参数如何相互——

**24:41** · another by taking a look at this chart so here what we have is we have our actual Theta that is the actual change from the change in time in our option price we have a Theta approximation and we have our initial option price here

> ——影响——通过观察这张图表。所以我们这里有：实际的 Theta，也就是由于时间变化导致的期权价格的实际变化；一个 Theta 近似值；以及我们这里的初始期权价格。

**24:55** · now what you'll notice is as we increase the time step the Theta approximation is significantly worse than the actual option price this is exactly what we saw when we looked at this chart up here as we get further and further away from the

> 现在你会注意到：当我们增大时间步长时，Theta 近似明显比实际期权价格差得多。这正是我们之前看上面那张图时看到的情况——我们离兴趣点越远，——

**25:11** · point of Interest the approximation is going to get worse and worse and worse so let's bring this back down to an incremental change and let's take a look at what happens when we change the moneyness of

> ——近似就会变得越来越差、越来越差。所以让我们把它调回一个微小的增量变化，然后看看当我们改变期权的实值程度时会怎样。

**25:25** · the option so let's say the underlying asset starts to increase significantly you can see the strike price is 103 the underlying or the spot of the underlying is 15 now the approximation

> 假设基础资产开始显著上涨。你可以看到行权价是 103，而基础资产（或者说基础资产的现货价）是 105。现在这个近似——

**25:38** · is very similar to the actual change what happens when we actually decrement time here look at that what happens when we increase the time step the magnitude of the effect is not

> ——与实际变化非常接近。当我们实际上缩短时间时会发生什么？看那个！当我们增大时间步长时，效应的大小就不太——

**25:57** · quite the same so when I decrease this you'll see wow that is a a significant amount of error but when we're deep in the money it's still a reasonable approximation so what's going on here this is what I want

> ——一样了。所以当我减小它时，你会看到，哇，那是相当可观的误差。但当我们在深度实值（deep in the money）状态下时，它仍然是一个合理的近似。那么这里到底发生了什么？这正是我想——

**26:12** · to leave you with is the linear approximations themselves are assuming that we're holding all of the other parameters constant but what you just witnessed is as the other parameters change the effectiveness of the linear

> ——留给你思考的：线性近似本身假定我们保持所有其它参数不变。但你刚刚目睹的是：随着其它参数变化，这个线性——

**26:25** · approximation itself will also change that is it's going to be your option price that is it's going to be less or more sensitive to the approximation and the error of the approximation further away from the point of Interest

> ——近似本身的有效性也会改变。也就是说，你的期权价格——它对该近似的敏感程度会变高或变低，而且离兴趣点越远，近似的误差——

**26:38** · depending on the parameter set that you're dealing with and that's exactly what we see here we see the initial option price we see the actual price and the Theta approximation and as our underlying changes we can see wow this

> 也会不同，这取决于你所处的参数集合。这正是我们在这里看到的：我们看到初始期权价格、实际价格和 Theta 近似值。而随着我们的基础资产变化，我们可以看到，哇，当它在虚值（out of the money）状态——

**26:53** · data approximation is terrible when it's out of the money like this or when it's deep in the money even though we're so far away from the initial point x0 we have a marginal error here right marginal relative to relative to this

> ——像这样，或在深度实值时，这个近似非常糟糕。但即使我们离初始点 x0 如此之远，这里仍然有一个很小的误差——相对于这个误差来说是边际的，对吧——

**27:09** · error so all that is to say is we don't just have a linear approximation for the change in option price relative to all of the inputs but we also have second order sensitivities we have gamma we have charm we have all of these other

> 所以这一切的意思是：我们不仅有期权价格相对于所有输入的线性近似，我们还有二阶敏感性——我们有 Gamma、有 Charm（魅惑）、有所有这些其它——

**27:24** · interesting quantities that we can compute to see how all of these changes work together I want to leave you with this idea of managing an option portfolio and the notion of hedging away your different exposures that is the

> 有趣的量，我们可以计算它们，来了解所有这些变化如何协同作用。我想留给你的是"管理期权组合"以及"对冲掉你不同敞口"这些想法。也就是说——

**27:38** · exposures that we discussed throughout this video the Greeks so how do you do this well let's say that I have a portfolio of options and stock as we said earlier I'm able to add all of those different exposures from all those

> 我们在整期视频中讨论的敞口——也就是希腊字母。那么怎么做呢？假设我有一个由期权和股票组成的组合。正如我们之前所说，我能够把来自所有这些不同合约和股票的那些不同敞口——

**27:52** · different contracts and Equity together and I'll have my overall portfolio Delta port portfolio Vega portfolio Theta so on and so forth right that's going to tell me how my portfolio value will change relative to all of those inputs

> 加总在一起，然后我就有了整个组合的 Delta、组合的 Vega、组合的 Theta，等等。没错，那会告诉我，相对于我们谈到的所有那些输入——

**28:06** · that we talked about the underlying asset the market volatility interest rates all of those inputs that would affect the price of the assets we're holding in this portfolio what if I wanted to hedge away

> ——基础资产、市场波动率、利率——也就是所有那些会影响我们组合中所持资产价格的输入，我的组合价值会如何变化。那如果我想对冲掉——

**28:20** · all of my Vaga risk my Delta risk well this turns into a a pretty much a system of of equations what we have is we have a market where we can go out and purchase option contracts we could sell option

> 我所有的 Vega 风险、Delta 风险呢？这就变成了一个基本上可以说是"方程组"的问题。我们有这样一个市场：我们可以出去买入期权合约，也可以卖出期权——

**28:39** · contracts and our goal is going to be to find a combination of option contracts that's going to hedge away the risk that we're interested in hedging away but moreover when we do that that new contract is going to bring to the

> ——合约。我们的目标是找到一组期权合约的组合，用它来对冲掉我们想要对冲的风险。而且更重要的是，当我们那样做时，那个新合约也会带来——

**28:54** · table its own Theta its own Delta it's own row and we're going to have to add that to our portfolio so this turns into a very interesting type of optimization problem SL system of equations where we're trying to figure out the best way

> 它自己的 Theta、自己的 Delta、自己的 Rho，我们必须把这些加进我们的组合。所以这就变成一个非常有趣的优化问题/方程组：我们要找出最佳方式——

**29:10** · that we can combine contracts available to us in our portfolio to hedge away the risk now you can only get Theta Vega gamma all of all of that exposure from option contract so the only way to offset it is using an option contract

> 来组合我们组合中可用的合约，以对冲掉风险。注意，你只能从期权合约中获得 Theta、Vega、Gamma 所有这些敞口，所以抵消它们的唯一方式就是使用期权合约。

**29:26** · right Delta however you can get Delta you can either get positive Delta by going long an underlying asset or negative Delta going short the underlying asset from exclusively the

> 对吧？然而 Delta 就不一样了。你可以从基础资产中专门获得 Delta——通过做多基础资产获得正 Delta，或做空基础资产获得负 Delta——

**29:40** · underlying asset that is typically when you're trying to hedge away this portfolio risk you start with options so you hedge away your Theta hedge away your row hedge away your Vega and then once you have that combination of

> ——所以通常，当你想对冲掉这个组合的风险时，你从期权开始：你先对冲掉你的 Theta，对冲掉你的 Rho，对冲掉你的 Vega；然后一旦你有了那一组——

**29:53** · options that all offset then you can go buy and sell stock to depending on your net Delta position to neutralize that one last because stock doesn't come with any Vega stock doesn't come with any Theta and that's a very interesting

> 互相抵消的期权组合，你就可以根据你的净 Delta 头寸去买入或卖出股票，来中和最后那一个敞口。因为股票不附带任何 Vega，股票也不附带任何 Theta。而这正是——

**30:08** · component of managing an option portfolio in a later video I would like to actually discuss how to solve this sort of system of equations and and you know maintain an offsetting position and talk about what rebalancing looks like

> ——管理期权组合中非常有趣的一个组成部分。在之后的一期视频中，我想实际讨论如何求解这类方程组，如何维持一个对冲头寸，并谈谈再平衡（rebalancing）是什么样的。

**30:22** · yes we have transaction costs yes there's all of these other you know actual implications when we go into the market and transact and that's something that I would like to explore in a in a later video along with these second

> 是的，我们有交易成本，当我们进入市场进行交易时，还有所有这些其它实际影响。这些连同那些二阶——

**30:33** · order sensitivities which are also very very important as well but until then thank you so much for watching I hope you enjoyed and I will see you in the next video

> ——敏感性（它们也非常非常重要），我想在之后的一期视频中一起探讨。但在此之前，非常感谢大家的观看，希望你们喜欢，我们下期视频再见。




