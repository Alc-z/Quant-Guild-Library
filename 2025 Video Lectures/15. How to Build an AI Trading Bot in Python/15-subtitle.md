---
title: "How to Build an AI Trading Bot in Python"
source: "https://www.youtube.com/watch?v=_87QHZXOOKA"
author:
  - "[[Roman Paolucci]]"
published: 2025-04-18
created: 2026-08-04
description: "*🚀 Master Quantitative Skills with Quant Guild*https://quantguild.com*📈 Interactive Brokers for Algorithmic Trading*https://www.interactivebrokers.com/mkt/?src=quantguildY&url=%2Fe"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=_87QHZXOOKA)

*🚀 Master Quantitative Skills with Quant Guild*
https://quantguild.com

*📈 Interactive Brokers for Algorithmic Trading*
https://www.interactivebrokers.com/mkt/?src=quantguildY&url=%2Fen%2Fwhyib%2Foverview.php

*👾 Join the Quant Guild Discord server here*
https://discord.com/invite/MJ4FU2c6c3
___________________________________________
Project:
https://github.com/romanmichaelpaolucci/AI_Trading_Bot

Alpaca:
https://app.alpaca.markets/account/login

OpenAI:
https://platform.openai.com/api-keys
___________________________________________
Articles and code walkthroughs can be found on our blog
https://medium.com/quant-guild
https://romanmichaelpaolucci.medium.com/

For more free tutorials and references see our GitHub
https://github.com/RomanMichaelPaolucci
https://github.com/Quant-Guild

## Transcript

**00:01** · [Music] in this video we're going to walk through building an AI trading bot I've put together this to-do list of basic steps that we're going to walk through in Python we're going to start by

> 在本视频中，我们将一步步搭建一个 AI 交易机器人（AI trading bot）。我准备了一份基础步骤的待办清单，我们会用 Python 逐一走一遍。首先，我们要——

**00:13** · building a basic user interface for trading a space where we can Define which equities we would like to trade our Max position size different parameters for our strategy the second step is going to be to establish a

> ——搭建一个基础的交易用户界面（user interface），在其中我们可以定义想交易的股票（equities）、最大仓位规模（max position size），以及策略的各种参数。第二步是建立——

**00:29** · connection to some sort of of brokerage via an API in this case we're going to be using alpaca it's quite easy to use of course you can substitute this for any you would like step three will be to develop a strategy in this case we're

> ——通过 API 连接到某种券商（brokerage）。这里我们用的是 Alpaca，它非常好用；当然你也可以换成任何你想要的券商。第三步是开发策略，在这个例子里我们——

**00:42** · going to be looking at a Martingale DCA sort of style strategy where as an equity dips from our initial entry price we will continue to increase our position size we will integrate an llm this is

> ——要研究一种马丁格尔-定投（Martingale DCA，即平均成本法）风格的策略：当股票从我们的初始入场价（entry price）下跌时，我们会持续增加仓位规模。我们还会集成一个大型语言模型（LLM），这就是——

**00:56** · the AI component so we're not using an AI for any sort of signal analysis of course you could in step three but this is going to be for position management we can ask our llm about our risk exposure

> ——AI 的部分。我们并不是用 AI 做任何信号分析（当然第三步里你也可以这么做），这里它是用来做仓位管理的：我们可以向 LLM 询问我们的风险敞口（risk exposure）之类的问题。

**01:14** · things of that nature and of course step five is going to be to deploy that is to just essentially run this whole system we're going to walk through each of these steps together but I will also post the entire project on my GitHub if

> 诸如此类。当然，第五步就是部署（deploy），也就是真正把整套系统跑起来。我们会一起走完每一步，但我也把整个项目发布到了我的 GitHub 上，如果你感兴趣——

**01:29** · you're interested I will leave a link in the description below all right let's get started with step one here I'm going to go ahead and create a new python script this is a pretty small trading bot so I'm just going to call this bot.

> ——我会在下方描述里留下链接。好了，我们开始第一步。这里我要创建一个新的 Python 脚本。这是一个相当小的交易机器人，所以我打算就把它叫做 bot.py。

**01:41** · py and we should be able to write everything in here to get started we're going to need to import some packages I have some notes Here on the necessary steps to building this GUI so we're going to go

> 我们应该能在这里写进全部内容。开始之前，我们需要导入一些包。我这里有关于构建这个 GUI（图形用户界面）所需步骤的笔记，所以我们要——

**01:54** · through this together and I'm going to talk about each step so first we're going to import TK enter as TK that's going to let us build this user interface we're going to import some other things from tter we're

> ——一起走一遍，我会逐一讲解每一步。首先，我们要 `import tkinter as tk`，它会让我们构建这个用户界面。我们还要从 tkinter 导入一些别的东西。我们——

**02:09** · also going to import Json and I'll explain why in a moment we're also going to import time import threading this is going to be important for updating our user interface and then we're also going to import random that should be

> ——还要导入 `json`（稍后我会解释为什么）。我们还要导入 `time`、`threading`——这对更新用户界面很重要——然后还要导入 `random`。这些应该就是——

**02:25** · everything that we need to get started one of the first things that we need to do is we need to create a file to save and load data from this makes sense right if I close the trading system and I reopen it it better know

> ——我们需要的一切，足以开始了。我们要做的第一件事之一，就是创建一个用于保存和加载数据的文件。这很合理，对吧？如果我关闭交易系统再重新打开，它最好还记得——

**02:40** · what equities I'm trading and the levels that I'm trading them at so that's exactly what we're going to do we're going to create a new file we're going to call it data file and this is going to be equal to I'm going to call it

> ——我在交易哪些股票、在哪些价位交易。所以这正是我们要做的：创建一个新文件，我们把它叫做 data file，它等于——我打算把它命名为——

**02:52** · equities do Json and this is essentially just going to store the the symbols that we're trading so app Apple Amazon for example and then the levels that we're trading at so it's going to record our active positions it's going to record

> equities.json，它本质上只是用来存储我们正在交易的标的代码——比如 Apple、Amazon——以及我们交易的价位。它会记录我们的活跃持仓（active positions），还会记录——

**03:08** · the entry price and it's going to record the prices that we want to enter at below our initial entry price following that sort of Martingale DCA style strategy now what we're going to do is we're going to create some mock

> ——入场价，以及我们想按照那种马丁格尔-定投（Martingale DCA）策略、在初始入场价下方继续买入的价位。接下来我们要做的是创建一些模拟（mock）——

**03:21** · functions that we're going to populate later we'll call this fch mock API for a symbol and for now we're just going to return just a price as a dictionary so we'll call this price and

> ——函数，稍后我们会用真实 API 把它们填上。我们把它叫做 `fetch_mock_api`：给它一个标的代码，目前我们只是返回一个以价格为键的字典。我们把它叫做 `price`，——

**03:39** · I'll say maybe 100 for now def mock GPT response this is going to be a mock message from our Ai and it's going to look something like this we're just going to return a string with a mock message and we're going to populate

> ——现在先让它返回 100 好了。`def mock_gpt_response`——这会是我们 AI 发来的一条模拟消息，看起来就像这样：我们只是返回一个包含模拟消息的字符串。稍后我们会用真实的——

**03:59** · those with our apis later on now we have to go about building the trading bot class what I'm going to do is I'm going to call this trading bot GUI bot in lowercase I'm going to create a

> ——API 调用把这些函数填上。现在我们开始构建交易机器人这个类。我打算把它命名为 `TradingBotGUI`（小写的 bot）。我要创建一个——

**04:16** · Constructor I'm going to give it a root window since we're using TK enter so this automatically populated for me I'm going to do self. root is equal to root the title is going to be AI trading bot and we don't have these functions so

> ——构造函数（constructor）。因为用的是 tkinter，我会给它一个根窗口（root window），所以这里会自动补全。我写 `self.root = root`，标题（title）设为"AI trading bot"。我们还没有这些函数，所以——

**04:32** · instead we're going to say self. equities is equal to self. load equities we're going to build this load equities function in a moment and this is exactly what we have this equities Json file for we need to populate the user interface

> ——我们改用 `self.equities = self.load_equities()`。稍后我们会构建这个 `load_equities` 函数。这正是我们这个 equities.json 文件的用途——我们需要用保存下来的信息来填充用户界面。

**04:47** · with our saved information essentially what we're going to do on load and close is we're going to save and load the information to and from this equities Json file that's going to do it I think for the

> 本质上，在加载和关闭时我们要做的，就是在这个 equities.json 文件之间保存和加载信息。我想构造函数这边——

**05:02** · initial Constructor we may also need a flag for whether or not a system is running so I'll leave this here for now this is pretty much telling us whether or not we are actively trading an equity

> ——就差不多可以了。我们可能还需要一个标志位（flag），用来表示某个系统是否在运行，所以这里我先把它留在这儿。它基本上告诉我们：我们是否在积极交易某只股票——

**05:19** · in the system so if I add apple to my system for example then we're going to want to be able to toggle that on and off so just because it exists in the system does doesn't mean we want to actively trade it at the different

> ——并把它纳入系统。比如，如果我把 Apple 加进我的系统，那我们会希望能把它打开或关闭。因为某只股票存在于系统中，并不意味着我们想在不同价位上积极交易它——

**05:32** · levels and that's exactly what a system flag would do we may build that into the equity data itself we'll we'll see how this actually shakes out now we need a form to add equities to our box so I'm going to say self. form

> ——而这正是系统标志位（system flag）要做的事。我们也可以把这个标志位直接做进股票数据本身，我们看看实际情况如何。现在我们需要一个表单（form）来把股票添加进我们的界面，所以我写 `self.form_`——

**05:48** · frame is equal to tk. frame and we're going to add it to that root window and then we're going to just go ahead and pack that form now we're going to go ahead and create the different labels so we're going to

> ——`frame = tk.Frame`，我们把它添加到根窗口中，然后直接把这个表单 pack 进去。接着我们创建各个标签（label），我们要——

**06:06** · do TK label self. form frame text symbol we're going to do a grid layout actually so okay good it already did it for me self. symbol label grid row 0 column Z that's good and now we need to go and add the actual form for

> `tk.Label(self.form_frame, text="Symbol:")`。我们实际上要用网格布局（grid layout）——好，它已经自动帮我写好了：`self.symbol_label.grid(row=0, column=0)`，很好。现在我们需要为它添加实际的输入框——

**06:25** · it so or we need the entry actually so this is this AI didn't actually help me all that much so we're going to do this we'll do grid row 0 column Z and then here's our entry and this is where we're going to go ahead and fill out that

> ——也就是 Entry（输入框）。嗯，这个 AI 其实没帮上太大忙，所以我们自己来：`grid(row=0, column=1)`，然后这里就是我们的输入框，我们将在这里填上——

**06:46** · symbol order partially filled looks like my trading system just filled an order with interactive brokers that's pretty cool self. symbol entry grid 01 so that is going to be for entering an equity symbol now we're going to have to

> ——股票代码。订单部分成交了——看起来我的交易系统刚刚在盈透证券（Interactive Brokers）那边成交了一笔订单，挺酷的。`self.symbol_entry.grid(row=0, column=1)`，这就是用来输入股票代码的。现在我们还得——

**07:04** · do this for the levels and draw down of our strategy so this is going to be formed to add a new Equity to our trading fot now we need a label for not quantity

> ——为策略的 levels（层数）和 drawdown（回撤）也做同样的操作。这就是用来向我们的交易机器人添加新股票的表格。现在我们需要一个标签，不是数量（quantity）——

**07:21** · but levels and the levels is going to have a new entry self out level levels entry and then we're going to do self. levels entry 11 one and then we need one for our draw

> ——而是 levels。levels 要有一个新的输入框 `self.levels_entry`，然后我们写 `self.levels_entry.grid(row=0, column=3)`。接着我们还需要一个用于 draw——

**07:37** · down so we're going to add this to row two or really this should be across the columns not rows so column zero column one column two we want them on the same row yeah this looks

> ——down（回撤）的输入框。我们把这个加到第 2 行——不过实际上应该横向跨列而不是跨行，所以是第 0 列、第 1 列、第 2 列。我们想让它们在同一行上，对，这样看起来——

**07:58** · good zer 0 1 01 no that should be two that should be two that should be three should be even should be four

> ——不错。0、1、0、1……不对，那个应该是 2，那个应该是 2，那个应该是 3，那个应该是偶数，那个应该是 4。

**08:14** · okay and then self dot we're going to do not quantity this is going to be levels no draw down percentage self. draw down entry and then one 5 all right perfect so what we just did is we created a form

> 好，然后 `self.`……我们不用数量，这里是 levels；再是回撤百分比（drawdown percentage），`self.drawdown_entry`，然后 `grid(row=0, column=5)`。完美。所以我们刚刚做的，就是创建了一个表单——

**08:35** · to add a new Equity to our trading bot this is going to be the symbol that we are going to trade this are going to be the number of levels to trade so we're going to assume a uniform position size of one you can edit this very easily on

> ——用来向交易机器人添加新股票。这里是要交易的股票代码，这里是要交易的层数。我们假设统一的仓位大小为 1，你可以非常容易地在——

**08:48** · the back end or you can add a new entry if you would like and then we're going to talk about the draw down to enter a new position at each level so that means if were trading at an entry price of 100 then if we had a draw down of 10% that's

