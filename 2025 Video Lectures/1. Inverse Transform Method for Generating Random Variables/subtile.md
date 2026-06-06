---
title: "Inverse Transform Method for Generating Random Variables"
source: "https://www.youtube.com/watch?v=1WB8PtKnaqU"
author:
  - "[[Roman Paolucci]]"
published: 2025-01-04
created: 2026-05-16
description: "🚀 Master Quantitative Skills with Quant Guild:https://quantguild.comJoin the Quant Guild Discord server here:https://discord.com/invite/MJ4FU2c6c3I hope you enjoyed this lecture, please feel fr"
tags:
  - "clippings"
---
---
title: "逆变换方法生成随机变量"
source: "https://www.youtube.com/watch?v=1WB8PtKnaqU"
author:
  - "[[Roman Paolucci]]"
published: 2025-01-04
created: 2026-05-16
description: "🚀 通过Quant Guild掌握量化技能：https://quantguild.com 加入Quant Guild Discord服务器：https://discord.com/invite/MJ4FU2c6c3 希望你喜欢这堂课，请随时留言或联系我提出任何问题。"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=1WB8PtKnaqU)

🚀 Master Quantitative Skills with Quant Guild:  
https://quantguild.com  
  
Join the Quant Guild Discord server here:  
https://discord.com/invite/MJ4FU2c6c3  
  
I hope you enjoyed this lecture, please feel free to leave a comment or reach out to me with any questions.  
  
Inverse Transform Method Jupyter Notebook:  
https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/1.%20Inverse%20Transform%20Method%20for%20Generating%20Random%20Variables/Inverse%20Transform%20Method.ipynb  
  
Articles and code walkthroughs can be found on our blog  
https://medium.com/quant-guild  
https://romanmichaelpaolucci.medium.com/  
  
For more free tutorials and references see our GitHub  
https://github.com/RomanMichaelPaolucci  
https://github.com/Quant-Guild

🚀 通过Quant Guild掌握量化技能：  
https://quantguild.com  
  
加入Quant Guild Discord服务器：  
https://discord.com/invite/MJ4FU2c6c3  
  
希望你喜欢这堂课，请随时留言或联系我提出任何问题。  
  
逆变换方法Jupyter笔记本：  
https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/1.%20Inverse%20Transform%20Method%20for%20Generating%20Random%20Variables/Inverse%20Transform%20Method.ipynb  
  
文章和代码演示可以在我们的博客找到  
https://medium.com/quant-guild  
https://romanmichaelpaolucci.medium.com/  
  
更多免费教程和参考资料请查看我们的GitHub  
https://github.com/RomanMichaelPaolucci  
https://github.com/Quant-Guild

## Transcript

## 文字稿

**0:01** · \[Music\] and we are back welcome back it's good to be back very excited to begin posting again 2025 the goal is to post every

**0:01** · [音乐] 我们回来了，欢迎回来，很高兴能重新开始，2025年的目标是每周发布

**0:16** · week on an interesting topic in lecture format please feel free to join the Discord and make sure that I stick to that um but nevertheless today we are going to get started with methodology for generating random variables today we're going to talk about the inverse transform method now this does assume

**0:16** · 一个有趣的主题，以讲座形式呈现，请加入Discord确保我坚持这个计划，不过今天我们要开始讲解生成随机变量的方法，今天我们要讨论逆变换方法，这需要

**0:38** · some background in probability and statistics if you've taken a statistics and probability course in in University then you will be very well prepared for this sort of discussion if not I encourage you to check out my other resources I have an article on common random variables that walk you through

**0:38** · 一些概率和统计学基础，如果你在大学修过统计学和概率课程，那么你将对此类讨论有充分准备，如果没有，我建议你查看我的其他资源，我有一篇关于常见随机变量的文章，带你了解

**0:55** · pretty much an first year undergraduate statistics course in one article talks about probability Mass functions probability density functions cumulative distribution functions applications of discrete and continuous random variables once you have a general idea

**0:55** · 几乎涵盖了一整年本科统计学课程的内容，讨论概率质量函数、概率密度函数、累积分布函数，离散和连续随机变量的应用，一旦你对这些不同主题有了基本了解

**1:13** · of those different topics we can kind of dive into this idea of the inverse transform method I'm going to give you an example even if you haven't seen that material before so hopefully it's it's intuitive we're going to be a little handwavy with this idea of pseudo randomness coming from number Theory we'll talk briefly when we get to the python code about what that actually is and what that looks like but for now bear with me we're going to look at some intuitive examples using a a dice rule for a discrete random variable and then

**1:13** · 我们可以深入探讨逆变换方法的概念，我会给你一个例子，即使你之前没看过这些材料，所以希望它能直观易懂，我们会稍微简单介绍一下来自数论的伪随机性概念，当我们讲到Python代码时会简要讨论它到底是什么以及它看起来如何，但现在请耐心听，我们将看一些直观的例子，使用骰子规则作为离散随机变量，然后

**1:43** · we're going to move over to a normal distribution or maybe not a normal distribution maybe a uniform distribution for a continuous or maybe exponential but we'll see when we get there we'll see how I'm feeling for now we'll get started with the idea of a discret random variable fully specified by its probability Mass function So discret Random \[Music\] variables probability Mass

**1:43** · 我们会转向正态分布，或者可能不是正态分布，可能是连续变量的均匀分布或指数分布，我们到时候再看，现在我们开始讲解由概率质量函数完全定义的离散随机变量的概念，所以离散随机变量概率质量

**2:22** · functions now all a probability Mass function is and hopefully you've heard this before if not then hopefully this is clear it's going to map an item in the sample space to a corresponding probability and here we are assuming a

**2:22** · 函数，概率质量函数是什么，希望你之前听过，如果没有，希望现在能清楚，它将样本空间中的一个项目映射到相应的概率，这里我们假设

**2:38** · frequency interpretation of that probability that is we're following Pav's axioms we're saying that if we iteratively repeat these experiments then we're expecting this outcome a specific fraction of the time so for example a very trivial examples a coin flip right if I flipped a coin right now right I don't know what that outcome is going to be it's going to be heads or tails I don't know what it's going to be but I do know if I flipped an infinite number of coins then I would expect the ratio to be 50/50 right that's the idea

**2:38** · 概率的频率解释，即我们遵循帕夫的公理，我们说如果我们反复重复这些实验，那么我们期望这个结果在特定比例的时间内出现，例如一个非常简单的例子是抛硬币，如果我现在抛硬币，我不知道结果会是什么，会是正面或反面，我不知道，但我确实知道如果我抛无限次硬币，我会期望比例是50/50，这就是

**3:09** · of the frequency interpretation if I flip 10 coins it's very possible I get 10 heads but we what we are saying and this is using the law of large numbers here is we're saying that if we were to do this this sample this event this particular experiment an infinite number of times and we would converge to some sort of population mean parameter

**3:09** · 频率解释的概念，如果我抛10次硬币，很有可能我得到10次正面，但我们所说的，这里使用大数定律，是说如果我们做这个采样、这个事件、这个特定实验无限次，我们会收敛到某种总体均值参数

**3:30** · and all that is to say is if I repeat this experiment then I'm going to have these fixed ratios for possible outcomes so let's look at what the mathematical notation would look like perhaps we have some function that's going to map items in the sample space to a probability between zero and one you know you could say to real numbers um it depends on really you know this is obviously going to be constrained because we need to make sure that all of the items in the sample space are going to sum to one you can't have.

**3:30** · 所有这些意味着如果我重复这个实验，那么我会有这些固定的可能结果比例，让我们看看数学符号会是什么样子，也许我们有某个函数将样本空间中的项目映射到零到一之间的概率，你可以说映射到实数，这取决于，这显然会受到限制，因为我们需要确保样本空间中的所有项目总和为一，你不能有...

