---
title: "星火APM琥珀包: 启发于玲珑杀手的容器包管理(demo)"
date: 2025-10-19T13:58:00+08:00
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

## 碎碎念
好久没搓轮子了

先前看到 @System233 写的 ll-killer ，使用层叠拼接overlayfs的方式进行应用制作，只需要安装应用即可自动记录变化并生成玲珑包，我大受启发，解决了打包软件的难题，就可以all in 玲珑了

但随着玲珑的更新，ll-killer 无法使用了，而玲珑服务端迟迟不开源，且不支持多线程下载的分发方式，这让星火难以切换到玲珑为主的分发格式

于是，我决定自己搓一个散装玲珑来满足需求，那就是

## APM: 琥珀软件包管理器
APM 是一套基于 ACE 兼容环境的，与主机隔离的容器软件包管理系统，可以提供类似玲珑应用使用体验，且完美兼容现有的 deb 软件分发基础设施，兼容传统镜像站，支持多线加速下载和自由灵活的定制

```
`APM - Amber Package Manager 0.1

Usage:
  apm [COMMAND] [OPTIONS] [PACKAGES...]

Commands:
  install      安装软件包
  remove       卸载软件包
  autoremove   自动移除不需要的包
  full-upgrade 完全升级软件包
  run  运行指定软件包的可执行文件
  debug        显示调试系统信息
  -h, --help   显示此帮助信息
  --amber      彩蛋功能
`
```

APM 基于三部分构建：

- 容器启动：基于 ACE 的 bwrap 极轻量级容器

- 容器融合：基于 fuse-overlayfs 进行拼接

- 容器分发和依赖管理：基于 apt/dpkg 进行管理

apm虽使用了apt进行软件包管理，但因容器环境隔离，所以并不需要主机使用dpkg，可在其他发行版安装

原理非常简单，首先准备一个依赖比较完整的ACE环境作为基础运行环境(base)，然后拼接一个包含了需要安装的软件的内容的应用(core)包，apm通过fuse-overlayfs进行融合挂载后即可拼成一个完整的ACE环境，从而启动应用

![录屏_gxde-terminal_20251019135643.gif](https://storage.deepin.org/thread/202510190557167203_录屏_gxde-terminal_20251019135643.gif)

这让制作APM应用变得非常简单。新建文件夹，指定为core包目录，和对应的ACE融合挂载即可完成准备工作。随后直接在融合挂载后的目录启动ACE，完成软件安装——在外面怎么装里面就怎么装，即可获得可以分发的core包

使用截图：

打包方式： https://gitee.com/amber-ce/amber-pm/blob/master/README.md

体验地址（目前仅amd64,可通过 sudo apm install org.eom.apm -y 来直接安装软件，首次安装APM需要重启来在启动界面展示）：https://gitee.com/amber-ce/amber-pm/releases
