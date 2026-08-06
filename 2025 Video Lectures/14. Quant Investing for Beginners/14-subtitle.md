---
title: "Quant Investing for Beginners"
source: "https://www.youtube.com/watch?v=aBfkf_0YsCY"
author:
  - "[[Roman Paolucci]]"
published: 2025-04-11
created: 2026-08-04
description: "🚀 Master Quantitative Skills with Quant Guild:https://quantguild.comJoin the Quant Guild Discord server here:https://discord.com/invite/MJ4FU2c6c3Solve our Monthly Promo Question for 25% Off"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=aBfkf_0YsCY)

🚀 Master Quantitative Skills with Quant Guild:
https://quantguild.com

Join the Quant Guild Discord server here:
https://discord.com/invite/MJ4FU2c6c3

Solve our Monthly Promo Question for 25% Off Access to Quant Guild!
http://youtube.com/post/Ugkx5x12aT_LSRL_tKQOxQtUNrFlcuwYp3Jv?si=hYkEZ0ajWj1rAyyI
___________________________________________
Jupyter Notebook:
https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/14.%20Quant%20Investing%20for%20Beginners/Quant%20Investing%20Strategies%20for%20Beginners.ipynb

Portfolio Visualizer:
https://www.portfoliovisualizer.com/
___________________________________________
Articles and code walkthroughs can be found on our blog
https://medium.com/quant-guild
https://romanmichaelpaolucci.medium.com/

For more free tutorials and references see our GitHub
https://github.com/RomanMichaelPaolucci
https://github.com/Quant-Guild

## Transcript

**00:01** · [Music] there's a big difference between quantitative trading and quantitative investing quantitative trading may involve a variety of different strategies maybe you have a large amount

> [音乐] 量化交易（quantitative trading）与量化投资（quantitative investing）之间存在巨大区别。量化交易可能涉及各种各样的策略——也许你拥有大量的——

**00:11** · of alternative data or you're doing something at a low latency and you're going to be executing a large number of Trades maybe trying to predict returns in the cross-section of a large number of financial

> ——另类数据（alternative data），或者你在做某种低延迟（low latency）的事情，并会执行大量的交易，也许是想在大量金融——

**00:23** · instruments but quantitative investing is an entirely different animal so in this video what I want to do is I want to talk about quantitative investing strategies for beginners I'm not telling you what stocks to buy rather what I

> ——工具的横截面上预测收益。但量化投资完全是另一回事。所以在这期视频里，我想做的是：聊聊面向初学者的量化投资策略。我不是要告诉你该买哪些股票，而是——

**00:36** · want to do is I want to discuss the underlying Financial mathematics so that you have an idea of what's going on when you involve yourself in the market in any capacity we're going to look at different facets of risk talk about

> ——我想讨论的是底层的金融数学，让你在以任何方式参与市场时，能明白背后到底发生了什么。我们会考察风险的不同侧面，讨论——

**00:49** · diversification and look at some nice charts to really understand the big picture let's begin by discussing this idea of portfolio risk there are a lot of different types of portfolio risk and depending on the financial instrument

> ——分散化（diversification），并看一些漂亮的图表，以真正理解大局。让我们从"投资组合风险"（portfolio risk）这个概念开始。投资组合风险有很多不同类型，而且取决于金融工具——

**01:02** · you may have different types of exposures we're going to focus on equities and Equity portfolios and in this case like I said you can narrow all the way down to something like you know regulatory risk and say Hey you know

> ——你可能会有不同类型的敞口（exposure）。我们将聚焦于股票（equities）和股票投资组合。在这种情况下，如我所说，你可以把风险一路细分到像监管风险（regulatory risk）这样的层面，然后说：嘿，你看——

**01:15** · this is a brand new company that recently ipoed and they're using emerging technology we don't yet know if the government is going to aim to regulate if this business can continue to operate as they are that's a very

> ——这是一家刚上市（IPO）的全新公司，他们使用新兴技术。我们还不知道政府是否会出手监管，这家企业能否按现在的模式继续经营——这是一个非常——

**01:28** · narrow component of risk what I want to do is I want to kind of zoom out and throw it into one of three buckets we have idiosyncratic risk we have industry risk and we have Market risk so idiosyncratic risk refers to firm

> ——细分的风险组成部分。我想做的是把视角拉远，把风险归入三大类之一：特异风险（idiosyncratic risk）、行业风险（industry risk）和市场风险（market risk）。特异风险指的是与公司——

**01:42** · specific risk so if I hold Apple in my stock portfolio it's risks associated with that specific firm industry risk is sector risk or sector specific risk and that could be all of healthcare that could be all of technology that could be

> ——相关的特定风险。所以如果我的股票组合里持有苹果（Apple），那么这就是与该特定公司相关的风险。行业风险是板块风险（sector risk）或板块特定风险，它可以是整个医疗保健行业，可以是整个科技行业，也可以是——