**4:04** · 5.5 not sum to one you can't have it sum to something greater than one that should be relatively intuitive having a 120% probability in the context of a frequency interpretation doesn't really make sense you know if I had 10 coins and I flipped you know five and five

**4:04** · 5.5总和不为一，你不能让总和大于一，这应该是相对直观的，在频率解释的背景下，120%的概率没有意义，你知道如果我有10枚硬币并且我抛了五次正面五次反面

**4:23** · maybe five heads five tails then that would be 50/50 but you can't flip seven heads and five tails and only have 10 trials that's that's not possible so this is going to be constrained between 0 and 1 Let's actually talk a little bit about what this probability Mass function is going to look like so let's talk about a dice roll we know the sample space for a dice roll is going to be 1 2 3 4 five

**4:23** · 可能五次正面五次反面，那会是50/50，但你不能抛出七次正面和五次反面却只有10次试验，那是不可能的，所以这将被限制在0到1之间，让我们实际谈谈这个概率质量函数会是什么样子，让我们谈谈掷骰子，我们知道掷骰子的样本空间是1、2、3、4、5
```
f: \Omega \to \mathbb{R}
```

**4:52** · and six the actual function we can Define as maybe P of a and we can say that if we give this function any possible outcome 1 through six we're going to have a 1 16th probability of seeing that outcome so this is for a is equal to 1 2 3 4 5

**4:52** · 和6，我们可以定义的实际函数可能是P(a)，我们可以说如果我们给这个函数任何可能的结果1到6，我们会有1/16的概率看到那个结果，所以这是对于a等于1、2、3、4、5

**5:15** · and 6 and any other outcome in this space maybe it's 1.5.5 whatever it is negative2 has a zero probability so I'm going to say zero otherwise

**5:15** · 和6，而在这个空间中的任何其他结果，也许是1.5.5，不管是什么，-2的概率为零，所以我要说其他情况为零

**5:30** · so this is a peie wise function that fully specifies what's called a discrete uniform random variable this particular discrete uniform random variable is a dice rule it's saying that given the numbers 1 through six there's an even probability of drawing 1 through six how do I plot this well this is just a piecewise function so all I have to do is draw my probability axis and draw my sample space axis 1 2

**5:30** · 所以这是一个分段函数，完全定义了所谓的离散均匀随机变量，这个特定的离散均匀随机变量是掷骰子，它说给定数字1到6，抽取1到6的概率相等，我怎么绘制这个，这只是一个分段函数，所以我只需要画概率轴和样本空间轴1、2

**6:05** · 3 4 5 six and plot the corresponding probabilities well the probability of each one of these outcomes is just 1 16 1 2 3 4 5

**6:05** · 3、4、5、6并绘制相应的概率，每个这些结果的概率只是1/6，1、2、3、4、5

**6:26** · six there is no probability Mass anywhere else if you wanted to be super specific in drawing this function you could just have open circles here and then it would be a straight line everywhere else even going from negative Infinity to positive Infinity because there is no probability Mass

**6:26** · 6，其他地方没有概率质量，如果你想在绘制这个函数时非常精确，你可以在这里有空心圆，然后其他地方是一条直线，甚至从负无穷到正无穷，因为那里没有概率质量

**6:53** · there okay so this is relatively intuitive right if I was to go anywhere in the sample space you'll find that the only place that has probability mass is going to be at 1 2 3 4 five and

**6:53** · 好了，这是相对直观的，如果我走到样本空间的任何地方，你会发现唯一有概率质量的地方是在1、2、3、4、5和

**7:11** · six anywhere else we're not going to have any probability mass and you can see that each one of these if we sum them all together 1 16 \* 6 we're going to get 1 and that is our entire sample space so the probability of anything happening is going to be one

**7:11** · 6，其他地方我们不会有任何概率质量，你可以看到如果我们把它们全部加起来，1/16乘以6，我们会得到1，那就是我们的整个样本空间，所以任何事情发生的概率将是1

**7:30** · so this is called a probability Mass function inextricably linked to the probability Mass function specifically because it's derived from either the cumulative distribution function or the probability Mass function can be used to derve the cumulative distribution function simply just going to be integration and differentiation if you were in a continuous space but since we're in a discret space it's differencing in summation so here what we have is a probability Mass function

**7:30** · 所以这被称为概率质量函数，与概率质量函数密不可分，特别是因为它要么是从累积分布函数导出的，要么概率质量函数可以用来导出累积分布函数，简单来说就是积分和微分，如果你在连续空间中，但由于我们在离散空间中，它是差分和求和，所以这里我们有概率质量函数

**7:59** · we can very easily find What's called the cumulative distribution function and this is also going to fully specify the random variable now it is a mess in the context of drawing it as a pie wise function in the sense that we have a a variety of conditions and I I'll have to draw each range to make it simple we can just look at the chart so that's what we're going to do we're going to look at the chart the cumulative distribution function all it's asking for is it's asking for an input and it's going to

**7:59** · 我们可以很容易找到所谓的累积分布函数，这也将完全定义随机变量，现在将其绘制为分段函数会很混乱，因为我们有各种条件，我必须绘制每个范围，为了简单，我们可以只看图表，所以我们这样做，我们看图表，累积分布函数只需要一个输入，它将

**8:33** · produce an input being some item in the sample space on the x- axis here and it's going to produce the cumulative probability okay that sounds pretty fancy but if we look let's start at negative Infinity we haven't accumulated any probability Mass starting at negative Infinity but once we get to one we jump from zero this is zero

**8:33** · 产生一个输入，即x轴上样本空间中的某个项目，它将产生累积概率，好的，这听起来很高级，但如果我们看，从负无穷开始，我们从负无穷开始还没有累积任何概率质量，但一旦我们到达1，我们从零跳跃，这是零

**9:02** · to 16 and you'll notice that if we keep doing this we keep working our way from left to right you can see that once we get to two we jump again because because we've accumulated more probability Mass so we take the 1 16 from the outcome of

**9:02** · 到1/6，你会注意到如果我们继续这样做，从左到右继续工作，你可以看到一旦我们到达2，我们再次跳跃，因为我们累积了更多概率质量，所以我们取来自结果

**9:22** · one and we add it to the 1 16 of the outcome of two and we have 26 so we're going to jump again here to 26 and then we're just going to kind of rinse and repeat this this scale may be a little bit off due to my artistic talent here but you can see that once we get to six we have 2 six 3

**9:22** · 1的1/6，加上结果2的1/6，我们有2/6，所以我们在这里再次跳跃到2/6，然后我们只是重复这个过程，这个比例可能因我的艺术天赋而稍有偏差，但你可以看到一旦我们到达6，我们有2/6、3

**9:54** · six 46 5 6 eventually we get to 66 which is just one and it's going to stay one forever okay so all we're simply doing

**9:54** · /6、4/6、5/6，最终我们到达6/6，就是1，它将永远保持为1，好的，所以我们简单做的所有事情

**10:11** · is working our way from left to right and we're summing up all of the probability Mass this is the cumulative distribution function and in fact we can write this and I'll maybe go ahead and just write this for completeness as capital P of a this is a

**10:11** · 是从左到右工作，我们汇总所有概率质量，这就是累积分布函数，实际上我们可以写成，为了完整性我可能就这样写，作为P(a)的大写形式，这是一个

**10:30** · little bit of a mess it's a little bit of a mess let me move this down so that I can can show you what I mean we're going to specify the range in which the probability mass is accumulated from left to right so how much probability Mass have we accumulated from a being negative Infinity to zero

