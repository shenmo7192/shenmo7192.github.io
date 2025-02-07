---
title: Ccc App Manager 查看包信息，可在线或离线提取安装包
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
发布时间： 2022-04-17T19:22:20+08:00

开发者是： [@ct243768648](https://bbs.deepin.org/user/183568) 原帖：https://bbs.deepin.org/zh/post/228853

因为原开发者似乎弃坑了。。。根据自己需求修改了下

<!--more-->


0.0.2 更新内容

* 删除了背景blur效果，降低系统占用+改善非DDE下显示效果
* 增加了“在星火商店打开”按钮，功能暂时没有实装（预计在星火4.0会可用）
* 关于界面文案修改
* 默认打开列表从“全部应用”更改为“界面应用”，更符合日常使用需求
* 修改启动参数，改善在非DDE下显示效果

> 如果想在非DDE完美使用，还需要额外在终端中执行 XDG_CURRENT_DESKTOP="Deepin"


仓库地址：https://gitee.com/shenmo7192/ccc-app-manager/

下载地址：https://gitee.com/shenmo7192/ccc-app-manager/releases/0.0.2

pr链接：https://gitee.com/ct243768648/ccc-app-manager/pulls/1

原开发者仓库：https://gitee.com/ct243768648/ccc-app-manager/



---

这是我在开发完a2d-sm之后的第一个魔改Qt界面程序，虽然还是不会写代码，但是复制粘贴改参数和面向CSDN/百度编程还算是不错