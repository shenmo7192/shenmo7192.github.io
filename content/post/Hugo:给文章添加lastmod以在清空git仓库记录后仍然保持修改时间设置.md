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
  echo "${file}"
  lastmod_date=$(git log --no-show-signature -1 --format=%aI "$file") # example: 2024-05-16T14:23:53+08:00
  echo "$lastmod_date"
  # Use awk to insert the lastmod line above the second ---
  awk -v lastmod="lastmod: $lastmod_date # remove this line if the content is actually changed" '
  BEGIN { frontmatter = 0 }
  /^---$/ { frontmatter++ }
  frontmatter == 2 && !printed { print lastmod; printed = 1 }
  { print }
  ' "$file" >tmpfile && mv tmpfile "$file"
done


```

添加 lastmod

```
./add-lastmod.sh content

```

即可固定lastmod时间，此时再进行清空即可