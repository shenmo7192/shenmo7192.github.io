---
title: 终于发现dtk应用移植的效果问题的解决方案了
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
date: 2022-04-07T15:56:33+08:00
---

就差这个

<!--more-->


附加参数：`-platformtheme deepin`

现已默认加入了星火的主程序 https://gitee.com/deepin-community-store/spark-store/commit/61c10944c97f367c061947982d234a0c5be8c3a3

deepin-contacts的补丁也打上了 

星火的webapp运行环境也打上补丁了 https://gitee.com/deepin-community-store/spark-web-app-runtime/commit/2ad0147477336dba48aa1ad2e80c79d75900e02b


新版本已发布（3.0.3.10/1.6.3），给ubuntu用户一个惊喜吧

----
可能需要`XDG_CURRENT_DESKTOP="Deepin"`才能消去双标题栏