**01:59** · all of utilities things of that nature it's things that affect a specific industry so you know you can look at that regulatory risk that was discussed a moment ago in the context of maybe idiosyncratic and Industry risk because

> ——整个公用事业行业，诸如此类。它是影响特定行业的因素。所以你看，刚才讨论的监管风险，就可以放在特异风险和行业风险的语境下去看待，因为——

**02:13** · regulation could impact an entire industry as a whole and lastly we also have this idea of Market risk and this is really driven by a lot of different factors you can look at macro factors to help guide your understanding of the

> ——监管可能会影响整个行业。最后，我们还有市场风险这个概念，它实际上由很多不同的因素驱动。你可以借助宏观因素（macro factors）来帮助理解——

**02:28** · current market climate things like GDP things like the current rate of inflation interest rates those type of metrics will give you an idea of the current market climate at a high level why do we care about these elements of

> ——当前的市场环境，比如 GDP、当前的通货膨胀率、利率这类指标，都会让你从宏观层面对当前市场环境有一个概念。为什么我们要关心这些——

**02:43** · portfolio risk well you need to assume some risk in order to earn a return that is the fundamental idea behind investing but you don't need to assume unnecessary risk moreover this quantitative investing strategy we're discussing in

> ——投资组合风险的要素呢？因为要想获得收益，你就必须承担一定的风险——这是投资背后的基本理念。但你不必承担不必要的风险。此外，我们在这期视频里讨论的这个量化投资策略——

**02:59** · this video is not about optimizing some sort of risk return metric this is not some sort of crazy quantitative trading strategy but rather we're trying to see if there's anything we can do about these different components of equity

> ——并不是关于优化某个风险收益（risk-return）指标，也不是某种疯狂的量化交易策略。相反，我们是想看看，能不能对这些股票——

**03:13** · risk in our portfolio this is where diversification comes into play I could put all of my eggs into one basket I could take my entire retirement account and put it into Nvidia stock that will give me exposure to idiosyncratic risk

> ——投资组合中不同成分的风险做点什么。这就是分散化登场的地方。我可以把所有的鸡蛋放进同一个篮子里——我可以把整个退休账户都投进英伟达（Nvidia）的股票，这会让我暴露于特异风险——

**03:28** · industry risk and Market risk but it's important to note that this risk is not equally split among that one investment so if I only hold Nvidia stock it's not like I have an equal split of risk across the idiosyncratic risk industry

> ——行业风险和市场风险。但需要注意的是，这些风险在那一笔投资中并不是平均分配的。所以如果我只持有英伟达的股票，并不意味着我在特异风险、行业——

**03:44** · risk and Market risk maybe you try to proxy this risk using some historical data but historical data is not indicative of future performance yes if Nvidia has an incredible year then I could make a lot of money but on the

> ——风险和市场风险之间平均分摊了风险。也许你可以尝试用一些历史数据来近似这种风险，但历史数据并不能预示未来的表现。没错，如果英伟达有惊人的一年，我确实可以赚很多钱，但反过来——

**03:59** · flip side if tech does poorly or Nvidia does poorly maybe new technology comes out and outpaces Nvidia then I'm going to be down a significant amount of money and this is this just turns into a game of stock picking and that's not our goal

> ——如果科技股表现不佳，或者英伟达表现不佳，也许新技术横空出世、超越了英伟达，那我就会亏掉一大笔钱。这样一来，这就变成了一场选股（stock picking）的游戏，而那并不是我们的目标——

**04:14** · that's not a good strategy we need a better quantitative investing strategy our strategy is going to be to diversify away the first two components of risk leaving us only with a market risk exposure now fundamentally if we were to

> ——那不是一个好策略。我们需要一个更好的量化投资策略。我们的策略将是：把前两类风险分散掉，只留下市场风险敞口。现在从根本上说，如果我们——

**04:30** · neutralize all components of risk then we wouldn't be assuming any risk and in the finance literature we would assume that we are earning some sort of risk-free rate it's essentially the equivalent of just buying a US Treasury

> ——把所有风险成分都中和掉，那我们就不会承担任何风险，而在金融文献里，这相当于我们赚取某种无风险利率（risk-free rate）——本质上等同于直接买入美国国债——

**04:43** · so that's not our goal here we are trying to run some sort of Quant investing strategy so we want some risk exposure but like I said earlier we don't want unnecessary risk exposure so here what we're going to do is we're

> ——所以那并不是我们的目标。我们是要运行某种量化投资策略，因此我们想要一些风险敞口，但正如我之前所说，我们不想要不必要的风险敞口。所以在这里我们要做的，是——

**04:56** · going to look to diversify away these components of risk the idiosyncratic industry risk leaving us only with the market risk let's take a look now at some charts that's going to illustrate this fundamental idea of

> ——设法把这些风险成分——特异风险和行业风险——分散掉，只留下市场风险。现在让我们看一些图表，它们将阐明分散化这个基本理念——

