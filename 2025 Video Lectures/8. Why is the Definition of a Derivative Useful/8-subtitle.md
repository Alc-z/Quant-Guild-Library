---
title: "Why is the Definition of a Derivative Useful?"
source: "https://www.youtube.com/watch?v=CD8XYP4lq4g"
author:
  - "[[Roman Paolucci]]"
published: 2025-03-01
created: 2026-08-04
description: "🚀 Master Quantitative Skills with Quant Guild:https://quantguild.comMarch 2025 Promo Question for Quant Guild Lifetime Access:https://www.youtube.com/channel/UCW1svfGxG4ADnbc1HCH6dqA/community?lb"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=CD8XYP4lq4g)

🚀 Master Quantitative Skills with Quant Guild:  
https://quantguild.com  
  
March 2025 Promo Question for Quant Guild Lifetime Access:  
https://www.youtube.com/channel/UCW1svfGxG4ADnbc1HCH6dqA/community?lb=UgkxIAhQCKcI8GHGE-T\_V0JIIZ4FB9nbkeLQ  
  
Join the Quant Guild Discord server here:  
https://discord.com/invite/MJ4FU2c6c3  
  
Articles and code walkthroughs can be found on our blog  
https://medium.com/quant-guild  
https://romanmichaelpaolucci.medium.com/  
  
For more free tutorials and references see our GitHub  
https://github.com/RomanMichaelPaolucci  
https://github.com/Quant-Guild

## Transcript

**0:01** · \[Music\] welcome back today I'd like to discuss the idea of analytical and numerical differentiation which can be particularly useful in understanding difference equations and differential equations also in understanding the idea
> [音乐] 欢迎回来。今天我想讨论解析微分（analytical differentiation）和数值微分（numerical differentiation）的概念，这对理解差分方程和微分方程特别有用，也有助于理解……

**0:17** · of numerical solutions to differential and partial differential equations so I'd like to kind of build the groundwork for those later videos by starting with this idea of analytical and numerical differentiation there's a lot of use cases a lot of use cases in machine learning in finance physics so on and so forth so let us begin with this idea of a derivative the definition of a derivative is given a function f ofx
> ……微分方程和偏微分方程的数值解。所以我想从解析微分和数值微分这个概念入手，为后面的那些视频打好基础。它在机器学习、金融、物理等众多领域都有大量应用场景。那么，让我们从导数的概念开始。导数的定义是：给定一个函数 f(x)，……

**0:48** · frime of x is equal to the Limit as H approaches zero of FX + hus FX / h which is essentially saying as we change the input a little bit how can we expect the
> ……f'(x) 等于当 h 趋近于 0 时，[f(x+h) − f(x)] / h 的极限。这本质上是在说：当我们稍微改变输入时，我们预期……

**1:06** · function value to change it's pretty much all it's saying you may have heard it as the instantaneous rate of change slope of the tangent line all of these things are also objectively true I have not defined the conditions for differentiability I have simply just discussed this definition let's apply this definition to a very simple function so if I have a function let's say G of X is equal to
> ……函数值会如何变化。差不多这就是它想表达的全部意思。你可能听过它被称为瞬时变化率、切线斜率，所有这些说法也都客观成立。我并没有定义可微性的条件，我只是讨论了这一定义。让我们把这一定义应用到一个非常简单的函数上。如果有一个函数，比方说 G(x) = ……

**1:33** · x^2 how can I find the derivative well many of you may be screaming power rule right now and fair enough if you know that g Prime of X is just simply going to be equal to 2x great there are plenty of derivative rules that you need to learn power rule product rule chain rule derivatives of cyclical functions s cosine tangent derivatives of inverse trig functions the there's plenty to learn and there's plenty to understand but you also need
> ……x²，我该如何求它的导数呢？嗯，你们很多人现在可能已经在喊"幂法则"了，确实如此。如果你知道 g'(x) 就等于 2x，很好。有很多求导法则需要你学习：幂法则、积法则、链式法则、三角函数（正弦、余弦、正切）的导数、反三角函数的导数。要学的东西很多，要理解的东西也很多，但你也需要……

**2:04** · or maybe at one point have appli the formal definition of the derivative to the function in calculus one this kind of is you know much to many students dis mayay a pain because you can just use the power rule and get the derivative and it's quite easy uh or you can go through the entire limit definition argument and
> ……或者说，在微积分一（Calculus One）课程中，你可能曾经把导数的形式化定义应用到函数上。你知道，对许多学生来说，这可能会是个痛苦的过程，因为你本可以直接用幂法则就得到导数，相当容易；或者你也可以走完整套极限定义的推导过程，而且……

**2:25** · just to kind of show you why it's agonizing if you've never seen it before then we would need to apply that definition to this function G so we would say the limit as H approaches zero of G of x + H minus G of x / H then we
> ……（我这么做）就是想让你看看为什么这很折磨人——如果你以前从没见过的话。我们需要把这一定义应用到函数 G 上，所以我们会说：当 h 趋近于 0 时，[G(x+h) − G(x)] / h 的极限。然后我们……

