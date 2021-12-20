---
title: 可以在deepin上运行的UOS版联系人（深谈）分享！
date: 2021-12-21T01:21:52+08:00
lastmod: 2021-12-21T01:21:52+08:00
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
---

我特别喜欢说一句话：众所周知

但是实际上并不是众所周知的是

我在账号更新的时候说过这么一句话

<!--more-->
![enter description here](https://storage.deepin.org/thread/202112210048348804_%E5%9B%BE%E7%89%87.png)

但是并没有实现

所以我们就自己实现吧！

负责登陆deepin-contacts的UOS账号的组件是deepin-deepinid-client。然而，deepin的账号系统并不支持接入deepin-contacts，这导致直接安装后登陆deepinid会显示错误无法进入

那么核心思路就是提取UOS的deepin-deepinid-client包给社区版使用！

提取出来之后试过用bwrap，不好用，推测是deepin-contacts利用dbus/daemon唤起deepin-deeppinid-client而不是自己拉

但是之前排障的时候发现过，dde-dock杀死后在daemon没反应过来的时候启动一个新的dock,daemon不会再次尝试拉起

这就是解决的方法了：在登陆前杀死deepin-deepinid*，然后瞬间启动UOS版本的deepin-deeppinid-client用于登陆，登陆成功后再拉回原版deepin的deepin-deeppinid-client

效果如下

![enter description here](https://storage.deepin.org/thread/202112210109325060_%E6%88%AA%E5%9B%BE_bizchat_20211221004201.png)

需要首先去UOS论坛注册一个账号（似乎可以直接注册，我没试过）

https://account.uniontech.com/register

依赖包下载地址：https://shenmo.lanzoul.com/b01d0ktcb
密码:5v3h

本体下载地址：https://shenmo.lanzoul.com/iw724xtgtre

星火商店可搜索：深谈（UOS联系人）

或者在浏览器打开

spk://store/chat/org.deepin.contacts
