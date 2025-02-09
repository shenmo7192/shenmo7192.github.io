---
title: repack-zstd：自动把.zstd的deb包转换成UOS/deepin能识别的.xz deb包
author: shenmo
avatar: /img/avatar.jpeg
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
date: 2022-04-26T23:06:54+08:00
---

当你遇到这样的报错时，可能会很迷惑

`dpkg-deb: error: archive 'linux-headers-5.14.15-051415_5.14.15-051415.202110270548_all.deb' **uses unknown compression for member 'control.tar.zst', giving up**`

(摘自：https://bbs.deepin.org/post/227527)
<!--more-->

这是因为，从21.10开始，ubuntu的默认打包格式从.xz变成了.zstd，而debian要到11才能支持

最近一些ubuntu用户向星火商店投稿的时候出现了兼容性问题：打出来的包在deepin上无法解包

```bash

dpkg-deb: 错误: 归档 /var/cache/apt/archives/com.github.ccc-app-manager_0.0.3_amd64.deb 对成员 control.tar.zst 使用了未知的压缩，放弃操作
dpkg: 处理归档 /var/cache/apt/archives/com.github.ccc-app-manager_0.0.3_amd64.deb (--unpack)时出错：
dpkg-deb --control 子进程返回错误状态 2
在处理时有错误发生：
/var/cache/apt/archives/com.github.ccc-app-manager_0.0.3_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

出现了这样的错误

我紧急写了个脚本，可以验证这个软件包是否为.zstd包，如果是，就自动重新打包

脚本地址：  [https://gitee.com/deepin-community-store/repo_auto_update_script/blob/master/repack-zstd](https://gitee.com/deepin-community-store/repo_auto_update_script/blob/master/repack-zstd)
```bash
用法：repack-zstd [-h|--help] [-i|--in] [-o|out] [-t|-tmpdir] [-s|--scan] path
-h|--help     显示这个帮助
-i|--in       输入的文件路径
-o|--out      输出的文件路径，默认为运行目录
-t|--tmpdir   设置解包路径，默认为运行目录
-s|--scan     进入扫描模式，扫描这个路径下的所有deb包。在此模式下，输出文件路径将变为输入文件所在目录

如果没有设置参数，将按照 [输入路径] [输出路径] [解包路径] 的顺序读取
例子 Examples：
repack-zstd -i ./spark-store_3.0.3-13_amd64.deb -o ./ -t ./
repack-zstd ./spark-store_3.0.3-13_amd64.deb ./ ./
repack-zstd ./spark-store_3.0.3-13_amd64.deb
repack-zstd --scan ./

```

原理：用`file`检查是否是.zstd格式包，如果是，则解包到指定目录

---

用法：详见上

-i来指定要检测的deb位置，-o来指定输出位置（就是重新打包为.xz后的包的位置）,  -t来指定解包位置（放置解包文件的位置，用后会删除）

如果不指定参数，会按照 deb位置 输出位置，解包位置的顺序读取

如果没有检测到输出位置和解包位置，则把当前工作目录作为输出和解包位置

**扫描**：会扫描指定目录下所有的deb包。在此模式下，输出目录**会被更改到和deb输入目录一致**，也就是拆完了放回去。默认的解包目录是当前目录，如果坛友有需求改成可以指定，欢迎pr

---

行为：

如果发现是.zstd包，则会把原包解包到`tmpdir/unpack-dir`，然后打包到`output`位置

如果发现不是.zstd包，则会把原包**移动**到output位置

---

用例：星火商店的仓库混入了一些`.zstd`格式的软件包，但是又不能一个一个安装测试

下载`repack-zstd`，执行`./repack-zstd --scan 仓库目录`，脚本自动寻找所有的.deb文件并在扫描过程中找到了`.zstd`格式软件包，实施了重新打包

---

备注：这个脚本**不附带zstd的解压功能**，如果你使用的操作系统不支持.zstd包（Debian <11/Ubuntu <18.04），则无法正常解包运行。由于.zstd包的资料过少，暂时无法在脚本内提供其他解包方法。你可以用ubuntu的docker镜像来解包（诶等等我附带一个镜像是不是就完美了？
