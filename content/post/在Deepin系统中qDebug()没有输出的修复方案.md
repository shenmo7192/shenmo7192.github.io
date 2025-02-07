---
title: 在Deepin系统中qDebug()没有输出的修复方案
date: 2022-10-11T22:39:12+08:00
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



<!--more-->

 问题

检查环境变量：export -p

发现有一行是`QT_LOGGING_RULES="*.debug=false"`，或者Qt Creator的帮助菜单的System Infomation，Qt Creator里面有个System Information检查环境变量，如下图：

![enter description here](https://www.qedev.com/res/2021/02-05/10/eepaj013hr3.jpg)


 

解决方案

用管理员身份打开`/etc/X11/Xsession.d/00deepin-dde-env`，用#注释`QT_LOGGING_RULES="*.debug=false"`，然后注销。

需要注意的是，深度编辑器因文件类型限制无法打开这个文件，可以用nano