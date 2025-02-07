---
title: GXDE OS 15.14.3 版本更新发布(2025.01.13)
date: 2025-01-14T00:48:49+08:00
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - Linux测评
tags:
  - Linux
  - 笔记
# nolastmod: true
draft: false
---

GXDE OS 15.14.3 版本更新

<!--more-->

GXDE 是基于 deepin 15 时期的深度桌面环境重生的桌面环境，在不改变主要设计风格的前提下融合了 deepin 15/20/23 各时期的优秀桌面组件和深度社区开发者的优秀作品，是一款带有怀旧风的轻量，易用，稳定且开箱即用的桌面环境

官网： https://www.gxde.top/

下载链接：

* 国内镜像 https://mirrors.sdu.edu.cn/GXDE/ISO/15.14.3/
* 星火网盘 [https://share.spark-app.store/index.php?share/folder&user=1&sid=RTvcs6A7](https://share.spark-app.store/index.php?share/folder&user=1&sid=RTvcs6A7)
* 海外源站 https://repo.gxde.top/ISO/15.14.3/

![图片.png](https://storage.deepin.org/thread/202501131157248081_图片.png)

GXDE OS是基于 Debian Stable/Sid 的一款以 GXDE 桌面为特色的本土Linux发行版，旨在提供 轻量，易用，稳定且开箱即用的使用体验。除 Debian 的基础外，GXDE OS 参考上游 deepin 的改动提供了Qt5Base, Linux Kernel 等基础软件包，额外提供了Linyaps (玲珑) , 星火应用商店 , ACE兼容环境 与 KMRE(麒麟移动应用运行环境) 等国内常用生态工具的适配。GXDE OS支持 amd64/arm64/loong64 架构。

相比于上游 deepin ，GXDE OS 更注重稳定和易用，对于新特性的支持**并不十分积极**，特效较为朴素和怀旧。喜欢追求最新桌面交互设计，AI助理，华丽特效以及更喜欢新技术的朋友**请继续关注 deepin V25~**

---

Hola，这里大概是年前最后一次大更新了，主要是根据用户反馈调整了一些 deepin 15 界面的设计，使其更易用，更符合操作习惯，并添加了安卓模拟器的支持

以下为更新日志

* 新增: 系统消息提示改为显示至右下角 感谢 [@魔法师](user/101467)
* 新增: 日历(gxde-calendar)每日一言支持英文
* 新增: 安装 ISO 支持国际化，提供多语言选项
* 新增: arm64 鲲鹏/通用内核更新到6.12.8 参考 deepin 内核配置 感谢 [@opsiff](https://github.com/opsiff)
* 新增: 推荐安装 扫雷 2048  深度计算器
* 新增: 文件管理器(DFM) 支持设置自定义背景 感谢 [@gfdgd_xi](user/239113)
* 新增: 添加了壁纸 Dream World 到社区壁纸包
* 新增: 565.77 N卡驱动 感谢 [@Elysia猫猫侠⁧](user/300575)
* 新增: 系统支持 KMRE 安卓模拟器，通过 `sudo aptss install kmre` 即可安装(暂仅x86支持)
* 更新: 玲珑(Linyaps)更新到 1.7.4-1
* 更新: 更新基础开发库 dtklog 至与 deepin 上游同步
* 更新: 更新深度应用 深度相册(deepin-album) 深度日志查看器(deepin log viewer)、深度相机(deepin-camera) 深度跨屏协同 (dde-cooperation)至与 deepin 上游同步
* 更新: 更新社区应用 星火动态壁纸 至与上游同步 感谢 [@depend](user/262214) 提供的原生动态壁纸支持
* 修复: 系统任务栏(dde-dock) dbus 接口无法调用的问题
* 修复: 系统任务栏(dde-dock)的全局搜索(dde-grand-search)插件按钮模糊/提示颜色错误/背景模糊 的问题
* 修复: 全局搜索(dde-grand-search) 打开任何文件都要打开两次
* 修复: Garma 图标模糊 未适配高分屏的问题
* 修复: 无法加入内测的问题
* 修复: 更新器修复升级systemd失败
* 修复: 优化 GXDE 热区在非特效模式下的使用体验
* 修复: 修复 loong64、riscv64 dtkgui5、dtkwidget5 无法构建、安装的问题
* 调整: 降低新安装用户bpo源的优先级，提高系统稳定性
* 调整: 因武汉线路无法访问 gxde.org ，系统源切换到 gxde.top