**2:42** · would have to use our knowledge of limits we would say this is equal 2 x + h^ 2 - x^2 / h of course we still have the limit as H approaches zero and then here we we would get x^2 + 2x H + h^2 - x^2 / H and of course it's
> ……就不得不运用我们对极限的知识。我们会说这等于 [(x+h)² − x²] / h，当然，我们仍然要取 h 趋近于 0 的极限。然后在这里，我们会得到 [x² + 2xh + h² − x²] / h，当然还有……

**3:08** · the limit as H approaches zero and here you'll see the X s's cancel out H is going to cancel out here and we're just left with the limit as H approaches zero of 2x + H which is simply 2x the same thing we get from our power
> ……当 h 趋近于 0 的极限。在这里你会看到 x² 相互抵消，h 在这里也会消掉，我们只剩下当 h 趋近于 0 时 (2x + h) 的极限，也就是 2x。这和我们从幂法则得到的结果完全一样。

**3:27** · rule I really wish wish that math professors in college instead of making you grind out these limit definition Arguments for the derivative of different functions would show you why the limit definition is so useful it's not useful for this
> ……我真希望大学里的数学教授们，与其让你苦苦为不同函数的导数推演那些极限定义的论证，不如向你展示极限定义为什么如此有用。它并不是为了……

**3:49** · 99.999 whatever percent going out a thousand decimal places if you have to of students are not going to be researching mathematics at an academic level and I think it does them an incredible disservice to just make them grind away at these types of problems not necessarily in the context of their mathematical development I'm all for that but it discourages the actual use and application of what a derivative is in fact I often times look to the
> ……（并不是为了让）99.999% 之类比例的学生——如果你非要较真到小数点后一千位的话——去做学术层面的数学研究。我认为，仅仅让他们在这类问题上苦练，是对他们极大的不公。就他们的数学发展而言，我完全赞成（这种训练），但它却阻碍了导数的实际使用与应用。事实上，我常常更倾向于依赖……

**4:20** · definition more than all of the rules because it's so intuitive and easy to implement in a numerical setting what what do I mean by this well these two ways got us to the same answer but we also have the power of computers at our disposal and one thing that you'll realize is calculus deals with infinity infinitely large and infinitely small
> ……（依赖）定义而不是所有那些法则，因为它在数值情境下如此直观、易于实现。我这么说是什么意思呢？嗯，这两种方式让我们得到了相同的答案，但我们还有计算机的力量可供使用。你会意识到的一点是：微积分处理的是无穷——无穷大和无穷小。

**4:48** · but you don't need to get infinitely small to get a very reasonable answer or even the answer that you're looking for and what do I mean by this well if we know that that g Prime of X is equal to the Limit as H approaches Z of G of x
> ……但你并不需要（让步长）趋近于无穷小，就能得到一个非常合理的答案，甚至就是你想要的答案。我这话是什么意思呢？嗯，如果我们知道 g'(x) 等于当 h 趋近于 0 时，[G(x+……

**5:09** · + hus G of x / H doesn't it follow that this would be approximately equal to G of x + H minus G of x ided h when H is small
> ……+h) − G(x)] / h 的极限，那么当 h 很小时，这不就意味着它约等于 [G(x+h) − G(x)] / h 吗？

**5:33** · in fact that that's true right and most of the time that is enough Precision to use the derivative for what we want to use it for you can think of this very simply as if you have $2 say you have $2 is this not approximately equal to 2.
> 事实上确实如此，对吧？而且大多数时候，这种精度已经足够我们用导数去做想做的事情了。你可以非常简单地把这理解为：假设你有 2 美元——比如说你有 2 美元，这难道不约等于 2.03 美元吗？

**5:54** · maybe 03 $23 do you really care about the3 cents if you were trying to buy a bag of chips or a bottle of water at a convenience store and you were really hungry you were really thirsty you really going to care about that very marginal error more often than not no and what
> ……也许是那 0.03 美元，2.03 美元。你真的在乎那 3 美分吗？如果你在便利店想买一袋薯片或一瓶水，而且你真的很饿、真的很渴，你真的会在乎那一点点边缘误差吗？大多数情况下不会。而……

**6:16** · I'm trying to emphasize here is you're not going to care about it for the use case that you're going to use the derivative for anyway so it turns out that this approximation is incredibly useful why is this approximation so useful because instead of going through this entire limit argument or trying to use our rules from calculus so long as
> ……我想在这里强调的是：反正对于你要使用导数的那个场景来说，你根本不会在乎这一点误差。所以事实证明，这种近似极其有用。为什么这种近似如此有用？因为与其走完整套极限论证，或者试图使用微积分里的法则——只要你……

**6:37** · you have a function you can compute the derivative you don't need to use the limit argument and you don't need to use any rules like the power rule the product rule the chain Rule and you can still arrive at a value for the derivative incredibly powerful incredibly powerful no rules from calculus and no limits so how does this work well it's not exactly a proof but here's
> ……有一个函数，你就能计算出导数。你不需要用极限论证，也不需要任何法则——比如幂法则、积法则、链式法则——你依然能得出导数的数值。极其强大，极其强大。不需要微积分的任何法则，也不需要极限。那么这是怎么运作的呢？嗯，这算不上严格的证明，但这里有一个……

