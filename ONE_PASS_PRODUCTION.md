# One-Pass Production Checklist

这份清单汇总四档播客真实跑通后得到的共用经验。目标：下一期尽量一次走通，避免重复 TTS、半发布、RSS metadata 错误和文字站延迟误判。

## 1. Canonical 先天 TTS-ready

- 定稿就是 Podcast 与文字版共用 canonical，不再派生“朗读版”。
- 数字、金额、百分比、年份、人名、英文缩写在 FREEZE 前做 spoken-form pass；连续数字属于一个语义单元，禁止因排版或预处理拆开（例如“11万”的 11 与 万之间不能产生 segment pause）。
- 空行只表示真的需要明显长停顿/转场；普通短停顿只靠逗号、句号和引擎 prosody。不要为了视觉强调多分段。
- 调长长停顿时优先改 segmented synthesis 的 paragraph pause，不用重复标点或奇怪标点 hack。

## 2. Voice/profile 必须显式确定

- 每档使用 repo 内 voice profile 作为 source of truth，不凭记忆猜 voice/speed/volume/pitch。
- 多 profile 节目（尤其龙虾人物）每期必须显式声明 profile，Preview 禁止硬编码成 default。
- 新 voice / 新 endpoint / 授权异常时先做极短 smoke test；`11200 LiccCheck` 优先检查具体 voice / private capability / APPID entitlement，不把账户余额和具体 voice licence 混为一谈。

## 3. Draft PR 是唯一 staging boundary

- Preview 只由 PR 更新触发；不要同时监听 build branch push + PR，避免一次 commit 双倍 TTS。
- `concurrency + cancel-in-progress: true`：连续改稿只保留最新 Preview。
- Preview 不得写 R2、RSS 或文字站。
- Audio QA 批准的是一个具体 artifact，不是抽象的“这版稿”。记录 run_id、artifact_name、audio_filename、SHA256。

## 4. 发布只复用 approved artifact

- 新一期正式发布使用常驻 `Publish Approved Artifact` workflow + request JSON。
- request 至少锁定 run_id / artifact_name / audio_filename / SHA256 / slug / title / description / article_url / prefix。
- 发布前先验证：Secrets、GUID 不存在、episode number 是 feed 的下一期、artifact SHA256、MP3 非空、ffprobe 真时长、文件字节数。
- R2 与 RSS 写入必须在 metadata validation 之后；失败要 fail closed。
- Shell 禁止使用 `SECONDS` 等特殊变量名；使用 `AUDIO_SECONDS`。复杂逻辑放 Python 脚本，不在 YAML command substitution 中嵌 heredoc。

## 5. “新一期”与“重制已发布单集”是两条流程

- 已存在 GUID 的单集禁止走 normal publish。
- 重制使用 `replace-*.json` + `Replace Approved Episode Audio` workflow，GUID / title / article URL / R2 URL 不变，只替换 approved MP3，并更新 enclosure length 与 itunes:duration。
- replacement 在覆盖 R2 前先备份旧对象；如果 RSS commit/push 失败，必须恢复旧 R2，避免线上音频与 feed metadata 不一致。

## 6. 文字版必须在正式 VERIFY 中单独检查

- “文字 repo source 已 commit”不等于“网站已发布”。
- 文字文章必须 `draft: false`，播放器指向与 Podcast enclosure 相同的 R2 object。
- Hugo front matter `date` **不得晚于实际 build 时间**。GitHub Pages/Hugo 默认会跳过 future-dated content；建议发布时间使用实际当前时间或安全回拨 1–2 分钟。
- VERIFY 顺序：source entry 存在 → Pages workflow/deployment 成功 → article URL 可访问 → 首页/列表出现新 entry。
- 如 source 正确但 Pages 未更新，可安全 retrigger Pages；不要重复创建文章或重复发布 Podcast。

## 7. 发布后最终 VERIFY

必须逐项确认：

`canonical ✓ → preview artifact ✓ → audio QA ✓ → approved SHA ✓ → merge ✓ → R2 ✓ → podcast RSS ✓ → duration/length ✓ → text source ✓ → Pages ✓ → online article/list ✓`

Workflow 显示 success 不是最终成功定义；最终成功定义是生产端实际可见且 metadata 一致。

## 8. 操作纪律

- 每个有副作用的步骤只走一条明确路径，不并行创建多个候选 response / workflow 去写同一生产资源。
- 不盲目 rerun 失败 workflow；先确认失败发生在副作用前还是后，再决定修复方式。
- 临时排障 workflow 用完删除；长期只保留 Preview / Publish Approved Artifact / Replace Approved Episode Audio 三类通用入口。
