# 龙虾头条 RSS 托管（GitHub Pages 免费版）

## 节目定位与调性（Editorial Memory）

> **从科技和社会变化出发，讨论普通人在变化中的真实处境与选择。**
>
> 不是新闻播报，不是科技媒体，也不是人生鸡汤。更像一个长期观察 AI 时代的人，把自己真正想明白的一件事，用几分钟讲给另一个成年人听。

### 核心视角

《龙虾头条》的核心不是“AI 新闻”，而是**AI 与社会变化中的人**。AI 是重要的观察窗口，但不是节目的边界。选题可以来自科技、工作、教育、住房、消费、人与人的关系、生活方式和社会结构，只要它最终回答一个问题：**世界的规则正在发生什么变化，这对普通人的生活意味着什么？**

节目不满足于“发生了什么”，而更关注“这件事意味着什么”。典型内容结构是：

**一个正在发生的变化 → 一个不那么显然的判断 → 对个人生活、工作或社会结构意味着什么。**

### 观点与语言

- **有观点，但不喊观点。** 从现象和事实出发，把推理过程讲清楚，最后给出克制但明确的判断。
- **寻找反常识，但不制造反常识。** 好选题通常包含一个小的认知翻转：大家已经知道 A，但真正值得讨论的可能是 B；B 必须有事实、逻辑或真实案例支撑。
- **技术最终落回人。** 即使讨论模型、Agent、算力、融资或基础设施，也要解释它与普通人的工作、钱、教育、关系和生活方式有什么关系。
- **像聪明朋友聊天，而不是论文、咨询报告或自媒体喊话。** 短句、口语、具体例子、少术语；即使是复杂技术，也尽量让非专业听众听懂。
- **避免信息堆砌。** 节目的价值不是覆盖尽可能多的信息，而是把一件值得想清楚的事情真正讲明白。

### 目标听众

大致面向 25–45 岁、对科技、社会与个人选择感兴趣，但并不希望每天泡在科技新闻里的城市成年人。他们可能关心 AI，但更深层关心的是：我的工作会怎样、应该学什么、钱怎么花、房子是否仍然重要、人与人的关系为什么变化、未来什么值得投入时间。

### 选题检查

每一期原则上用以下问题筛选：

1. 这件事最近真的在发生吗？
2. 它背后有没有一个比新闻本身更大的变化？
3. 有没有一个值得讲的非显然观点？
4. 它和普通人的工作、钱、教育、关系或生活方式有什么关系？
5. 能不能用具体例子讲清楚，而不是堆概念？
6. 最后能不能留下一个判断，而不是只做信息汇总？

只有事实和信息、没有第二层含义，容易变成普通新闻；只有观点和人生判断、没有事实基础，又容易变成鸡汤。**最好的《龙虾头条》选题位于“科技 / 社会观察”和“个人生活”的交界处。**

可以把节目的隐性 slogan 理解为：

> **世界正在变，我们聊聊这对你意味着什么。**

## 内容制作流程（重要）

每一期先在 ChatGPT 对话中完成内容创作，再进入 GitHub 发布流程：

**讨论选题 → 明确核心判断 → 打磨结构与文字 → 用户确认定稿 → 进入 GitHub 流程 → Podcast 与文字版同步发布。**

在用户明确表示“定稿”“可以发布”“进入 GitHub 流程”之前，不应直接修改发布内容或开始发布。Podcast 与文字版是同一期内容的两种输出形态，应保持标题、核心观点和内容语义一致。

这部分 README 同时作为节目长期的 **editorial memory / agent context**：未来 ChatGPT、Codex 或其他 agent 参与选题、写稿或发布时，应先遵循这里记录的节目定位、调性和工作流。

---

## 1) 上传到 GitHub
```bash
cd ~/Downloads/龙虾头条/rss-hosting
git init
git add .
git commit -m "init podcast rss"
git branch -M main
git remote add origin git@github.com:YOUR_GITHUB_USERNAME/lobster-headlines-podcast.git
git push -u origin main
```

## 2) 开启 GitHub Pages
- Repo Settings → Pages
- Source: Deploy from branch
- Branch: `main` / `/root`

## 3) 替换 feed.xml 里的占位符
把 `YOUR_GITHUB_USERNAME` 全部改成你的 GitHub 用户名。

## 4) 提交到小宇宙
RSS 地址：
`https://YOUR_GITHUB_USERNAME.github.io/lobster-headlines-podcast/feed.xml`

## 5) 新增单集（命令行）
```bash
cd ~/Downloads/龙虾头条/rss-hosting
python3 scripts/publish_episode.py \
  --base-url "https://YOUR_GITHUB_USERNAME.github.io/lobster-headlines-podcast" \
  --audio "/path/to/new-episode.mp3" \
  --slug "ep004-your-slug" \
  --title "你的标题" \
  --description "你的 shownotes" \
  --duration "00:05:00"

git add .
git commit -m "publish ep004"
git push
```
