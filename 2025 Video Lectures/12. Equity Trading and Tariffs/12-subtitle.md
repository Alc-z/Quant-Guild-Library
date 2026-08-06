---
title: "Equity Trading and Tariffs"
source: "https://www.youtube.com/watch?v=Yms19aI3eu4"
author:
  - "[[Roman Paolucci]]"
published: 2025-03-28
created: 2026-08-04
description: "🚀 Master Quantitative Skills with Quant Guild:https://quantguild.comJoin the Quant Guild Discord server here:https://discord.com/invite/MJ4FU2c6c3Solve our Monthly Promo Question f"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Yms19aI3eu4)

🚀 Master Quantitative Skills with Quant Guild:
https://quantguild.com

Join the Quant Guild Discord server here:
https://discord.com/invite/MJ4FU2c6c3

Solve our Monthly Promo Question for 35% Off Lifetime Access to Quant Guild!
https://www.youtube.com/post/UgkxoBZZglamNEpbhPln41wAVbxSuvOlBfCs
___________________________________________
Jupyter Notebook:
https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/12.%20Equity%20Trading%20and%20Tariffs/Equity%20Trading%20and%20Tariffs.ipynb
___________________________________________
Articles and code walkthroughs can be found on our blog
https://medium.com/quant-guild
https://romanmichaelpaolucci.medium.com/

For more free tutorials and references see our GitHub
https://github.com/RomanMichaelPaolucci
https://github.com/Quant-Guild

## Transcript

**00:01** · [Music] I want to talk about the lens that I look at the equity markets through, especially when there are significant regime changes, such as with this new administration and policy on tariffs. In

> ［音乐］我想谈谈我看待股票市场（equity market）的视角，尤其是在发生重大制度性变化（regime changes）的时候，比如本届新政府及其关税（tariffs）政策。在——

**00:15** · this video, I want to go through a basic quantitative argument. We're kind of dismissing all of the politics and and nonsense and all the different levers that we can pull to make different things happen and just try to look at

> ——本期视频中，我想梳理一个基本的量化论证（quantitative argument）。我们暂且撇开各种政治、各种噪音，以及所有可以拉动以实现不同结果的杠杆，只是试图去审视——

**00:28** · what's going on in the equity market through a purely quantitative conjecture. And hopefully this is going to allow you to gain some intuition as to what could be going on in the equity markets. A popular model for equity

> ——纯粹从量化的推测（conjecture）出发，看看股票市场正在发生什么。希望这能让你对股票市场可能发生的情况获得一些直觉。一个流行的股票估值模型——

**00:43** · valuation is the discounted cash flow analysis. All we do is forecast a company's future cash flows out to a certain point in time and then every year beyond that we just value it in perpetuity. Discount all of those cash

> ——是贴现现金流分析（discounted cash flow，DCF）。我们所做的就是预测一家公司未来某个时间点之前的现金流，然后在那个时间点之后的每一年，都以永续（in perpetuity）方式估值。把所有那些——

**00:59** · flows back to the present. Get rid of some debt divide by total shares outstanding and you actually arrive at a model stock price. In this example, I want to talk about an equity's price in the context of no tariffs and then in

> ——现金流贴现回现在，减去部分债务，再除以总流通股本，你就得到了一个模型化的股票价格。在这个例子中，我想讨论的是：在没有关税的情境下，以及——

**01:14** · the context of tariffs. And the way that I view these sorts of macroeconomic changes is through a lens of where money is going, not necessarily whether or not value is created or destroyed, but we'll talk more about that in a moment. And

> ——有关税的情境下，一只股票（equity）的价格会如何。我审视这类宏观经济变化的方式，是透过"钱流向哪里"的镜头，而不一定关心价值是被创造还是被摧毁——这一点我们稍后再详谈。并且——

**01:33** · we'll talk about some implications in equity trading. We're just going to walk through assuming that you're familiar with the DCF process. If you're not, I encourage you to check out quankill.com. We have lessons on the equity valuation

> ——我们还会谈谈这对股票交易（equity trading）的一些启示。我们直接往下讲，前提是你熟悉 DCF 的过程。如果你不熟悉，我建议你去 Quant Guild 网站（quankill.com）看看。我们有关于股票估值——

