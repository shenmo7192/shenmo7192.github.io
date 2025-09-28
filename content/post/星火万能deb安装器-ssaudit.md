---
title: 星火万能deb安装器：ssaudit 
date: 2025-09-28T23:23:46+08:00
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

ssaudit指令会随星火应用商店或aptss安装到系统中

<!--more-->



```
-----------------------------------------------------------------------------
Spark Store Anstall script. 星火商店审核脚本
用法: ssaudit [选项] <deb路径>
选项:
  -h, --help                   显示帮助信息
  --delete-after-install       安装成功后删除软件包
  --no-create-desktop-entry    不创建桌面快捷方式
  --force-create-desktop-entry 强制创建桌面快捷方式
  --amber-ce-bookworm          使用bookworm-run ACE容器安装
  --amber-ce-trixie          使用trixie-run ACE容器安装
  --amber-ce-deepin23          使用deepin23-run ACE容器安装
  --amber-ce-sid          使用sid-run ACE容器安装
  --native                     只在主机安装，不使用ACE容器
```

若无任何参数，直接 sudo ssaudit 把deb拖进来，则会：

* 先尝试在主机安装，若失败，则尝试在ACE Debian 12 安装；若再失败，则尝试在 ACE Debian 13 安装
* 如果安装成功，则自动创建桌面快捷方式（与星火配置一致，可改为默认关闭）

---

也可加上参数

* 对于输入法，虚拟机，主题类应用，应当使用 --native 只安装到主机
* 不想自动创建快捷方式，则 --no-create-desktop-entry
* 安装成功后删除安装包，则 --delete-after-install

