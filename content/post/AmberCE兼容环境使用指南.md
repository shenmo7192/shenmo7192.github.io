---
title: AmberCE兼容环境使用指南
date: 2025-02-03T19:46:35+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# images:
#   - /img/cover.jpg
categories:
  - 笔记
tags:
  - Linux
# nolastmod: true
draft: false
---
通过使用ACE兼容环境，可以简洁而快速地解决依赖问题

<!--more-->


1. 安装兼容环境

可通过 深度应用商店 或 星火应用商店 安装，亦可前往官网手动安装

![图片.png](https://storage.deepin.org/thread/202405141522277887_图片.png)

[spk://store/tools/cn.flamescion.bookworm-compatibility-mode/](https://spk-resolv.spark-app.store/?spk=spk://store/tools/cn.flamescion.bookworm-compatibility-mode/)

![图片.png](https://storage.deepin.org/thread/202309041655242175_图片.png)

或者下载安装包后 [手动安装](https://gitee.com/amber-ce/amber-ce-bookworm#%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97-debianfedoraarch)

2. 从启动器中打开兼容环境

![图片.png](https://storage.deepin.org/thread/202405141523372019_图片.png)

ACE Bookworm中包含了一个Debian12环境，可方便地安装应用

场景演示：

1. 软件包不存在

在deepin 23的软件仓库中不包含归档管理器（file-roller)，直接apt install file-roller会报错无法安装

通过ACE兼容环境可直接安装file-roller（如果是首次安装ACE兼容环境需要重启或者注销桌面以在启动器显示入口）

![图片.png](https://storage.deepin.org/thread/202405141526571847_图片.png)

安装后即可使用file-roller打开压缩文件

![图片.png](https://storage.deepin.org/thread/202405141527304059_图片.png)

![图片.png](https://storage.deepin.org/thread/202405141527512081_图片.png)

2. 依赖关系不满足

一些软件包的依赖关系损坏，无法安装，用ACE兼容环境即可解决问题

![图片.png](https://storage.deepin.org/thread/202405141529121318_图片.png)

3. 注意事项

* 安装的应用不能直接右键卸载。除直接在ACE兼容环境内敲命令之外，也可以用提供的卸载器来卸载应用

![图片.png](https://storage.deepin.org/thread/202405141530537807_图片.png)

* 若这是您首次安装ACE兼容环境，您 **需要重启或者注销桌面** 以在桌面启动器上显示安装在容器内的应用
* 暂不支持systemd,若需要安装的应用有服务，您可能需要手动启动

Tips: 有些命令行应用，希望可以直接从系统调用，可使用此脚本快速融合

```
#!/bin/bash
CMD_TO_ACE="$(basename $0)"
bookworm-run "$CMD_TO_ACE" "$@"
```

在ACE容器中安装过需要的应用后（假设是neofetch）在/usr/bin下创建同名文件，把以上内容写入，然后给予可执行权限即可

sudo nano /usr/bin/neofetch

sudo chmod +x /usr/bin/neofetch