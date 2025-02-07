---
title: 配置Pandavan老毛子的校园网ipv6支持
date: 2022-10-09T22:40:07+08:00
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - Linux
  - 笔记
# nolastmod: true
draft: false
---

踩坑记录

<!--more-->

> 前言：校园网认证部分不写，这部分自行配置。这里要踩的坑是老毛子固件不支持ipv6的upnp和NAT6，只能用napt66来支持ipv6访问，用socat来实现nat

## 一、开启ipv6支持
1. 打开napt66
  * 系统管理-->服务-->其他服务-->启用napt66(重启后生效)
* 重启

2. wan-->ipv6--->如下设置

https://zhuanlan.zhihu.com/p/91901946

已经购买的刷好的机器不需要点那个重置，到ipv6了之后再照做即可

此时已可访问ipv6地址（如果你所在的网络不是校园网，不需要nat6，则不需要第一步，直接到这里设置个自动，ipv6内网也用dhcpv6获取即可）

## 二、开启ipv6映射
 
 * ip6tables不可行，老毛子固件不支持NAT6
 * napt66不能设置端口转发

使用：socat

`socat TCP6-LISTEN:外网端口,reuseaddr,fork TCP4:内网ipv4:内网端口`

`socat UDP6-LISTEN:外网端口,reuseaddr,fork UDP4:内网ipv4:内网端口`

socat找不到命令就去opkg装，在 配置扩展功能 那里启动opt环境，然后用webssh连接

开机启动的话，在前面加nohup，后面加&，加到

自定义设置-->脚本-->在防火墙规则启动后执行

```bash
nohup socat TCP6-LISTEN:22224,reuseaddr,fork TCP4:192.168.123.19:22224 &
nohup socat UDP6-LISTEN:22224,reuseaddr,fork UDP4:192.168.123.19:22224 &
nohup socat TCP6-LISTEN:38324,reuseaddr,fork TCP4:192.168.123.19:38324 &
```

这里是我的配置