**05:09** · diversification and how we can go about building a diversified Equity portfolio I've written some code to help us understand this diversification strategy and what goes into selection what we have here is 30 Equity pric paths all of

> ——以及我们如何着手构建一个多元化的股票投资组合。我写了一些代码，帮助我们理解这种分散化策略以及选股时需要考虑的因素。我们这里有 30 条股票价格路径（price path），所有这些——

**05:24** · these price paths are going to exhibit a drift of 7% but they're also going to have 20% annualized volatility that volatility is a shock to the expected return based on different facets of risk exposure now the volatility itself in

> ——价格路径都会呈现 7% 的漂移（drift），但它们也会有 20% 的年化波动率（volatility）。这个波动率，是基于不同风险敞口面对预期收益产生的冲击。现在，波动率本身——

**05:41** · this context is not necessarily just the market risk but also the industry and idiosyncratic risk there is some correlation component here among the randomness that I've baked into this simulation but we'll focus a little bit

> ——在这个语境下，并不仅仅代表市场风险，还包括行业风险和特异风险。在我写进这个模拟的随机性当中，还有一些相关性成分。但我们先把注意力稍微——

**05:57** · on the bigger picture before narrow back into what that means for selection in our portfolio if you take a look at this picture I have 30 Equity price paths now according to my simulation the average drift or return for any stock in this

> ——放在更大的画面上，然后再收窄回这对组合选股意味着什么。如果你看这幅图：我有 30 条股票价格路径。根据我的模拟，这个组合中任何一只股票的平均漂移或收益——

**06:13** · portfolio is 7% each stock starts at 100 and you'll notice that not every stock ends at 107 it's because that return is expected or on average some stocks Finish Well above Maybe they did well

> ——是 7%。每只股票都从 100 起步，你会注意到并非每只股票都收在 107。这是因为那个收益是"预期的"或者说"平均而言的"。有些股票收得远高于 107——也许它们在——

**06:30** · idiosyncratically or via their industry maybe they did poorly via that idiosyncratic or industry component we don't necessarily know where any of the equities are going to be however what we do know is that average return that I

> ——特异层面或行业层面表现得很好；也许它们因为在特异或行业成分上表现不佳而收得很差。我们无法确切知道任何一只股票会落在哪里。然而，我们确实知道的是，我——

**06:45** · have baked into my simulation is roughly 7% now that 7% you can kind of look at that as a market return that is you know if the market does well in a given year we expect a positive return and what we can do to exposure to just that market

> ——写进模拟里的平均收益大约是 7%。现在，你可以把这个 7% 大体看作市场收益。也就是说，如果市场在某个年份表现良好，我们预期获得正收益。而我们要获得只针对那个市场收益的敞口，所能做的——

**07:02** · return is invest in a well Diversified selection of equities and then if we take the average return at the end of the year yes some may underperform some may overperform but on average we will get exposure to just that market return

> ——就是投资于一个经过良好分散化挑选的股票组合。然后，如果我们在年底取平均收益——没错，有些股票可能跑输，有些可能跑赢——但平均而言，我们只会获得对市场收益本身的敞口——

**07:17** · component so this one stock that did the worst of the bunch is not going to weigh down our portfolio however on the flip side this one stock that did astronomically well will not bring our portfolio value up as significantly as

> ——成分。所以，那一只表现最差的股票不会拖累我们的组合；反过来说，那一只表现极其出色的股票，也不会像我们孤注一掷于那一个篮子时那样，把组合价值抬得那么高。

**07:33** · it would if we had all of our eggs in that one basket so what does the overall portfolio value look like so these are the individual equities in our portfolio but if I run this cell here we can see the value of our equally weighted

> 那么，整体组合的价值看起来是什么样呢？这些是我们组合中的单只股票，但如果我运行一下这个单元格，我们就能看到我们的等权（equally weighted）——

**07:46** · portfolio over time that is if I have say $30,000 to invest and I have 30 stocks I allocate $11,000 to each one of those stocks that creates an equally weighted portfol folio and this is the value of that portfolio over time you'll

> ——组合随时间变化的价值。也就是说，如果我有 3 万美元要投资，并且我有 30 只股票，我给每只股票分配 1000 美元，这就构成了一个等权组合。这就是该组合随时间变化的价值。你会——

**08:03** · notice from the original chart that we just looked at some outperformed some underperformed but we expected a 7% return on average that's exactly what we get here we're essentially diversifying away all the components of the industry

> ——注意到：在我们刚看过的原始图表中，有些股票跑赢、有些跑输，但我们预期平均 7% 的收益——我们在这里得到的恰好就是它。我们本质上是在分散掉所有行业——

**08:19** · and idiosyncratic risk that is the stocks that did extremely well and the stocks that didn't do so well maybe underperformed or lost money in a given year were Diversified buying away those two facets of risk and we're just going