**01:44** · process along with equity portfolio management and other finance probability and math related topics. Nevertheless, here is a set of assumptions for this DCF in the state of the world where we have no tariffs. This is very important

> ——过程、股票投资组合管理（equity portfolio management），以及其他金融、概率和数学相关主题的课程。不过，这里给出这一 DCF 在"没有关税的世界"中的一组假设。这一点非常重要，因为——

**01:59** · because all of these levers here, we can pull them to make different things happen. But I'm going to assume that everything is held constant in this DCF relative to the next one except for the idea that we now have tariffs. For

> ——所有这些杠杆我们都可以拉动，以实现不同的结果。但我要假设：相对于下一个 DCF，这个 DCF 中所有其他变量都保持不变，唯一的区别就是"现在有了关税"。为了——

**02:14** · simplicity sake, let's say this is your business. You have a lemonade stand and you're currently importing a lot of the materials you need for your business to operate internationally. Let's go down here and

> ——简单起见，假设这就是你的生意：你经营着一个柠檬水摊（lemonade stand），目前正从国际上进口大量经营所需的材料。让我们往下看——

**02:27** · take a look at the present value of the cash flows for your business out to year 10. Again, we don't know what those are actually going to be. We're forecasting them and beyond that we're going to value your company in perpetuity. The

> ——看看你的生意在今后第 10 年之前的现金流现值（present value）。再说一遍，我们并不真正知道这些现金流会是多少——我们在预测它们；在那之后，我们以永续方式为你的公司估值。——

**02:38** · present value of those cash flows is going to be 245.78. Maybe this is in millions and you have a very successful lemonade stand. And the present value of your company in perpetuity beyond year 10 is

> ——这些现金流的现值是 245.78。也许单位是百万美元，你的柠檬水摊相当成功。而第 10 年之后、以永续方式计算的你公司的现值是——

**02:50** · 154.22. The total equity value is going to be 400 in the state of the world where there are no tariffs. And this nice bar chart here is going to essentially summarize this for us. We have the present value of each year's

> ——154.22。在没有关税的世界里，总股权价值（total equity value）是 400。这里这张漂亮的柱状图基本上帮我们做了总结：我们列出了每一年——

**03:04** · cash flow going out to year 10. And then beyond that, we value your company in perpetuity. Discount all these cash flows to the present. That's what each bar represents. We sum them all up and we get the value of 400. You've been

> ——一直到第 10 年的每一年现金流的现值，在那之后，我们以永续方式为你的公司估值。把这些现金流全部贴现到现在——这就是每一根柱子所代表的含义。把它们全部加总，就得到 400 这个价值。你已经在——

**03:17** · running this business successfully for the past three maybe four years under the previous administration. In doing so, you've IPOed and now you have a duty to your shareholders. You need to maximize their value. To do that, you're

> ——前一届政府执政下，成功地经营这家公司大约三、四年了。在此期间你完成了 IPO，现在你对股东负有责任：你必须最大化他们的价值。要做到这一点，你就要——

**03:28** · going to maximize your company's profits. To do that, you must minimize cost. There is no way to pursue a maximum profit without minimizing your cost. To do this, you've been engaging in the international markets, growing

> ——最大化公司的利润。而要做到这一点，你必须最小化成本。不把成本压到最低，就没有办法追求利润最大化。为此，你一直在参与国际市场，通过进口商品来——

**03:41** · your business year-over-year, minimizing your cost by importing goods. What do you think is going to happen to the present value of your future cash flows if there are tariffs on the trade that you have been doing internationally?

> ——年复一年地壮大你的生意，并最小化成本。如果对你一直在进行的国际贸易征收关税，你觉得你未来现金流的现值会发生什么变化？

**03:56** · Well, clearly your profit generating capacity is going to decline, at least in the short run, because you need to reoptimize. You need to reorder and figure out whether or not it's still effective to import those goods or buy

> ——显然，你创造利润的能力会下降，至少短期内如此，因为你需要重新优化（reoptimize）。你需要重新调整订单，弄清楚继续进口那些商品，还是改为——

**04:08** · them domestically. And that is essentially what this next DCF is going to reflect. If you take a look, I've adjusted some of the model assumptions to reflect the tariffs in the market. And you'll see that initially our cash

