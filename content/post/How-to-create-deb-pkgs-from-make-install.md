---
title: Linux 进阶教程（二）：如何从源代码打包成 .deb 软件包
date: 2025-01-16T18:10:28+08:00
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - Linux学习
tags:
  - Linux
  - 笔记
# nolastmod: true
draft: false
---

内容转载自 [玄圭SwenGway](https://bbs.deepin.org.cn/user/319620)

<!--more-->

在 Linux 的世界里，.deb 是 Debian 系列发行版（如 Ubuntu 和 Deepin）通用的软件包格式。相比直接从源代码编译安装，将软件打包成 .deb 的好处非常多，比如更容易分发、管理和卸载，同时还可以更好地处理依赖关系。这篇教程将手把手教你如何将源代码打包成 .deb，并深入分析可能遇到的问题及其解决办法。
一、为什么要打包 .deb？

    方便管理：直接编译安装的软件无法通过包管理器轻松卸载，而 .deb 包可以使用 dpkg 或 apt 命令进行统一管理。
    易于分发：如果你开发了一个软件，只需发布 .deb 包，别人下载后就能轻松安装。
    解决依赖问题：.deb 包可以自动定义所需的依赖库，安装时自动检查和安装。

二、从源代码到 .deb 的完整流程

我们以一个简单的软件 hello 为例，展示如何从源码开始打包成 .deb 包。
1. 准备工作

在正式开始之前，需要安装一些打包工具。这些工具会帮你完成编译、配置和打包等任务。

sudo apt update
sudo apt install build-essential checkinstall devscripts dh-make fakeroot
​

每个工具的作用：

    build-essential：包含基本的编译工具，如 gcc、make 等。
    checkinstall：快速将编译后的软件直接打包成 .deb 文件。
    devscripts 和 dh-make：生成 .deb 包所需的模板和工具。
    fakeroot：无需超级用户权限，也能完成打包任务。

2. 下载并解压源代码

以 GNU 的经典程序 hello 为例。

wget http://ftp.gnu.org/gnu/hello/hello-2.10.tar.gz
tar -xvzf hello-2.10.tar.gz
cd hello-2.10
​

这里我们下载的是 hello 程序的源码并解压到当前目录，然后进入解压后的目录。
3. 配置和编译源代码（详细请看这篇Linux 进阶教程（一）：从源代码编译软件的超详细指南－论坛－深度科技）

通常情况下，开源项目会提供一个 configure 脚本，用来检查系统环境和配置编译参数。在终端中运行：

./configure
​

这个命令会生成 Makefile，用于后续的编译。接着运行：

make
​

小贴士：不要运行 make install！因为我们要通过打包工具代替这一步。
4. 使用 checkinstall 打包成 .deb

接下来，用 checkinstall 直接打包编译好的程序：

sudo checkinstall
​

执行后，你会看到一个交互式界面，要求填写一些信息：

    软件包名称：默认是项目的名字，可以修改。
    版本号：默认读取源码中的版本信息。
    维护者信息：填写你的名字和邮箱（也可以留空）。

完成后，checkinstall 会自动生成一个 .deb 文件，例如：

hello_2.10-1_amd64.deb
​

然后，你可以用 dpkg 命令安装这个包：

sudo dpkg -i hello_2.10-1_amd64.deb
​

安装完成后，运行 hello 程序测试：

hello
​

三、高级方法：手动创建 .deb 包

虽然 checkinstall 非常方便，但它不适合复杂的项目。下面我们讲解如何手动打包 .deb，让你了解其背后的原理。
1. 创建 Debian 的目录结构

进入源码目录后，运行以下命令：

dh_make --createorig
​

这会生成一个 debian/ 文件夹，里面包含创建 .deb 包所需的模板文件。

debian/ 文件夹的内容：

debian/
├── changelog     # 软件的版本更新日志
├── compat        # debhelper 的兼容版本
├── control       # 软件的元信息文件
├── copyright     # 版权声明
├── rules         # 软件编译和安装规则
├── *.install     # 安装文件和路径
​

2. 配置 debian/control 文件

debian/control 是 .deb 包的核心文件，描述软件的元信息。打开它进行编辑：

Source: hello
Section: utils
Priority: optional
Maintainer: 你的名字 <你的邮箱>
Build-Depends: debhelper (>= 9)
Standards-Version: 4.5.0
Homepage: http://example.com

Package: hello
Architecture: amd64
Depends: libc6 (>= 2.29)
Description: A friendly program that says hello
 A longer描述，可以多行写。
​

字段说明：

    Source：源码包名称。
    Maintainer：包的维护者信息。
    Build-Depends：编译时需要的依赖包。
    Depends：运行时需要的依赖包。
    Description：简短和详细的说明。

3. 定义安装文件

编辑 debian/hello.install，定义哪些文件需要安装到系统路径：

src/hello /usr/local/bin
​

4. 打包 .deb 文件

运行以下命令构建 .deb：

debuild -us -uc
​

成功后，.deb 文件会出现在上一级目录中。
四、常见错误及解决方法

    找不到 ./configure 文件
        原因：源码未提供配置脚本。
        解决办法：运行 autogen.sh 或手动生成：

        autoreconf -i
        ./configure
        ​

    依赖问题
        问题：安装 .deb 时提示缺少依赖。
        解决办法：在 control 文件的 Depends 字段中添加依赖项。
    打包冲突
        问题：安装 .deb 时提示文件冲突。
        解决办法：修改软件包的名称或版本号，确保唯一性。

五、实战练习：打包 htop

完整步骤如下：

    下载源码：

    wget https://github.com/htop-dev/htop/archive/refs/tags/3.2.2.tar.gz
    tar -xvzf 3.2.2.tar.gz
    cd htop-3.2.2
    ​

    配置和编译：

    ./autogen.sh
    ./configure
    make
    ​

    打包为 .deb：

    sudo checkinstall
    ​

    安装测试：

    sudo dpkg -i htop_3.2.2-1_amd64.deb
    htop
    ​

六、总结

本节内容涵盖：

    使用 checkinstall 快速打包 .deb 文件。
    手动打包 .deb 包的高级方法。
    常见错误的原因及其解决方法。

打包成 .deb 是分发软件的高级技能，通过实践逐步掌握这些技术，你就能轻松管理和发布自己的 Linux 应用！🎉