> ——和特异风险成分。也就是说，那些表现极好的股票，以及那些表现不太好、可能在某个年份跑输或亏钱的股票，都被分散化了——通过分散买入，我们消除了那两类风险，我们只会——

**08:31** · to be left with the market component so here we can say that the market maybe returned roughly 7% and this is going to be the proxy for how we can expect our portfolio to perform over time because we are not looking to make crazy bets

> ——剩下市场成分。所以在这里我们可以说，市场大概回报了 7% 左右，而这将是我们预期组合随时间表现如何的代理指标，因为我们不是要下疯狂的赌注——

**08:49** · and pick stocks we are looking to just accumulate wealth and to do this we're going to try to diversify away as much risk as we can but we're not going to be riskless if you want to be entirely riskless then you can go invest in

> ——和选股，我们只是想积累财富。为了做到这一点，我们将尽可能分散掉多的风险，但我们不会做到无风险。如果你想完全无风险，那你可以去投资——

**09:02** · treasuries here we're maintaining Market risk exposure and we're trying to accumulate this positive Market drift over time diversifying away idiosyncratic and Industry risk leaving us only with Market risk exposure does

> ——国债。在这里，我们保持市场风险敞口，并试图随时间积累这种正向的市场漂移，分散掉特异风险和行业风险，只留下市场风险敞口。这——

**09:17** · not ensure that we will make money in the previous example there was a overall positive drift associated with the return for each of those equities that is the market did well that year in this setting I have the flip side I have the

> ——并不能保证我们一定会赚钱。在之前的例子里，每只股票的收益都关联着一个整体为正的漂移，也就是说市场那一年表现良好。在这个设定里，我放了相反的情况——我让——

**09:34** · market is doing poorly so if we scroll down and take a look at the simulation you'll see that on average everything is tending around the initial entry price and generating negative returns if you take a look some are actually

> ——市场表现不佳。所以如果我们往下滚动，看一下这个模拟，你会看到平均而言一切都围绕初始进场价格波动，并产生负收益。如果你仔细看，有些实际上——

**09:48** · outperforming right we have this Green Path Orange Path maybe this this blue and pink path are actually generating roughly 20% but remember we are diversifying away the facets of industry and

> ——正在跑赢，对吧？我们有这条绿色路径、橙色路径，也许这条蓝色和粉色路径实际上产生了大约 20% 的收益。但请记住，我们正在分散掉行业和——

**10:00** · idiosyncratic risk meaning that not one particular stock in our portfolio is going to be responsible for carrying positive returns or negative returns we are equally waiting this portfolio of 30 equities and we're going to be looking

> ——特异风险这两个维度，这意味着我们组合中不会有一只特定的股票来承担正收益或负收益的责任。我们给这 30 只股票等权配置，我们将去看——

**10:15** · at the average performance at the end of the year and that's going to be the return that we expect for our portfolio in this case you would expect it to accumulate roughly a NE 7% return and that's exactly what we have here so just

> ——年底的平均表现，那将是我们对组合的预期收益。在这种情况下，你会预期组合大致积累负 7% 的收益，而我们在这里得到的恰好就是它。所以，仅仅——

**10:30** · because we have only Market risk exposure by implementing this diversification strategy it does not mean we will make money on average however if the market drift component tends to be positive then we can

> ——因为我们通过实施这种分散化策略只保有市场风险敞口，并不意味着我们平均会赚钱。然而，如果市场漂移成分倾向于为正，那么我们就能——

**10:44** · accumulate that positive drift over time accumulate that wealth and this is exactly what we've seen historically otherwise nobody would be interested in investing in the US Stock Market having discussed different elements of our

> ——随时间积累那种正向漂移、积累那份财富，而这正是我们在历史上看到的情况。否则，就不会有人对美国股市感兴趣了。在讨论了我们的——

**10:58** · portfolio risk and the idea of the investment strategy diversifying away the first two components of our portfolio risk to try to accumulate this Market return over time I want to talk about the role of correlation and how

> ——投资组合风险的不同要素，以及"分散掉前两类组合风险、试图随时间积累市场收益"这一投资策略思想之后，我想谈谈相关性的作用，以及它——

**11:12** · this plays into selection in this sort of Quant investing strategy and this is really what makes it you know a a quantitative investing strategy I want to talk about the financial mathematics but I also don't

> ——如何影响这种量化投资策略中的选股。而这正是让它成为量化投资策略的关键所在。我想讲讲其中的金融数学，但我也不想——

**11:24** · want to get too far in the weeds so to do that we're going to look at some very simple examp examp of correlation we're going to talk about the idea of a statistic and a statistic changing over time then we're going to look at some

> ——陷得太深、走得太远。为了做到这一点，我们将看一些非常简单的相关性例子。我们会讨论"统计量"（statistic）这个概念，以及一个统计量如何随时间变化，然后我们再看一些——

**11:36** · real life examples using the portfolio visualization tool which I will link in the description below generally speaking we want to pick equities that are inversely correlated with one another that is as one Equity goes up the other