> ——后端修改它，或者如果你愿意，也可以新增一个输入框。然后我们会讨论在每一层买入新仓位的回撤幅度：也就是说，如果我们以 100 的入场价交易，那么如果回撤设为 10%，那就是——

**09:04** · when we will enter a new position and then at another 10% drop we will enter a new position and and so on so that is going to be the idea of this trading strategy all right so now we need a table to

> ——我们买入一个新仓位的时点，然后每再下跌 10%，我们就再买入一个新仓位，以此类推。这就是这个交易策略的思路。好了，现在我们还需要一个表格（table）来——

**09:24** · track the traded equities so I'm going to say self. Tre is equal to ttk do Tree View and we're going to go ahead and show headings but our columns are going to be symbols we're going to do the position we're going to do the entry

> ——跟踪已交易的股票。所以我写 `self.tree = ttk.Treeview`，然后我们显示表头（headings）。我们的列有：Symbols（股票代码）、Position（仓位）、Entry——

**09:45** · price we will also do the levels which is going to be a dictionary and the status status may be unnecessary but regardless we have this tree View and of course we're going to show

> ——价格（price），我们还有 Levels（层数），它会是一个字典（dictionary），以及 Status（状态）——状态也许可有可无，但不管怎样，我们有了这个 Treeview，当然我们还要显示——

**10:06** · headings and now we're going to say for call in and we're going to say symbol position entry price levels and status then we are going to do self. tree. heading call text call so all we're doing is we're setting the heading to

> ——表头。然后我们写 `for col in`……我们列出 symbol、position、entry price、levels、status，然后写 `self.tree.heading(col, text=col)`。我们所做的，就是把表头设置为——

**10:27** · these column headers and we are going to say self. tree. column call we're going to make the width 120 120 should be sufficient and then we'll do self. tree. Pac and that is

> ——这些列标题，然后写 `self.tree.column(col)`，把宽度设为 120，120 应该足够了。然后我们 `self.tree.pack()`，这就是——

**10:47** · going to be where we see our current portfolio so essentially What's Happening Here is we're creating a table and in this table we have levels that we're creating each Equity at and based on our API calls we're going to update

> ——我们查看当前投资组合（portfolio）的地方。所以本质上，这里我们创建了一个表格，表格里有我们为每只股票创建的各个层级（levels），基于 API 调用我们会更新——

**11:02** · this table and we're going to update this table with our position for each relative symbol the entry price maybe the status of the order and so on and through this table we're also going to be able to toggle whether or not we are

> ——这个表格，用每个对应股票代码的仓位、入场价、也许还有订单状态等来更新它。通过这个表格，我们还能切换是否——

**11:17** · traing that particular equity and I think that's everything we need so now what we're going to do is we're going to add buttons to add and remove not just add and remove we also need to toggle equi so buttons to control the bot we're

> ——交易那特定的股票。我想这就是我们需要的一切。所以现在我们要做的是添加"添加"和"移除"按钮——不只是添加和移除，我们还需要切换（toggle）股票，也就是用来控制机器人的按钮。我们——

**11:33** · going to say self. toggle system button is equal to tk. button root we're going to add it to the main window we're going to say toggle selected system and then we're going to say the command for that button is self. toggle

> ——写 `self.toggle_system_button = tk.Button(root)`，我们把它添加到主窗口中，文本为"Toggle Selected System"，然后该按钮的命令是 `self.toggle_`——

**11:53** · system which is going to make sense we're going to say self. toggle system button we're going to pack pad y5 now we're going to add a remove button tk. button remove selected Equity

> ——`system`，这会说得通。我们写 `self.toggle_system_button.pack(pady=5)`。现在我们要添加一个移除按钮：`tk.Button`，文本为"Remove Selected Equity"——

**12:14** · we're going to make the command remove Equity or we really should make it remove selected Equity remove selected equity and we're going to make these right so we don't have we don't have the command to load

> ——我们把命令设为 remove equity，或者更确切地说，应该设为 `remove_selected_equity`。我们把这些弄对——我们还没有 load——

**12:28** · equities we don't have have or I should say we don't have the function to load equities and we don't have the functions to toggle system or remove the selected equities yet but that is what we are going to do in a moment uh we're also

> ——equities，我们还没有——或者说，我们还没有 load_equities 这个函数，也还没有 toggle_system 或 remove_selected_equity 这些函数，但这些正是我们马上要做的。我们还要——

**12:40** · going to pack the remove button and that's going to allow us to add or not add but remove from the table it's going to allow us to remove from the table okay seems that I forgot the add button so I'm just going to go ahead and

> ——把移除按钮 pack 起来，它让我们能从表格中移除（不是添加）。好，看来我忘了添加按钮，所以我就直接——

**12:56** · put that up here cuz it should be a part of the form the original form to add equities so above the table I'm going to create a new button self. add button and I'm going to say equals

> ——把它放在上面，因为它应该是添加股票那个原始表单的一部分。所以在表格上方，我要创建一个新按钮 `self.add_button`，我写 `=`——

**13:11** · TK um not self. form frame um we we could well actually in this case we would use the form frame because that's the that's the root for this particular um widget so we're going to use self

> `tk.Button`，嗯，不是 `self.form_frame`……我们，嗯，其实可以用 form frame，因为它是这个特定组件的父容器，所以我们用 `self.`——

**13:29** · form frame here notice we used Root down here because we're adding this to a different component or we're adding this to a different part of the the user interface so here we're using self. form frame because we want it to be a part of

> ——`form_frame`。注意，下面这里我们用的是 Root，因为我们要把它添加到另一个组件、或者说用户界面的另一部分。而这里我们用 `self.form_frame`，因为我们想让它成为——

**13:42** · this symbol levels draw down form adding in equity so we're going to say that and then we're going to say self. add button and then we're just going to put it on 06 so same row but the sixth column and this makes sense right so the

> ——这个 symbol / levels / drawdown 表单的一部分，用来添加股票。然后我们写 `self.add_button`，把它放到第 0 行第 6 列——同一行，但第 6 列。这很合理，对吧？所以——

**13:58** · labels are all even uh and in this this case the button to add is also even so it's going to be in line with those and then um we're also going to have the row one being the entry but offset by the odd columns so we can see the label see

> ——标签都在偶数列，而这个添加按钮也在偶数列，所以它会跟它们对齐。然后我们让输入框那行按奇数列错开排列，这样你就能看到"标签、输入框、标签、输入框"——

**14:16** · the entry see the label see the entry and of course add the equity at the end of the form then we also have our toggle system button or remove button and the tree view of all the equities in our system and that should be everything we

> ——的排布，最后当然是在表单末尾添加股票。然后我们还有切换系统按钮、移除按钮，以及系统里所有股票的 Treeview 表格。这应该就是我们需要的——

**14:30** · need now we need to actually make a interface for our AI component so what I'm going to do is I'm going to say this is the AI component I'm going to say self. chat frame is equal to tk. frame

> ——全部东西了。现在我们还需要为 AI 组件做一个界面。所以我要做的，就是……我写"this is the AI component"（注释），然后 `self.chat_frame = tk.Frame`——

**14:46** · roots and then we'll say self. chat frame we'll just pad we'll pack it and Pad y1 we need an input and this is just going to be a simple entry and we're going to add that to the chat frame and then we're also

> ——`(root)`，然后我们写 `self.chat_frame.pack(pady=10)`，把它 pack 起来。我们需要一个输入框，就是一个简单的 Entry，我们把它添加到 chat_frame 中，然后我们还要——

**15:02** · going to do self de chat input and we're not going to pack it I want to do a grid so we're going to do grid row z0 we'll have some pad on the X that should be good and then we also need a button to send the

> ——写 `self.chat_input`，我们不打算 pack 它，我要用 grid：`grid(row=0, column=0, padx=5)`，这样应该不错。然后我们还需要一个发送——

**15:20** · message send button is equal to tk. button we're going to add it to that chat Frame send we don't have the command or the function send message yet that's something we will work on and then of course we are going to

> ——消息的按钮：`send_button = tk.Button`，我们把它添加到那个 chat frame，文本为"Send"。我们还没有 send_message 这个命令/函数，那是我们接下来要做的。然后当然我们还要——

**15:34** · just pack the or we'll do grid for the button and we'll pack the chat output layout so we'll do self. send button we'll grid 01 and this is just the same idea as what we did up here with the grid

> ——对按钮用 grid 而不是 pack，然后把聊天输出的布局 pack 起来。我们写 `self.send_button.grid(row=0, column=1)`，这和上面我们做的网格布局是同一个思路——

**15:51** · layout now what we're going to do is we're going to say self. chat output is equal to tk. textt and we'll say root height is equal to five width is equal to we'll say maybe

> ——。现在我们要写 `self.chat_output = tk.Text`，然后 `root.height` 设为 5，宽度（width）设为——大概——

**16:09** · 50 60 maybe and the state is going to be tk. disabled because remember this is a response so we don't want to just be able to edit the response from the AI we want it to just read is plain text and then we're just going to pack this

> ——50、60 左右吧，状态（state）设为 `tk.DISABLED`，因为记住：这是响应内容，我们不想让你能直接编辑 AI 的回复，我们只想让它以纯文本形式展示。然后我们直接把这个——

**16:26** · output just going to pack this output okay we're going to load the saved data now so we finished building the the UI essentially and now what we want to do

> ——输出（output）pack 起来。好，现在我们要加载保存的数据。我们基本上已经完成了 UI 的构建，现在我们要做的——

**16:44** · is we want to start to get into the functionality so we're going to load save the data so we will say self. refresh table that's going to load from our Json we got to build this function as well

> ——是开始进入功能实现部分。所以我们要加载/保存数据：我们写 `self.refresh_table()`，它会从我们的 Json 中加载。这个函数我们也得构建。

**16:58** · then we're going to say self. running is equal to true and this is going to be for auto refreshing and then we have self. auto update thread is equal to threading do

> 然后我们写 `self.running = True`，这是用于自动刷新（auto-refreshing）的。接着我们有 `self.auto_update_thread = threading.Thread`——

**17:17** · thread Target is going to be self. auto update which we also have to create and then we're going to make MCH true and we're going to just go ahead and start this this thread that we've

> ——`(target=self.auto_update)`，这个函数我们也得创建。然后我们把它设为守护线程（daemon），直接启动这个我们——

**17:36** · created right here this will allow us to query the updates in a continuous fashion so on some sort of you know time increment maybe it's 5 seconds or something which is why we imported time earlier so

> ——创建的线程。这将让我们能以连续的方式查询更新，比如每隔某个时间增量——也许 5 秒什么的——这就是我们之前导入 time 的原因。所以——

**17:51** · that's just going to be for auto refreshing the table with data from our API now we actually need to create the functions that we've used earlier to say add Equity save and so on let's start by creating a function to add an equity so

> ——这只是为了用 API 的数据自动刷新表格。现在我们需要创建之前用到的那些函数，比如 add_equity、save 等等。我们先从创建添加股票的函数开始，所以——

**18:09** · I'll call this add Equity add Equity self and we're going to say symbol is equal to self. symbol entry. get.

> 我把它叫做 `add_equity`：`def add_equity(self)`，然后我们写 `symbol = self.symbol_entry.get()`——

**18:26** · uper levels is equal to self. levels entry. getet draw down is equal to self. draw down entry. getet so here we're just getting the symbol levels and draw down

> ——`.upper()`，`levels = self.levels_entry.get()`，`drawdown = self.drawdown_entry.get()`。所以这里我们只是获取 symbol、levels 和 drawdown——

**18:45** · for the entry form that we had up here all right and this is that ad Equity command that we're creating right now

> ——，也就是上面那个输入表单里的内容。好，这就是我们正在创建的这个 add_equity 命令。

**19:05** · so this also I think this is still inside the Constructor yeah this is still inside the Constructor so it's my fault got to tab that out now it's being used so I have this tabbed in now if we tab this out you can see it's it's

> 所以这里——我想这还在构造函数里面。是的，这还在构造函数里，这是我的失误，得把它缩进出来。现在它被用到了——我把它缩进进去了。如果我们把它缩进出来，你会看到它——

**19:21** · actually being used by this button see all right so now we're creating this function outside of the construct ctor symbols levels draw down all good there now we need to do some handling for valid input so if not

> ——实际上是被这个按钮使用的，看到了吧。好了，现在我们是在构造函数之外创建这个函数。symbol、levels、drawdown 都好了。现在我们需要做一些有效输入的处理，所以 `if not`——

**19:39** · symbol or not levels. is digigit or not draw down. replace decimals with nothing then we have it as a number is digit these are all invalid entries this

> ——`symbol or not levels.isdigit() or not drawdown.replace('.', '', 1).isdigit()`——这些都是无效输入（invalid entries）。这个——

**20:00** · is not going to catch everything that's not really the the goal of this right now but this is a a reasonable first line of defense messagebox doow error that means that you just did not enter anything that was

> ——并不能捕获所有情况，这也不是现在的目标，但它是一个合理的第一道防线。`messagebox.showerror`，表示你输入的内容并不——

**20:16** · valid and we're just going to return from that the levels is going to be equal to in levels which makes sense right so if you have five levels and you're trading down

> ——有效，我们直接从这里返回。然后 `levels = int(levels)`，这很合理，对吧？如果你有 5 层（levels）、并且你在向下——

