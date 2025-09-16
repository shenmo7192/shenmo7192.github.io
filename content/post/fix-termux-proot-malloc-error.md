---
title: 在proot-distro debian 13上解决WPS Office安装失败的问题
date: 2025-09-16T19:57:02+08:00
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - Linux
tags:
  - Linux
# nolastmod: true
draft: false
---

在proot-distro升级到**debian 13**后，不少同学反馈从星火安装的WPS Office在安装时出现了安装失败的问题

<!--more-->


经过查询，发现是原版的malloc在proot下在某些情况下会崩溃

暂时的解决方法是安装 tcmalloc 后指定使用其安装

```
aptss install libtcmalloc-minimal4t64 -y
```

```
LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libtcmalloc_minimal.so.4 aptss install wps-office -y
```

效果：


![图片.png](https://storage.deepin.org/thread/2025091611560252_图片.png)
