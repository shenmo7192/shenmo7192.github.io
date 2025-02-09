---
title: 禁止kwin的自动关闭3D窗管的方法
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
date: 2022-03-11T13:34:28+08:00
---

在玩OSU/CS:GO等游戏的时候，kwin 3D效果会自动关闭，对于一些显卡来说会造成画面撕裂，同时会使深度录屏失效/造成界面不美观，因此需要关闭。

<!--more-->


`deepin-editor ~/.config/kwinrc`

找到`[Compositing]`项目，在其下添加
```
WindowsBlockCompositing=false
UnredirectFullscreen=true

```
注销或重启窗管即可应用
