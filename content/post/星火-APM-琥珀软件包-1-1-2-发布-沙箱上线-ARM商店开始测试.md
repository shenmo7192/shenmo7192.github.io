---
title: 星火 APM 琥珀软件包 1.1.2 发布：沙箱上线，ARM商店开始测试
date: 2025-11-02T12:03:39+08:00
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

1.1.2版本优化了 wine 应用清理逻辑，同时加上了实验性沙箱功能

使用 apm sandbox-run 包名 启动应用即可让应用运行在主目录沙箱中，只可以访问主目录 下载，桌面，音乐等目录，应用文件均会被保存在 ~/.apm/包名 下，避免了卸载残留难以清理的问题

```
`APM - Amber Package Manager 1.1.2

Usage:
  apm [COMMAND] [OPTIONS] [PACKAGES...]

Commands:
  install           安装软件包
  remove            卸载软件包
  run      运行指定软件包的可执行文件
  sandbox-run  运行指定软件包的可执行文件（主目录沙箱化）

  update            更新软件包信息
  hold              锁定软件包版本
  unhold            解锁软件包版本
  full-upgrade      升级全部软件包
  list              查看可用软件包信息
  search            搜索软件包

  download          下载包
  show              展示包信息
  clean             清除缓存软件包
  autoremove        自动移除不需要的包
  ssaudit     使用 ssaudit 进行本地软件安装，详情见 spark-store
  debug             显示调试系统信息并进入调试环境

  amber             彩蛋功能
  xmp360            彩蛋功能
  bronya            彩蛋功能

  -h, --help        显示此帮助信息
  -v, --version     展示APM版本号
`
```

此外，ARM64架构的 APM 琥珀网页商店 开始测试了，支持 deepin 23 / 25 , UOS , 银河麒麟V10SP1，Debian, Ubuntu

https://erotica.spark-app.store/arm64-apm/