**10:30** · 有点混乱，有点混乱，让我把这个移下来，这样我可以向你展示我的意思，我们将指定从左到右累积概率质量的范围，所以从a为负无穷到零，我们累积了多少概率质量

**10:56** · or I should say to positive one well that's this blue line right here we've clearly accumulated zero probability Mass okay what about a being between 1

**10:56** · 或者我应该说到正1，那是这里的这条蓝线，我们显然累积了零概率质量，好的，那么a在1之间

**11:13** · and 2 well that's this blue line right here this is while we have reached one so we are between 1 and two but not two inclusive because remember at two we jump to 26 so here while we're on this

**11:13** · 和2之间呢？那是这里的这条蓝线，这是当我们到达1时，所以我们介于1和2之间，但不包括2，因为记住在2时我们跳跃到2/6，所以当我们在这条

**11:34** · blue line we have 16 accumulated probability and this is just essentially looking at all of these bars and specifying the range okay there is a a more concise way to do this with a summation but I'm going to disregard that just for Simplicity sake so here we're going to have 26 for a is between 2 and 3 36 for

**11:34** · 脉线上时，我们有1/6累积概率，这基本上就是看所有这些柱并指定范围，好的，有一个更简洁的方法用求和来做，但为了简单我将忽略它，所以这里对于a在2和3之间我们有2/6，对于

**12:02** · a is between 3 and 4 and you can start to see what I mean this is kind of just you know a little bit four and five and then 56 for a 56 and then at six what happens well at six we've accumulated all of our probability Mass so it's going to be one for a is between 6 and

**12:02** · a在3和4之间是3/6，你可以开始明白我的意思，这只是有点...对于4和5，然后对于a在5和6之间是5/6，然后在6时发生什么，在6时我们已经累积了所有概率质量，所以对于a在6和

**12:37** · infinity and that's going to be our cumulative distribution function okay so now that we have everything written down we're ready to actually generate this this random variable

**12:37** · 无穷之间，它将是1，这将是我们的累积分布函数，好的，现在我们已经写下所有内容，我们准备好实际生成这个随机变量

**12:57** · computationally the inverse transform method is not the only way to generate a random variable in fact it doesn't work in the case that there is no analytical solution to the

**12:57** · 用计算机计算，逆变换方法不是生成随机变量的唯一方法，实际上，当没有解析解来

**13:12** · inverse of the density function or mass function whatever it is you're you're working with but for something like this it is quite easy to implement so just keep in mind the inverse transform method is just kind of a very

**13:12** · 求密度函数或质量函数的逆时，它不起作用，但对于像这样的情况，它很容易实现，所以请记住逆变换方法只是一种非常

**13:29** · a very basic way to generate a random variable when the mass function or the density function you are working with is willing to be cooperative and invertible if you think of something like the normal distribution function so let's take a look really quickly at the standard normal so this is the the CDF of a standard normal f ofx

**13:29** · 基本的生成随机变量的方法，当你使用的质量函数或密度函数是可合作且可逆时，如果你想到正态分布函数，让我们快速看一下标准正态分布，这是标准正态分布的CDF，F(x)

**14:03** · one over two < TK of 2 piun e to x^2 / 2 DX really I should use a placeholder variable here S2 over 2

**14:03** · 1/(2π的平方根) e^(x²/2) dx，实际上我应该在这里使用占位符变量，s²/2

**14:23** · DS this isn't invertible right like this is this is going to be something that is uh is not easily invertible so the inverse transform method would not necessarily work in this in this context you're going to have to use something else like maybe acceptance rejection or or another type of uh way to generate

**14:23** · ds，这是不可逆的，对吧，像这将是不容易可逆的东西，所以逆变换方法在这种背景下不一定有效，你将不得不使用其他方法，比如可能是接受拒绝方法或其他生成方式

**14:44** · these these random variables which we may cover in a later V video but for now let's let's take a look at the inverse transform method I just wanted to put that on your radar that this is not a cure all for any probability mass or density function so let's go back to what we have here well we can see that each one of these outcomes has a 1 Sixth probability so what we want to do is we want to figure out a way to draw

**14:44** · 这些随机变量，我们可能会在以后的视频中介绍，但现在让我们看看逆变换方法，我只是想让你知道这不是解决任何概率质量或密度函数的万能药，所以让我们回到我们这里的内容，我们可以看到每个这些结果都有1/6的概率，所以我们想要做的是找出一种方法来抽取

**15:12** · from this distribution such that if we did this 10 bajillion times we would have approximately a 1 16th probability for each outcome that's how we know we've generated it correctly okay you can just say oh like we we'll draw this we'll draw this we draw this that's that's great that's all well and good

**15:12** · 来自这个分布，这样如果我们做无数次，我们会对每个结果有大约1/6的概率，这就是我们知道我们已经正确生成它的方式，好的，你可以说哦，像我们我们会抽取这个，我们会抽取这个，我们抽取这个，那很棒，那都很好

**15:32** · but you need to make sure that you know to to ensure that you're drawing from the correct probability Mass function or correct probability density function you need to ensure that in the context of the frequency interpretation if you repeat draws iteratively then you take the ratio of total number of ones drawn total number of twos drawn threes fours fives and sixes they all need to be roughly one 16

**15:32** · 但你需要确保你知道，为了确保你从正确的概率质量函数或正确的概率密度函数抽取，你需要确保在频率解释的背景下，如果你重复抽取，那么你取抽取的总数1、抽取的总数2、3、4、5和6的比例，它们都需要大约是1/6

**16:00** · right law of large numbers as that approaches Infinity everything will be 16 that's the idea here so you need a way to ensure that the structure of the mass function or the distribution function is preserved and the inverse transform method is going to use the distribution function along with a different random variable to produce the correct probability for each output and the corresponding desired output what do

**16:00** · 对吧，大数定律，当它接近无穷时，一切都将是1/6，这就是这里的想法，所以你需要一种方法来确保质量函数或分布函数的结构被保持，逆变换方法将使用分布函数以及另一个随机变量来为每个输出产生正确的概率和相应的期望输出，

**16:29** · I mean by this well let's take a look at the CDF here this is the CDF what do we notice about the range of the CDF well the range of the CDF starts at zero and it goes to

**16:29** · 我是什么意思？让我们看看这里的CDF，这是CDF，我们注意到CDF的范围是什么？CDF的范围从零开始，它到

**16:50** · one this will be true for every cumulative distribution function because that is the framework for probab ability in which we are operating in every cumulative distribution function as the limit of the functional input approaches negative Infinity will be zero and the limit as the functional

**16:50** · 1，这对每个累积分布函数都是正确的，因为那是我们正在运作的概率框架，每个累积分布函数当函数输入的极限接近负无穷时将是零，而当函数

**17:13** · input approaches positive Infinity will always be one and that's what you see here you see as we go to negative Infinity as we go to Infinity we get zero and we get one

**17:13** · 输入的极限接近正无穷时将始终为1，这就是你在这里看到的，当我们去负无穷，当我们去无穷时，我们得到零和1

**17:30** · okay how does this help us well if we had a way to essentially flip this map then if we give it anything between zero and one randomly then we're going to draw an outcome with the correct

**17:30** · 好了，这如何帮助我们？如果我们有一种方法来基本上翻转这个映射，那么如果我们给它零到一之间的任何随机数，那么我们将以正确的

**17:47** · corresponding probability mass for each outcome let me give you an example if I was to draw out of a hat this is my hat that's a pretty good hat give it a little Buckle let's say I draw of a hat the number

**17:47** · 相应概率质量抽取一个结果，让我给你一个例子，如果我要从帽子里抽取，这是我的帽子，这是个不错的帽子，给它一个小扣子，假设我从帽子里抽取数字