> ——使用 Portfolio Visualizer 工具（我会在下方描述里给出链接）的真实案例。一般来说，我们希望挑选彼此呈负相关（inversely correlated）的股票——也就是当一只股票上涨时，另一只——

**11:51** · one tends to go down this can even look like having a relatively neutral correlation as both equities are also going to exhibit bit positive returns from that market component over time or at least we would hope that they

> ——往往倾向于下跌。这甚至也可以表现为相对中性（neutral）的相关性，因为随着时间的推移，两只股票也都将表现出来自市场成分的一些正收益——或者至少我们希望它们如此——

**12:04** · do but what is the issue with measuring correlation in the real world well there's two cases and I want to show you what both may look like so here what I have is I have a simulation where I fix the correlation to be roughly 0.5 that

> ——。但在现实世界中，度量相关性有什么问题呢？这里有两种情况，我想向你展示两者可能的样子。我这里有一个模拟，我把相关性固定为大约 0.5，也——

**12:21** · is on average when one asset moves up the other one tends to move up relative to that one by 05 that increment what does it look like in a chart well it look something like this we have asset one which is you know trending down a

> ——就是说，平均而言，当一个资产上涨时，另一个资产相对于它倾向于上涨 0.5 那个增量。这在图表上看起来是什么样呢？看起来就像这样：我们有资产一，它在一点——

**12:35** · little bit and then it starts to rebound and we have asset 2 which is kind of just moving sideways but you can see that the moves at any point in time are relatively correlated to one another this kind of looks like an imprint this

> ——点下跌，然后开始反弹；还有资产二，它基本上是横盘震荡。但你可以看到，在任何时间点，两者的波动都相对相关。这看起来有点像一种印记——这条——

**12:47** · blue one of the orange one and vice versa that's because there's some positive correlation there we expect that when there is a given move in one of the assets that the other one moves in the similar capacity but by 50%

> ——蓝色路径映着橙色路径，反之亦然。这是因为其中存在某种正相关：我们预期，当一个资产出现某个给定的波动时，另一个资产会以类似的方式、但按 50% 的比例——

**13:01** · having a positive correlation means they tend to move in the same way if I were to make it a negative correlation these would be mirror images of each other given everything we've discussed about this diversification strategy should be

> ——波动。正相关意味着它们倾向于朝相同的方向运动；如果我把它改成负相关，这两条线就会互为镜像。考虑到我们讨论过的关于分散化策略的一切，它应该——

**13:15** · easy to implement right we just go about finding equities that are reminiscent of this 30 stock Equity portfolio that exhibit these types of pairwise correlations with one another and we can go about accumulating this positive

> ——很容易实施，对吧？我们只需要去寻找那些与这个 30 只股票组合类似的、彼此呈现出这类两两相关性（pairwise correlation）的股票，然后我们就可以着手积累这种正向的——

**13:30** · Market return over time well it's not quite that simple and that's because in this simulation and the the simulation before what I've done is I've fixed this correlation coefficient so I've fixed the correlation coefficient to be

> ——市场收益了。嗯，事情并没有那么简单。原因在于，在这个模拟和之前的模拟里，我所做的是把相关系数（correlation coefficient）固定下来——我把相关系数固定为——

**13:47** · 0.5 in real life equities don't have a constant correlation with other equities they're pairwise correlations that is their tendency to move together or away from each other over time changes over time I've built another simulation here

> ——0.5。在现实生活中，股票与其他股票的相关系数并不是恒定的——它们的两两相关性，也就是它们随时间一起移动或彼此背离的倾向，会随时间变化。我在这里又构建了一个模拟——

**14:03** · to visualize this and we're also going to look at some real examples in a moment here you can see these two paths do exhibit some sort of correlation with one another but over time you can see they tend to be more correlated in their

> ——来可视化这一点，稍后我们也会看一些真实例子。在这里，你可以看到这两条路径确实表现出某种彼此的相关性，但随着时间推移，你可以看到它们在某些时期——

**14:17** · movements at some periods more than others and that's exactly what this time variating correlation coefficient is indicative of so if we compute this correlation over time you can see the average is roughly 7 or 70% but it

> ——的波动上比其他时期更相关。这正是这种时变（time-varying）相关系数所指示的。所以，如果我们随时间计算这个相关性，你可以看到平均值大约是 7，也就是 70%，但它——

**14:32** · shoots up closer to 80 it goes down to 60 so over time the correlation is changing now there's nothing that says that this correlation also has to be stationary which means you can see it kind of revolves around this 70%

> ——会飙到接近 80，也会降到 60。所以随时间推移，相关性是在变化的。而且，没有任何规定说这个相关性必须平稳（stationary）——也就是说，你可以看到它大致围绕着这个 70%——

**14:49** · correlation so on average we expect these assets to move together in a correlation coefficient of of roughly 7 but if we look at another another example here you can take a look at this time variant correlation where there's

