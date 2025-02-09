---
title: 删除所有git历史记录
author: shenmo
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
date: 2022-05-19T16:00:37+08:00
---

原文链接：https://blog.csdn.net/yc1022/article/details/56487680

<!--more-->

1.Checkout

   git checkout --orphan latest_branch

2. Add all the files

   git add -A

3. Commit the changes

   git commit -am "commit message"


4. Delete the branch

   git branch -D master

5.Rename the current branch to master

   git branch -m master

6.Finally, force update your repository

   git push -f origin master



————————————————

版权声明：本文为CSDN博主「yanchengyc」的原创文章，遵循CC 4.0 BY-SA版权协议

方便直接使用：
```
 git checkout --orphan latest_branch
 git add -A
 git commit -am "重置仓库到最新一次commit"
 git branch -D master
 git branch -m master
 git push -f origin master
```

注意：Gitee上还需要进行储存库GC来清理占用空间
