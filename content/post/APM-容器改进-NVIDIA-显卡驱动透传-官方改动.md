---
title: "APM 容器改进 NVIDIA 显卡驱动透传 （官方改动）"
date: 2026-01-24T11:53:06+08:00
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

感谢 @罐子 的启发和 DeepSeek V3.2 的伟力，我改善了 APM 容器的 Nvidia 透传方案，现在可完整透穿 **OpenGL / GLX Vendor**的配置和库了，修复了部分应用透传驱动后仍无法正常调用 Nvidia 显卡加速的问题

相关代码：

- 玲珑社区增强版改动：https://github.com/guanzi008/linyaps/blob/rework/mainline/libs/linglong/src/linglong/runtime/host_nvidia_extension.cpp

- APM/ACE 对应的改动： https://gitee.com/amber-ce/amber-pm/blob/master/src/var/lib/apm/apm/files/bin/amber-ce-configure-nvidia

以下是参考 https://bbs.deepin.org.cn/post/295153 的更新说明，再次感谢 @罐子 和 @mozixun

## 【功能说明】APM 容器已改进 NVIDIA 显卡（N 卡）透传（官方改动）
本帖说明 ​**APM容器（Amber CE / Amber PM）中已改善的 NVIDIA 显卡透传相关功能**​。

**该功能为官方实现**

## 项目源码地址：https://gitee.com/amber-ce/amber-pm/

### 一、已支持的 NVIDIA 显卡能力
当前在 ​**APM容器运行环境中**​，已实现对 ​**宿主机 NVIDIA 显卡的用户态驱动透传支持**​，主要包括：

**1. 宿主机 NVIDIA 闭源驱动直通**

容器安装时会自动从宿主机系统中收集 NVIDIA 相关用户态驱动库，并软链接到容器中，使容器内应用可以直接使用宿主机已安装的 NVIDIA 闭源驱动。

**2. 正确的 OpenGL / GLX Vendor 选择**

同步注入 NVIDIA 的 GLVND vendor 组件，避免容器环境下 OpenGL / GLX 走 Mesa 或其它错误实现，保证显卡能够正常工作。

**3. 同时支持 64 位与 32 位 NVIDIA 库**

自动处理 32 位 NVIDIA OpenGL / GLX 相关库路径，保障部分 32 位应用或兼容运行环境在容器内也可以正常使用显卡。

**4. NVIDIA 相关环境变量透传**

运行时会透传宿主机 NVIDIA 所需的环境变量，与主机配置一致，确保不会让不必要使用独立显卡的软件强制启动显卡。

### 二、宿主机驱动要求（重要）
该功能 ​**依赖宿主机已正确安装 NVIDIA 闭源驱动**​。

宿主机驱动安装方法可参考 deepin 论坛帖子：

https://bbs.deepin.org/post/294981

请确认：

- 宿主机 NVIDIA 驱动可正常使用

- `nvidia-smi` 在宿主机可正常运行

- OpenGL / GLX 已由 NVIDIA 驱动接管

### 三、注意事项与风险提示

- APM 容器内使用的是宿主机 NVIDIA 用户态驱动，宿主机驱动变动会直接影响容器内应用。

- 属于运行时级别的驱动透传与库注入实现，并非 NVIDIA 官方容器方案。

- 遇到问题需同时排查宿主机驱动状态与APM容器运行环境。

## 📥 下载地址
https://amber-pm.spark-app.store/