**20:29** · in a particular Equity then that's that's an integer you can have fractional levels that doesn't make any sense I I also like implementing this strategy as an example because blowing out is very difficult um if you just

> ——交易某只股票，那层数就该是整数——你不可能有分数层，那没有意义。我之所以喜欢把这个策略作为例子，还因为爆仓（blowing out）很难发生，嗯，如果你只是——

**20:42** · follow this tutorial blindly you know we're using even if you used 100 Levels right you're you're not necessarily going to be entering a position of of 100 plus the API isn't going to let you just use

> ——盲目地跟着教程走的话。你知道，即使你用了 100 层，你也未必会加到一个 100+ 的仓位。而且 API 不会让你就这么使用——

**20:57** · a massive amount of Leverage so I think this is a very reasonable um strategy even if you're following blindly which is which is good I like that aspect of it as well but we have this this level's integer we also have the draw down which

> ——大量的杠杆。所以我认为这是一个相当合理的策略，即使你是盲目跟做。这挺好的，我也喜欢它的这一点。但我们有 levels 这个整数，还有 drawdown，它——

**21:11** · is going to determine the entry price for the next levels we of course have our entry price which we're going to have to fetch from the

> ——将决定后续各层的入场价。我们当然还有一个入场价（entry price），我们需要从——

**21:29** · from the API now we need to determine the prices to trade at for the following levels so I'm going to say levels I'll say level prices is equal to we'll say i+ one for and we're going to round the

> ——从 API 那里获取它。现在我们需要确定后续各层要交易的价位。所以我写 `level_prices = {i+1: round(`——

**21:48** · entry price times 1us the draw down times I + one we're going to round that to two for I in range levels so this is that Martin

> ——`entry_price * (1 - drawdown * (i+1))`，四舍五入到两位小数，`for i in range(levels)`。这就是那个马丁——

**22:07** · Gil style DCA strategy where what I'm doing is I'm taking that draw down threshold that we set for the equity and I am going to trade at each level specified by the draw down from the entry price so we enter at 100 if we

> ——格尔（Martingale）风格的 DCA（定投）策略：我所做的是，取我们为该股票设置的回撤阈值，然后在从入场价算起、由回撤指定的每一个层级上交易。所以我们在 100 买入，如果我们——

**22:26** · have a 10% draw down per level then we're going to assume that initial entry price is fixed every $10 we're going to place a buy and that is essentially what's happening here okay let's update the equities now

> ——每一层有 10% 的回撤，那我们假定初始入场价是固定的，每下跌 10 美元，我们就会下买入单。这基本上就是这里发生的事。好，现在我们来更新 equities——

**22:42** · this is the data being saved so self. equities we have our symbol and we want to make sure this is equal to a dictionary where the position is initially zero the entry price is going to be the

> ——这就是被保存的数据。`self.equities[symbol]`，我们想确保它等于一个字典，其中 position（仓位）初始为 0，entry price（入场价）是——

**23:02** · entry price we have the levels where the levels are the level prices and we have the status which is going to be on or off for the system so we'll start it as

> ——entry price，levels 就是 level prices，还有 status（状态），它表示系统开或关。所以我们先把它设为——

**23:20** · off so I think instead of the status being the order status from the API instead we'll make this the status of the system where the system can be on or off for you know any equity in the table I think that will make the most

> "off"（关闭）。所以我想，与其把 status 当作来自 API 的订单状态，不如把它当作系统的状态：系统可以对表格中的任何一只股票处于开或关。我想这最——

**23:42** · sense anytime we go about adding the new symbols to the dictionary we we're going to want to go ahead and save that data so we're going to say self. saave equities and we're also going to say self. refresh table and that's just

> ——合理。任何时候我们往字典里添加新股票，我们都要顺便保存这些数据，所以写 `self.save_equities()`，还要写 `self.refresh_table()`，这只是——

**24:02** · going to save the data and update the table which makes sense to me want to make sure that this is correct I think this notation is correct for I and range round I think

> ——保存数据并更新表格，这在我看来很合理。我要确保这是正确的——我想 `for i in range`、`round` 这个写法是正确的。我想——

**24:20** · this needs to be here yeah it was not reaching that I my round parentheses was at the end it needed to be next to this two to close that function I don't want to close the function around the comprehension for

> ——这里需要它。对，之前它没有碰到那个 `i`——我的 round 的括号放到了末尾，它需要紧挨着这个 `2` 来闭合那个函数。我不想把函数闭合在——

**24:39** · this this Loop here that's going to create the level prices effectively so if you had that warning as well that I wasn't defined that's why it's because the round function needed to needed to adjust this

> ——这个推导式（comprehension）的循环外面。这个循环会创建 level prices。所以如果你也看到过那个"i 未定义"的警告，原因就在这里——因为 round 函数需要调整一下——

**24:51** · parentheses all right so that's going to do it for the add Equity function I think that is everything that we need to do there okay now we need to create a function to toggle a selected system so I'll call

> ——括号。好了，add_equity 函数这样就完成了，我想那里需要做的就这些。好，现在我们还需要创建一个切换所选系统的函数，所以我把它叫做——

**25:04** · this toggle selected system and we will say let me scroll down toggle selected system we will say selected items equals self. tree. selection so

> ——`toggle_selected_system`。我们写——让我往下滚动——`toggle_selected_system`，我们写 `selected_items = self.tree.selection()`，所以——

**25:23** · we're going to get what is selected in the table if not selected items that means we we didn't select anything so we're going to have a warning the warning is no equity is selected

> ——我们要获取表格中被选中的内容。如果 `not selected_items`，那就意味着我们什么都没选中，所以我们要弹出一个警告，警告内容是"no equity is selected"（未选中任何股票）——

**25:40** · shocker we'll return from that otherwise for item in selected items we will say symbol is equal to self. tree. item the item that we are iterating through in the selected items and of

> ——真是意外。我们从这个分支返回。否则，`for item in selected_items`，我们写 `symbol = self.tree.item(item)['values'][0]`——也就是我们在 selected_items 中遍历的那个条目——当然——

**25:58** · course we're going to look at the values we're going to look at zero the symbol and we're going to say self. equities that's our equities dictionary we just got the symbol from the table we will toggle the

> ——我们要看它的 values，取第 0 个值，也就是 symbol。然后我们写 `self.equities[symbol]['status']`——这是我们的 equities 字典，我们刚从表格中取出 symbol，现在要切换它的——

**26:13** · status and we will say Java tary style if statement on if the self. equities symbol status is going to be off otherwise we will turn

> ——status。我们用类似三元表达式（ternary）的 if 写法：如果 `self.equities[symbol]['status']` 是 off，那就把它打开（On），否则就把它——

**26:31** · it on I think I had that backwards so essentially what we're doing is we're looking we're saying okay if it's off we're going to turn it on otherwise turn it off and that's what we're doing in

> ——关闭。我想我刚才写反了。所以本质上我们在做的是：看看状态——好，如果是 off，我们就把它打开；否则就关闭。这就是我们在这个——

**26:44** · this self. equities dictionary which is saving all of our data and we're going to this data and we're looking at the symbol based on what is selected in the tree that is this initial self. tree selection and that's how we're itera

> ——self.equities 字典中所做的，它保存了我们所有数据。我们查看这个数据，根据 Tree 中选中的内容找到对应的 symbol——就是最初的 `self.tree.selection()`——我们就是这样——

**26:58** · ating through the selection to find the correct symbol and then toggle that system and that is how we're going to determine whether or not we are actively trading that symbol we are cooking now of course since we've updated the data

> ——遍历选中项来找到正确的 symbol，然后切换那个系统。这就是我们判断是否积极交易那个股票代码的方式。我们渐入佳境了！当然，既然我们更新了数据——

**27:12** · we're going to call self. saave equities and we're going to call self. refresh table and that will do it we now need to write code to remove an equity so we'll say def move selected equity

> ——就要调用 `self.save_equities()` 和 `self.refresh_table()`，这样就行了。现在我们还需要写移除股票（equity）的代码，所以我们写 `def remove_selected_equity`——

**27:30** · and this shouldn't be really surprising we're just going to get the selection from the table just as we did before uh if nothing is selected so if not selected items then clearly we can't remove the equity so we're going

> ——。这应该不会让人意外：我们和之前一样，从表格获取选中的内容。嗯，如果没有选中任何东西——`if not selected_items`——那我们显然无法移除股票，所以我们要——

**27:50** · to warn them we're going to say warning no equity selected we'll return from there then for item in selected items this is exactly what we just did we're going to say symbol is equal to self. tree. item

> ——警告用户：`messagebox.showwarning`，提示"no equity selected"（未选中股票），然后从那里返回。接着 `for item in selected_items`——这正是我们刚才做的——我们写 `symbol = self.tree.item`——

**28:08** · item and we will look at the values look at the zero value that is going to be the symbol that we've selected then if the symbol is in self. equities then we are just going to delete

> ——`(item)['values'][0]`，查看 values 里的第 0 个值，那就是我们选中的 symbol。然后，如果这个 symbol 在 `self.equities` 中，我们就直接删除——

**28:22** · it self. Equity symbol and then we are going to of course need to to save that change and we are going to need to update refresh the table that shouldn't be too much of a surprise it's literally just the

> ——它：`del self.equities[symbol]`。然后当然我们需要保存这个改动，还需要更新/刷新表格。这不应该太让人意外，它基本上就是我们——

**28:41** · opposite of what we did up here when we added the equity we're just removing it and we accessed it in the same way as the toggle so shouldn't be too much of a surprise uh now we're going to fill in sort of just like a a filler function

> ——在上面添加股票时所做操作的相反操作。我们只是移除它，而且我们访问它的方式和 toggle 一样，所以不应该太意外。嗯，现在我们来实现一个有点像占位（filler）的函数——

**28:53** · for sending a message via the chat GPT or the LM that you choose to use so message is equal to self. chat input we're going to get the message and on the back end here once we get that message from the form we can populate it

> ——，用于通过 ChatGPT 或你选择的任何 LLM 发送消息。所以 `message = self.chat_input.get()`，我们获取这条消息。在后端，一旦我们从表单拿到这条消息，就可以给它填充——

**29:09** · with the portfolio information and then we can ask the AI whatever we would like about our portfolio that's our our AI portfolio manager essentially so if there's no message then we're not doing anything so we're going to return

> ——投资组合（portfolio）的信息，然后我们就可以就我们的投资组合向 AI 询问任何问题。本质上，这就是我们的 AI 投资组合经理。所以如果没有消息，那我们什么也不做，直接返回。

**29:23** · response is equal to mock check GPT response we have this message is the input makes sense chat output. config state is going to be tk. normal self. chat output we're going to

> `response = mock_chatgpt_response(message)`——我们把消息作为输入，这说得通。然后 `chat_output.config(state=tk.NORMAL)`，接着我们 `self.chat_output`——

**29:40** · insert that message right as the response so tk. and it's just going to be a formatted print statement we will say you and then the message and then we have a response

> ——把它插入（insert）到输出中，作为响应内容。所以 `tk.END`，它只是一个格式化的打印语句：我们写 "You:"，然后是消息，接着是来自 AI 的——

**29:58** · from the AI we could even break it up actually into some more new lines after that that should be fine uh of course this is disabled right so the output chat output.

> ——响应。我们甚至可以在那之后拆分成更多的新行，这应该没问题。嗯，当然，这是禁用的，对吧？所以输出 `chat_output.`——

**30:16** · config after it's updated state is equal to tk. disabled and then we are going to do self. chat input we're going to delete what was

> ——`config`，在更新完成之后，把 state 设回 `tk.DISABLED`。然后我们 `self.chat_input.delete(0, tk.END)`，删除原来——

**30:31** · sense and that's expected functionality right so if you if you type something into an input and you send it to exct GPT your text doesn't stay in that input form that's what we're doing here we're just going to delete that from zero all

> ——的内容。这是预期的功能，对吧？如果你往输入框里输入一些内容并发送给 ChatGPT，你的文字不会停留在那个输入框里。我们这里做的就是：把它从 0 一直删到——

**30:42** · the way to the end of the form and here we're inserting at the end of the output field the message that we sent and the response from the AI of course we need to get this response from this function which we will build later on uh as we go

> ——表单末尾。而这里，我们在输出字段的末尾插入我们发送的消息和 AI 的响应。当然，我们需要从这个函数得到响应——我们会在稍后继续——

**30:57** · through the the API work but we're almost there we just need to build a few more functions that's going to be it for the send message now we're going to go and update the table so the the def refresh table

> ——推进 API 工作时构建它。不过我们快完成了，只需再构建几个函数，send_message 就完成了。现在我们来更新表格，所以 `def refresh_table`——

**31:14** · function self to access the table we'll say for Row in self. tree. get children self. tree. delete row we need to delete everything right and we're going to repopulate it with some

> ——函数。用 self 来访问表格，我们写 `for row in self.tree.get_children(): self.tree.delete(row)`——我们需要清空所有内容，对吧？然后我们用一些——

**31:32** · new information so for symbol data in self. equities do items and what this is going to do is it's just going to iterate through all the data that we have saved so we're

> ——新信息重新填充它。所以 `for symbol, data in self.equities.items()`，这会做的只是遍历我们保存的所有数据，所以我们要——