**18:13** · .5 could I map5 to an outcome in the dice roll well based on this cumulative distribution function here I sure can right so where is 0. five well if we take a look here right 0.5 is going to be right here it's 1 half so at 1/2 if we take a look on the

**18:13** · .5，我能把.5映射到掷骰子的一个结果吗？基于这里的这个累积分布函数，我肯定可以，对吧，那么0.5在哪里？如果我们看这里，0.5将在这里，它是1/2，所以在1/2如果我们看

**18:43** · chart right we are at the number what well what number caused this jump to.5 the number three so 0. five would map three let's say I could draw another number maybe I get

**18:43** · 图表，我们在数字什么？什么数字导致了这个跳跃到.5？数字3，所以0.5将映射到3，假设我可以抽取另一个数字，也许我得到

**19:08** · 73 well where does 73 lie so hopefully you start to see this where does zero lie where does 3 lie we can map all of these numbers between 0 and 1 to their

**19:08** · 73，那么73在哪里？所以希望你开始看到这个，零在哪里，3在哪里，我们可以将0到1之间的所有这些数字映射到它们

**19:26** · corresponding numbers in the sample space for this discrete uniform random variable just using the cumulative distribution function this is the idea of the inverse transform method how do we get these numbers though between zero and one well what we're going to do is we are going to generate a uniform random variable and what this is going to do is this is just going to draw a number between 0 and one where every single

**19:26** · 在这个离散均匀随机变量的样本空间中的相应数字，只使用累积分布函数，这就是逆变换方法的想法，但我们如何得到零到一之间的这些数字？我们将要做的是我们将生成一个均匀随机变量，这将只是抽取0到1之间的一个数字，其中每个

**19:56** · number is going to have an even or equ equal distribution of probability across that entire space 0 to 1 what that does is it ensures that when we draw that number and we plug it in to this little map here where we drew a number out of the hat and then produce the correct draw based on the draw from

**19:56** · 数字将在整个空间0到1上有均匀或相等的概率分布，这确保了当我们抽取那个数字并将它插入到这个小映射中，我们从帽子里抽取一个数字，然后基于从帽子中的抽取产生正确的抽取

**20:19** · the Hat it's going to ensure that we have the correct probability Mass assigned to each outcome in our random variable it it's pretty amazing that it works like this but it's also pretty simple so coming up with that that map is very easy because all you have to do is invert the cumulative distribution

**20:19** · 它将确保我们有正确的概率质量分配给我们随机变量中的每个结果，它像这样工作是很神奇的，但也相当简单，所以创建那个映射很容易，因为你只需要做的是对累积分布

**20:42** · function so all you have to do is swap these places here and that's going to give you a new function such that when you input a draw between zero and one you're going to get the outcome of the dice roll

**20:42** · 函数求逆，所以你只需要做的是交换这些位置，这将给你一个新函数，这样当你输入零到一之间的抽取时，你将得到掷骰子的结果

**21:00** · that's pretty cool that's pretty cool this is successfully mapping some draw between zero and one to the outcome of a dice roll this is literally rolling a dice okay now this begs the question hopefully you've you know maybe the particularly Keen Among Us are like we we'll hold on a second um aren't you drawing a random variable

**21:00** · 那很酷，那很酷，这成功地将零到一之间的某个抽取映射到掷骰子的结果，这实际上就是掷骰子，好的，现在这引发了一个问题，希望你...也许我们中特别敏锐的人会说等等，你不是在抽取一个随机变量

**21:24** · here so you need to draw a random variable to draw another random variable the answer to that question is is yes you do need to draw from a uniform distribution to be able to draw from any other probability Mass function or probability uh density function now how do you get this initial

**21:24** · 吗，所以你需要抽取一个随机变量来抽取另一个随机变量，这个问题的答案是是的，你确实需要从均匀分布中抽取才能从任何其他概率质量函数或概率密度函数中抽取，那么你如何得到这个初始

**21:46** · draw here well that is the the hand wavy part of this this video and we're going to get to the Jupiter notebook in a moment where we actually walk through a little bit of the the theory here but this is where the whole IDE of pseudo Randomness comes from okay that is you're going to have some sort of some sort of seed some sort of series of operations and you're going to attempt to draw from this uniform distribution

**21:46** · 抽取？那是这个视频中略显草率的部分，我们马上会讲到Jupyter笔记本，我们实际上会稍微讲解一些这里的理论，但这正是伪随机性的整个概念来源，好的，那就是你将有某种种子、某种操作序列，你将尝试从这个均匀分布中抽取

**22:10** · to produce the correct probabilistic outputs for each item in your sample space iteratively and eventually the idea is that it with some sort of cyclicality it's going to repeat but again this is a little a little hand wavy for this this part of the video at least until we start talking about the the theory there but for now the steps to generate a random variable are actually quite easy so number

**22:10** · 来迭代地为你的样本空间中的每个项目产生正确的概率输出，最终的想法是它会有某种周期性，它会重复，但这对于这部分视频来说还是略显草率，至少直到我们开始讨论那里的理论，但目前生成随机变量的步骤实际上相当简单，所以第

**22:39** · one find the CDF number two invert the CDF number three draw from a standard uniform random variable number four so I'll call this G of U I'll call this F of a step four

**22:39** · 一步找到CDF，第二步对CDF求逆，第三步从标准均匀随机变量中抽取，第四步，所以我将称这个为G(U)，我将称这个为F(a)，第四步

**23:11** · is input and return G of capital u so once you've drawn from your uniform distribution you're going to plug that into your inverse cumulative distribution function and that is going to give you the output that you are looking for in other words this map that we came up with here this is going to allow us to produce the probability that we are interested in for each possible outcome

**23:11** · 是输入并返回G(U)，所以一旦你从均匀分布中抽取，你将把它插入到你的逆累积分布函数中，这将给你你正在寻找的输出，换句话说，我们在这里想出的这个映射，这将允许我们为我们样本空间中每个可能结果产生我们感兴趣的概率

**23:43** · in our sample space this is again a little bit handwavy because what we need to do is we need to use a loop to iteratively accumulate the probability mass and spit out the desired outcome that is the 1 2 3 4 5 or six but you'll see this in the python

**23:43** · 在我们的样本空间中，这再次略显草率，因为我们需要做的是我们需要使用循环来迭代累积概率质量并输出期望的结果，即1、2、3、4、5或6，但你会在Python

**24:06** · code this is for the discrete case but the continuous case is even easier this right here is the formal set of steps for the continuous case you just need to invert the CDF draw a uniform random variable input that uniform random variable into the CDF and you will have your output and again for the discrete case you'll have to accumulate that probability mass and then once you fall within the range that you're looking for

**24:06** · 代码中看到这个，这是离散情况，但连续情况更容易，这里显示的是连续情况的正式步骤集，你只需要对CDF求逆，抽取一个均匀随机变量，将该均匀随机变量输入到CDF中，你将得到你的输出，而对于离散情况，你必须累积那个概率质量，然后一旦你落入你正在寻找的范围

**24:35** · you'll spit out the number so if you take a look here when we drew a 0 five I said this corresponds to three well how do we know that it's you know 3 not 4 how do we know that it's 3 not2 that's what you're going to use your Loop to discern because you're going to be accumulating probability Mass from left to right so as we accumulate 16 16 1 16 well hey

**24:35** · 你将输出该数字，所以如果你看这里，当我们抽取了一个0.5时，我说这对应于3，那么我们怎么知道它是3而不是4？我们怎么知道它是3而不是2？那就是你将使用你的循环来辨别，因为你将从左到右累积概率质量，所以当我们累积1/6、1/6、1/6时，嘿

**25:04** · once we get that third 16 we notice that we've done it three times right 16 plus 16 plus 16 that gives us our 0 five we've done it three times that maps to the dice outcome