**7:10** · a good example let's say h of X is equal to X cubed and I want to find the derivative H Prime of X okay well let's say I don't know my
> ……很好的例子。假设 h(x) = x³，我想求它的导数 h'(x)。好的，假设我不知道……

**7:31** · rules I don't know I don't know the power rule I don't know any rules let's say all I have is the limit definition but I'm no good at limits maybe there's not even a solution let's say it is differentiable let's let's kind of just throw that off to the side if you're screaming cusp or Screaming you know discontinuities then let's just kind of dismiss that let's assume that the functions differentiable here x cubed is a polinomial function continuous everywhere differentiable everywhere but but we don't know we're no good at limits we don't know any rules well we
> ……（我不知道）这些法则。我不知道幂法则，不知道任何法则。假设我只有极限定义，但我不擅长极限——也许根本没有解。假设它是可微的，我们先把这一点放到一边。如果你在高喊"尖点"，或者高喊"不连续点"，那我们就先忽略这些。让我们假设这个函数在这里是可微的：x³ 是一个多项式函数，处处连续、处处可微。但我们（假设）不知道这些——我们不擅长极限，不知道任何法则。那我们……

**8:03** · know that this is approximately equal to H of X plus some small value let's call it Delta xus h ofx / Delta
> ……就知道这约等于 [h(x + Δx) − h(x)] / Δx，其中 Δx 是加上的某个小值。

**8:22** · X do we need a derivative here do we need a limit definition do we need rules no we just need to pick a small Delta X so so let's do this let's go ahead and and pick a small Delta X I'm going to say Delta X is equal to
> ……这里需要导数吗？需要极限定义吗？需要法则吗？不需要。我们只需要选一个很小的 Δx。所以让我们来做吧：我们选一个小的 Δx，我说 Δx = ……

**8:45** · 0.001 001 okay so what does that imply that implies that H Prime of X is approximately equal to let's do X+ 001 cubed Min - x cubed /
> ……0.001。好的，这说明了什么呢？这说明 h'(x) 约等于 [(x + 0.001)³ − x³] / 0.001。

**9:06** · 001 that's our derivative it's as simple as that that's our numerical solution for the derivative it's an approximation of course we have an analytical solution and we can compute some error and you could do some error analysis and it's a very interesting subject to study but for now let's just kind of come up with a very simple application and take a look at the results so let's do I'm going to put in purple
> ……0.001，这就是我们的导数。就这么简单。这就是导数的数值解。当然，它是一个近似；我们有解析解，可以计算一些误差，你也可以做一些误差分析，这是一个非常有趣的研究课题。但现在，我们只想做一个非常简单的应用，看看结果。那么让我们来做——我要用紫色写……

**9:36** · here H Prime of X is equal to 3x^2 we know this to be true we know this to be true using the power rule we know H Prime of 1 is equal to 3 I'm going to use blue as the approximation what is h Prime of one when we use the
> ……这里 h'(x) = 3x²。我们知道这是对的——用幂法则我们就知道这是对的。我们知道 h'(1) = 3。我要用蓝色表示近似值。当我们使用……

**10:00** · approximation well H Prime of 1 is approximately equal to 1 +1 cubed minus 1 / 001 going to go ahead and plug this into a calculator I'm actually going to do it on my phone so 1.001 cubed -1 /
> ……近似值时，h'(1) 约等于 (1.001³ − 1) / 0.001。我要把它输入计算器，实际上我打算在手机上算。所以 1.001³ − 1，除以……

**10:33** · 0.001 and look what we get 3.3 okay so in other words we have H
> ……0.001，看看我们得到了什么：3.003（转录稿误写为 3.3）。好的，换句话说，我们有 h'……

**10:51** · Prime of one I'll say hat is approximately equal to H Prime of one we have 3.3 is approximately equal to 3 and here's where you have to ask
> ……h'(1)，我说这个估计值约等于 h'(1)。我们得到 3.003 约等于 3。而在这里，你必须问自己……

**11:10** · yourself is that good enough or do we really need the Precision and that's going to depend on the problem that you are working on if we're working on a machine learning problem then really does it matter if
> ……这样的精度够不够？还是说我们真的需要更精确？这取决于你所处理的问题。如果我们在做一个机器学习的问题，那么如果有一点偏差，真的重要吗？

**11:26** · we're off by a little bit maybe maybe not we really just need to figure out what direction to step in in a machine learning context but that's going to be a video for another day I hope you've enjoyed this video discussing analytical and numerical differentiation see you in the next one
> ……也许重要，也许不重要。在机器学习的情境下，我们其实只需要弄清楚该往哪个方向迈步。但那就是另一天的视频了。希望你喜欢这期关于解析微分和数值微分的视频，我们下期见。
