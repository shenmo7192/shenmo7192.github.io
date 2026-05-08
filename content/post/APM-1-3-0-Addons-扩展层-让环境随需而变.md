---
title: APM 1.3.0 ：Addons 扩展层：让环境随需而变
date: 2026-04-25T11:31:13+08:00
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

# APM 1.3.0 正式发布 —— Addons 扩展层：让环境随需而变

## 引言
APM 1.3.0 带来了大家期待已久的 **Addons 扩展层**功能，这是一次从"打包灵活"到"使用灵活"的关键跨越。

在过去，APM 已经通过全自动转换器 `amber-pm-convert` 和多层依赖机制，让打包过程变得足够灵活。但在实际使用中，我们遇到了一个新的问题：

> 
**开发环境的需求千差万别，如何在保持精简的同时满足个性化？**

## 曾经的困境
不同的开发者需要不同的工具链：Java、Python、DTK、Git、CMake……如果在构建每个包的时候就直接把开发环境打包进 base，势必造成严重的存储浪费——毕竟并不是每个用户都需要这些环境。

也许有人会说："用 `override_layer` （详见） 不就好了？"

确实可以，但 `override_layer` 是在 **APP侧**配置的。这意味着开发环境只能和具体的软件包绑定——一个 IDE 就要配一套开发环境。对于拥有多个开发工具的用户来说，硬盘的处境可想而知：

> 
💾 硬盘：想想就刺激。

## APM 1.3.0 的解决方案：Addons 扩展层
APM 1.3.0 引入了 **Addons 扩展层**，将环境扩展的能力从"应用侧"转移到了 **base 侧（以及中间层）**。

只要在 base 侧安装 addons 包，**所有运行在这个 base 上的应用都会自动获得该扩展**——无需逐个配置，无需重复安装。

### 核心理念

- **一次安装，全局复用**：安装在 base 上的 addons 自动对基于该 base 的所有应用生效

- **按需组合，灵活隔离**：通过中间层机制，可以选择性地让部分应用获得特定扩展

- **结构精简**：Addons 包不需要 `info` 文件和 `entries/` 目录，极轻量

## 架构图

### 普通应用（以 Firefox 为例）

```
`┌─────────────────────────────────┐
│           APP: Firefox          |
├─────────────────────────────────┤
│  amber-pm-bookworm              │
│  ┌───────────────────────────┐  │
│  │  Addons: ffmpeg-addons    │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
`
```

Firefox 运行在 `amber-pm-bookworm` base 上，admin 只需安装 `ffmpeg-addons`，所有基于 bookworm 的应用都会自动获得 ffmpeg 支持。

### 开发应用（以 Trae AI IDE 为例）

```
`┌─────────────────────────────────────────┐
│            APP: Trae AI IDE              │
├─────────────────────────────────────────┤
│  amber-pm-bookworm-dev（中间层）         │
│  ┌─────────┐ ┌────────┐ ┌───────┐      │
│  │git-addon│ │cmake-  │ │java-  │      │
│  │   s     │ │addons  │ │addons │      │
│  └─────────┘ └────────┘ └───────┘      │
├─────────────────────────────────────────┤
│  amber-pm-bookworm（base）              │
└─────────────────────────────────────────┘
`
```

Trae AI IDE 的 base 指向 `amber-pm-bookworm-dev` 中间层，该中间层挂载了 git、cmake、java 等 addons。普通应用仍然使用原版 `amber-pm-bookworm`，不会加载开发环境。即使 addons 之间有冲突，也可以通过不同的中间层来隔离。

## addons 不止 base 能用
Addons 不仅能挂载在 base 上，还能挂载在**中间层**上。这意味着你可以：

1. 创建一个 `amber-pm-bookworm-dev` 中间层

1. 将 git、cmake、java 等开发工具 addons 注册到这个中间层

1. 把需要开发环境的应用的 base 换成 `amber-pm-bookworm-dev`

这样，**普通应用仍然使用原版 base，只有开发类应用才会获取到开发环境**。即使 addons 互相冲突，也可以通过中间层来隔离。

## 使用方法
APM Addons 秉承了 APM 一贯的新手友好设计。你不需要手动创建目录、编写配置文件，只需要一条命令：

### amber-pm-addons-maker 使用说明

```
`用法: amber-pm-addons-maker --base  [--manual] [--pkgname <包名>] [--version <版本>] [deb文件路径]

参数说明:
  --base       必填参数，指定基础环境名称
  --manual     启用手动模式：融合挂载后打开交互 shell
  --pkgname    可选参数，指定包名（建议格式：-<描述>-addons）
  --version    可选参数，指定版本号（默认 1.0.0-apm）
  deb文件路径  可选参数，要安装到 addons 环境中的 Deb 文件
`
```

### 示例 1：手动模式（交互式安装）
适合需要自定义安装、配置环境的场景：

```
`amber-pm-addons-maker --base amber-pm-bookworm --manual --pkgname amber-pm-bookworm-git-addons
`
```

执行后会自动挂载目标 base 并进入交互式 shell，你可以像操作普通 Debian 环境一样：

```
`apt update
apt install git git-lfs
exit
`
```

退出后工具会自动打包，生成的 deb 安装后即可在对应 base 上生效。

### 示例 2：自动模式（直接安装 deb）
适合已经有现成 deb 包的场景，一键完成：

```
`amber-pm-addons-maker --base amber-pm-trixie ./nvidia-driver.deb --pkgname amber-pm-trixie-nvidia-addons
`
```

### 示例 3：创建开发环境中间层

```
`# 先分别创建各个 addons
amber-pm-addons-maker --base amber-pm-bookworm --manual --pkgname amber-pm-bookworm-git-addons
amber-pm-addons-maker --base amber-pm-bookworm --manual --pkgname amber-pm-bookworm-cmake-addons
amber-pm-addons-maker --base amber-pm-bookworm --manual --pkgname amber-pm-bookworm-java-addons

# 然后创建一个 dev-base 中间层（通过 amber-pm-convert 或手动打包）
# 将上述 addons 注册到 dev-base 的 info_layer_addons.d/ 中
`
```

安装后的 addons 包会自动在对应 base 的 `info_layer_addons.d/` 中注册，所有依赖该 base 的应用**下次启动时即可自动加载**，无需任何额外配置。

## 技术要点

- **命名规范**：建议格式为 `-<描述>-addons`，例如 `amber-pm-bookworm-nvidia-addons`

- **自动注册**：安装后自动在 base 的 `info_layer_addons.d/` 中创建注册文件

- **优先级控制**：`info_layer_addons.d/` 中的文件名格式为 `优先级-addons包名`，数字越小优先级越高

- **兼容 override_layer**：Addons 层与现有的 `info_layer_override` 完全兼容，协同工作

## 方案对比

方案
配置位置
复用性
隔离性
存储效率

预装进 base
打包时
✅ 全局复用
❌ 无
❌ 浪费

override_layer
应用侧
❌ 逐应用绑定
⚠️ 受限
❌ 重复

**Addons（1.3.0）**
**base/中间层侧**
✅ 全局复用
✅ 中间层隔离
✅ 精简

## 总结

> 
**一次安装，全局复用；按需组合，灵活隔离。**

APM 1.3.0 的 Addons 功能，让环境管理真正做到了"随需而变"。感谢每一位用户的反馈与建议，APM 会持续向更灵活、更友好的方向进化。

**立即体验 APM 1.3.0：**

https://amber-pm.spark-app.store/
