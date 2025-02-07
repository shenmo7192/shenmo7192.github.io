---
title: 星火微信原生Linux2.1.2-2版
author: shenmo
avatar: /img/avatar.jpeg
lastmod:
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
---
发布时间：2022-01-28T15:37:51+08:00

优麒麟源的微信Linux更新了，在此同步更新星火版微信Linux

<!--more-->



更新说明：2.1.2-2修改了启动脚本，修复了原版进程退出不干净导致的下次启动失败

感谢 [@sgb76](https://bbs.deepin.org/user/145764)

分享地址：

1.  全发行版可用：[https://d.store.deepinos.org.cn//store/chat/wechat-linux-spark/wechat-linux-spark_2.1.2-1_amd64.deb](https://d.store.deepinos.org.cn//store/chat/wechat-linux-spark/wechat-linux-spark_2.1.2-1_amd64.deb)

2.  仅适用于deepin/UOS/安装了星火商店的发行版版本（有这个东西是因为我在尝试把这个魔改包扔到deepin商店）

    [https://com-store-packages.uniontech.com/appstore/pool/appstore/s/store.spark-app.wechat-linux-spark/store.spark-app.wechat-linux-spark_2.1.2-2~dstore0_amd64.deb](https://com-store-packages.uniontech.com/appstore/pool/appstore/s/store.spark-app.wechat-linux-spark/store.spark-app.wechat-linux-spark_2.1.2-2~dstore0_amd64.deb)

> 如果你想在非UOS/deepin发行版上使用UOS包，你可以下载这个

https://shenmo.lanzoul.com/icDyn00cglxi

* * *

优麒麟源的微信Linux更新了，在此同步更新星火版微信Linux

优麒麟包的破解方法是用银河麒麟的lsb-release信息替换系统的lsb-release

修改的版本不再替换，而是用bwrap来模拟该lsb-release以及激活信息来过校验，同时不会再在/etc留下垃圾

[http://core.shenmo.tech/index.php?share/file&user=1&sid=a6j3ARvf](http://core.shenmo.tech:38324/index.php?share/file&user=1&sid=a6j3ARvf)

![图片.png](https://storage.deepin.org/thread/202201281550106159_%E5%9B%BE%E7%89%87.png)