> ——在国内购买，哪种仍然更有效。而这基本上就是下一个 DCF 要反映的内容。你看，我调整了部分模型假设，以反映市场上的关税。你会看到，最初我们的现金——

**04:22** · flow generating capacity declines relative to the previous DCF. But after reordering and reoptimizing, eventually we get back to that original cash flow generating capacity and we're back to business with the value of our company

> ——流创造能力相对于前一个 DCF 有所下降。但在重新调整订单并重新优化之后，我们最终又回到原来的现金流创造能力，公司的价值也随之恢复——也就是第 10 年之后——

**04:36** · in perpetuity after year 10. This whole idea here is very important because companies aren't just going to roll over and accept that the tariffs are going to be a burden on their profit. They're going to reoptimize and reorder to

> ——以永续方式计算的公司价值。这里的整个思想非常重要，因为公司不会坐以待毙、接受关税成为其利润的负担。它们会重新优化、重新调整订单，以确保——

**04:53** · ensure that they achieve their maximum cash flow generating capacity. And if that means transacting domestically, so be it. If that means transacting internationally, so be it. But that is the goal of the company. The goal of the

> ——达到它们最大的现金流创造能力。如果那意味着在国内交易，那就国内交易；如果那意味着在国际上交易，那就国际交易。但这就是公司的目标。公司的——

**05:06** · company is to maximize profit. Again, they're not just going to sit there, roll over, and take these increased costs. But this is the only location that they can find that good. Okay. Well, fine. They're going to have to

> ——目标就是利润最大化。再说一次，它们不会坐在那里乖乖接受这些增加的成本。但如果这已经是它们能找到的、唯一有利可图的货源了，那好吧——它们就必须——

**05:19** · optimize their cost function elsewhere. That means maybe somewhere in the labor market, maybe somewhere in cutting projects, whatever it may be. The whole purpose of these firms existence is to generate profit. When you IPO, your duty

> ——在其他地方优化它们的成本函数（cost function）。那可能意味着在劳动力市场某处下手，可能意味着砍掉某些项目，无论是什么。这些公司存在的全部目的就是创造利润。当你 IPO 之后，你的责任——

**05:34** · is to maximize the value to the shareholder. You can go about suggesting that there's corruption or agency problems that you know make this process impure and fair enough. But overwhelmingly the whole goal of all of

> ——就是最大化股东价值。你当然可以说这里面存在腐败或代理问题（agency problems），使这个过程不那么纯粹——好吧，这没错。但压倒性地看，所有这些公司——

**05:47** · these firms, whether it's in technology, healthcare, whatever it may be, is to make money. And if their cost function increases and they're making less money and executive compensation is going to fluctuate maybe in a downward direction

> ——无论身处科技、医疗还是其他行业，目标都是赚钱。如果它们的成本函数上升、赚的钱变少，高管的薪酬也许还会随之波动、甚至往下走——

**06:01** · because of these increased costs, you better believe that they're going to attempt to offset them elsewhere in their company. Let's talk about the implications in the equity market. Now, regardless of your opinion on the

> ——由于这些增加的成本，你大可以相信，它们会试图在公司的其他地方把这些成本抵消掉。让我们谈谈这对股票市场意味着什么。现在，无论你对——

**06:13** · previous administration or the current administration, I hope everybody has the wherewithal to at least understand that any administration in place does not have a goal of destroying the economy. The levers that are available to pull in

> ——前任政府还是现任政府持什么看法，我希望每个人都至少具备这样的判断力：任何一届政府，其目标都不是摧毁经济。在——

**06:29** · fiscal policy vary based on the administration and the constituents that they serve. That is a very important idea because you'll see people crying in each regime, but the people that are crying in each regime are very

> ——财政政策（fiscal policy）中可供拉动的杠杆，因政府及其所服务的选民（constituents）不同而各异。这是一个非常重要的观点，因为你会发现每一届政府下都有人在叫苦，但每一届政府下叫苦的群体却——

**06:43** · different. And that's because they serve different constituents and the levers that they're pulling are fundamentally affecting different macro variables. Trading in general is very sentimentdriven. So, of course, when

> ——完全不同。这是因为他们服务不同的选民，他们拉动的杠杆从根本上影响着不同的宏观变量（macro variables）。交易总体上是高度受情绪驱动的。所以，当然，当——