**31:45** · going to say self. tree. insert we're going to insert it into the table the values in this Tuple which are going to be the symbol it's going to be the data the position it's going to be the data

> ——写 `self.tree.insert(...)`，把它插入表格。这个元组（tuple）中的 values 包括：symbol（symbol）、data（数据）里的 position（仓位）——

**32:05** · entry price it's going to be the string of the data levels and it's going to be the status of the system and that should be everything for the refresh table all we're doing is

> ——、entry price（入场价）、data levels 的字符串形式，以及系统的 status（状态）。refresh_table 这样就差不多了。我们所做的只是——

**32:24** · deleting all of the rows in the table and updating with the new information and we can always just go through and update the equities dictionary whenever we like in any function of course in the API uh for the actual live data we can

> ——删除表格中的所有行，并用新信息更新。我们随时可以在任何函数里遍历并更新 equities 字典——当然，对于真实的实时数据，我们可以在 API 部分——嗯，我们可以——

**32:38** · go back and we can update this data here and every time we call this refresh table it's going to update with the correct information that's exactly what we're looking to do right we want to update the you know equities dictionary

> ——回过头来更新这里的数据，每次调用 refresh_table，它都会用正确的信息更新。这正是我们想做的，对吧？我们想用实时数据更新 equities 字典——

**32:50** · with live data now we need to figure out what data to query from the broker from the AP which is exactly why we're saving and loading this you know we don't particularly care about the stale price

> ——。现在我们需要弄清楚要从券商/API 查询哪些数据——这正是我们保存和加载这些东西的原因。你知道，我们并不特别关心过时（stale）的价格——

**33:03** · information but we need to know what tickers we're trading and whether or not we were actively trading it which is why we're keeping the status I also want to maintain the draw down and the levels so that's why we have

> ——信息，但我们需要知道我们在交易哪些股票代码、我们是否在积极交易它——这就是我们保留 status 的原因。我还想保留 drawdown 和 levels，所以这就是——

**33:17** · that now we're going to add an auto update def auto update and this is just to auto update the user interface we're going to say while self. running we can just go ahead and do time. sleep maybe we'll call it 5 seconds and self. update

> ——我们有它们的原因。现在我们添加自动更新：`def auto_update`，这只是用来自动更新用户界面。我们写 `while self.running:`，然后直接 `time.sleep`，也许设为 5 秒，然后 `self.update_`——

**33:35** · prices update prices we can go ahead and update the prices we need our save equities function this is going to allow us to save that dictionary so we'll say with open data file as right or I'm sorry as

> ——`prices`（update_prices），我们可以更新价格。我们需要 save_equities 函数，它让我们能保存那个字典。所以我们写 `with open(DATA_FILE, 'w') as f:`——或者，抱歉——是——

**33:53** · read no I'm sorry this is a write because we're saving so this is going to be a W for right as F we will do json. dump self. equities as file F that's going to allow us to save the equities now we need to

> ——读？不，抱歉，这是写入（write），因为我们是在保存，所以用 'w'。`with open(DATA_FILE, 'w') as f: json.dump(self.equities, f)`，这让我们能保存 equities。现在我们需要——

**34:12** · load them so loading the equities we are going to do a with open data file as read as F we're going to do to return json. load

> ——加载它们。加载 equities 时，我们写 `with open(DATA_FILE, 'r') as f:`，然后 `return json.load(f)`——

**34:34** · f um we probably need to tr accept around this so we're going to try this isn't Java so we're going to use a tri block to try to load this file and we're going to accept a file not found and a Json decode error so if there's an issue

> ——。嗯，我们可能需要用 try/except 把它包起来，所以我们要用 try 块。这不是 Java，我们用的是 try 块来尝试加载这个文件，捕获 `FileNotFoundError` 和 `json.JSONDecodeError`。所以如果有什么问题——

**34:55** · with for some reason parsing the Jon we can just catch that we're going to return an empty dictionary uh this really probably should throw a warning as well this should never really be the case nothing should trigger this unless

> ——，比如由于某种原因解析 Json 失败，我们捕获它并返回一个空字典。嗯，这其实大概也应该抛出一个警告。正常情况下这不应发生，除非——

**35:08** · you go in you edit the Json and it uh it can't read into the dictionary but that should be that should suffice for what we're doing here def on close self we need to save on close so

> ——你手动编辑了 Json，导致它无法读入字典。但对我们这里做的事来说，这样就足够了。`def on_close(self)`——我们需要在关闭时保存，所以——

**35:25** · we're going to set running equal to false we're going to self. saave equities we're going to self. root. destroy some house keeping stuff and then that should be everything

> ——把 `running = False`，调用 `self.save_equities()`，调用 `self.root.destroy()`——一些收尾（housekeeping）工作，然后这应该就是全部——

**35:41** · we need so then we could say if name is equal to main we will do root is equal to tk. TK this is our main window we're going to pass that through our trading bot G

> ——了。然后我们可以写 `if __name__ == '__main__':`，`root = tk.Tk()`——这是我们的主窗口，我们把它传给 `TradingBotGUI`——

**35:58** · there's our root then we will do root. protocol we will say on close which is WM delete Window app.on close that's this on close function we just built here so we're

> ——，这就是我们的 root。然后写 `root.protocol("WM_DELETE_WINDOW", app.on_close)`——这个 on_close 就是我们现在构建的这个函数。所以我们——

**36:16** · going to save sure running is false and destroy the root and then we'll just run that that main Loop run that main Loop there so ahead and run this

> ——要确保保存、把 running 设为 False 并销毁 root。然后我们直接运行那个主循环（mainloop）。运行主循环。好，那就运行它吧——

**36:30** · guy all right looks like we're getting trading bot has no attribute toggle system so let's go back and try to figure out where this issue

> 运行这家伙。好，看起来我们遇到了"trading bot has no attribute 'toggle_system'"（交易机器人没有 toggle_system 属性）的错误。所以我们回去，试着找出这个问题——

**36:49** · is toggle [Music] system toggle selected system so I'm just going to call this toggle selected system instead that was the issue here so if you recall when we created this

> ——出在哪里。`toggle`（音乐）`system`……`toggle_selected_system`。所以我直接把它叫做 `toggle_selected_system` 来代替，这就是这里的问题。所以如果你还记得，当我们创建这个——

**37:05** · toggle system button I call this toggle system this is toggle selected system toggle selected system and now we have our user interface for our AI trading bot our user interface seems like I've

> ——system 按钮时，我叫它 `toggle_system`。这里应该是 `toggle_selected_system`。现在我们有 AI 交易机器人的用户界面了。我们的用户界面看起来，我好像——

**37:25** · offset these by one these entries for the levels and draw down which isn't bad for our first run I'm pretty impressed that this turned out as structurally as nice as it did just

> ——把这些错开了一格——levels 和 drawdown 的输入框。对于我们第一次运行来说，这不算差。我挺惊讶它竟然能出来得结构这么好看，纯粹——

**37:38** · coding so here is the row one we're going to make this row zero we're going to make this row zero and that's going to fix the offset entries if I rerun this we have a nice user interface let's try to add a symbol Apple levels let's

> ——靠敲代码敲出来的。所以这里本来是第 1 行，我们要改成第 0 行——把这个改成第 0 行，那就能修复错位的输入框。如果我重新运行，我们就有个不错的用户界面了。我们来试着添加一个股票代码：Apple，levels 就——

**37:56** · do five levels with a 5% draw down add Equity looks like I called the I called this levels entry instead of levels entry by accident so let's go fix

> ——设 5 层，5% 的回撤，然后 Add Equity。看起来我不小心把这个叫成了 levels entry 而不是 levels_entry，所以我们去修一下——

**38:15** · that levels entry let's rerun this guy so we'll say apple say five and five and Tuple doesn't Define around

> ——那个 levels_entry。我们重新运行它。所以输入 apple，5 和 5，然后——"Tuple doesn't define round"（元组没有定义 round 方法）——

**38:35** · method looks like I have to fix my Tuple here round entry price I see round

> ——。看起来我得修一下这里的元组：`round(entry_price`……我看到了，`round`——

**38:53** · two there we go I think I have my parenthesis backwards let's try this so that was for the round function I got this error tupal doesn't Define round function of course we still have to add the update prices function but if

> ——`(…, 2)`，好了。我想我把括号放反了。我们试试这个——那就是 round 函数的问题，我收到了"Tuple doesn't define round"这个错误。当然，我们仍然需要添加 update_prices 函数，但如果——

**39:10** · you take a look this should fix the round I think I just stacked the parenthesis here by accident let's do symbol Apple levels five draw down five add Equity there we go so here we have our mock entry price of 100 our levels

> ——你看一下，这应该能修复 round 的问题。我想我只是在这里不小心把括号叠错了。我们输入 symbol: Apple，levels: 5，drawdown: 5，Add Equity。成功了。所以这里我们有模拟的入场价 100、我们的 levels——

**39:26** · that we're going to be trading at whether or not the system is on and off we can toggle that here toggle on toggle off we have our chat component so we can enter a message to our AI chatbot it'll respond here and that should be it for

> ——，我们要交易的各层级，以及系统是否开/关——我们可以在这里切换它（toggle on / toggle off）。我们还有聊天组件，所以可以输入一条消息给我们的 AI 聊天机器人，它会在这里回复。这就是——

**39:42** · our user interface now this is not the sexiest user interface in the world nevertheless that's something that you can enhance when you know all of the functionality is as you would like I'm not going to spend too much more time on

> ——用户界面的全部了。这不是世界上最性感的用户界面，尽管如此，当你确定所有功能都符合预期之后，这是你可以去增强的部分。我不打算在——

**39:57** · the user interface I really want to get into the rest of the functionality of the system but this will suffice for what we are trying to do now when I close the system you'll see we have an equities de Json here when I rerun the

> 用户界面上花太多时间，我真的很想进入系统其余的功能部分。但对我们试图做的事情来说，这就够了。现在，当我关闭系统时，你会看到这里生成了一个 equities.json。当我重新运行——

**40:09** · system it loads that information which is exactly what we're looking for so we have these symbols that we're traing the status of the system on close saved and when we run it you can see it repopulates can also

> ——系统时，它会加载那些信息，这正是我们想要的。所以我们有这些正在交易的股票代码、系统的状态，在关闭时保存；当我们运行它时，你可以看到它重新填充了。还可以——

**40:23** · remove it it'll save it rerun onun it and it no longer exists so everything seems to be working as intended of course we don't have our cack GPT integrated but if I enter this I get a mock message and this is you and then

> ——把它移除，它会保存；重新运行后，它就不再存在了。所以一切似乎都按预期运行。当然，我们还没有集成我们的 ChatGPT，但如果我输入这个，我会得到一条模拟消息，显示 "You:"，然后是——

**40:38** · the mock response we had it just remember post the message if you recall from our mock API call up here that is exactly what we had it's just going to re- return the message so now what we're going to do is we're going to go back to

> ——我们的模拟响应。还记得吧，它只是回显这条消息——如果你回想一下我们上面的模拟 API 调用，那正是我们写的东西：它只是把消息原样返回。所以现在我们要做的，是回到——

**40:51** · the checklist and boom this is done step one step two is to establish a connection to a brokerage via an API so in this case we're going to use alpaca and we're

> ——待办清单，看，这一步完成了。第一步完成。第二步是通过 API 连接到券商，所以在这种情况下我们要用 Alpaca，我们——

**41:09** · going to go ahead and get started with the alpaca API I'm going to create a new script here or maybe I'll create a new um Jupiter notebook for alpaca just so that we can walk through the initial connection together I'm

> ——要开始使用 Alpaca API。我要在这里创建一个新脚本，或者也许我会为 Alpaca 创建一个新的 Jupyter notebook，这样我们就可以一起走一遍初始连接。我——

**41:22** · going to open up Al Packer really quick and I'm going to walk you through just setting up an initial connection and then how we can integrate this into our bot head on over to alpaca and create a free account you can scroll down and

> ——会很快打开 Alpaca，带你走一遍如何建立一个初始连接，然后如何把它集成到我们的机器人里。前往 Alpaca 并创建一个免费账户，你可以往下滚动——

**41:33** · generate some API keys I regenerated my keys right now I have this key and this secret key of course your secret key will disappear so make sure you keep track of it I'm going to go back into the code here and I am going to add my

> ——生成一些 API 密钥（API keys）。我刚才重新生成了我的密钥，现在我有这个 Key 和这个 Secret Key。当然，你的 Secret Key 之后会消失，所以一定要把它记好。我会回到代码这里，添加我的——

**41:50** · key and I'm going to add my secret key as well so this is actually my secret key and this is my key so I'm going to go ahead and copy this key as well paste this key here and once we do that we can start to actually add the functionality

> ——Key，也添加我的 Secret Key。所以这实际上是我的 Secret Key，这是我的 Key。我继续把这个 Key 也复制、粘贴到这里。一旦我们这么做，就可以开始真正添加——

**42:08** · we're looking for quering the prices and also placing trades that is these buy orders at the levels according to the levels we set and the draw down for each equity in our trading bot because I know it's going to come up it comes up in

> ——我们想要的功能：查询价格，以及下单（placing trades）——也就是按照我们在交易机器人为每只股票设置的 levels 和 drawdown，在这些层级下买入单。因为我知道这会出现——它几乎在我——

