---
title: APM 1.1.9 发布：实验性支持在 deepin 25 上右键卸载
date: 2026-03-25T21:12:15+08:00
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

参考 https://github.com/linuxdeepin/dde-application-wizard/pull/59

APM 1.1.9 新增了自动加入 X-Deepin-PreUninstall 参数的功能，实现在 deepin 下可以右键卸载，和其他普通应用的使用体验较为一致

使用方法：在星火商店更新 APM 到 1.1.9 版本或以上，然后执行sudo apm update &&  sudo apm install apm -y 即可在启动器右键卸载 APM 应用了

原本计划是用 DDE 的卸载弹窗，但似乎 X-Deepin-PreUninstall 并不会拉起弹窗，只好单独搓了一个用

效果如下

![1774453060426.png](https://storage.deepin.org/thread/202603251538186971_1774453060426.png)
