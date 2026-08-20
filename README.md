# 龙虾头条

## Editorial Memory

> **从科技和社会变化出发，讨论普通人在变化中的真实处境与选择。**

不是新闻播报，不是科技媒体，也不是人生鸡汤。更像一个长期观察 AI 时代的人，把自己真正想明白的一件事，用几分钟讲给另一个成年人听。

核心结构：**一个正在发生的变化 → 一个不那么显然的判断 → 对个人生活、工作或社会结构意味着什么。** 有观点但不喊观点；寻找反常识但不制造反常识；技术最终落回人；像聪明朋友聊天，避免信息堆砌。

选题检查：最近真的在发生吗？背后有没有更大的变化？有没有非显然观点？和普通人的生活有什么关系？能否用具体例子讲清楚？最后能否留下一个判断？

## Production Gates

**IDEA → WRITE → FREEZE → PREFLIGHT → BUILD → LISTEN → PUBLISH → VERIFY**

- **IDEA**：对话中形成 Episode Brief：题目、为什么现在值得讲、核心判断、第二层含义、关键事实/案例、普通人视角。
- **WRITE / FREEZE**：在对话中写 canonical 稿、标题和 shownotes。用户明确“定稿”前不进入 GitHub 发布流程。
- **PREFLIGHT**：Editorial / Facts / TTS / Metadata QA。episode number 必须从现有 feed 推导；guid、音频文件名、文章音频链接必须一致。
- **BUILD / LISTEN**：生成与发布分离。先生成试听，检查发音、数字、断句、句间/段间停顿和整体节奏。
- **PUBLISH / VERIFY**：用户明确确认发布后才更新 R2、Podcast RSS 和文字版；随后验证线上音频、RSS、文章和 metadata 一致。

需要用户判断的核心节点只有：**选题、定稿、正式发布。**

## Canonical 稿 / TTS-ready

**定稿本身就是 TTS-ready canonical 稿；Podcast 与文字版正文使用同一份内容，不派生另一份改写稿。**

- 短句优先，一句话尽量一个主要意思；复杂句主动拆开。
- 朗读节奏是正文的一部分。自然使用逗号、句号和分段；少用括号、分号、连续破折号，不用奇怪标点 hack TTS。
- 数字、金额、百分比、年份、英文、缩写、品牌和人名在定稿前处理成自然、明确、可正确朗读的形式。
- URL、Markdown 元数据、脚注不进入需要朗读的正文。
- 不为了机器牺牲可读性：目标是同一份文字既好读，也像真人自然说出来。
- 文字文章正文与 canonical 口播稿保持逐字一致；标题/front matter、音频模块和 shownotes 属于正文之外的发布结构。
- 头条以约五分钟为基准；避免为了凑时长堆信息。成片明显低于约四分半时，应回看稿件是否论证不足，而不是机械拉慢语速。

## TTS / Pause Baseline

使用讯飞，默认 voice profile 为 `scripts/xfyun-tools/voice_profiles/default.json`。长文正式主路径恢复旧 SOP 已验证方案：**按自然段分段合成 + 段间约 350ms 短静音拼接**。

- 自然段优先作为 segment；过长段落才按句号/问号/感叹号继续拆，绝不从一句话中间切开。
- 经验区间约 **240–420 字/segment**；350ms 是 baseline，不是不可修改的常数。
- canonical 稿的标点负责句内自然 prosody；额外静音只负责段落/segment 层级，不用重复标点制造 double pause。
- 正式长文使用 `scripts/xfyun-tools/xfyun_segmented_run.py`；`xfyun_super_official_run.py` 保留用于短样片和排障。
- TTS 前必须确认 `XFYUN_APPID`、`XFYUN_API_KEY`、`XFYUN_API_SECRET` 均存在，并按脚本真实 CLI 参数调用，不凭经验猜参数。
- 首次使用新稿/新环境时先合成第一段作为最小样本，再批量生成。
- `pronunciation.json` 只处理少量 provider-specific 发音例外；`prepare_tts_text.py` 是辅助工具，不是 canonical 转换层。

## Audio QA

固定检查：**发音 ✓ 数字 ✓ 断句 ✓ 句间停顿 ✓ 段间停顿 ✓ 整体语速/节奏 ✓**。至少试听开头、随机中段、结尾；首次校准或出现异常时扩大试听。发现文本问题回到 canonical 稿修正；引擎 pause/prosody 问题则调整 profile/segmented synthesis，不用奇怪标点补救。

## Publishing Guardrails

每期至少有标题、shownotes、canonical 正文和音频。最终音频文件名不得包含内部音色名。RSS description 使用真实换行，禁止字面量 `\\n`。发布后留下轻量记录：`canonical ✓ tts ✓ audio QA ✓ R2 ✓ podcast RSS ✓ text RSS ✓ verified ✓`。

长期目标是 episode metadata 成为 single source of truth，避免 Podcast repo 与文字 repo 手工维护两套 metadata。

README 是当前 **editorial / TTS / workflow source of truth**。旧 OpenClaw SOP 只作为历史参考；其中本机绝对路径、旧 rss-hosting/audio 架构、消息平台交付规则和逐段进度回报不再属于现行标准。

## Tools

- `scripts/xfyun-tools/xfyun_segmented_run.py` — 正式长文 TTS
- `scripts/xfyun-tools/xfyun_super_official_run.py` — 单段/短样片/排障
- `scripts/publish_episode.py` — 发布工具
