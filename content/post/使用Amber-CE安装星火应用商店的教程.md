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


# 利用 ACE 容器，星火应用商店现已（几乎）全平台可用

## 安装指南

### 1. 安装ACE Bookworm环境

https://gitee.com/amber-ce/amber-ce-bookworm#%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97

**从 「手动安装」的链接中下载Debian/Fedora/Arch所需的安装包并安装，对于大多数用户来说，你不需要构建，直接下载成品即可**

![](https://shenmo7192.atomgit.net/imgs/1732814515-626882-1732814331824.png)

![](https://shenmo7192.atomgit.net/imgs/1732814526-867548-1732814350340.png)

![](https://shenmo7192.atomgit.net/imgs/1732814647-713262-76af9417-159f-4de2-af77-e61fb7abbeab.png)

![](https://shenmo7192.atomgit.net/imgs/1732814736-809583-a888adee-4c2e-4b33-abd9-93c657df0a51.png)


或直接从宿主机的星火应用商店或者星火应用商店终端版中安装 ACE兼容环境 应用

#### 首次安装后请注销或重启以展示启动器入口

### 2. 在其中安装星火应用商店



1. 下载商店（从官网即可）

* 到下载到的目录右键在终端中打开

![](https://shenmo7192.atomgit.net/imgs/1702393570-39331-50b96148-d3d4-4796-b2d6-9e19acb55bc1.png)

* 输入`bookworm-run`进入ACE环境，并进行安装

1. `sudo apt update`确保软件是最新的
2. `sudo apt install `，注意install 后面有个空格，然后拖进来对应架构的应用包（家用一般是amd64，树莓派，飞腾，鲲鹏等是arm64），随后回车
3. 现已不需要下载ACE特别版，直接安装普通版即可

![](https://shenmo7192.atomgit.net/imgs/1702393896-412459-3d5385c2-992e-48fb-82ab-33054750e1ed.png)

---

然后就可以愉快地使用啦~

---
# 注意事项


* 若无法输入中文，请在bookworm-run后安装fcitx5-frontend-all 或您所使用的输入法的前端
* 若已经在主机安装过星火应用商店，则启动器优先展示主机安装过的，卸载主机的商店即可使用容器内的商店，或者在终端中`bookworm-run spark-store`指令来启动容器中的商店
* AOSC OS已经适配，但需要注意的是龙芯架构下AOSC OS的架构名称和其他debian不同，请AOSC 龙芯用户下载AOSC专版
* 已有 deepin 23 容器支持，容器里面是deepin 23,把指令换成deepin23-run即可
* 银河麒麟的启动器不支持XDG_DATA_DIRS规范，请手动去以下路径查找应用入口
`/opt/apps/amber-ce-bookworm/files/ace-env/usr/share/applications` 或 `/opt/apps/amber-ce-deepin23/files/ace-env/usr/share/applications` 取决于你安装的是哪种容器

已知问题：

* 部分应用无法使用，如输入法，主题

请多多反馈以让我们改善！