**25:04** · 一旦我们得到第三个1/6，我们注意到我们已经做了三次，对吧，1/6加1/6加1/6给了我们我们的0.5，我们已经做了三次，那映射到骰子结果

**25:20** · three so that's going to do it for this portion of the video on the iPad I want to Pivot over to python to talk a little bit more about the inverse trans for method you'll see some some latch and maybe that'll be a little more clear but let's go ahead and pivot over there you'll see some charts you'll see some some applications of it and uh we'll talk a little bit more about what this whole idea of drawing from a uniform distribution has to do with anything and the corresponding theory behind

**25:20** · 3，所以这将是iPad上这部分视频的结束，我想转到Python来更多地讨论逆变换方法，你会看到一些...也许那会更清楚，但让我们转到那里，你会看到一些图表，你会看到一些应用，我们将更多地讨论从均匀分布抽取的整体想法与任何事情有什么关系以及背后的相应理论

**25:47** · it all right so let's actually look at an implementation of this algorithm this inverse transform method in Python we're going to talk about synthesizing uniform random variabl and some of the theory behind that to kind of at least look into the hand wavess behind the stuff we did on the iPad uh and then we're going to look at applications in the discrete case and the continuous case and you'll see that the pseudo code for the algorithm that I had written is going to

**25:47** · 好了，所以让我们实际看看这个算法的实现，在Python中的逆变换方法，我们将讨论合成均匀随机变量和其背后的一些理论，以至少深入了解一下我们在iPad上做的东西背后的草率之处，然后我们将看离散情况和连续情况的应用，你会看到我写的算法伪代码将

**26:15** · fully correspond to the steps we take in the continuous setting but in the discrete setting we're going to need some sort of loop to accumulate the probability and then spit out the desired output so let's go ahead and get started with this idea of generating a uniform random variable so we need a uniform random variable for a variety of

**26:15** · 完全对应我们在连续设置中采取的步骤，但在离散设置中我们需要某种循环来累积概率然后输出期望的结果，所以让我们开始生成均匀随机变量的概念，我们需要均匀随机变量用于各种

**26:38** · random variable generation techniques we need we need it for the inverse transform method we need it for acceptance rejection we need it for a variety of different ones and this is only going to work the inverse transform method when the random variable that we are looking to generate has a distribution function that is invertible if it's not invertible then you're not going to be able able to plug in a number between 0 and one and get an output it's not going to work like that because there is no map that's going to correspond to the correct probability mass for each desired output in that

**26:38** · 随机变量生成技术，逆变换方法需要它，接受拒绝方法需要它，各种不同的方法都需要它，而且逆变换方法只在我们要生成的随机变量具有可逆的分布函数时才能工作，如果它不可逆，那么你将不能插入0到1之间的数字并得到输出，它不会那样工作，因为没有映射会对应那个样本空间中每个期望输出的正确概率质量

**27:10** · sample space given the structure given by that density function normal distribution may be a good example of that but here we're looking at a very easy case because this is just discrete so we can use numpy random. uniform

**27:10** · 给定由该密度函数给出的结构，正态分布可能是一个很好的例子，但这里我们看一个非常简单的情况，因为这只是离散的，所以我们可以使用numpy random.uniform

**27:26** · that's very easy if we wanted to do something like that we could just draw uh a uniform number this is not necessary at all this this whole section for methodology this is only if you have some interest in the the pseudo Rando the pseudo random number generators you can completely handwave this idea away

**27:26** · 那非常简单，如果我们想做那样的事情，我们可以直接抽取一个均匀数字，这完全不必要，这整个方法论部分，这只是如果你对伪随机、伪随机数生成器有兴趣，你可以完全忽略这个概念

**27:44** · and just use a uniform uh random variable and say okay you know what that's good enough for me I know that I need to generate this probability Mass function this probability density function they have this cumulative distribution function I don't particularly care you know how to generate a uniform random variable I just know that if I want to draw from this desired density that I need to use it that's completely fine you know you don't need to know why this is

**27:44** · 只使用一个均匀随机变量并说好吧，你知道吗，那对我来说足够好了，我知道我需要生成这个概率质量函数，这个概率密度函数，它们有这个累积分布函数，我并不特别在乎均匀随机变量是如何生成的，我只知道如果我想从这个期望的密度中抽取，我需要使用它，那完全可以，你知道吗，你不需要知道为什么这是

**28:12** · functioning the way it is under the hood in the context of the uniform random variable but I figured I'd sprinkle it in because I don't like hand waving without at least you know glossing over the idea so let's just talk about that generally speaking we use pseudo random number generators prngs to create sequences of numbers that mimic Randomness so if you've ever heard this before prngs are looking to essentially

**28:12** · 在均匀随机变量的背景下以它的方式运作，但我认为我应该加入它，因为我不喜欢在没有至少简要介绍概念的情况下草率处理，所以让我们谈谈那个，一般来说，我们使用伪随机数生成器PRNGs来创建模仿随机性的数字序列，所以如果你之前听过这个，PRNGs正在寻求本质上

**28:42** · mimic Randomness in that uniform random variable such that we can generate distribution functions of other types of random variables that actually follow the correct frequency interpretations and assign the correct probability masses to each outcome in the sample

**28:42** · 在那个均匀随机变量中模仿随机性，这样我们可以生成其他类型随机变量的分布函数，它们实际上遵循正确的频率解释并为样本空间中的每个结果分配正确的概率质量

**28:59** · space so these are deterministic algorithms which can be a problem there is some element of predictability if you are to have the seed beforehand right because think about it if we're using a prng to generate a random variable and it's a deterministic function then even

**28:59** · 空间，所以这些是确定性算法，这可能是个问题，如果你预先拥有种子，会有某种可预测性元素，对吧，因为想想看，如果我们使用PRNG生成随机变量，它是一个确定性函数，那么即使

**29:17** · though you are generating a draw from the density or mass function that you were looking to generate a draw from you still have a deterministic aspect of that that random draw it's going to follow that mass function correctly in the sense of the like I say the frequency interpretation you draw a million draws all of the probabilities are going to be assigned to the outcomes in the sample space correctly but the

**29:17** · 你正在从你想要生成抽取的密度或质量函数生成抽取，你仍然有那个随机抽取的确定性方面，它将正确遵循那个质量函数，在我所说的频率解释意义上，你抽取一百万次抽取，所有的概率将被正确分配到样本空间中的结果，但

**29:42** · problem is the underlying algorithm that is going to determine that is deterministic so if I have the seed and I have the function then I'm going to be able to predict with 100% accuracy every single outcome of the random variable a lot has been done and a lot can be done to avoid this especially if the randomness has some sort of financial incentive but I just want to keep that in mind that in the context of this this idea here uh there is some

**29:42** · 问题是一旦决定那个的底层算法是确定性的，所以如果我有种子并且我有函数，那么我将能够以100%的准确率预测随机变量的每一个结果，已经做了很多工作并且可以做很多事情来避免这种情况，特别是如果随机性有某种财务激励，但我只是想记住在这个想法的背景下，这里有某种

**30:12** · sort of deterministic structure underlying it now you could use like very small fractions at the time and blah blah blah make it very difficult but theoretically yes you can predict it perfectly um depending on how you structure your uh your prng here so each prng and this is just one basic example I'm just going to walk through one way we can generate draws from a a standard uniform distribution is uh we

**30:12** · 确定性结构支撑着它，现在你可以使用像非常小的时间分数等等让它变得非常困难，但理论上是的，你可以完美预测它，取决于你如何结构化你的PRNG，所以每个PRNG，这只是一个基本例子，我将介绍我们可以从标准均匀分布生成抽取的一种方法

