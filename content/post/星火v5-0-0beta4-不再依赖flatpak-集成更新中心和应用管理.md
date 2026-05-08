---
title: 星火v5.0.0beta4：不再依赖flatpak，集成更新中心和应用管理
date: 2026-04-13T20:40:10+08:00
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

v4时代很多的组件都是散装的，v5现在可以用AI编程了，开始逐渐组件集中化，软件更新器和应用管理器（好像还有点小问题，可以先用首页推荐的凑合下）现已合并到主程序，更新的时候也不是单独开窗口了，而是和其他软件一样一起走主程序下载列表

![图片.png](https://storage.deepin.org/thread/202604131302543183_图片.png)

![图片.png](https://storage.deepin.org/thread/202604131237231216_图片.png)

![图片.png](https://storage.deepin.org/thread/202604131237416230_图片.png)

![图片.png](https://storage.deepin.org/thread/202604131239163371_图片.png)

下载地址：https://www.spark-app.store/

更新信息：

### Features

- 更新中心: 实现集中式软件更新中心功能

- 更新中心: 添加更新列表图标

- 更新中心: 统一使用下载包文件进行安装

- 更新中心: 添加全选功能及状态管理

- 搜索: 优先匹配应用名称

- 更新管理器: 添加安装参数以禁用桌面快捷方式和使用原生安装

- 应用管理: 添加 APM 可用性检查并调整相关逻辑

- 滚动: 添加分类切换时重置滚动位置功能

### Bug Fixes

- 修复更新中心发送的下载项和普通下载故障覆盖的问题

- 修复模态框滚动和点击事件处理

- 为多个组件添加 overscroll-contain 并处理滚轮事件

- 为滚动容器添加 overscroll-contain 防止滚动溢出

- 将 host-spawn 替换为 systemd-run --user 以不再依赖flatpak

- 软件管理器滚到底部后应用列表不再透滚

- 修复更新工具缺少软件名检查的问题

- 修复点击更新后无法推送到下载列表的问题

- 更新中心级联本地和远程图标回退

- 将更新中心 apm 命令从 ssaudit 改为 ssinstall 并优化打印 URI 命令

- 将 aptss 升级失败的错误提示从弹窗改为日志输出

- 修复 shell-caller 无法安装 apm 的问题

- 修复 Fedora 安装指令

### Other Changes

- 集成更新器

- 支持更新下载时展示图标

- 更新 electron 构建配置和 vite 别名设置

- 许可证更改为 GPL3

- 优化 README 格式

- 移除并重新添加 engines 字段到 package-lock.json，解决风险插件问题

- 安全加固 electron-builder 工具链
