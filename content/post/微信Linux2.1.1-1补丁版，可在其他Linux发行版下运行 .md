---
title: 微信Linux2.1.1-1补丁版，可在其他Linux发行版下运行 
date: 2022-01-10T18:32:21+08:00
lastmod: 2022-01-10T18:32:21+08:00
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
---

因升级网盘系统，原下载链接已失效，现下载链接已更新，请使用新链接下载

<!--more-->


* * *

下载链接：[http://core.shenmo.tech/index.php?share/file&user=1&sid=J2PueKAc](http://core.shenmo.tech:38324/index.php?share/file&user=1&sid=J2PueKAc)

基于优麒麟的2.1.1改包

优麒麟包的破解方法是用银河麒麟的lsb-release信息替换系统的lsb-release（<https://bbs.deepin.org/zh/post/229854>）

我修改的版本不再替换，而是用bwrap来模拟该lsb-release以及激活信息来过校验，同时不会再在/etc留下垃圾

欢迎测试！