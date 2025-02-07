---
title: 一键解决由于没有公钥，无法验证下列签名： NO_PUBKEY XXXXXXXX的问题
date: 2022-06-11T16:49:53+08:00
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

还在为没有公钥导致的无法更新而烦恼吗？这里有解决方案

<!--more-->

很多时候，我们添加第三方源或者安装了第三方软件后，系统无法更新。终端里执行 `sudo apt update` 时提示 `由于没有公钥，无法验证下列签名： NO_PUBKEY XXXXXXXX`

![image.png](https://storage.deepin.org/thread/202205191141579300_image.png)

这时，我们就需要这条命令了，可以一键解决上边的问题

```
sudo apt update 2>/dev/null | awk 'match($0, /NO_PUBKEY\ (\w{16})/, a) {print a[1]}' | sort | uniq | xargs sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 

```

使用效果如下

![image.png](https://storage.deepin.org/thread/202205191143405060_image.png)

再次更新即可

转载自 ：https://bbs.deepin.org/post/237312  by deepin-superuser