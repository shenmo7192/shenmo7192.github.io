---
title: 星火APM琥珀包：支持Wine应用，一键转制，在任意Linux运行
date: 2025-10-28T14:41:06+08:00
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

APM 1.0.10 支持了解析多层 Base Layer 并按顺序叠加的功能，因此多个扩展组件可以按顺序加载成运行环境，因此我们可以快捷地转制 Wine 软件包而不占用过量空间

经过转制，统信兼容引擎/Wine运行器标准的软件包可被一键转制成支持安装到任意Linux发行版运行的APM包

目前支持的 Wine环境：

- deepin-wine10-stable

- deepin-wine8-stable

- deepin-wine6-stable

- deepin-wine5

- deepin-wine ( 最老的 wine2 版本）

- spark-wine （实时指向最新的spark-wine）

- spark-wine10

- spark-wine9

- spark-wine8

- spark-wine7-devel

- spark-wine-wow

- spark-wine10-wow

- spark-wine9-wow

- spark-wine8-wow

转制方法

1. 安装 apm

若安装过星火应用商店，只需执行 `sudo aptss install apm -y`

若您正在使用 Debian / fedora 或者 Arch ，需前往 https://gitee.com/amber-ce/amber-pm/releases/ 下载安装对应发行版的安装包

目前 APM 支持

- Deb: deepin 20/23/25 ，Ubuntu 20.04/22.04/24.04/25.10 ， Debian 10/11/12/13/SID ，Kali Linux，LinuxMint， UOS 家庭版， UOS专业版 ， 银河麒麟V10SP1，openKylin 2.0/3.0等

- Rpm: fedora, openSUSE

- Arch：从AUR获取 amber-package-manager

上安装和运行

安装后，需重启电脑或注销桌面后重新登录来完成安装

1. 获取对应的deb包：

可从深度商店/星火应用商店下载对应的软件包

`aptss download 包名 ` 即可下载 此处用企业微信作为例子

![图片.png](https://storage.deepin.org/thread/202510280623307248_图片.png)

![图片.png](https://storage.deepin.org/thread/202510280628005650_图片.png)

也可使用自己打包的 Wine 包。对于统信Wine兼容引擎，可使用 deepin-wine 系列。对于 Wine运行器，可使用 deepin-wine 系列和 spark-wine 系列

1. 识别对应使用的环境

使用指令 `dpkg -I 拖入文件` 即可查看文件的依赖信息

![图片.png](https://storage.deepin.org/thread/202510280632511731_图片.png)

注意到使用了 deepin-wine8-stable

执行 `sudo apm install amber-pm-bookworm-deepin-wine8-stable -y ` 配置对应的Wine环境（amber-pm-bookworm-对应的wine环境的名字）

执行 `amber-pm-convert --base amber-pm-bookworm-deepin-wine8-stable 把deb文件拖进来` 即可开始全自动转换

转换后，可获得apm deb包。 该软件包可使用 `sudo apm install `安装到任意支持了APM的Linux发行上，欢迎分享并上传到 APM 商店中

同时，任意APM包也支持直接使用投稿器投递到星火应用商店
