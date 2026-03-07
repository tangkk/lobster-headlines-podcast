# 龙虾头条 RSS 托管（GitHub Pages 免费版）

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
