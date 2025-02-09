---
title: Apt卸载残留的清理
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - linux
# nolastmod: true
draft: false
date: 2022-03-10T23:01:36+08:00
---

当你使用 apt remove卸载软件的时候，其实软件的配置文件会残留到系统里

<!--more-->
而使用apt purge卸载的软件就不会出现残留

而使用`apt remove`卸载过而有残留配置文件的该怎么清理呢？

教程如下

---

1. 确认是否有残留

`apt search "" | grep 配置文件残留`

如果有输出，就是有残留

![图片.png](https://storage.deepin.org/thread/202203102257154728_图片.png)

2. 执行

`dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P`

自动清除残留的配置文件

来源： https://blog.csdn.net/huangbo_2020/article/details/84419158