**42:22** · pretty much every python video that I've created if you have a mo module not found error that means that you need to install the package or the module via pip so I opened up my command prompt I have Pip install alpaca trade API for

> ——制作的每一个 Python 视频里都会出现：如果你遇到 "ModuleNotFoundError"（找不到模块）错误，那意味着你需要通过 pip 安装这个包或模块。所以我打开命令提示符，运行 `pip install alpaca-trade-api`，比如——

**42:38** · example and this is going to install the alpaca API it's going to let me use it in Python so when I actually go about importing it and I say import alpaca trade API as trade API I'm not going to get a module not found errors so that

> ——这会安装 Alpaca API，让我能在 Python 里使用它。所以当我真正导入它，写 `import alpaca_trade_api as tradeapi` 时，就不会再收到 ModuleNotFoundError 了。所以——

**42:57** · goes for any M jeel um that is you know not built built into your version of python in this case the alpaca create API is most likely not going to be built in so I just wanted to touch on that before we get into actually implementing

> ——这对于任何没有内置于你的 Python 版本中的模块（module）都适用。在这种情况下，alpaca_trade_api 很可能不是内置的。所以在我们真正开始实现之前，我只是想先提一下这一点。

**43:12** · the API it makes the most sense to start in a Jupiter notebook so I'm just going to copy all of this over to my Jupiter notebook and for the API we're going to have a base URL L and I believe this base URL I'm just going to copy and

> 实现 API 时，最合理的做法是在 Jupyter notebook 里开始。所以我把所有这些复制到我的 Jupyter notebook 里。对于这个 API，我们会有一个 Base URL（基础 URL），我相信这个 Base URL 是——我直接复制粘贴——

**43:30** · paste it it's going to be paper- alpaca or paper D api. alpaca markets very important also because I I don't think that I had mentioned it but please make sure you are on the paper trading you're not going to get very far anyway

> ——它：`https://paper-api.alpaca.markets/`。非常重要的是——我想我之前没提过——请务必确认你在使用纸面交易（paper trading，即模拟交易）。反正如果你不在模拟盘上，你也走不了多远——

**43:48** · if you're not on the paper trading and of course you can fund a live account and trade with a live account in the exact same capacity but for the sake of develop let's start with the paper account so go

> ——，而且当然你也可以给真实账户充值，用同样的方式在真实账户上交易。但为了开发方便，我们先从模拟账户（paper account）开始。所以去——

**43:59** · to your paper account generate your API keys for your paper account uh if it doesn't work and you're on the Live account that's probably because you have insufficient funds just make sure that you are on your paper and you go down to

> ——你的模拟账户，为你的模拟账户生成 API 密钥。嗯，如果它不工作而你用的是真实账户，那大概是因为你资金不足。只要确保你在模拟账户上，然后往下走到——

**44:10** · the endpoint this is going to be the endpoint I'll pack markets V2 so I'm going to copy that I'm going to paste that right here and that's what we're going to use to attempt to query some data from from

> ——端点（endpoint）。这个端点将是 `.../alpaca.markets/v2`。所以我把这个复制下来，粘贴到这里。这就是我们要用来尝试从——

**44:24** · alpaca so I'm going to say API is equal to trade api. rest and I'm going to use my key my secret key I'm going to use the base URL and the API version is in fact version two so I'm going to go ahead and run this everything seems like

> ——Alpaca 查询一些数据的东西。所以我写 `api = tradeapi.REST(key, secret_key, BASE_URL, api_version="v2")`。我使用我的 Key、Secret Key、Base URL，API 版本确实是 v2。我继续运行这个，一切看起来——

**44:44** · it's working okay and now we're going to actually go ahead and try to create a basic request from this trade API and we'll see if we can get some data to get data we're going to create a function def get data we'll take a

> ——正常。好，现在我们要真正尝试从这个 tradeapi 发起一个基本请求，看看能否取到一些数据。为了取数据，我们要创建一个函数 `def get_data`，它接受一个——

**45:00** · symbol as an input and we're going to say try baret is equal to api. getet latest trade look at the symbol that we give it we're going to return that

> ——symbol 作为输入。然后我们写 `try:`，`barset = api.get_latest_trade(symbol)`——查看我们给它的那个 symbol——然后返回那个——

**45:19** · price bar set. price and then we're going to accept an exception as e we're just going to catch any error and return a price of -1 now we can test this function I'm going to say get data let's look at the

> ——`barset.price`（价格）。然后 `except Exception as e:`，我们捕获任何错误并返回 -1 的价格。现在我们可以测试这个函数了。我调用 `get_data`，看看——

**45:37** · data for apple 21396 and let's see if we can go here and look [Music] at apple 21396 looks about right so we are successfully fetching the live data

> ——Apple 的数据，213.96。让我们到这边看看（音乐）——Apple 是 213.96，看起来差不多是对的。所以我们成功地从——

**45:57** · from alpaca now what we have to do is we have to integrate this into our bot so if we go to our checklist here we've established a connection to a brokerage via the API that's exactly what we've

> ——Alpaca 获取到了实时数据。现在我们必须做的是把它集成到我们的机器人里。所以如果我们回到待办清单，我们已经"通过 API 建立了到券商的连接"——这正是我们——

**46:10** · done here now we need to actually integrate this into our bot to ensure that we are placing buy orders at each of the levels that we create we also need to make sure that we are updating the entry price in our data correctly so

> ——在这里做的。现在我们需要真正把它集成到我们的机器人里，确保我们在创建的每一层都下买入单。我们还需要确保正确地更新数据中的入场价，所以——

**46:24** · if you recall when we run this trading bot currently when I create a apple let's create a system for Apple here it creates my levels but the entry price is clearly wrong the status of the

> ——如果你还记得，当我们当前运行这个交易机器人时，当我创建一个 Apple——我们在这里为 Apple 创建一个系统——它创建了各层，但入场价明显是错的，系统的——

**46:40** · system is of course off but what we need to do is when we turn this on we want to make sure that buy orders are placed at each of these levels and we want to update this entry price with the actual entry price that we filled at and to do

> ——状态当然是 off。但我们需要做的是：当我们把它打开时，要确保在每一层都下买入单，并且用我们实际成交的入场价来更新这个入场价。要做到这一点——

**46:55** · this what we can do is just iterate through from alpaca all of the entry prices for our stock in that specific system so in this case the system is for apple we're going to iterate through all the entry prices take the Max and that's

> ——，我们能做的就是从 Alpaca 遍历我们那套特定系统里股票的所有入场价。所以在这种情况下，系统是针对 Apple 的，我们遍历所有入场价，取最大值，那就是——

**47:07** · going to be our initial entry price then we're going to have these levels that fill orders and we're going to track the quantity at each of these levels to make sure that we are not placing more than one order

> ——我们的初始入场价。然后我们会有这些触发订单的层级，我们要跟踪每个层级的数量，以确保我们不会下超过一单——

**47:21** · we're going to make sure that every time we run this system you know we're going to iterate through from that initial entry price and ensure that okay you know if there are active orders we're not going to place more active orders

> ——。我们要确保每次运行这个系统时，我们都会从初始入场价开始迭代，并确保——好，如果已经有活跃订单，我们就不再下更多活跃订单——

**47:32** · and then everything should be all set on the trading side and we can get to the AI component all right the first thing we got to add to our trading bot here is a function to check to see if an existing order at a price level

> ——。然后交易方面就万事俱备了，我们可以进入 AI 组件部分。好了，我们首先要添加到交易机器人的，是一个用来检查某个价格层级是否——

**47:47** · currently exists so what we're going to do is we're going to add May We'll add it at the bottom add it right here after the send message so we'll say def check existing

> ——已经存在订单的函数。所以我们要做的是——我们把它加在底部，就加在 send_message 之后。所以我们写 `def check_existing_`——

**48:07** · orders self dot or self symbol price we will say try and this is where we're actually going to use the alpaca API so if we scroll on up over here you know we need to add the alpaca API just as we used it here so I'm going to copy this

> ——`orders(self, symbol, price)`。我们写 `try:`——这就是我们真正使用 Alpaca API 的地方。如果我们向上滚动到这里，你知道，我们需要像刚才那样添加 Alpaca API。所以我把这行代码——

**48:25** · line of code I'm going to paste it underneath this secret key so that we can use it I also need the base URL so that we can use this API Endo then I'm going to scroll on

> ——复制下来，粘贴到 Secret Key 下面，这样我们就能使用它。我还需要 Base URL，这样我们才能使用这个 API 端点。然后我往下滚动——

**48:38** · down and we are going to try to get the orders from our account api. list orders and we will say status equals open and symbol is equal to symbol for order in orders we are going

> ——，我们要尝试从账户获取订单：`api.list_orders(status='open', symbols=symbol)`。然后 `for order in orders:`，我们要——

**48:59** · to check to see if the float of the order. liit price is equal to the price that we are checking in which case we return true and that means that an order already exists for this level and we don't want

> ——检查 `float(order.limit_price)` 是否等于我们正在检查的那个价格。如果是，我们返回 True，那意味着这个层级已经存在订单，我们不想——

**49:14** · it we are just going to catch a blanket exception and we are going to say that there is an error in the API and we have an error checking orders and that error is going to be

> ——它。我们只是捕获一个笼统的异常（blanket exception），我们会提示：API 出了错误——"error checking orders"（检查订单出错）——这个错误会是——

**49:31** · given by E we can add that as the fprint here otherwise we're going to return false and that means we need to place an order at that level okay so this is uh the first usage of the API in our trading bot you know if we go up here we

> ——由 e 给出的，我们可以把它加在这里的 f-string 里。否则我们返回 False，那意味着我们需要在那个层级下订单。好，所以这就是我们交易机器人里第一次使用 API。你知道，如果我们回到上面——

**49:50** · can see that we have our key secret key base URL and the API established underneath our Imports then if you scroll all the way down to where we've added this function to the trading bot class then you can see that we have a

> ——可以看到，在 Imports 下面，我们建立了 key、secret_key、base_url 和 api。然后如果你一路滚动到我们在 TradingBotGUI 类里添加这个函数的地方，你可以看到我们有一个——

**50:07** · symbol a price we're going to iterate through all the orders based on the symbol that are open and we're going to check to see okay is the limit price of that order equal to the price in our function if it is we'll return true and

> ——symbol、price 参数。我们遍历该 symbol 的所有未成交（open）订单，检查：嗯，这个订单的 limit price（限价）是否等于我们函数里的价格？如果是，就返回 True——

**50:19** · hey we're not going to place an order at that level otherwise we can return false and any errors we're just going to give a message box showing that there's API error this is our first use of alpaca in our trading bot we're also going to need

> ——，嘿，我们就不在那个层级下订单了；否则我们可以返回 False。任何错误，我们只是弹一个消息框，显示有 API 错误。这是我们交易机器人里第一次使用 Alpaca。我们还需要——

**50:32** · to get current pricing information to set an initial order so we're going to say def F I think we should call it fet Market data F alpaca data I know we called it get data in our jupyter notebook it really is arbitrary

> ——获取当前价格信息来设置初始订单。所以我们写 `def fetch_`——我想我们应该把它叫做 `fetch_alpaca_data`。我知道我们在 Jupyter notebook 里叫它 get_data，名字其实随意——

**50:47** · but fetch alpaca data we're going to say self symbol then we will say try TR and it's actually exactly the same as what we wrote here so I'm just going to copy and paste it so we're going to use the get

> ——，但就叫 fetch_alpaca_data 吧。我们写 `(self, symbol)`，然后 `try:`——它其实和我们刚才写的一模一样，所以我直接复制粘贴。我们使用 get——

**51:03** · data function to get the bar set for a symbol and that is going to let us get the current pricing information okay so now we have pricing information we have the ability to check orders and we need to

> ——data 函数来获取某个 symbol 的 barset，这会让我们拿到当前价格信息。好，现在我们有了价格信息、有了检查订单的能力，我们还需要——

**51:20** · create um the functionality to send an order for an initial entry price and then based on that initial entry price we're going to update the data on the back end set our levels and then Place more trades all right looks like we need

> ——创建下单的功能：为初始入场价下一个订单，然后基于那个初始入场价，我们在后端更新数据、设置各层级，然后再下更多单。好，看来我们还需要——

**51:34** · a few more things we're going to create a helper function here to get the max entry price so get Max entry price self symbol and we'll say try orders equals api. list

> ——一些别的东西。我们要在这里创建一个辅助函数（helper function）来获取最大入场价：`get_max_entry_price(self, symbol)`，我们写 `try:`，`orders = api.list_orders`——

**51:54** · orders and we're going to say status equals Fields symbols or symbol is equal to symbol and the limit will be 50 you can adjust this as needed the prices are going to be the float of the orders

> ——`(status='filled', limit=50)`，symbol 过滤就是 symbol，limit 设为 50，你可以按需调整。prices 将是订单的 float 值——

**52:15** · average fill so filled average price and this is going to be for order in orders if order do filled average price in other words assuming we have an average fill price then we are going to

> ——average fill（平均成交价），即 `filled_avg_price`。这将用 `for order in orders if order.filled_avg_price` 实现。换句话说，假设我们有一个平均成交价，那么我们就——

**52:34** · iterate through and check to see which one is the highest because that is going to be where we initially entered the equity position and we are going to be trading levels based on that draw down we're going to return Max of the prices

