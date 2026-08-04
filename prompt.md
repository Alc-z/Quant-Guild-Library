# Quant Guild 教学视频整理任务 Prompt

## 项目背景

该项目是 YouTube 教学视频（Roman Paolucci @QuantGuild）的配套项目，用于记录视频教学内容。每个视频对应一个目录，目录内应有以下文件：

- **视频地址文件**：`YouTube_Video_Link.txt.txt`（地址可能过期，需验证）
- **字幕文件**：`<序号>-subtitle.md`（英文字幕 + 逐段中文翻译）
- **教材文件**：`<序号>-notebook.md`（基于字幕和本地 ipynb 整理的中文教材）
- 本地已有的配套 ipynb 及其中的图片（如有）

## 执行步骤

### 1. 定位并验证视频

1. 读取目标目录中的 `YouTube_Video_Link.txt.txt`，用 yt-dlp 验证 URL 是否有效。
2. 若地址过期（视频不存在/标题不符），按**目录名去掉序号**在 YouTube 搜索对应视频（Roman Paolucci 频道）。
3. 确认视频归属：频道必须是 **Roman Paolucci @QuantGuild**，标题与目录名一致。

### 2. 获取视频元数据

```bash
yt-dlp --skip-download --print "%(title)s | %(upload_date)s | %(channel)s" "<watch_url>"
yt-dlp --skip-download --print "%(description)s" "<watch_url>"
```

记录：标题、上传日期、频道、视频简介。

### 3. 下载字幕

使用 yt-dlp 下载**自动生成的英文字幕**（注意用 `--write-auto-subs`）：

```bash
yt-dlp --skip-download --write-auto-subs --sub-langs en --sub-format srt -o "lec" "<watch_url>"
```

### 4. 检查配套 ipynb

1. 先看**本地课程目录**里是否已有 ipynb。
2. **有** → 直接使用，从中提取代码与图片供教材使用。
3. **没有** → **不要从 GitHub 下载**，跳过此步。该期视为概念向视频，教材直接基于字幕整理，视频中涉及的核心图表用 matplotlib 复现（保存为 PNG 嵌入教材）。

> 只有本地已存在的 ipynb 才会被利用；GitHub 仅作为查找/确认视频的辅助，不作为 ipynb 的来源。

### 5. 生成 `<序号>-subtitle.md`

**字幕分段**：解析 SRT，按约 15-20 秒/段（约 5-6 条字幕）分组为段落，段落间以时间戳开头（`**MM:SS** · 文本`），保留自动字幕原始断句。

**文件结构**：

```markdown
---
title: "<视频标题>"
source: "<完整 watch URL>"
author:
  - "[[Roman Paolucci]]"
published: <YYYY-MM-DD>          # 取上传日期
created: <YYYY-MM-DD>            # 今天
description: "<简介摘要>"
tags:
  - "clippings"
---

<视频简介全文>

## Transcript

**0:01** · <英文段落原文>

> <该段落的中文翻译>

**0:17** · <英文段落原文>

> <该段落的中文翻译>
...
```

要求：
- 英文原文保留自动字幕原始文本（含 `[Music]` 标记）
- **逐段翻译**，译文紧跟在对应段落下方（用 `>` 引用块）
- 译文需通顺、语义完整，术语保留英文注释（如 真实水平（true level）、实现值（realization）、方差窗口（variance window）、累积均值（cumulative mean）、滚动均值（rolling mean）、非平稳性（non-stationarity））

### 6. 生成 `<序号>-notebook.md`

**结构**（参考已完成目录的教材风格）：

- 标题 + 引言（标注视频来源链接）
- `1. 概述`：视频核心思想
- 若干章节：按视频逻辑组织（概念定义、方法、图表、代码示例、直觉解释）
- 表格总结关键概念
- 关键要点/一句话总结
- 延伸阅读（视频简介中的链接）
- 结尾注明整理来源

**要求**：
- 正文用中文
- **有本地 ipynb**：引用其中的代码块、图片（图片复制到目录下，用相对路径嵌入 `![说明](xxx.png)`）
- **无本地 ipynb**：不下载、不补做 ipynb，用 matplotlib 复现视频图表嵌入教材即可
- 术语中英对照，公式用 LaTeX

### 7. 更新视频地址文件

将 `YouTube_Video_Link.txt.txt` 内容更新为验证过的**完整 watch URL**：

```
https://www.youtube.com/watch?v=<视频ID>
```

### 8. 命名与存放

文件放在对应课程目录内，命名规范：

| 文件 | 命名 |
|------|------|
| 字幕 | `<序号>-subtitle.md` |
| 教材 | `<序号>-notebook.md` |
| 视频地址 | `YouTube_Video_Link.txt.txt` |
| 复现图表 | `<描述性名称>.png` |

## 参考模板

`2025 Video Lectures/10. A Quant's Visual Guide to Progress` 已按本规范完成，作为最新模板（无 ipynb 情形：`10-subtitle.md` + `10-notebook.md` + matplotlib 复现图表）。早期 1-9 目录使用无序号命名（`subtitle.md`/`notebook.md`），**新规范以带序号为准**。
