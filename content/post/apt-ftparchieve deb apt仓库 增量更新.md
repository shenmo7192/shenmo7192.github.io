---
title: 利用apt-ftparchieve和脚本创建一个简易且支持增量更新的APT仓库
date: 2022-09-04T00:49:07+08:00
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
---

为了SEO也是做了点优化

<!--more-->

#### 使用方法
很多网站都有使用apt-ftparchieve的使用教程，我在这里再讲一下

### 创建仓库

在放置deb的位置创建文件夹，cd到文件夹中执行

```bash

apt-ftparchive packages . > Packages
apt-ftparchive release . > Release
gpg --clearsign -o InRelease Release


```

即可创建仓库，此时开启http server即可完成创建

但是：每次更新仓库，都会从头生成一遍Packages，随着你的仓库大小增加，每次刷新Packages的时间会越来越长，而且这对你的磁盘也是一种损伤！

### 解决方法：

```bash
wget https://gitee.com/shenmo7192/momo-and-mox-tool-scripts/raw/master/other-tools/deb-repo-script/incremental-update.sh
chmod +x ./incremental-update.sh
```

把这个脚本放到你的仓库根目录上

这个脚本可以让你的仓库的`Packages` 增量更新，只会更新相比上次更新新增的软件包，这样会大大减少较大仓库的刷新时间，也可降低磁盘损耗！

更好的是，这个脚本支持多线程生成`Packages`，对于固态硬盘来说，速度会大大提升（机械硬盘就没啥效果了）

若要使用该脚本，上一节的指令应当是

```bash
/abosolute/path/to/repo/incremental-updating-packages.sh
gpg --clearsign -o InRelease Release


```

### 配置crontab

把上一节的脚本保存为文件，给予可执行权限并配置到crontab每日任务中，实现自动刷新

### 开启网络服务，对外提供apt仓库服务

推荐的方法是使用nginx等专业工具，然而，如果你不想或者不想学如何配置nginx，那么你可以用我提供的这个极简的python脚本

先`sudo apt install python3`，然后`wget https://gitee.com/shenmo7192/momo-and-mox-tool-scripts/raw/master/server.py`

使用这个脚本创建服务器的方法非常简单，`python3 ./server.py `

在服务器上后台运行，请先安装screen，再在screen中运行，这样断开连接之后仍然可以host服务器

退出screen的方法是ctrl+A+D，再次进入用的是screen -r 对应的id，终结screen的方法是在screen内部输入exit

如果你的对应端口放通了，那么不出意外的话，你已经可以从`ip:8000`上访问你的仓库了~（如果有域名可换成域名）

### 用户如何使用此仓库

只需要在`/etc/apt/sources.list`中加入

```bash
deb [trusted=yes] http://ip:8000/ / 
```

然后`sudo apt update`即可连接到你的apt仓库！

---

以下为脚本解析

#### 开发理由

最开始星火选型的时候并没有考虑到仓库变大该怎么办

于是根据CSDN上的流行帖子，使用apt-ftparchieve来更新

然鹅这东西不支持增量更新，每次刷新都需要从头到尾生成一遍Packages....

而支持增量更新的工具如reprepro，aptly都需要操作对应的工具来添加包，而软件包也只能以标准的方式组织。众所周知，星火的软件包根本不是按照正常的deb源放的。。。所以用不了

发展了两年多之后，星火的源大小已经逼近150G，而每天的刷新推送的时长也开始逼近2小时.....

于是我就写了这么个东西来增量更新Packages

核心思路就是让每一个deb对应一个.deb.package，然后通过合成.deb.package来更新Packages文件

---


#### 需求

* 对于任意的 `.deb`，发现 `.deb`的更改时间比 `.deb.package`新时，表明这个包在上一次保存信息之后出现了变动，应当重新生成信息
* 对于任意的 `.deb`，如果没有 `.deb.package`与之对应，表明这个包之前在仓库中不存在，需要新增信息
* 对于任意的 `.deb.package`，如果没有对应的 `.deb`与之对应，表明这个包已经下架，需要删除信息
* 多线程同时进行hash操作，但是可控制线程数量最大值

#### 实现方法

* 首先对已存在的 `.deb.package`，查找是否存在对应的 `.deb`。如果没有，则是该包已经下架，执行删除操作；如果有，则验证更改时间

  * 若 `.deb.package`的时间比 `.deb`新，则说明此包从上次生成信息起没有改动，跳过即可；否则，说明此包在上次生成信息之后发生了变动，应该重新生成。此时执行删除信息操作，在下一个阶段时将会被认为是新增的软件包而重新生成
* 然后对已存在的 `.deb`，查找是否存在对应的 `.deb.package`。若有，则说明此包已上架，可跳过生成；否则，则认为是新包，执行信息生成
* 最后，合成所有的 `.deb.package`到 `Packages`，继续进行后续的签名等操作

---

### 效果

现在星火商店仓库一次同步的时间降低至10分钟左右