> ——在波动，所以平均而言，我们预期这些资产以大约 0.7 的相关系数一起移动。但如果我们看另一个例子，你可以看到这种时变相关性中——

**15:03** · this non-stationarity in in the correlation coefficient and we have asset one drifting further and further away from asset 2 um even though over time the correlation coefficient is actually

> ——存在着非平稳性（non-stationarity）：资产一与资产二之间漂移得越来越远——嗯，尽管随着时间推移，相关系数实际上——

**15:15** · increasing so just because we have this measure of correlation it does not mean it is constant over time in fact it is always changing every single day and it's going to depend how you compute the Cor ation coefficient with respect to

> ——在增加。所以，仅仅因为我们有这个相关性度量，并不意味着它随时间恒定。事实上，它每天都在变化，而且它取决于你如何计算相关系数——相对于——

**15:31** · daily return monthly return annual return and we're going to take a look at a moment of some examples of real Equity correlations over time but this is what makes this a quantitative investing strategy you have to consider these

> ——日收益（daily return）、月收益（monthly return）还是年收益（annual return）。稍后我们会看一些真实股票相关性随时间变化的例子。但这正是让这成为量化投资策略的原因：你必须考虑这些——

**15:44** · correlations these correlations of equities in your portfolio how they evolve over time and you also have to consider different elements of rebalancing in your equally weighted portfolio just as an anecdotal example

> ——相关性，即组合中股票彼此的相关性如何随时间演变；你还必须考虑等权组合中再平衡（rebalancing）的各个要素。举个例子——

**15:58** · another consideration is let's say that I had two stocks in my portfolio I have Nvidia and I have Sigma let's say I put $100 into Sigma $100 into Nvidia next year Nvidia doubles okay that's pretty good I made

> ——另一个考虑是：假设我的组合里有两只股票，英伟达和 Sigma。假设我给 Sigma 投 100 美元，给英伟达投 100 美元。第二年英伟达翻倍了——不错，我赚了——

**16:15** · 150 bucks all right let's say siga stays the same now I don't have an equally weighted portfolio anymore so I have to go and I have to rebalance that portfolio so it's very important that you understand that just because

> ——150 美元。好吧，假设 Sigma 保持不变。现在我拥有的就不再是等权组合了，所以我必须去对这个组合进行再平衡。所以，你非常重要的一点是要明白：仅仅因为——

**16:32** · this whole idea of diversification and this quantitative investing strategy diversifying away the two components of uh of risk we talked about in an equity portfolio the idiosyncratic and Industry risk uh exists does not mean that it is

> ——分散化这套理念，以及这个"分散掉我们谈过的股票组合中两类风险成分（特异风险和行业风险）"的量化投资策略——它的存在，并不意味着它就是——

**16:45** · a set and forget in fact that's what makes this more of a quantitative investing strategy than just a blanket you know Buy and Hold the market portfolio strategy you are essentially determining you're twisting the knobs

> ——一劳永逸（set and forget）的。事实上，正是这一点，让它更像一个量化投资策略，而不只是"买入并持有市场组合"（buy and hold the market portfolio）这样一刀切的策略。你本质上是在决定——你是在转动旋钮——

**17:00** · based on the equities you select of how much adios sycratic industry and Market exposure your portfolio is going to have and that's going to be based on the equities that you select and the amount of money you put into each equity in

> ——根据你所选择的股票，来决定你的组合将会有多少特异风险、行业风险和市场风险的敞口。而这将取决于你选择的股票，以及你在组合中投入每只股票的金额——

**17:13** · that portfolio given all of this you're going to want to select Assets in that portfolio or equities in that portfolio that have a net neutral or negative correlation with one another such that

> ——。考虑到这一切，你会希望在组合中挑选那些彼此净中性（net neutral）或负相关的资产或股票，这样一来——

**17:26** · you know you can diversify away those idiosyncratic and components the overall pairwise correlation the average pairwise correlation of equities in your portfolio may be a reasonable measure of

> ——你就能分散掉那些特异和行业成分。组合中股票的整体两两相关性——平均两两相关性——可能是衡量——

**17:37** · how Diversified your portfolio is and of course you can take a look at your overall portfolio beta to see what it actually looks like relative to the market return rebalancing and capm are topics for another day what I want to do

> ——你的组合有多分散化的一个合理度量。当然，你也可以看看你组合的整体贝塔（beta），看看它相对市场收益实际上是什么样子。再平衡和资本资产定价模型（CAPM）是改天再谈的话题。我现在想做的——

**17:51** · now is talk about some real world correlations we're going to do this on portfolio visualizer so you can head on over to Port portfolio visualizer decom go to their correlation tool and you can enter some Equity tickers here to get

> 是讨论一些现实世界中的相关性。我们将在 Portfolio Visualizer 上做这件事。你可以前往 portfoliovisualizer.com，进入他们的相关性工具，输入一些股票代码（ticker），然后——