**30:37** · have something called periodicity in the I want to call it a function so it's it's really um it's iterative and it's it's more like a it's more reminiscent of like a difference equation than anything else but let's take a look at this generator here so it has periodicity uniformity and C based reproducibility so if you've ever seen in any python code previously you know np. random.

**30:37** · 有所谓的周期性，我想称之为函数，所以它实际上是迭代的，它更像是一个差分方程而不是其他任何东西，但让我们看看这里的这个生成器，它有周期性、均匀性和基于C的可复现性，所以如果你之前在任何Python代码中见过，你知道np.random.

**31:03** · seed that's what you're doing is you're you're setting a seed for Randomness for reproducibility so if You observe some sort of set of outcomes after doing simulation and you want to plot it and you want other people to see that particular set of outcomes then they can reproduce it in that context is that a good thing is that a bad thing I don't know you've seen this in Minecraft before too when you set a world seed so you know tomato tomato um but in the context of this you know you you're not

**31:03** · seed，那就是你正在为随机性设置种子以便复现，所以如果你在做模拟后观察到某种结果集，你想绘制它并想让其他人看到那个特定的结果集，那么他们可以在那个背景下复现它，这是好事还是坏事，我不知道，你之前在Minecraft中也见过这个，当你设置世界种子时，所以你知道番茄番茄，但在这个背景下，你

**31:31** · really looking for necessarily reproducibility as you are looking for the the pseudo Randomness to implement in your uh mass and density functions such that you can produce the outputs you're looking for with the correct probability assignment so here we have this this is called the linear uh con

**31:31** · 不一定是在寻找复现性，而是在寻找伪随机性来在你的质量和密度函数中实现，这样你可以以正确的概率分配产生你正在寻找的输出，所以这里我们有这个，这被称为线性con

**31:51** · congruential generator lcg um I'm good at math I've never been good at English so you're going to have to bear with me um so here we have xn + 1 is equal to a xn + C Mod M so a C and M are constants

**31:51** · 线性同余生成器LCG，我擅长数学，但我从来擅长英语，所以你得耐心听，所以这里我们有xn+1等于a*xn+c mod M，所以a、c和M是常数

**32:08** · and then the output is going to be normalized by dividing by m and that's that should be clear that if you did something mod M and you divide by m it's going to be normalized between zero and one uh and then you know we can use to emulate this idea of the the lcg we can use numpy um and here we have 10 th000

**32:08** · 然后输出将通过除以m来归一化，这应该很清楚，如果你做了mod M然后除以m，它将在零到一之间归一化，然后你知道我们可以用numpy来模拟这个LCG的想法，这里我们有10000

**32:28** · samples from random uniform and we're just going to go ahead and plot it if I was to continue to run this we would get different distributions and that is the idea is we are going to draw something that looks like a uniform random variable uh using some sort of generator like this what should you pick for a what should you pick for C what should you pick for M consult the literature I don't know

**32:28** · 来自随机均匀的样本，我们只是要绘制它，如果我继续运行这个，我们会得到不同的分布，这就是想法，我们将使用像这样的某种生成器抽取看起来像均匀随机变量的东西，你应该为a选什么，你应该为c选什么，你应该为M选什么，查阅文献，我不知道

**32:53** · that's just uh that's just a function of the lcg is you know you're going to have to pick these these parameters and it's going to produce some sort of series of uh seemingly random draws uh just as a uniform random variable or I should say a standard uniform random variable appears so this is just uh one this is also just one prng I know we said that the inverse transform method is but one

**32:53** · 那只是LCG的一个函数，你知道你将不得不选择这些参数，它将产生某种看起来随机的抽取序列，就像均匀随机变量或我应该说标准均匀随机变量出现的那样，所以这只是其中一个PRNG，我知道我们说过逆变换方法只是

**33:22** · uh way to generate a random variable uh moreover this is just one way to generate an lcg what is good what is bad what is better what is worse arbitrary depends on the metrics you assign is reproducibility um a priority is Randomness a priority is

**33:22** · 一种生成随机变量的方法，而且这只是生成LCG的一种方法，什么是好的什么是坏的什么是更好的什么是更差的，任意取决于你分配的指标，复现性是优先级吗，随机性是优先级吗，

**33:39** · efficiency a priority uh it's again a little bit arbitrary depending on on the context of your application so for here just to try to you know get rid of as much handwavy as we possibly can here's one way of generating from a standard uniform uh distribution for for use in the inverse transform method that is this lcg uh and then there are there is

**33:39** · 效率是优先级吗，这再次有点任意取决于你的应用背景，所以对于这里，为了尽可能消除草率处理，这是从标准均匀分布生成的一种方法，用于逆变换方法，就是这个LCG，然后有

**34:03** · a lot of theory behind choosing these constants as well so it's not like you're just in the dark pick one two and three um typically they're they're very large numbers um that is that is for the uh for m at least so now that we have this idea of a way to generate a standard uniform draw we can go back to what we learned uh on the iPad right so we we saw that to generate a particular output what we're going to do is is we're going to find the cumulative distribution function invert it draw from a standard uniform random

**34:03** · 很多关于选择这些常数的理论，所以不是你只是在黑暗中选择一、二和三，通常它们是非常大的数字，那是对于m至少，所以现在我们有了生成标准均匀抽取的方法的概念，我们可以回到我们在iPad上学到的内容，所以我们看到要生成特定输出我们要做的是找到累积分布函数，对它求逆，从标准均匀随机

**34:34** · variable this will give me some sort of number between zero and one and notice how they all have roughly the same probability that's the whole point then we could take that outcome and map it to an item in our original sample space so this is that algorithm that I had you know the four steps that I I wrote out on the iPad here is we're starting with the the order here is is again doesn't really matter but you're starting with something sort of uniform draw from a

**34:34** · 变量中抽取，这将给我某种零到一之间的数字，注意它们都有大致相同的概率，这就是整个要点，然后我们可以取那个结果并将它映射到我们原始样本空间中的一个项目，所以这是我在iPad上写的四步算法，我们从这里的顺序开始，顺序真的不重要，但你从某种均匀抽取开始，从

**35:00** · standard uniform distribution you're going to define the target distribution CDF so we set it was a dice roll then we're going to invert that to obtain the inverse CDF which I said was G and we're going to transform the uniform random variable and then we're going to get the outcome that we're looking for so essentially we're turning a number between 0o and one into the outcome that we're looking for so I can map5 to 3 I

**35:00** · 标准均匀分布中抽取，你将定义目标分布CDF，所以如果是掷骰子，那么我们将对它求逆以获得逆CDF，我称之为G，我们将变换均匀随机变量，然后我们将得到我们正在寻找的结果，所以本质上我们将零到一之间的数字转换成我们正在寻找的结果，所以我可以将.5映射到3，我

**35:27** · can map zero to something else maybe that's one in the context of our dice rule so on and so forth so this is how we can actually generate outcomes from a discrete probability Mass function or even a continuous uh probability density function just needs to be invertible that CDF that is the the criteria here that we are looking for so here's our dice roll we have X

**35:27** · 可以将零映射到其他东西，也许在我们的掷骰子背景下那是1，以此类推，所以这是我们实际上可以从离散概率质量函数甚至连续概率密度函数生成结果的方式，只需要CDF是可逆的，那就是我们正在寻找的标准，所以这里是我们的掷骰子，我们有X

**35:53** · instead of a so we're just saying you know if x is 1 2 3 4 5 or six then there's a one sixth probability of that occurring zero otherwise and then this is that iterative way of doing it um that I said was a little more compact than just drawing out each of the um you

**35:53** · 代替a，所以我们只是说如果x是1、2、3、4、5或6，那么有1/6的概率发生，其他情况为零，然后这是那种迭代方式，我说比只是画出每个

