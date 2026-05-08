---
title: "APM全自动转换器：把deb全自动转换成APM包的工具"
date: 2025-10-22T00:33:53+08:00
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

关于 APM : https://bbs.deepin.org.cn/post/292352

APM 琥珀容器包管理系统启发于 玲珑杀手 ll-killer ，感谢 @System233的思路

apm现已进入星火仓库，可通过 `sudo aptss install apm -y`进行安装

APM全自动转换器：

https://gitee.com/amber-ce/amber-pm/blob/master/src/usr/bin/amber-pm-convert

通过模拟安装的方式，全自动转换普通deb为APM deb

APM deb 的好处：

- 在构建时指定运行环境，指定什么用户就会用什么，无需担心依赖不满足（目前支持deepin25 debian12 debian 13）

- 完全兼容debian软件包管理器，可作为普通deb安装，应用可正常通过右键卸载

- 除debian系外，任意安装了apm的发行版均可通过apm安装apm deb（已测试fedora，正在打包rpm和arch的apm支持）

目前的局限性:

- APM暂不支持需要系统服务的应用打包，依赖系统服务运行的应用无法使用

- 因APM目录为只读挂载，对于需要读写系统目录运行的应用(如vpn，WPS专业版)需要手动定制启动指令才能正常运行如激活程序

使用方法：

`amber-pm-convert --base 运行环境名称 deb路径`

目前支持的运行环境：

- amber-pm-deepin25

- amber-pm-trixie

- amber-pm-bookworm

> 
若报错缺乏相关运行环境，请使用 `sudo apm install `安装

例：

![图片.png](https://storage.deepin.org/thread/202510211618483772_图片.png)

![图片.png](https://storage.deepin.org/thread/202510211620046878_图片.png)

![图片.png](https://storage.deepin.org/thread/202510211620281167_图片.png)

![图片.png](https://storage.deepin.org/thread/202510211633328141_图片.png)
