---
title: 星火商店打包与投递须知
date: 2021-10-12T19:01:14+08:00
lastmod: 2021-10-12T19:01:14+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
cover: https://gitee.com/superendermansm/shenmo-map-bed/raw/master/小书匠/1634036510663.png
# images:![enter description here]()
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - 闲聊
# nolastmod: true
draft: false
---

一、打包标准

1、官方包：

<!--more-->



请从软件官网下载，经自行测试可用后投递。

2、自行打包：

请将程序打包在/opt/durapps/目录，推荐使用debreate打包，全图形化，比较方便

deb包经检验位置合格后投递。

Debreate获取方法：

deepin20可以在商店获取debreate；


3、Appimage包：

建议使用星火商店专用转换器，下载地址：[spk://store/development/appimage2deb/](spk://store/development/appimage2deb/)（该下载地址需要先安装星火商店）

请注意，该程序有已知bug，请打开后认真阅读启动提示后运行

如果出现点击启动后没有反应，尝试执行

`sudo apt install zenity -y`

如果掌握打包流程，也可以自行拆包打包

拆包指令为

`./xxxxx.AppImage --appimage-extract`

AppImage包的简单操作可以参考 https://www.jianshu.com/p/5ce61cbae73a


二、投递流程

1、准备好软件图标、软件截图（不超过5张）、软件描述和软件包本体。

2、打开网址：<https://upload.deepinos.org/index>

3、点击左上角上传，并按要求输入软件包信息。

4、等待审核，审核通过后，您提交的软件会在对应分类下出现，如果审核未通过，我们会通知您未通过的原因

P.S. 因为国际化计划搁浅，英文名项可以复制粘贴中文名