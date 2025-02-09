---
title: 解决hugo无法使用git提交时间作为更新时间
date: 2022-03-04T11:04:56+08:00
lastmod: 2022-03-04T11:04:56+08:00
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
---

在此之前我一直以为是`dream theme`不支持git date作为修改日期，提了issue，直到......

<!--more-->

https://github.com/g1eny0ung/hugo-theme-dream/issues/259  
这就是和作者的issue，真没想到，这个theme已经很久没更新了，没想到作者还在活跃
解决方案在这里  
https://github.com/gohugoio/hugo/issues/3071

---------

The reason I ask about the macOS is the NFD way they store filenames.

So, given a Git repo:
```
▶ echo "test" >> π.txt                                                                       ◒
▶ git  add -A && git commit
[master (root-commit) a5dd87f] Test
 1 file changed, 1 insertion(+)
 create mode 100644 "\317\200.txt"
```
So, this is an issue that lives outside of Hugo.

Try:

`git config --global core.quotePath false`

Alternatively:

`git config --global core.precomposeunicode true`

更改后即可按git时间更改

---

为了让主页的排序转为修改日期，我把`:git`也加入了`date`优先序列，指定优先，不指定则为git时间，这样只要更新帖子就会放到最前面

更改位置：`config.toml`

同时更改了`archetypes`，以后的新的Post不会再指定创建日期，转而在帖子正文写明