**36:09** · know each of the ranges that we drew on the chart so if this doesn't make any sense you can disregard this but if you want to write it in a more compact fashion here's one way to do so um you can also do it with the summation in the context of the pmf but this is just the cumulative distribution function okay so we notice that when X

**36:09** · 范围更紧凑一点，如果这没有任何意义你可以忽略它，但如果你想以更紧凑的方式写它，这里有一种方法，你也可以在PMF的背景下用求和来做，但这只是累积分布函数，好的，所以我们注意到当X

**36:29** · is less than one that's the same as the netive infinity to one we don't have any probability Mass go back to that chart you know you could see that there was no accumulated probability Mass once we get to one we get 1 16 we get to two we get to 26 3 we get to 3 six so on and so forth once we get to six all the way to Infinity we have accumulated all possible probability mass and that's it okay

**36:29** · 小于1时，那与负无穷到1相同，我们没有任何概率质量，回到那个图表，你知道你可以看到没有累积的概率质量，一旦我们到达1我们得到1/6，我们到达2我们得到2/6，3我们得到3/6，以此类推，一旦我们到达6一直到无穷，我们已经累积了所有可能的概率质量，就是这样，好的

**36:58** · so here is a way to apply the inverse transform method to the discret random variable that is a dice roll the discrete uniform random variable so we have our dieces right here 1 through six and we have the corresponding probabilities right

**36:58** · 所以这里是一种将逆变换方法应用于离散随机变量掷骰子即离散均匀随机变量的方式，所以这里我们有骰子1到6，我们有相应的概率

**37:18** · here so we're going to first calculate the cumulative sum of the probabilities and that is going to be that 16 the 2 six 3 six 46 56 so that's all we're doing here is we're calculating that cumulative sum then what we're going to do is we are going to draw and this is more of a a vectorized way of doing it in the sense that what we're doing here is we're drawing end samples but let's

**37:18** · 这里，所以我们将首先计算概率的累积和，那将是1/6、2/6、3/6、4/6、5/6，所以这就是我们在做的，计算那个累积和，然后我们将要做的是我们将抽取，这是更像向量化的方式，因为我们在这里做的是抽取n个样本，但让我们

**37:44** · just walk through this algorithm once as if we're just drawing one sample so we draw a uniform sample we pick our number between zero and one we're going to create a list to keep track of all of the outcomes for our dice roll then we're going to say we're going to do a search sorted CDF and U and then we're going to append the generated sample to

**37:44** · 只是走一遍这个算法，就像我们只是抽取一个样本，所以我们抽取一个均匀样本，我们选择零到一之间的数字，我们将创建一个列表来跟踪我们掷骰子的所有结果，然后我们将说我们将做一个search sorted CDF和U，然后我们将将生成的样本追加到

**38:07** · the generated samples list and then we're going to return the list of generated samples okay so this is what we're doing here is we're taking that CDF list that is this this CDF here the cumulative probabilities and we're saying given this value u i want you to find the corresponding index of that

**38:07** · 生成的样本列表，然后我们将返回生成的样本列表，好的，所以这就是我们在做的，我们取那个CDF列表，就是这里的这个CDF，累积概率，我们说给定这个值u，我要你找到那个

**38:31** · probability so if you recall when we said we we pulled that point five out of the Hat we landed between three and four but we know that the four didn't contribute to the jump and probability Mass the three did so because we landed on that interval of 0.5 we know that the outcome that we're looking for is three so that's what this search sorted does here is we're saying find the index of the drawn probability between 0

**38:31** · 概率的相应索引，所以如果你回忆当我们说我们从帽子里取出那个点五时，我们落在三和四之间，但我们知道四没有贡献跳跃概率质量，三是的，所以因为我们落在那个0.5的区间上，我们知道我们正在寻找的结果是3，这就是这个search sorted在这里做的，我们说找到零

**39:03** · and 1 in the context of our cumulative distribution function and then we're going to append the corresponding value here we're going to do that end times so we can roll as many dice as we'd like and then we're going to get a distribution that Maps each outcome to its correct probability mass and you can see down here everything has roughly a 1 16

**39:03** · 到1之间在我们的累积分布函数背景下的抽取概率的索引，然后我们将追加相应的值，我们将做n次，所以我们可以掷任意数量的骰子，然后我们将得到一个将每个结果映射到其正确概率质量的分布，你可以在下面看到一切都有大约1/6

**39:34** · probability of occurring after 10,000 rolls if we were to run this again and again we're going to get different outcomes of course because it is random but nevertheless you could see that it's following the correct structure of its probability Mass function okay so this

**39:34** · 发生概率，在10000次掷骰后，如果我们一次又一次运行这个，我们会得到不同的结果，当然因为它是随机的，但仍然你可以看到它遵循其概率质量函数的正确结构，好的，所以这个

**39:52** · right here is just one way to write the inverse transform method you can see this Loop here is actually iterating through all of the uniform samples there is another way to do this using a while loop and accumulating probability Mass across the space that would look something like this I'd say Def iidt and then I would say the current probability mass is f is equal to zero then we are going to accumulate a probability of 16 each time and the

**39:52** · 这里只是写逆变换方法的一种方式，你可以看到这里的这个循环实际上正在遍历所有均匀样本，还有另一种方式使用while循环并在空间上累积概率质量，那看起来会像这样，我会说Def iidt然后我会说当前概率质量f等于零，然后我们将每次累积1/6的概率，而

**40:23** · current outcome is going to be say one and I'll say we need to draw a u as well so U is equal to mp. random.

**40:23** · 当前结果将是比如1，我会说我们也需要抽取一个u，所以U等于np.random.

**40:34** · uniform and then we'll say 0 to one and then we'll say while F or while U is greater than or equal to F then we are going to increment the probability mass by 16 so we'll say F + = p and then

**40:34** · uniform然后我们会说0到1，然后我们会说while F或while U大于或等于F，然后我们将增加概率质量1/6，所以我们会说F += p然后

**41:00** · we'll say a + = 1 and then we will return a when this is all done so what's going to happen here is each round let's just see if I flip this

**41:00** · 我们会说a += 1然后当这一切完成时我们将返回a，所以这里会发生什么，每一轮让我们看看如果我翻转这个

**41:17** · inequality by accident so the the CDF is going to start at zero we've accumulated no probability Mass thus far uh and if we draw something that is below \[Music\] the below the current threshold so this has to start at6 so we start at 1 16 if we draw something that is below yeah while U is less than F

**41:17** · 不等式是否是偶然的，所以CDF将从零开始，我们迄今没有累积任何概率质量，如果我们抽取低于当前阈值的东西，所以这必须从1/6开始，如果我们抽取低于的东西，对，while U小于F

**41:47** · otherwise return a yeah that seems about right so we start at6 we're going to accumulate probability in increments of 1 16 and if this is a function so this is fixed because we have a discrete uniform random variable but if this is a function then we can very easily just write this as a function of what as a function of a this is our input so even if this is not discrete

**41:47** · 否则返回a，对，那看起来是对的，所以我们从1/6开始，我们将以1/6的增量累积概率，如果这是一个函数，这是固定的因为我们有离散均匀随机变量，但如果这是一个函数，那么我们可以很容易地将这写成什么的函数，a的函数，这是我们的输入，所以即使这不是离散

**42:13** · uniform let's say it's geometric let's say it's it's something else altogether binomial whatever it may be you can still do this inverse transform method instead of it being a fixed probability that's being accumulated it's just a functional probability that's being accumulated we'll draw a number between 0 and 1 let's say we draw zero well zero

**42:13** · 均匀，假设它是几何分布，假设它完全是其他东西，二项分布，不管它是什么，你仍然可以做这个逆变换方法，代替被累积的固定概率，它只是被累积的函数概率，我们将抽取零到1之间的一个数字，假设我们抽取零，那么零

