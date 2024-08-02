---
title: 使用Amber CE安装星火应用商店的教程
date: 2024-08-02T22:46:05+08:00
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - Linux
# nolastmod: true
draft: false
---

使用Amber CE安装星火应用商店的教程

<!--more-->

ACE兼容环境是一款基于bubblewrap的容器化应用打包和分发方案。用极为轻量的容器方案让你可以在几乎任何的Linux发行版上运行一个操作系统容器

利用 ACE 容器，星火应用商店现已（几乎）全平台可用

----


## 安装指南

### 安装ACE环境

https://gitee.com/amber-ce/amber-ce-bookworm#%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97

从 「手动安装」的链接中下载Debian/Fedora/Arch所需的安装包并安装

或直接从宿主机的星火应用商店或者星火应用商店终端版中安装 ACE兼容环境 应用

*首次安装后请注销或重启以展示启动器入口*

* 在其中安装星火应用商店



### 下载商店（从官网即可）

* 到下载到的目录右键在终端中打开

![图片](imgs/1702393570-39331-50b96148-d3d4-4796-b2d6-9e19acb55bc1.png)

* 输入`bookworm-run`进入ACE环境，并进行安装

* * `sudo apt update`确保软件是最新的
* * `sudo apt install `，然后拖进来对应架构的应用包（家用一般是amd64，树莓派，飞腾，鲲鹏等是arm64），随后回车
* * 现已不需要下载ACE特别版，直接安装普通版即可


![IMG](https://wiki.spark-app.store/Amber-CE/imgs/1702393570-39331-50b96148-d3d4-4796-b2d6-9e19acb55bc1.png)

---

然后就可以愉快地使用啦~

已知问题：

* 部分应用无法使用
* 输入法/字体/主题无法使用（因容器原因无法修复）

请多多反馈以让我们改善！