> ——遍历它们，找出哪一个最高，因为那将是我们最初建立股票仓位的地方。然后我们会基于那个回撤来交易各层级。我们将返回 prices 的最大值——

**52:50** · um if prices otherwise we're just going to do zero so if it's empty we're just going to return zero really we should probably turn NE -1 okay accept exception as e and this is

> ——，如果有 prices 的话；否则我们直接返回 0。所以如果它是空的，我们返回 0——其实我们大概应该返回 -1。好，`except Exception as e:`，然后这是——

**53:04** · just going to be a message box to show that there was an API error and this is going to be an error um affection orders as e and then we'll just return uh Zero from there as a different error

> ——只是弹一个消息框，显示发生了 API 错误：`messagebox.showerror("API Error", f"Error fetching orders {e}")`。然后我们从那里返回 0，作为不同的错误码——

**53:23** · code and that is what we're going to use to get the max entry price so we have the ability to check existing orders we have the ability to fetch price information and the ability to check our Max entry price for a symbol all right

> ——。这就是我们用来获取最大入场价的东西。所以我们有了检查现有订单的能力、获取价格信息的能力，以及检查某个 symbol 最大入场价的能力。好——

**53:38** · some housekeeping stuff it looks like the V2 is specified twice here that was my mistake so this is actually going to append that to this URL so we can get rid of this V2 here moreover if we scroll down I think I forgot in the

> ——一些收尾工作。看起来这里 V2 被指定了两次，这是我的失误——这实际上会把 v2 追加到这个 URL 后面。所以我们可以删掉这里的 V2。此外，如果往下滚动，我想我在——

**53:54** · initial ad it function to add the draw down silly let's add the draw down as we draw down this way we can save that value and

> ——最初的 add_equity 函数里忘了加 drawdown，真粗心。让我们加上 drawdown 作为 drawdown，这样我们就能保存那个值——

**54:13** · use it for later we are also going to update this get Max entry price function instead of filtering for the symbol on the API call I'm going to get rid of that and I am going to say if the order. average price

> ——留到以后用。我们还要更新这个 get_max_entry_price 函数：与其在 API 调用里按 symbol 过滤，我打算去掉那个，改成 `if order.filled_avg_price`——

**54:29** · exists and the order. symbol matches the symbol that we are filtering for then we will consider it for a price in the list and we'll take the max price that's going to be our initial entry price then we're

> ——存在，并且 `order.symbol` 匹配我们正在过滤的 symbol，那么我们就把它的价格纳入列表，取最大价格，那将是我们初始入场价。然后我们——

**54:44** · going to place buy orders at each level corresponding to the draw down that we set initially okay home stretch for the trading system itself we need to create a new function here this is probably going to be the most

> ——会在对应于我们最初设置的回撤的每一层下买入单。好，交易系统本身到了最后冲刺阶段。我们需要在这里创建一个新函数，这可能是最——

**55:00** · involved function we're going to call this trade system and we're going to iterate through all of the rows so we're going to say for symbol data in self. equities do

> ——复杂的函数。我们把它叫做 `trade_systems`，我们要遍历所有的行。所以我们写 `for symbol, data in self.equities.items():`——

**55:14** · items we are going to go ahead and say if the status of the system is equal to on that means we are trading we're going to say that a position does not exist initially we're going to try to get the

> ——我们要写：如果系统的 status 等于 On，那就意味着我们在交易。我们先把 position（仓位）设为不存在（position_exists = False），然后我们尝试从 API 获取——

**55:33** · position from the API we're going to get the entry price as the max entry price we're going to set the

> ——仓位。我们把入场价取为最大入场价，然后设置——

**55:54** · position set the position exists flag to True should all of this run with no error if we don't have any active positions we're not going to find any data so we can actually accept exception as

> ——position（仓位），把 position_exists 标志设为 True，这一切都应该无错误运行。如果我们没有任何活跃持仓，我们将找不到任何数据，所以我们可以 `except Exception as`——

**56:07** · e and we can say api. submit order and we're actually going to place an initial Market order here so we'll say symbol is equal to symbol that's the symbol that we are creating in that system quantity is equal to one this

> ——`e:`，然后调用 `api.submit_order`。我们实际上要在这里下一个初始市价单（market order）。所以我们写 `symbol=symbol`——那是我们在那个系统里创建的股票——`qty=1`，这个——

**56:26** · side will be a buy we will use a market order and the time and force will be good until canell so this is our initial order we can add a message box to show

> ——side 是买入（buy），我们使用市价单，time_in_force 设为 good till canceled（一直有效，直到取消，gtc）。所以这是我们的初始订单。我们可以加一个消息框来显示——

**56:45** · the info that we have placed in order so we'll call this order placed this is our initial order so we can say initial order placed for and we can use the

> ——我们已经下了一笔订单的信息。所以我们把它叫做 "Order Placed"——这是我们的初始订单——我们写 "Initial Order Placed for"，然后可以用——

**57:05** · symbol let's sleep for 2 seconds to let it fill and then we can say the entry price is equal to self. Max entry price symbol and this is hopefully going to be our initial entry price based on the order the initial

> ——symbol。让我们 `time.sleep(2)` 两秒，让它成交。然后我们说 `entry_price = self.get_max_entry_price(symbol)`，希望这是我们基于刚才提交的初始订单——

**57:24** · order that we've submitted here we could also print the we could print the the entry price so we can print the entry price uh

> ——的初始入场价。我们也可以打印——我们可以打印入场价，所以 `print(entry_price)`，嗯——

**57:44** · we're going to generate levels based on this entry now so this is pretty much what we had written before but we're actually applying it to the real price so we're going to say level prices is equal to to I + 1 and then

> ——现在我们要基于这个入场价生成各层级。这基本是我们之前写过的，但现在我们真正把它应用到真实价格上。所以我们写 `level_prices = {i+1: round(`，然后——

**57:59** · round the entry price * 1us the draw down that we specified when we created that Equity system time I + 1 and then we're going to round that to two and this is going to be for I in range and this is going to be the

> ——`entry_price * (1 - data['drawdown'] * (i+1))`，四舍五入到两位小数，`for i in range(...)`。这就是——

**58:18** · length of the levels so data levels So based on the number of levels we have we are going to want to preserve our existing levels so we're going to say existing levels is equal to self.

> ——levels 的长度，即 `data['levels']`。所以基于我们已有的层数，我们想要保留现有的层级，所以写 `existing_levels = self.`——

**58:36** · equities do get symbol an empty dictionary. getet levels and now we're going to actually iterate through the level prices so we

> ——`equities.get(symbol, {}).get('levels', {})`。现在我们要真正遍历 level prices，所以我们——

**58:56** · will say for level in or we should say level and price in level prices do items we're going to say if level in self. equities symbol based on the symbol that

> ——写 `for level, price in level_prices.items():`，我们写：如果 level 在 `self.equities[symbol]` 里，基于我们——

**59:12** · we're traing based on the levels if this exists then we are going to place an order we're going to place an order at the symbol at the price and at that level of course once we do this we're

> ——交易的股票，基于这些层级，如果这存在，那么我们就会下单。我们会在那个股票、那个价格、那个层级下订单。当然，一旦我们这样做，我们就——

**59:31** · going to want to make sure that we [Music] save we're going to make sure that we save this information so self that save equities we also want to refresh the table and this is going to be inside the

> ——要确保（音乐）保存——我们要确保保存这些信息，所以 `self.save_equities()`，我们还想刷新表格。这要在——

**59:45** · for Loop so this is making sure that it's in line with the if statement here um we're going to make sure that we save the information and update the

> ——for 循环里面，所以要确保它与这里的 if 语句对齐。嗯，我们要确保保存信息并更新——

**60:08** · table for level price I guess we need to update the equities data as well so I should really do that before saving so I'll say for level and levels we have our existing levels

> ——表格。对于 level_price，我想我们也需要更新 equities 数据，所以其实应该在保存之前做这个。所以我写 `for level in levels:`，我们有 existing_levels——

**60:29** · right so for level and level prices if level okay I see what's going on here so really this should be level prices and level items if level is not in existing levels and negative level not in

> ——对吧。所以 `for level, price in level_prices.items()`——如果 level……好，我明白这里是怎么回事了。所以其实应该是 `level_prices.items()`：如果 level 不在 existing_levels 里，而且 -level（负层级）也不在——

**60:49** · existing levels then the existing levels is going to be equal to the level price that makes sense and then self. equities symbol the entry price and this is where we're actually going to update the data

> ——existing_levels 里，那么 `existing_levels[level] = price`，这说得通。然后 `self.equities[symbol]['entry_price'] = entry_price`——这就是我们真正更新数据——

**61:08** · to be the true entry price self do self. equities symbol this is going to be the levels we're going to update the levels to be the existing levels and then we're going to update the

> ——、把 entry_price 设为真实入场价的地方。`self.equities[symbol]['levels']`——把 levels 更新为 existing_levels，然后我们更新——

**61:29** · position as a flag to indicate that we are in an active position now we go about placing the ORD so now that we have the levels in which the orders need to be placed at based on the initial entry price and that initial

> ——position（仓位），作为一个标志来表示我们正处于活跃持仓中。现在我们开始下单。既然我们有了基于初始入场价需要下单的各个层级，而那个初始——

**61:47** · entry price is based on the max entry we can go through here and say four level prices and level price do items we will say if level in self. equities

> ——入场价又基于最大入场价，我们就可以在这里遍历：`for level, price in level_prices.items():`，我们写：如果 level 在 `self.equities`——

**62:05** · symbol levels exists then we can place an order place order and we're going to place an order at the symbol at the price and the

> ——`[symbol]['levels']` 里存在，那么我们就能下单（place_order），我们会在那个股票、那个价格、那个——

**62:23** · level wonderful and then we we're going to go ahead and save the equities data that we just updated here we're going to refresh the table and we are also going to return if the system is off so this is if the system is on then we're going

> ——层级下订单，太好了。然后我们会保存我们刚刚更新的 equities 数据，刷新表格。如果系统是关的，我们就返回。所以这里：如果系统是开的，那么我们就——

**62:40** · to go through this argument to try to to try to trade otherwise we will just return nothing now we got to write a function to place the order so we take a symbol a price and a

> ——走完这一整套逻辑去尝试交易；否则我们什么都不做，直接返回。现在我们要写一个下单的函数：它接受一个 symbol、一个 price 和一个——

**63:02** · level and that's going to allow us to update the data on the back end so we will say if there's a negative level in self. equities that means that we have an active order out for that level and we

> ——level，这将让我们在后端更新数据。所以我们写：如果 `self.equities[symbol]['levels']` 里有一个负的层级（negative level），那意味着我们有一个针对该层级的活跃订单，我们——

**63:17** · don't want to trade and this could be either a string or an integer representation so I'm going to include both depending on if you've reloaded the

> ——就不想交易。这可能是字符串或整数表示形式，所以我会同时包含两者，取决于你是否重新加载了——

**63:33** · system okay so if we have active orders out then we're just going to return otherwise we can try to submit the order and we're submitting the order for each level iteratively that's what this trade system function

> ——系统。好，所以如果我们已经有活跃订单在外面，就直接返回；否则我们可以尝试提交订单。我们为每一层迭代式地提交订单——这正是这个 trade_systems 函数——

**63:50** · is doing it's iterating through each of the levels and here we're going to say try API submit order we're going to submit an order where we have the symbol is equal to the given symbol and then we're going to

> ——在做的事：它遍历每一层。这里我们写 `try: api.submit_order`，我们提交一个订单，symbol 等于给定的 symbol，然后我们——

**64:08** · have quantity is equal to one side is equal to BU type is equal to limit the time and force is going to be good till cancelled and the limit price of course

> ——设置 qty=1，side=buy，type=limit（限价单），time_in_force 设为 good till cancelled，当然还有 limit_price——

**64:27** · is going to be the price that we have passed through as an argument to this function from the trade system function and now we need to Mark the level in the data so we can update the user interface so we'll say self.

> ——就是我们从 trade_systems 函数传进来的那个 price 参数。现在我们需要在数据中标记这个层级，以便更新用户界面。所以我们写 `self.`——

**64:46** · equities symbol we're going to update the levels we're going to make it negative level to indicate that we have an active position we'll set price equal to the price we're going to delete the original

> ——`equities[symbol]['levels'][-level] = price`，我们把它设为负层级，以表示我们有一个活跃持仓。我们把价格设为 price，然后删除原来的——

**65:01** · positive level delete the original positive level and we can even print if we so choose to place order for

> ——正层级：`del self.equities[symbol]['levels'][level]`。如果我们愿意，甚至可以打印："Placed order for"——

**65:21** · symbol at and we'll just give it the limit price and then if this does not work then we can just we'll do a message box. show

> ——`{symbol}@{price}`，给它限价。如果这不管用，那么我们就弹一个消息框（messagebox）——

**65:39** · error and then the error will be order error and whatever the response is and that should do it so these are probably the most involved functions um

> ——`showerror`，错误内容会是 "Order Error" 以及响应信息。这样就行了。所以这些大概是最复杂的函数，嗯——

**65:58** · unsurprisingly we are going to check to see if the position exists um you know that's kind of just baked into this function call here so you know we don't really need an if statement directly and then we're going

> ——毫不意外。我们会检查仓位是否存在——嗯，你知道，这其实已经隐含在这个函数调用里了，所以我们并不真的需要直接的 if 语句。然后我们要——