**42:36** · is going to be less than F so we want to say while it's greater than here I believe this is correct while U is greater than F we're going to draw f+ = P A+ = 1

**42:36** · 将小于F，所以我们想在这里说while它大于，我相信这是正确的，while U大于F，我们将抽取f += p，a += 1

**43:10** · was a very easy way to to test this let's just try it two three two five all right looks good so while U is greater than F we are going to add the probability Mass to F and then we're going to increment a by 1 and we know this is always going to end at one because U is never going to

**43:10** · 这是一个非常简单的测试方法，让我们试试它，二、三、二、五，好的，看起来不错，所以while U大于F我们将添加概率质量到F然后我们将a增加1，我们知道这总是会在1结束，因为U永远不会

**43:44** · exceed one so we can see that when F accumulates enough probability Mass 1 16 + 1 16 + 1 16 + 16 it gets to one then this Loop will break because this can condition will no longer be true U will not be greater than F because U has a zero probability of being one then we

**43:44** · 超过1，所以我们可以看到当F累积足够的概率质量，1/6加1/6加1/6加1/6，它到达1，然后这个循环将中断，因为这个条件将不再为真，U不会大于F，因为U有零概率为1，然后我们

**44:05** · will have a is equal to 6 and we will produce that outcome so this is just a different way of doing it if this way made more sense then that's totally fair this is another way of doing it and in this way here uh this is a little more dynamic because if you don't have a discrete uniform random variable then you can always use a functional uh

**44:05** · 将有a等于6，我们将产生那个结果，所以这只是另一种方式，如果这种方式更有意义，那完全合理，这是另一种方式，在这种方式中，这更动态一些，因为如果你没有离散均匀随机变量，那么你总是可以使用函数

**44:27** · probability Mass function here to accumulate probability in your cumulative distribution function so this way that I had written it here is a little bit more dynamic because here you may not always have access to the entire CDF so one example would be a geometric

**44:27** · 概率质量函数在这里来在你的累积分布函数中累积概率，所以我在这里写的这种方式更动态一些，因为在这里你可能不总是有整个CDF的访问权，所以一个例子将是几何

**44:45** · random variable right a geometric random variable can technically go to Infinity so how do you account for that well you would have to use a y Loop and you would accumulate probability Mass according to a function function so it's not a fixed probability here but rather the probability Mass function that specifies the geometric random variable so this is going to be more Dynamic this function that I had just written and this is off the top of my head so I apologize for the confusion in the uh inequality here but yes this is going to be correct uh

**44:45** · 随机变量，对吧，几何随机变量技术上可以到无穷，所以你如何处理那个？你必须使用while循环，你将根据一个函数累积概率质量，所以这里不是固定概率，而是指定几何随机变量的概率质量函数，所以这将更动态，我刚写的这个函数，这是我想出来的，所以我为这里的不等式混乱道歉，但这将是正确的

**45:16** · in the way of generating a probability Mass function in a more general setting um but this is still just an implementation of what we had drawn out uh previously on the chart so as you can see each outcome here has the correct probability Mass assignment uh the frequency interpretation says that everything is roughly 16 that is great uh now in the context of a continuous distribution it's a lot easier because here you'll notice that we had to accumulate probability mass in this ivt uh even here you know there is this

**45:16** · 在更一般设置中生成概率质量函数的方式，但这仍然只是我们之前在图表上画出的东西的实现，所以如你所见，这里的每个结果都有正确的概率质量分配，频率解释说一切都是大约1/6，那很棒，现在在连续分布的背景下，它更容易，因为在这里你会注意到我们必须在这个ivt中累积概率质量，即使在这里你知道有这个

**45:46** · accumulation of probability Mass we're just kind of cheating using a search sorted here um but if we scroll on down to the cumulative um distribution function for a continuous random variable you'll see that it's it's quite easy to implement because once you invert this CDF we have an exponential distribution here we find the cumulative distribution function by integrating then we just invert it this is a very easily inverted equation because remember X is just what we're going to

**45:46** · 概率质量的累积，我们只是有点作弊使用search sorted，但如果我们向下滚动到连续随机变量的累积分布函数，你会看到实现它相当容易，因为一旦你对这个CDF求逆，我们这里有指数分布，我们通过积分找到累积分布函数，然后我们只是对它求逆，这是一个非常容易求逆的方程，因为记住X只是我们将要

**46:18** · plug into the function that's our uniform random variable so if we just swap these guys and solve then we get the inverse cumulative distribution function and this is just look it's Ln 1 U over Lambda the function or the

**46:18** · 插入函数的，那是我们的均匀随机变量，所以如果我们只是交换这些并求解，那么我们得到逆累积分布函数，这只是ln(1-U)/λ，函数或

**46:34** · parameter of the exponential distribution so this is very very very quick relative to even the discret case because if we scroll on down here we can see all we need to do is Define the inverse CDF then after we draw we can just plug in our draws to the inverse CDF and what you'll notice here here if I run this guy you'll see

**46:34** · 指数分布的参数，所以这相对于甚至离散情况来说非常非常非常快，因为如果我们向下滚动，我们可以看到我们需要做的就是定义逆CDF，然后在我们抽取后，我们可以只是将我们的抽取插入逆CDF，你会注意到这里，如果我运行这个，你会看到

**47:00** · that the true PDF aligns with the probability Mass assigned to the generated samples and that is exactly what we are looking to do okay so that's going to do it for this video on the inverse transform method I hope you found it informative uh again my goal is to start to post on a more consistent basis in 2025 I want to cover a variety of different topics um in probability statistics ICS um

**47:00** · 真实PDF与分配给生成样本的概率质量一致，这正是我们要做的，好的，所以这将是关于逆变换方法的视频的结束，我希望你觉得它有信息量，再次，我的目标是开始在2025年以更一致的基础发布，我想涵盖各种不同的主题，在概率统计ICS，

**47:28** · mathematics computer science uh quantitative Finance all of these all of these different fields these are the fields that I have the most interest in um and you know there's been a lot of Buzz around the the algorithmic trading um videos that I've posted in the past and on Quant Guild I have a whole course dedicated to algorithmic trading using alpaca's API I also have a course

**47:28** · 数学、计算机科学、量化金融，所有这些所有这些不同的领域，这些是我最感兴趣的领域，你知道在我过去发布的算法交易视频周围有很多热议，在Quant Guild我有整个课程专门用于使用alpaca的API进行算法交易，我还有一个课程

**47:49** · getting started with python I'm considering putting together courses um for other apis as well if if there is interest um but nevertheless you know that's that's the goal for 2025 please check out Quon Guild please check out GitHub I'm going to post this Jupiter notebook to a repository on GitHub I'll link it in the description below um if you have any comments or questions please leave them down below I'll do my best to respond um I'm I'm much more

**47:49** · Python入门，我正在考虑为其他API也组装课程，如果有兴趣的话，但无论如何你知道那是2025年的目标，请查看Quant Guild，请查看GitHub，我将把这个Jupyter笔记本发布到GitHub上的一个仓库，我会在下面的描述中链接它，如果你有任何评论或问题请留在下面，我会尽我所能回应，我在

**48:17** · active in the Discord if you ask me a question directly there comes up on my phone it's very easy for me to see so I'll post the link to join down there as well but other than than that it's good to be back I hope this video was again informative and I will see you in the next one thanks for watching

**48:17** · Discord中更活跃，如果你在那里直接问我一个问题，它会出现在我的手机上，对我来说很容易看到，所以我也会在下面发布加入的链接，但除此之外，回来真好，我希望这个视频再次有信息量，我会在下一个视频中见到你，感谢观看