**06:55** · there's news of tariffs impacting value, everything is going to go down to some capacity. But I want to paint a picture of what the administration is trying to do in a best case scenario and talk about sort of the implications of this

> ——有消息说关税正在影响价值时，一切都会在某种程度上下跌。但我想描绘出政府在最佳情景下试图做的事情，并谈谈这对于——

**07:10** · relative to the previous administration's policy. We're not going to touch too much on the macro variables. We're not going to talk too much about interest rates and inflation and Fed policy. That's really a

> ——相对于前一届政府的政策而言，意味着什么。我们不会过多触及宏观变量，不会过多谈论利率、通胀和美联储政策。那真的是——

**07:21** · different topic for another day. But here what I have is I have the stock price that we have valued in the two previous DCFs in two states of the world. The first state of the world is this light blue line with no tariffs.

> ——另一天的另一个话题了。但在这里，我有的是：我们在此前两个 DCF 中、在两种世界状态下估值出来的股票价格。第一种世界状态就是这条浅蓝色线，没有关税——

**07:35** · That is the base case. And as you can see, the price is just merrily kind of moving along here and the upward trend that it was moving in. And in this other state of the world, we have this tariff price path. And this is the blue dashed

> ——这是基准情形（base case）。如你所见，价格只是顺着它原本的上升趋势一路前行。而在另一种世界状态下，我们有这条关税价格路径，就是那条蓝色虚线——

**07:49** · line, this dark blue line. And this red vertical line is when tariffs have been imposed. And you can see that there's a massive value drop relative to the base case with no tariffs. Why would anybody excuse to enact tariffs if they know

> ——这条深蓝色的线。而这条红色竖线就是关税被实施的时间点。你可以看到，相对于没有关税的基准情形，出现了巨大的价值下跌。如果人们明知道——

**08:05** · that there's going to be this massive value drop and everyone's 401ks are out the window and whatever? Well, there's this period of reordering, restructuring, reoptimization. And the goal is that across the board, you're

> ——会有这么大的价值下跌、所有人的 401k 账户都要打水漂，那为什么还有人要推行关税呢？好吧，因为有这么一段"重新调整、重组、重新优化"的时期。其目标是，在整体上，你将会——

**08:17** · going to see this growth that outpaces the original base case with no tariffs. Not to mention that this original base case with no tariffs may not be serving other macro variables like inflation and interest rates domestically. The hope is

> ——看到这种超过原始无关税基准情形的增长。更不用说，那个原始的无关税基准情形，可能并不利于国内其他宏观变量，比如通胀和利率。人们的希望是——

**08:30** · that through this process, all of that shakes out in a positive direction or a net positive direction for the domestic economy. However, in the short run, traders have to respond to these shocks by trading equities at a lower relative

> ——通过这个过程，所有这一切都会朝着对国内经济积极、或净积极的方向发展。然而，在短期内，交易者必须对这些冲击作出反应，在相对更低的水平上交易股票——

**08:44** · level. And there's a theoretical value gap that you can capitalize on by taking a long position. This is not financial advice. This is how I trade. I take a look at what the market climate would have been like without an event. And I

> ——这就产生了一个理论上的价值缺口（value gap），你可以通过建立多头头寸（long position）来加以利用。这不是投资建议，这是我自己的交易方式。我会先看看"如果没有该事件，市场氛围会是什么样"。然后我——

**08:59** · ask myself whether or not that event is the de facto binary zero and one between whether or not that equity space will recover to the previous level. And if it's not, which it most likely isn't, then I'm going to take a net long

> ——会问自己：这个事件，是否真的是决定"该股票板块能否恢复到此前水平"的二值开关（binary 0/1）。如果答案是否定的——而大多数时候是否定的——那么我就会建立一个净多头——

**09:13** · position. This is very similar to event trading, but I'll make a video on that for another day. And after taking a net long position, you can kind of capitalize on this theoretical statistical arbitrage, if you will,

> ——头寸（net long position）。这与事件交易（event trading）非常相似，不过那是另一个话题，改天我再做一期视频。在建立净多头头寸之后，你多少可以利用这种理论上的统计套利（statistical arbitrage），如果你愿意这么叫的话——

**09:26** · across the board in the equities market. Now, that is essentially just buying the dip relative to a negative event as the entire world preaches doomsday. You can kind of capitalize on this as a buying opportunity. Keep in mind, like every