**66:12** · to go through this entire argument to set up an initial order set that as our entry price create levels based on that new entry price based on our draw down to enter more positions into that Equity uh and then we're going to create this

> ——走完这一整套逻辑：设置初始订单、把它作为入场价、基于那个新入场价和我们的回撤创建各层级、以在该股票中建立更多仓位。嗯，然后我们要创建这个——

**66:26** · function here which is going to iteratively update the I'm sorry the trade system iteratively places orders and we're going to update the level on the place order function and that level is going to be positive if an

> ——函数，它用来迭代更新——抱歉，trade_systems 是迭代地下单，而在 place_order 函数里我们要更新层级。如果某个——

**66:41** · open order needs to be created or negative if an open order already exists the last thing to do looks like I forgot a for got a Col in here the last thing we need to do here

> ——开放订单需要被创建，层级就为正；如果开放订单已存在，层级就为负。最后要做的事——看起来我在这里忘了加一个冒号——我们这里需要做的最后一件事——

**66:56** · is scroll on down to the scroll on down to the def auto update function and I've already updated it here self. trade systems I believe this was self. update prices so you'll just replace this with self. trade

> ——是往下滚动到——往下滚动到 `def auto_update` 函数。我已经在这里更新过了：`self.trade_systems`。我相信这之前是 `self.update_prices`，所以你只要把它替换成 `self.trade_`——

**67:13** · systems all right looks like I called this trade systems and this really should be trade systems because we're iterating through each system all right so now we have trade system systems trade system if I

> ——`systems`。好，看起来我把它叫做 trade_systems，这其实就应该叫 trade_systems，因为我们在遍历每一个系统。好，现在我们有了 trade_systems。如果我——

**67:27** · run this guy here going to go ahead and create a apple trade at five levels with a draw down of 5% from the initial entry price we add it its status is currently off so we're not going to trade anything every time the system attempts to update

> ——运行它，我会创建一个 Apple，从初始入场价以 5% 的回撤交易 5 层。我们添加它，它的状态目前是 off，所以我们不会交易任何东西。每次系统尝试更新时——

**67:44** · so I will go ahead and toggle it turn it on I get an initial order placed message here if I go to my alpaca we can see that I have placed an order for Apple right

> ——所以我继续把它 toggle 打开。我在这里收到一条 "initial order placed"（初始订单已下单）的消息。如果我打开我的 Alpaca，我们可以看到我已经为 Apple 下了一笔订单，就——

**68:04** · here it looks like we're getting a little key error so we have a key error for level ah because it should be levels not level levels I do apologize this should be

> ——在这里。看起来我们遇到了一个小 key error（键错误）。我们有一个针对 level 的 key error——啊，因为它应该是 levels 而不是 level。抱歉，这应该是——

**68:24** · levels not level going to go ahead and I'm actually going to remove this apple ticker going to cancel that order on alpaca to cancel an order on alpaca all you got to do is go to your

> ——levels 而不是 level。我继续，实际上我要移除这个 Apple 股票。在 Alpaca 上取消那个订单——要在 Alpaca 上取消订单，你只需去你的——

**68:38** · positions cancel cancel all open and then we can retry so let me rerun this rerun this guy let's create a new Apple

> ——positions（持仓），然后 Cancel / Cancel All Open（取消所有未成交），然后我们就可以重试。所以我重新运行它，重新运行这个程序，让我们创建一个新的 Apple——

**68:56** · trade five levels 5% draw down add the equity there's our default data default levels we're going to go ahead and turn it on we'll get an initial entry price good there's our initial order we go on over to alpaca we see our Apple trade

> ——，交易 5 层、5% 回撤，添加这个股票。这是我们默认的数据、默认的层级。我们把它打开，会得到一个初始入场价。好，这是我们的初始订单。我们转到 Alpaca，看到我们的 Apple 交易——

**69:14** · has filled and now we see that we've placed orders at the subsequent levels so if we go back into [Music] our back into our alpaca here you can

> ——已成交。现在我们看到我们已经在后续的层级下了订单。所以如果我们回到（音乐）我们的 Alpaca 里，你可以——

**69:32** · see in the recent orders we have our 1 2 3 4 five orders and they're placed at the limits based on the draw down that we set in our user interface and as you can see now we're not placing any more orders

> ——在最近订单（recent orders）里看到，我们有 1、2、3、4、5 笔订单，它们都按照我们在用户界面里设置的回撤放在了对应的限价上。正如你看到的，现在我们不再下更多订单了——

**69:47** · everything should be correct and we are ready to let those orders fill and we can go ahead and modify those as we please we could enter new systems into our our trading bot if we wanted to we could add exit conditions we could do a

> ——。一切应该都正确，我们已经准备好让这些订单成交。我们也可以随意修改它们。如果我们愿意，可以往交易机器人里加入新系统，可以添加退出条件（exit conditions），可以做——

**70:04** · whole bunch of things uh we have our level prices here that match our limit prices negative keys to ensure that we don't replace orders in fact if I turn this off and I turn this back on you'll see that it requies the collect the

> ——一大堆事情。嗯，我们这里有的 level prices 与限价匹配，负的键（negative keys）用来确保我们不会重复下单。事实上，如果我把这个关掉再打开，你会看到它重新收集——

**70:18** · correct levels and level information you'll also see that it does not accident Al Place more trades right it's not placing those trades at the levels so we've successfully built our trading bot I can

> ——正确的层级和层级信息。你还会看到它不会意外地下更多单——对吧，它不会在这些层级重复下单。所以我们已经成功构建了我们的交易机器人。我可以——

**70:34** · go ahead and I can add other equities now here's one for J&J it's going to enter an initial trade as well if I turn it on so as soon as we turn it on here's our initial order for johnon and Johnson

> ——继续添加其他股票。现在这里有一个 J&J（强生）的：如果我打开它，它也会进入一笔初始交易。所以一旦我们打开它，这里就是强生（Johnson & Johnson）的初始订单——

**70:50** · and then it's going to update the levels and boom we are ready to go so now we have successfully built the trading component of our bot and we can move on to the artificial intelligence component the AI portfolio manager component all

> ——然后它更新各层级，轰的一下，我们就准备好了。所以现在我们已经成功构建了机器人的交易组件，可以进入人工智能组件——AI 投资组合经理组件。好——

**71:06** · right so we knocked out two knocked out three we're going to do four and then we're we're ready to go we can run this guy so of course we need to pip install open AI so we don't get a module not found error so we're going to do pip

> ——我们搞定了步骤二，搞定步骤三，接下来做步骤四，然后我们就可以运行了。当然，我们需要 `pip install openai`，以免出现找不到模块的错误，所以我们要运行 pip——

**71:20** · install open AI once this is good to go we're going to do what we did before and we are going to create a new Jupiter notebook and there is going to be open. iynb and we can test the API here before integrating

> ——install openai。一旦装好，我们就像之前一样，创建一个新的 Jupyter notebook，它就是 openai.ipynb。在把它集成进我们的机器人之前，我们可以在这里测试这个 API——

**71:39** · it into our bot in this jupyter notebook we're going to try to integrate the open AI API and you're going to need to go to openai and get an API key this is the platform. open.com API keys where you can go and get get it I'm going to be

> ——。在这个 Jupyter notebook 里，我们要尝试集成 OpenAI API。你需要去 OpenAI 获取一个 API key——就是 platform.openai.com/api-keys，你可以去那里拿到它。我打算——

**71:56** · using this secret key here I'm going to delete this afterwards but this is the key that I'm going to use you may need a paid account to access this I have a paid chat GPT subscription um but that being said you

> ——使用这里的这个 Secret Key。我稍后会删除它，但这就是我要用的密钥。你可能需要一个付费账户才能访问它——我有付费的 ChatGPT 订阅。嗯，但话虽如此，你——

**72:08** · could use any llm you would like it doesn't have to be a track GPT I'm just going to be using it for Simplicity sake all right we're going to import open Ai and open AI going to run this guy make sure

> ——可以用任何你喜欢的 LLM，不一定要是 ChatGPT。我只是为了简单起见才用它。好，我们导入 openai，运行一下，确保——

**72:25** · everything's imported correctly good and now we're going to create a function def get we'll we'll call it send maybe analyze message call it analyze message take a message as an

> ——一切导入正确。好，现在我们要创建一个函数 `def`……我们把它叫做 send，或者也许叫 `analyze_message`。就叫 analyze_message 吧，它接受一个 message 作为——

**72:44** · input and this is really where we're going to [Music] be you know sending that input message but also pre- prompting the llm with the information that we want it to speculate

> ——输入。这正是我们要（音乐）发送那条输入消息的地方，同时也要用我们希望 LLM 去分析的信息对 LLM 进行预提示（pre-prompting）——

**72:57** · on this will make sense in a moment so you know we need to construct some sort of portfolio data um and we're going to have to effect our open orders as well so what I'm going to do is I'm going to say portfolio data is equal to fetch

> ——。这稍后就有意义了。你知道，我们需要构建某种投资组合数据（portfolio data），嗯，我们还得包含我们的未成交订单（open orders）。所以我要写 `portfolio_data = fetch_`——

**73:13** · portfolio and then I will say open orders is equal to fetch open orders and what this is going to do is this is going to get the current information for our account and allow

> ——`portfolio()`，然后写 `open_orders = fetch_open_orders()`。这会做什么呢？这会获取我们账户的当前信息，并允许——

**73:29** · our llm to essentially act as our portfolio manager our pre- prompts is going to be a string we'll just make this

> ——我们的 LLM 本质上充当我们的投资组合经理。我们的 pre_prompt（预提示）将是一个字符串，我们直接把它——

**73:47** · a string and it's going to have all of the information about our account but also we're going to give it kind of like this just blanket instruction so we'll say you are an AI portfolio

> ——做成一个字符串，包含关于我们账户的所有信息，同时我们还要给它一条类似于笼统指令（blanket instruction）的内容。所以我们写："You are an AI Portfolio"——

**74:03** · manager responsible for analyzing my portfolio your tasks are the following one evaluate risk exposures of my current

> ——"Manager responsible for analyzing my portfolio. Your tasks are the following:"（你是一名 AI 投资组合经理，负责分析我的投资组合。你的任务如下：）第一，评估我当前——

**74:22** · Holdings to analyze my open limit orders and their potential impact three provide insights into portfolio Health

> ——持仓（holdings）的风险敞口（risk exposures）；第二，分析我的未成交限价单及其潜在影响；第三，提供关于投资组合健康度（portfolio health）的见解——

**74:41** · diversification trade adjustments Etc 4 we can [Music] say maybe I'll collapse this so we can

> ——、分散化（diversification）、交易调整（trade adjustments）等。第四，我们可以（音乐）——也许我折叠一下，这样我们就能——

**74:55** · see etc for speculate on the market Outlook based on current market conditions uh and then maybe five

> ——看到等等。第四，基于当前市场状况对市场前景（market outlook）进行推测。嗯，然后也许第五——

**75:14** · identify potential Market risks and suggest risk management strategies over overall answer the following question with priority having that background and this

> ——，识别潜在的市场风险并建议风险管理策略。总体而言，优先结合以上背景回答下面的问题。而这是——

**75:35** · is just going to be your message okay um you can also add here is my portfolio and this will be our portfolio data here is my

> ——你的消息。好，嗯，你还可以加上"Here is my portfolio:"（这是我的投资组合），这将是我们的 portfolio_data；"Here are my"——

**75:55** · my here are my open orders whoops this need to scroll down here are my open orders give it the open orders so we're getting the open orders getting the portfolio data giving it to the prompt and then we want them to answer the

> ——"open orders:"（这些是我的未成交订单）——哎呀，需要往下滚动——"Here are my open orders"，把 open_orders 给它。所以我们获取未成交订单、获取投资组合数据、把它们喂给提示词，然后我们希望它们回答——

**76:13** · message from the user based on the input into the form oky dokie that should be it now the respon response is going to be open ai. chat

> ——用户基于表单输入的消息。好的，就这样。现在 response 将是 `openai.Chat`——

**76:31** · completion. create and we're going to create a new session here model is equal to gp4 then we're going to say messages equal to we'll have this dictionary of rule and then there's

> ——`Completion.create`。我们要在这里创建一个新会话，model 设为 gpt-4，然后写 messages，它会是这个字典：role 是——

**76:47** · the system and then the content is going to be the pre- prompt and then we can say API key is equal to this crazy API key which I copied from that

> ——system，然后 content 将是 pre_prompt。然后我们可以写 `api_key=`，等于这个我复制的超长 API key，我是从那个——

**77:05** · developer portal okay so then the analysis s should just [Music] be equal to the Gap portfolio or what do we call this analyze

> ——开发者门户复制的。好，那么 analysis 应该（音乐）等于——Gap portfolio？还是我们把这个叫什么？`analyze_`——

**77:22** · message um how is my Port how is my [Music] portfolio portfolio doing now we need to create these functions to actually get the data so to get the portfolio data we need to

> ——`message("How is my portfolio doing?")`。现在我们需要创建这些函数来真正获取数据。所以为了获取投资组合数据，我们需要——

**77:42** · create death portfolio and this is just going to be positions is equal to api. list positions uh portfolio is equal to nothing and then we're going to say for position in

