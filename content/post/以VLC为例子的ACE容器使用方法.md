---
title: 使用ACE容器运行deepin不支持的新应用的教程:以VLC为例
date: 2023-09-03T19:46:35+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - linux
# nolastmod: true
draft: false
---
琥珀兼容环境——书虫兼容模式的一个使用例

<!--more-->


这里是正文开始的内容
以下为 琥珀兼容环境——书虫兼容模式的一个使用例，想要体验书虫兼容模式的同学可以接着往下看

![图片.png](https://storage.deepin.org/thread/202309041648374834_图片.png)

这个是我在鲲鹏平台的ACE兼容模式跑的VLC的截图。就VLC而言，对于deepin 20.9的用户，想要用最新最好用的vlc，直接用 [@Ziggy](user/95253)制作的VLC增强版就可以（深度商店可获取）

UOS比较旧版本/非x86平台/deepin 23的朋友，会需要这个，可以接着往下看如何操作

1. 安装兼容模式

在UOS商店的版本比较旧了，是稳定+适配应用签名的版本，对于支持显卡加速，请前往星火商店获取最新的版本（在Arm和x86都有上架）

[spk://store/tools/cn.flamescion.bookworm-compatibility-mode/](https://deepin-community-store.gitee.io/spk-resolv/?spk=spk://store/tools/cn.flamescion.bookworm-compatibility-mode/)

![图片.png](https://storage.deepin.org/thread/202309041655242175_图片.png)

2. 进入容器和配置应用

一般进入容器都使用 `bookworm-run` 指令，这个指令进入容器后没有root权限，操作是安全的；如果需要root权限，请 `sudo bookworm-run`

这里我们 `sudo bookworm-run` 进入root权限的环境

![图片.png](https://storage.deepin.org/thread/202309041702143380_图片.png)

然后只要 `apt install vlc -y`

就可以了

装完了请 `exit`退出root，然后 `bookworm-run`启动非root，然后 `vlc` 测试下vlc能否启动

可以在主机执行 `bookworm-run vlc`来直接启动

3. 配置和主机的融合（修改desktop）

`bookworm-run` 进入容器

`cp /usr/share/applications/vlc.desktop ~/.local/share/applications`

把desktop文件复制到主机的目录下

但是这时候在主机看不到这个desktop，这是为什么呢？

让我们打开 `deepin-editor ~/.local/share/applications/vlc.desktop`(这里deepin-editor可以换成你喜欢的编辑器，或者直接在文件管理器打开目录双击)

可以看到，这里有一项 `TryExec`

![图片.png](https://storage.deepin.org/thread/202309041709039023_图片.png)

这一行的意思是告诉桌面，如果这个文件不可执行，则不显示。我们把vlc装到容器里了，对于主机来说，自然是不可执行的。为了正常显示桌面，我们删掉这一行

删掉后保存，现在应该可以在启动器看到vlc了。但是点击还是打不开，这是因为 `Exec`还没改，桌面会尝试从主机启动vlc。那怎么办呢？琥珀兼容环境把容器启动包装的很简单，你只需要在 `Exec=`后面的文字前面加一个 `bookworm-run`，即可完美唤起容器中的vlc

4. 标记容器应用（可选）

因为我们并没有制作一个wrapper deb包来让主机管理容器，所以对这个desktop的卸载操作是无效的。我个人会对这样的desktop加一个标记来提醒自己

在Name[zh_CN]后面加一个标注即可

这是我最终的成品desktop

![图片.png](https://storage.deepin.org/thread/202309041713153162_图片.png)

效果如下

![图片.png](https://storage.deepin.org/thread/202309041713319673_图片.png)

![图片.png](https://storage.deepin.org/thread/202309041713416972_图片.png)

可正常播放视频（MMD）

![图片.png](https://storage.deepin.org/thread/202309041714249253_图片.png)

5. 容器应用的卸载

因为没有制作wrapper deb，deepin 启动器无法直接操作卸载。我们不想要的时候，需要手动清理

* 去~/.local/share/applications下手动删掉我们制作的desktop
* `sudo bookworm-run apt autoremove vlc -y`