**18:04** · started and it's going to show you the pairwise correlations between the asset price paths here what I've done is I've entered Johnson and Johnson and chipotle to seemingly unrelated stocks and we're going to take a look at their

> ——启动这个工具，它会显示资产价格路径之间的两两相关性。在这里，我输入了强生（Johnson & Johnson）和 Chipotle——两只看似毫无关联的股票——我们将看看它们的——

**18:18** · correlation coefficient to see if we can confirm this idea so if we go on down here to the asset correlations Matrix you can see that relative to its own price path each price path will have a perfect correlation this makes sense

> ——相关系数，看看我们能否证实这个想法。如果我们往下看，到资产相关性矩阵（asset correlations matrix），你会看到，相对于它自身的价格路径，每条价格路径都会有完美的相关性。这很合理——

**18:33** · because if you compare the same price path with itself then they should move perfectly together but if you compare a price path to a different price path so in this case it's Johnson and Johnson relative to Chipotle we have a

> ——因为如果你拿同一条价格路径和它自己比较，那么它们应当完全同步地移动。但如果你拿一条价格路径和另一条不同的价格路径比较——在这个例子里是强生相对于 Chipotle——我们得到的是——

**18:49** · 01 correlation so .1% correlation seemingly no correlation between the two Price p this could be a reasonable candidate to include in a well Diversified portfolio

> ——0.1 的相关性，也就是 0.1% 的相关性——两条价格路径之间看起来毫无相关性。这可以成为一个合理的候选，纳入一个充分分散化的组合中——

**19:03** · but keep in mind this is just for the annual return what if we look at the monthly returns well there's not just one way to compute a monthly return you can do it on a rolling basis so let's look at the 12-month rolling correlation

> ——但要记住，这只是针对年收益的。如果我们看月收益呢？嗯，计算月收益并不只有一种方式，你可以用滚动（rolling）的方式来做。所以我们来看看 12 个月滚动相关性——

**19:15** · here we get the correlation coefficient over time so that 0.001 changed to 0.13 here on average and this is going to be the path of the correlation coefficient over time this is this is exactly what I was showing you here this is an example

> ——在这里我们得到随时间变化的相关系数。所以那个 0.001 变成了平均 0.13，而这将是相关系数随时间变化的路径。这正是我刚才向你展示的东西——这是一个——

**19:32** · of a relatively stationary correlation coefficient we can draw this horizontal line here and you can see on average there's a tendency for this correlation to stick around 7 there is no natural tendency for the

> ——相对平稳（stationary）的相关系数的例子。我们可以在这里画一条水平线，你可以看到平均而言这个相关性倾向于保持在 7 左右。对于任何股票来说，相关性都没有一个自然的倾向——

**19:46** · correlation to stick around any value for any Equity this is what the 12-month rolling correlation coefficient looks like for this Equity pair you have to keep this in mind as you build your portfolio the correlations between your

> ——要停留在某个值上。这就是这对股票 12 个月滚动相关系数看起来的样子。在构建你的组合时，你必须牢记这一点：你的股票之间的相关性——

**20:02** · equities will change over time this is with monthly returns look at Daily returns it's completely different this may look a little bit more stationary kind of hovering around this like0 2 here but there are periods where there

> ——会随时间变化。这是用月收益算的；看看日收益——那完全不同。这看起来可能更平稳一些，大致徘徊在这个 0.2 附近，但也存在一些时期——

**20:14** · is negative correlation where there's significant correlation look 7 it's pretty remarkable so you have to keep all of this in mind this is the 60 60-day rolling correlation if we go to 120 days this is what it looks like kind

> ——相关性为负，也有一些时期相关性显著——看，0.7，相当惊人。所以你必须把这一切都记在心里。这是 60 天滚动相关性；如果我们换成 120 天，它看起来就是这样，有点——

**20:28** · of smooth it out a little bit if we go to 20 days it'll probably be even noisier look something like this this may be a little bit more I don't even know if this would be centered around zero it's kind of got this positive

> ——把它平滑了一点。如果我们换成 20 天，它可能会更嘈杂，看起来像这样。这个可能更——我甚至不知道它会不会以零为中心，它带着某种正的——

**20:40** · almost uh cyclical nature to it here but regardless we're not analyzing this this time series I'm simply trying to show you that this statistic correlation is a statistic that is time varying it changes over time and even though this

> ——近乎周期的性质。但不管怎样，我们不是在分析这个时间序列。我只是想向你展示：相关性这个统计量，是一个随时间变化的统计量，它会随时间改变。而且即使这对——

**20:54** · Equity pair is seemingly unrelated if we go to the 60-day correlation you can see at some points the correlation was 7 here it was I think this was even 735 that's a significantly High correlation between two seemingly unrelated equities

