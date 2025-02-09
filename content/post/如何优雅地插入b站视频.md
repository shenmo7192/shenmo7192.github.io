---
title: 如何优雅地插入b站视频
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
date: 2022-03-07T19:12:08+08:00
---

在b站官方的分享链接复制的代码现在专为移动端设计了，在桌面端上非常小，通过使用旧版的分享链接播放器来解决这个问题

<!--more-->


![enter description here](https://xiaoshujiang-shenmo.oss-accelerate.aliyuncs.com/小书匠/1646651681437.png)

对比

![enter description here](https://xiaoshujiang-shenmo.oss-accelerate.aliyuncs.com/小书匠/1646651694175.png)

代码如下
```html
<iframe src="https://player.bilibili.com/player.html?bvid=这里替换为bv号&page=1" allowfullscreen="allowfullscreen" width="100%" height="500" scrolling="no" frameborder="0" sandbox="allow-top-navigation allow-same-origin allow-forms allow-scripts"></iframe>

```

用于复制：
> `<iframe src="https://player.bilibili.com/player.html?bvid=这里替换为bv号&page=1" allowfullscreen="allowfullscreen" width="100%" height="500" scrolling="no" frameborder="0" sandbox="allow-top-navigation allow-same-origin allow-forms allow-scripts"></iframe>`

--------

例子：

<iframe src="https://player.bilibili.com/player.html?bvid=BV1iL4y1x739&page=1" allowfullscreen="allowfullscreen" width="100%" height="500" scrolling="no" frameborder="0" sandbox="allow-top-navigation allow-same-origin allow-forms allow-scripts"></iframe>
