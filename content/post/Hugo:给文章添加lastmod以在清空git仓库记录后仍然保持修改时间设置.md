---
title: Hugo:给文章添加lastmod以在清空git仓库记录后仍然保持修改时间设置
date: 2025-02-09T23:04:20+08:00
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - 折腾博客
# nolastmod: true
draft: false
---

修改自 https://cyrusyip.org/zh-cn/posts/2024/05/25/hugo-add-lastmod-to-posts/

<!--more-->


背景：本站文章的 lastmod（上次修改时间）就是 Git 提交的 author date（作者日期）。我需要清空git提交记录以精简仓库，这会导致所有文章的 lastmod 都变成清空日。文章内容没变就不应该改 lastmod，所以我打算给每篇文章都加上 lastmod，后面改动文章就 lastmod 就不会变。

先把 lastmod 的优先级调至最高，不然 Hugo 会继续使用 Git 提交日期。

```toml
# config.toml
[frontmatter]
  lastmod = ['lastmod', ':default']

```
在根目录新建 add-lastmod.sh，添加执行权限

```
touch add-lastmod.sh
chmod +x add-lastmod.sh
```

往 add-lastmod.sh 填入脚本内容。

```bash
#!/usr/bin/env bash
# usage: ./add-lastmod.sh directory-name
directory="$1"
files=$(find "$directory" -type f)
for file in $files; do
  echo "Processing: ${file}"
  # 获取该文件最新一次 Git 提交的作者日期，示例格式：2024-05-16T14:23:53+08:00
  lastmod_date=$(git log --no-show-signature -1 --format=%aI "$file")
  echo "Last modified date: $lastmod_date"
  
  # 使用 awk 检查 front matter 内是否已存在 lastmod 字段：
  # 如果存在则替换，否则在 front matter 结束前插入该字段
  awk -v new_lastmod="lastmod: $lastmod_date # remove this line if the content is actually changed" '
  BEGIN { frontmatter = 0; updated = 0 }
  # 检测到 front matter 分隔符（假设单独一行 ---）
  /^---[[:space:]]*$/ {
    frontmatter++
    # 当检测到第二个 --- 时，如果还没更新过，则在其前面插入 lastmod 字段
    if (frontmatter==2 && !updated) {
      print new_lastmod
      updated = 1
    }
    print
    next
  }
  # 如果当前处于 front matter 内（frontmatter==1）且发现已有 lastmod 字段，则替换
  (frontmatter==1 && !updated && $0 ~ /^[[:space:]]*lastmod:/) {
    print new_lastmod
    updated = 1
    next
  }
  { print }
  ' "$file" > tmpfile && mv tmpfile "$file"
done



```

添加 lastmod

```
./add-lastmod.sh content

```

即可固定lastmod时间，此时再进行清空即可