> ——在股票市场的整体范围内。这本质上就是在全世界都在宣讲末日来临的负面事件面前"逢低买入"（buying the dip）。你可以把它当作一个买入机会来加以利用。请记住，就像我讨论的——

**09:43** · other model I discuss, this is just a model. DCFs are just a model for stock price. If you go on YouTube and search up Nvidia DCFS before that massive stock price increase, you'll see that they were valued significantly less. And

> ——每一个其他模型一样，这只是一个模型。DCF 只是股价的一种模型。如果你上 YouTube 搜索英伟达（Nvidia）在股价大幅上涨之前的 DCF 估值，你会看到它们被估得明显更低。而——

**09:59** · that's because when there are substantial information changes through events that are unforeseen, you don't know what the impact on the future cash flows is going to be. You're just essentially using a whole set of

> ——这是因为，当通过不可预见的事件发生大规模的信息变化时，你并不知道这对未来现金流会产生什么影响。你基本上只是在用一整组——

**10:10** · assumptions and a history to try to model cash flows going forward. So you're not going to be predicting these sort of idiosyncratic events that are going to be, you know, massively increasing one stock price or massively

> ——假设和历史数据，来尝试为未来的现金流建模。所以你不会去预测这类特质性事件（idiosyncratic events）——比如那些会让某一只股票价格暴涨或——

**10:26** · decreasing one stock price. This is using the idea of a DCF in a cross-section of equities across the board, suggesting, hey, you know, this creates a buying opportunity. Essentially, you're entering at a lower

> ——暴跌的事件。这是在横截面（cross-section）的股票整体上应用 DCF 的思想，暗示：嘿，你知道，这就创造了一个买入机会。本质上，你在更低的水平入场——

**10:39** · level in the market and you're able to invest or trade uh getting it at a lower price per share for each of your equities that you are trading. Pretty much all of the algorithms that I trade on a daily basis have to do with this

> ——你能够在市场上，为你交易的每一只股票获得更低的每股价格。我日常交易所用的几乎所有算法，都与此有关——

**10:53** · idea of an overreaction in a negative capacity. That is, trading is very sentiment driven. And when there is a negative set of information released for a cross-section of equities, I'm going to be entering at a lower level and then

> ——也就是"负面方向上的过度反应"（overreaction）这一思想。也就是说，交易高度受情绪驱动。当一揽子股票发布一组负面信息时，我会在更低的水平进场，然后——

**11:08** · cashing out when everything inevitably recovers. But that's going to be a video for April. Stay tuned for how to build a trading bot that is going to implement that draw down feature along with some sort of AI component for portfolio

> ——在一切不可避免地恢复时套现离场。但那是四月份的视频。敬请期待如何构建一个交易机器人（trading bot），它将实现那种回撤（drawdown）功能，并带有人工智能组件用于投资组合——

**11:24** · management. You can even extend that to creating live news if you integrate some sort of live news feed API. So that's something to look forward to. To summarize my quantitative perspective, I see a value gap between

> ——管理。你甚至可以通过接入某种实时新闻推送 API（live news feed API），把它扩展成实时新闻。所以这是值得期待的事情。总结一下我的量化视角：我看到在——

**11:38** · what traders are currently pricing equities at and the value that they should be priced at. And in order to capitalize that, I am net long in a large cross-section of equities. I don't do this manually. I do this

> ——交易者当前为股票定价的价格，与它们本应被定价的价值之间，存在一个价值缺口。为了利用这一点，我在一个大型股票横截面上保持净多头。我不是手动做这件事，我是——

**11:50** · algorithmically. But again, a video for a later date. I hope you enjoyed this video. Again, all of these are models, assuming a lot of variables are fixed. These are very complicated environments, nothing that a simple model can

> ——用算法来做。不过再说一次，那是以后某天的一期视频。希望你们喜欢这期视频。再次强调，所有这些都是模型，假设了大量变量保持不变。这些都是非常复杂的环境，绝非一个简单模型所能——

**12:06** · perfectly explain. But I think this is a reasonable conjecture for the current market climate. I hope you enjoyed this video and I will see you in the next one.

> ——完美解释。但我认为，对于当前的市场环境，这是一个合理的推测。希望你们喜欢这期视频，我们下期再见。
