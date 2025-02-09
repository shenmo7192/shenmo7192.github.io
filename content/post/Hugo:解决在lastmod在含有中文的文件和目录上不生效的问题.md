---
title: Hugo:解决在lastmod在含有中文的文件和目录上不生效的问题
date: 2025-02-09T23:08:41+08:00
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

原因是 git 默认未设置 core.quotepath 为 false

<!--more-->


需要手动执行下 `git config  core.quotepath false` 后才能正确地读取到 lastmod 信息。然而，提交到github后，默认的流水线仍然没有设置这个变量，所以需要额外在部署的机器中执行此指令

其实[之前](https://blog.shenmo.tech/post/%E8%A7%A3%E5%86%B3hugo%E6%97%A0%E6%B3%95%E4%BD%BF%E7%94%A8git%E6%8F%90%E4%BA%A4%E6%97%B6%E9%97%B4%E4%BD%9C%E4%B8%BA%E6%9B%B4%E6%96%B0%E6%97%B6%E9%97%B4/)踩过这个坑，但是 尽管在提交的时候在本地已经完成了推送，但是并不会同步到服务端上
