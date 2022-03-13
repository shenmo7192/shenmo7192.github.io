---
title: 360压缩去升级版 星火dstore补丁
date: 2021-12-02T17:12:07+08:00
lastmod: 2021-12-02T17:12:07+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
cover: https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1638436446003.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - linux
# nolastmod: true
draft: false
---

52pojie太费劲了，删帖自己都不能看，还是备份一下好

<!--more-->

众所周知，UOS标准的软件包在非统信系发行版上安装会出现无desktop等问题
经检测，发现与之相关的可执行文件为"deepin-app-store-tool"
于是将相关文件提取并重新打包

为避免未知问题，可执行文件已被更名为"spark-dstore-patch"

运行截图
![](https://attach.52pojie.cn/forum/202112/02/170629bgesx44z5j34l63j.png)

下载链接

~~https://shenmo.lanzoux.com/iW31kx5891g~~
新版本可以和星火共存 https://shenmo.lanzoul.com/iqj2vyrkhgj

注意：UOS/deepin用户不需要安装此补丁，自带的深度商店就可以正确处理软件包。为防呆，已设置与深度商店冲突

----

360看图是360压缩看图工具独立出来的独立应用
日常使用比较方便，但是会自动升级到支持360安全云盘的版本

新版本没有新功能，且看着碍眼。无可设置能关闭自动更新的选项
于是去除升级模块，使用Inno Setup重新打包

运行截图

![](https://attach.52pojie.cn/forum/202112/02/171054pz83y40m8yu80d6h.png)

![](https://attach.52pojie.cn/forum/202112/02/171058xbepqh3ar7k8irap.png)

![](https://attach.52pojie.cn/forum/202112/02/171101g4nczidbu8ju8c83.png)

下载链接

https://shenmo.lanzoux.com/iQ6JBwclwgd