> ——股票看起来毫无关联，如果我们去看 60 天相关性，你会看到在某些时间点相关性达到了 0.7，在这里，我记得这甚至到了 0.735——两只看似无关的股票之间竟有这么高的相关性——

**21:12** · on that particular uh set of days so important to understand that the correlation coefficient is a means for implementing this type of quantitative investing strategy that is you can look at the you know overall portfolio beta

> ——就发生在那一组特定的日子里。所以，重要的是要理解：相关系数是实施这类量化投资策略的一种工具。也就是说，你可以看组合的整体贝塔——

**21:26** · like I had mentioned earlier or you can even look at the average pairwise correlation between equities and your portfolio but you have to acknowledge the window in which you are doing that because they will change over time here

> ——就像我之前提到的，或者你甚至可以看组合中股票之间的平均两两相关性。但你必须意识到你是在哪个窗口期内做这件事的，因为它们会随时间变化。在这里——

**21:38** · the daily average is17 that's quite different from .13 which is quite different from 01 okay so these are two seemingly unrelated equities what about two seemingly related equities here I have

> ——日频的平均值是 0.17，这和 0.13 差别很大，和 0.1 差别就更大了。好了，所以这是两只看似无关的股票。那两只看似相关的股票呢？在这里我有——

**21:54** · the annual return of apple and Amazon and this is quite a high correlation something that we might expect because both of them are in the technology sector we have 0.52 that is quite a high correlation

> ——苹果（Apple）和亚马逊（Amazon）的年收益，这是一个相当高的相关性——这是我们可能会预料到的，因为它们都处在科技板块。我们得到 0.52，这是相当高的相关性——

**22:06** · that's exactly actually the correlation that I used in generating this example here so this is a real world example of this implementation this this implementation that was generated with a constant correlation coefficient this is

> ——这实际上正是我生成这个例子时所使用的相关性。所以这是一个真实世界中"固定相关系数实现"的例子——这个用恒定相关系数生成的实现，这就是——

**22:21** · the annual return correlation coefficient which is 0.52 again if we go to monthly this is going to change so this is 31 in a monthly capacity and this is the correlation over time if we take a look at the daily correlation

> ——年收益相关系数，也就是 0.52。如果我们换成月频，这又会变化：月频下是 0.31，这是相关性随时间的变化。如果我们看日频相关性——

**22:34** · that will also be different you can see it's kind of exhibiting that sort of cyclical nature as well to some to some degree I would say um but it it's not stationary right it's not it doesn't look like it's being drawn around a a

> ——那也会不同。你可以看到它在某种程度上也表现出那种周期性，我会说有一定程度吧，但它是非平稳的，对吧？它看起来并不像是围绕某个——

**22:50** · central value like like this one it's really evolving over time and that is a consideration you have to make when you're deploying this type of investment strategy is you know these are just considerations in general anytime you

> ——中心值在波动，就像之前那个一样。它真的在随时间演变。而当你在部署这类投资策略时，这就是你必须做的一个考虑。你要知道，这些只是一般意义上的考虑——任何时候你——

**23:04** · involve yourself with an equity portfolio is you know how do your equities play with one another how do that those relationships evolve over time and do you need to rebalance your portfolio to ensure that you have the

> ——只要参与股票组合，就会遇到：你的股票彼此之间如何互动？这些关系如何随时间演变？你是否需要再平衡你的组合，以确保你拥有——

**23:18** · exposure that you think you have because you know just with that Sigma Nvidia example I gave earlier in a given year if one stock explodes all of a sudden you don't have the same risk profile that you did at the start of the year so

> ——你以为自己拥有的敞口？因为正如我早些时候举的 Sigma 和英伟达的例子：在某个年份里，如果一只股票突然暴涨，你就不再拥有年初时那样的风险状况了。所以——

**23:33** · all of those are considerations in this overall quantitative investing strategy and that is going to do it for this video on Quant investing strategies for beginners this strategy is about trying to accumulate the positive drift

> ——所有这些，都是这个整体量化投资策略中的考量。那么，关于"面向初学者的量化投资策略"这期视频，到这里就讲完了。这个策略，就是要设法积累——

**23:49** · associated with market returns over time by diversifying away the different elements of risk associated with your Equity portfolio mainly the idiosyncratic and Industry risk of course this is no guarantee of a

> ——与市场收益相关的正向漂移——通过分散掉你的股票组合所关联的不同风险成分，主要是特异风险和行业风险。当然，这并不能保证——

**24:03** · positive return but this will reduce your overall exposure to Crazy gains and crazy losses and we would hope that over time if you bet on the US economy that you will be able to accumulate wealth that being said I hope you

> ——获得正收益，但这会降低你对疯狂上涨和疯狂下跌的整体敞口。而且我们希望，随着时间推移，如果你押注美国经济，你就能积累财富。话虽如此，我希望你——

**24:18** · enjoyed this video thank you so much for watching and I will see you in the next one

> ——喜欢这期视频。非常感谢你们的观看，我们下期再见。
