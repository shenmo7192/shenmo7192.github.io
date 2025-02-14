---
title: AmberCE兼容环境 12.6.1 更新：支持N卡加速
date: 2025-02-14T21:03:09+08:00
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - Linux
  - 笔记
# nolastmod: true
draft: false
---

ACE Bookworm 兼容环境迎来了久违的更新

<!--more-->

-->如果您不知道什么是 ACE 兼容环境，请查看：[AmberCE兼容环境使用指南](https://blog.shenmo.tech/post/amberce%E5%85%BC%E5%AE%B9%E7%8E%AF%E5%A2%83%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97/)

更新内容如下

* 默认容器位置改为 /opt/apps/amber-ce-bookworm
* 支持了N卡加速

N卡加速的条件：

* 主机已经安装好了N卡驱动
* ACE Bookworm 兼容环境版本号>=12.6.1 ，若您先前在深度商店安装过，请使用星火应用商店检查更新；若您在网页端安装过，请前往 [这里](https://blog.shenmo.tech/post/amberce%E5%85%BC%E5%AE%B9%E7%8E%AF%E5%A2%83%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97/) 下载更新的版本

加速方法：

0. 若您已经在主机配置好了 Nvidia 驱动，更新或者全新安装 ACE Bookworm兼容环境到 12.6.1 即可在安装时自动配置好N卡驱动
   
   ![图片.png](https://storage.deepin.org/thread/202502141348488081_图片.png)
1. 若您在安装后升级过N卡驱动，或者想要手动刷新安装，仅需在终端中输入 `sudo amber-ce-bookworm-configure-nvidia` 即可
   
   ![图片.png](https://storage.deepin.org/thread/202502141349152081_图片.png)

现在，您即可在 ACE Bookworm 兼容环境中使用 Nvidia 显卡加速了