> ——创建 `def fetch_portfolio`。它只是：`positions = api.list_positions()`，`portfolio = []`，然后我们写 `for position in`——

**78:03** · positions we are just going to append all of the information to the portfolio um as a dictionary so we have the symbol is going to be equal to the position. symbol we have the quantity is equal to

> ——`positions:`，我们只是把所有信息作为字典 append 到 portfolio 里。所以我们有：symbol 等于 `position.symbol`；quantity（数量）等于——

**78:20** · the position. quantity we have the entry price is equal to to the pos. average entry price we have the current price is going to be equal to the current

> ——`position.qty`；entry price 等于 `position.avg_entry_price`；current price（当前价格）等于 `position.current_`——

**78:39** · price we have the unrealized pnl which is equal to the unrealized pnl of our position respectively and then of course the side which is going to be long or short in this system everything should be long

> ——`price`；unrealized pnl（未实现盈亏）分别等于仓位的未实现盈亏；然后当然还有 side（方向），它是多头（long）或空头（short）——在这个系统里一切都应该是——

**78:59** · only all right so that's going to be our portfolio and we're going to return this portfolio and we're going to use that portfolio in our pre-prom and then we're just going to do the exact same thing with the uh the

> ——多头（long-only）。好，那就是我们的投资组合，我们返回这个 portfolio，把它用在我们的 pre_prompt 里。然后我们对——嗯——未成交订单——

**79:11** · open orders and this is a lot easier because you know all we got to do is orders equal to api. list orders status is equal to open uh and then we can just say open

> ——做完全相同的事情。这会容易得多，因为你知道，我们只需要 `orders = api.list_orders(status='open')`，嗯，然后我们可以直接写 `open_`——

**79:29** · orders is equal to an empty list and then we'll say for order in orders we can just do open orders. append we're just going to pen that dictionary just as we did before where we have our symbol being

> ——`orders = []`，然后我们写 `for order in orders:`，我们只需 `open_orders.append` 那个字典，就像我们之前做的那样，其中有我们的 symbol——

**79:45** · the order. symbol we have the quantity being the order. quantity we have the limit price being equal to the order. liit price and we have the side being it's always going to be long here

> ——等于 `order.symbol`；quantity 等于 `order.qty`；limit price 等于 `order.limit_price`；还有 side——在这里它总是——

**80:05** · so I think it's Buy in this API so I'm just going to live it leave the side as bu um that should be should be okay all right and then clearly the API is not in this Jupiter notebook so I'm just going to go back to the alpaca notebook and

> ——多头（long），所以我想在这个 API 里它是 buy（买入），所以我直接把 side 留成 buy。嗯，那应该没问题。好，然后显然这个 API 不在这个 Jupyter notebook 里，所以我回到 Alpaca notebook，——

**80:21** · I'm going to copy all the information that establish that object run it here and we should be able to actually get a response from from this guy here so let's take a look all right this

> 我把建立那个对象（API 连接）所需的所有信息复制过来，在这里运行，我们就应该能从这个家伙那里得到真实的响应。我们来看看。好，这个——

**80:41** · is the API removed in V1 so I should pep install uh version 28 so let's do that open AI equal equals 0.28 so I'm going to run this pip install

> ——API 在 V1 中被移除了，所以我应该 pip install……嗯……0.28 版本。让我们做 `pip install openai==0.28`，所以我运行这个 pip install——

**81:01** · instead and then I'm going to restart this so all I did was I ran this this pep install pep install openingi equals equals 0.28 because I was having a version issue it looks like run this guy run this guy we'll run

> ——来代替。然后我重启这个（内核）。所以我做的只是运行 `pip install openai==0.28`，因为之前遇到了版本问题。看起来……运行它，运行它，我们运行——

**81:19** · this guy see if we can get a response B Bas on our

> ——它，看看我们能否根据我们的——

**81:44** · portfolio Okay let's look at the analysis and and I forgot to return the response so that is going to make it so that the analysis is empty so we'll

> ——投资组合得到响应。好，我们看一下 analysis——我忘了 return response（返回响应），所以这会导致 analysis 是空的。所以我们——

**82:03** · return the response choices I'm going to edit that part out because we sat there for like 20 seconds so choices zero message and

> ——返回 `response['choices'][0]['message']['content']`。我要把那部分剪掉，因为我们坐在那里等了大约 20 秒。所以是 `choices[0]['message']` 和——

**82:19** · content so that's going to actually return the information to that analysis so let's try this again can't believe I forgot the return statement explains why this was blank

> ——`['content']`，这会把信息真正返回给 analysis。所以我们再试一次。真不敢相信我忘了 return 语句——这解释了为什么之前是空白的——

**82:38** · though it's going to take a little bit of time we run this I've analyzed your portfolio and boom here's some risk exposures use a concentrated position so

> ——。虽然会花一点时间。我们运行这个："I've analyzed your portfolio"（我已分析你的投资组合），轰，这里是一些风险敞口："use a concentrated position"（你的持仓集中度很高）——所以——

**82:53** · on so pretty cool now we have a way for AI to speculate about our portfolio all right we got to integrate this now into our trading bot so that it functions and then we'll be all done and we have a AI

> ——。挺酷的。现在我们有了让 AI 分析我们投资组合的方法。好，我们现在必须把它集成到我们的交易机器人里，让它发挥作用，然后我们就大功告成，拥有一个——

**83:09** · trading bot capable of placing trades and managing our portfolio analyzing our portfolio so what I'm going to do is I'm going to first start by copying and pasting these fetch portfolio functions these are just you know functions that

> ——能够下单、管理我们投资组合、分析我们投资组合的 AI 交易机器人。所以我要做的第一件事，是复制粘贴这些 fetch_portfolio 函数——你知道，它们就是——

**83:23** · can exist outside side of the trading bot class and I'm going to be replacing um really we don't need these anymore um there there's still placeholders for different initial calls in our trading b class so I'm just going

> ——可以独立于交易机器人类的函数。我会替换——嗯，其实我们不再需要这些了——嗯，我们交易机器人类里仍然有一些不同初始调用的占位符，所以我打算——

**83:40** · to leave them for now and I'm going to place these F portfolio and F open orders functions right underneath where I Define the alpaca API similarly I'm going to actually Define that open AI uh package so I'm going to say import open

> ——暂时留着它们。我会把这些 fetch_portfolio 和 fetch_open_orders 函数放在我定义 Alpaca API 的正下方。同样地，我实际上要定义那个 openai 包，所以我写 `import open`——

**83:58** · Ai and I'll go back over here and I'm going to just go ahead and create this function analyze message so I'm just going to copy all this guy here turn response everything should be good so I'm going to copy it

> ——`ai`。我会回到这里，直接创建 analyze_message 这个函数。所以我把这一整段复制过来——turn、response——一切应该都没问题。我把它复制——

**84:13** · going to come back over to the bot and notice here this is the mock response right to that initial message um instead we can just make that the actual response so the response here right that's this analysis we stored it in

> ——过来，回到机器人代码。注意，这是对那条初始消息的 mock（模拟）响应。嗯，我们反而可以直接把它变成真正的响应。所以这里的 response——对，就是那个 analysis，我们把它存在——

**84:28** · analysis and this was the response so it's actually returning the correct response from the llm so I'm going to come over here and I'm going to just replace this with mock chat GPT

> ——analysis 里，这就是响应。所以它实际上返回了来自 LLM 的正确响应。我过来这里，直接把它替换成 mock_chatgpt_——

**84:44** · response you know if we're particularly lazy we could just leave it like this but I'm going to call this uh track GPT response I'm going to find that mock track GPT response where we actually Define that send

> ——response。你知道，如果我们特别懒，可以就这样留着，但我要把它叫做 chatgpt_response。我要找到那个 mock_chatgpt_response，找到我们实际定义 send——

**84:56** · message function and I am going to call that cck GPT response because this is no longer a mock function call this is a true function call and that should do it that should

> ——message 函数的地方，把它改成调用 chatgpt_response，因为这不再是一个模拟函数调用，而是一个真正的函数调用。这样就该行了，应该——

**85:13** · do it so this is going to be the Moment of Truth here let's see if we can run this creating system we got our our AI portfolio manager here can ask what does my risk exposure look like

> ——就可以了。所以这将是一个关键时刻。我们看看能否运行它。创建一个系统，我们这里有了 AI 投资组合经理，可以问："我的风险敞口看起来怎么样？"——

**85:34** · holding both J&J and Apple so we can send this this is going to take some time to populate

> ——同时持有 J&J 和 Apple。所以我们发送这个，这会花一些时间来生成——

**86:04** · and here we go we have our AI portfolio manager responding to our question based on our pre- prompt and this is a pretty hefty response you could pre- prompt to make this you know shorter you could ask more

> ——。好了，我们的 AI 投资组合经理基于预提示（pre-prompt）响应了我们的问题。这是一个相当详尽的回答。你可以调整预提示让它更简短，你可以问更——

**86:24** · tar targeted questions or maybe even make it more General but this is an AI trading bot we have a trading bot that has success or we really built a system from scratch here we built our user interface we built a trading component

> ——有针对性的问题，或者甚至让它更泛化。但这是一个 AI 交易机器人——我们有一个成功的交易机器人。或者，我们真的从零构建了一个系统：我们构建了用户界面，构建了交易组件——

**86:39** · so there's the automated trading component and then we also have our portfolio management component the AI portfolio manager who can analyze our risk and risk exposures there's so much you can do built off of this just

> ——，所以有了自动化交易组件；然后我们还有投资组合管理组件——AI 投资组合经理，它能够分析我们的风险和风险敞口。基于这个——

**86:53** · initial shell of a a platform you can add exit conditions you can add uh events such that the large language model could actually execute trades you you can do so much you could do it based on live news feeds Uh current current uh

> ——初始的平台外壳，你可以做太多事情了：可以添加退出条件，可以添加事件——让大型语言模型真正执行交易。你能做的太多了，可以基于实时新闻源（live news feeds）、当前——嗯——

**87:10** · macro factors you can just go down the line but this is uh probably the most this is a a workshop video really we we built this entire system from scratch I'm going to post this on my GitHub so of course you know you access to all of

> ——宏观因素（macro factors），你可以一路列举下去。但这可能是最——这真的是一场工作坊式的视频。我们从零构建了整个系统。我会把它发布到我的 GitHub 上，当然你知道，你可以访问——

**87:24** · the code but this is some pretty cool stuff man I I really hope you enjoyed uh building this guy with me or you know if you're just checking out the the final product I I hope you enjoy um you know seeing the functionality here

> ——所有代码。但这确实是很酷的东西。老兄，我真的很希望你喜欢和我一起构建这个家伙——或者你知道，如果你只是在欣赏最终成品，我希望你喜欢，嗯，看到这里的这些功能。

**87:40** · essentially what we've done is we've built this user interface from scratch we have the ability to define a trading system for a particular Equity we specify the levels that we want to trade at the draw down percentage for each of

> 本质上，我们做的是从零构建了这个用户界面。我们有能力为某只特定的股票定义一个交易系统：我们指定想要交易的层级、每一个层级的回撤百分比——

**87:51** · those levels then our system automatic ly places those trades with alpaca it's going to place an initial order that's our entry price and it's going to Define levels below that entry price and it's going to do that for every equity in our

> ——。然后我们的系统通过 Alpaca 自动下单：它会下一个初始订单——那是我们的入场价——然后在那个入场价下方定义各层级。它会对我们投资组合里的每一只股票都这样做——

**88:06** · portfolio here um we can toggle the systems on and off as we choose to do so and we can even you know remove them and whatnot and we also have this you know AI portfolio management component this AI you know this AI aspect where we have

> ——。嗯，我们可以随心所欲地把系统打开或关闭，甚至还可以移除它们等等。我们还有这个 AI 投资组合管理组件——这个 AI 方面，我们——

**88:20** · an llm llm integrated into our trading system and it's receiving our portfolio and our trades in real time you know as we ask it questions it knows what's going on based on our pre-prom in so that being said I hope you enjoy this

> ——把一个 LLM 集成到了我们的交易系统中，它实时接收我们的投资组合和交易。你知道，当我们问它问题时，它基于我们的预提示了解正在发生什么。话虽如此，我希望你喜欢这——

**88:34** · video where we've built an AI trading bot together if you're interested in more videos like this in the future please let me know and I would be happy to make them I know this was quite a long one but I think the final product

> ——期视频——我们一起构建了一个 AI 交易机器人。如果你以后对更多这样的视频感兴趣，请告诉我，我会很乐意制作。我知道这期相当长，但我认为最终成品——

**88:47** · is pretty cool and we can even go about building off of this maybe we do some signal processing with a maybe we do you know some sort of of Entry exit condition uh based on the llm there's really a an infinite number of ways we

> ——非常酷。我们甚至可以在它基础上继续构建：也许我们做某种信号处理，也许做某种基于 LLM 的进出场条件。嗯，真的有无穷无尽的方式——

**89:03** · could go uh from here so I hope you've enjoyed this video this one was was quite a long one but like I said I think the final product is is pretty cool and uh I just want to thank you guys so much for watching and I will see you in the

> ——可以继续往前走。所以我希望你喜欢这期视频。这一期确实相当长，但就像我说的，我认为最终成品非常酷。嗯，我只想非常感谢大家的观看，我们——

**89:18** · next video

> ——下期视频见。
