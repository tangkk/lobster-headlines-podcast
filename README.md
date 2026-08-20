# 龙虾头条 RSS 托管（GitHub Pages 免费版）

## 节目定位与调性（Editorial Memory）

> **从科技和社会变化出发，讨论普通人在变化中的真实处境与选择。**
>
> 不是新闻播报，不是科技媒体，也不是人生鸡汤。更像一个长期观察 AI 时代的人，把自己真正想明白的一件事，用几分钟讲给另一个成年人听。

### 核心视角

《龙虾头条》的核心不是“AI 新闻”，而是**AI 与社会变化中的人**。AI 是重要的观察窗口，但不是节目的边界。选题可以来自科技、工作、教育、住房、消费、人与人的关系、生活方式和社会结构，只要它最终回答一个问题：**世界的规则正在发生什么变化，这对普通人的生活意味着什么？**

节目不满足于“发生了什么”，而更关注“这件事意味着什么”。典型结构：

**一个正在发生的变化 → 一个不那么显然的判断 → 对个人生活、工作或社会结构意味着什么。**

### 观点与语言

- **有观点，但不喊观点。** 从事实和现象出发，把推理过程讲清楚，最后给出克制但明确的判断。
- **寻找反常识，但不制造反常识。** 大家已经知道 A，但真正值得讨论的可能是 B；B 必须有事实、逻辑或真实案例支撑。
- **技术最终落回人。** 模型、Agent、算力、融资或基础设施最终都要解释与普通人的关系。
- **像聪明朋友聊天。** 短句、口语、具体例子、少术语；避免论文、咨询报告和自媒体喊话。
- **避免信息堆砌。** 重点是把一件值得想清楚的事情真正讲明白。

### 选题检查

1. 这件事最近真的在发生吗？
2. 背后有没有一个比新闻本身更大的变化？
3. 有没有值得讲的非显然观点？
4. 和普通人的工作、钱、教育、关系或生活方式有什么关系？
5. 能否用具体例子讲清楚？
6. 最后能否留下一个判断？

> **世界正在变，我们聊聊这对你意味着什么。**

## Episode Production Gates

标准流程：

**IDEA → WRITE → FREEZE → PREFLIGHT → BUILD → LISTEN → PUBLISH → VERIFY**

### Gate 1 — IDEA / 选题

只在对话中进行，不碰 GitHub。形成简短 Episode Brief：**题目、为什么现在值得讲、核心判断、第二层含义、关键事实/案例、最终落到普通人的什么问题。**

### Gate 2 — WRITE + FREEZE / 成稿与定稿

在对话中完成结构和 canonical 稿。写作阶段同时遵守 Editorial 与 TTS-ready Guidelines。用户明确说“定稿”后，正文冻结为本期 canonical version；标题和摘要/shownotes 同时确认。**定稿之前 GitHub = 0 发布操作。**

### Gate 3 — PREFLIGHT

定稿后、生成音频前做一次简短检查：

- **Editorial QA**：调性、核心判断、结构、事实风险。
- **TTS QA**：人名、英文、数字、年份、符号、长句、断句与预期停顿。
- **Metadata QA**：episode number、slug、标题、description、日期。

结果应尽量简洁，例如：`Editorial ✓  Facts ✓  TTS ✓  Metadata ✓`。有问题先修 canonical 稿。

### Gate 4 — BUILD + LISTEN

从冻结的 canonical 稿生成音频，但**生成和发布分离**。Build 阶段不应自动对外发布。

Audio QA 固定检查：**发音 ✓　数字 ✓　断句 ✓　句间停顿 ✓　段间停顿 ✓　整体语速/节奏 ✓**。

至少试听开头、随机中段和结尾；首次校准或发现问题时应扩大试听范围。

### Gate 5 — PUBLISH + VERIFY

正式发布前展示简短 summary，包括 episode、标题、音频时长以及将更新的目标。用户确认发布后再执行：**R2 audio → Podcast RSS → 文字版 / 文字 RSS**。

发布后必须验证线上结果，而不是把 commit 成功视为发布成功。确认音频 URL、Podcast RSS 和文字版均可访问且 metadata 一致。

需要人工判断的三个核心节点只有：**选题、定稿、正式发布。** 其他步骤尽量由 agent / script 承担。

## Canonical 稿 / TTS-ready Guidelines

**定稿本身就是 TTS-ready 的 canonical 稿。不存在另一份自动改写后的 TTS transcript。** 文字版和 Podcast 使用同一份正文。

- 像真人说话：短句优先，一句话尽量只承载一个主要意思；复杂句主动拆开。
- **朗读节奏是 canonical 稿的一部分。** 定稿时必须按实际朗读逻辑检查断句和停顿，而不只是检查文字含义。
- 标点就是节奏：自然使用逗号、句号和分段；少用括号、分号、连续破折号。不要用奇怪标点 hack TTS。
- 数字、金额、百分比、年份在定稿时就写成**人能顺畅读、TTS 也能正确念**的形式。
- 英文、缩写、品牌、人名和术语在定稿时逐项考虑实际朗读效果。容易读错的表达直接改成自然可朗读写法。
- URL、Markdown 元数据、脚注等不应成为需要朗读的正文。
- 不为了 TTS 写出生硬的机器稿；目标是**同一份文字既适合阅读，也像真人自然说出来**。
- 本节目声音应清晰、理性、自然，避免新闻播报腔。

### 停顿原则

停顿问题分两类：

1. **稿件/标点造成的节奏问题**：在 canonical 稿阶段解决。
2. **TTS 引擎本身的 pause/prosody 问题**：不要通过反复添加奇怪标点解决；应在试听后记录为节目级 TTS/profile 调整。

目前不预设固定毫秒数。下一期开始以真实音频重新校准句间、段间和转折停顿；一旦找到稳定参数，再固化到 voice/TTS profile，使其成为脚本行为而不是人工记忆。

`scripts/pronunciation.json` 只记录少量 provider 特有发音 workaround；`scripts/prepare_tts_text.py` 是可选辅助工具，不属于标准稿件转换流程。

## Episode Record

每期发布后应留下轻量记录，至少能够确认：

`canonical ✓  tts ✓  audio QA ✓  R2 ✓  podcast RSS ✓  text RSS ✓  verified ✓`

长期目标是让 episode metadata 成为单一数据源，避免 Podcast repo 与文字 repo 手工维护两套相同信息。

README 同时作为长期 **editorial / TTS / workflow memory 与 agent context**。未来 agent 在选题、写稿、TTS 和发布前应先遵循本 README。

---

## 发布工具

音频发布脚本：`scripts/publish_episode.py`  
讯飞 TTS：`scripts/xfyun-tools/`