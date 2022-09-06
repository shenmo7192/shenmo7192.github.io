---
title: apt-ftparchieve制作的deb apt仓库 增量更新的脚本
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

#### 开发理由

最开始星火选型的时候并没有考虑到仓库变大该怎么办

于是根据CSDN上的流行帖子，使用apt-ftparchieve来更新

然鹅这东西不支持增量更新，每次刷新都需要从头到尾生成一遍Packages....

而支持增量更新的工具如reprepro，aptly都需要操作对应的工具来添加包，而软件包也只能以标准的方式组织。众所周知，星火的软件包根本不是按照正常的deb源放的。。。所以用不了

发展了两年多之后，星火的源大小已经逼近150G，而每天的刷新推送的时长也开始逼近2小时.....

于是我就写了这么个东西来增量更新Packages

核心思路就是让每一个deb对应一个.deb.package，然后通过合成.deb.package来更新Packages文件

---

### 代码讲解：

地址：  https://gitee.com/deepin-community-store/repo_auto_update_script/blob/master/repo-maintain/incremental-updating-packages.sh

#### 需求

* 对于任意的 `.deb`，发现 `.deb`的更改时间比 `.deb.package`新时，表明这个包在上一次保存信息之后出现了变动，应当重新生成信息
* 对于任意的 `.deb`，如果没有 `.deb.package`与之对应，表明这个包之前在仓库中不存在，需要新增信息
* 对于任意的 `.deb.package`，如果没有对应的 `.deb`与之对应，表明这个包已经下架，需要删除信息

#### 实现方法

* 首先对已存在的 `.deb.package`，查找是否存在对应的 `.deb`。如果没有，则是该包已经下架，执行删除操作；如果有，则验证更改时间

  * 若 `.deb.package`的时间比 `.deb`新，则说明此包从上次生成信息起没有改动，跳过即可；否则，说明此包在上次生成信息之后发生了变动，应该重新生成。此时执行删除信息操作，在下一个阶段时将会被认为是新增的软件包而重新生成
* 然后对已存在的 `.deb`，查找是否存在对应的 `.deb.package`。若有，则说明此包已上架，可跳过生成；否则，则认为是新包，执行信息生成
* 最后，合成所有的 `.deb.package`到 `Packages`，继续进行后续的签名等操作

---

### 效果

现在星火商店仓库一次同步的时间降低至10分钟左右