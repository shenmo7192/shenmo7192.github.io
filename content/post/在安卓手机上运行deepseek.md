---
title: 在安卓手机上运行deepseek
date: 2025-02-02T23:40:46+08:00
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - 闲聊
# nolastmod: true
draft: false
---

建议：在要部署的安卓手机打开这个文章，方便复制指令


<!--more-->



步骤：


第一步：安装termux。

第二步：打开termux，运行下面指令，以获取访问手机存储的权限

`termux-setup-storage`

第三步：安装依赖

`pkg install git cmake golang`

第四步：下载并安装ollama

```bash
git clone --depth 1 https://github.com/ollama/ollama.git
cd ollama
go generate ./...
go build .
```
第五步：启动ollama

```
./ollama serve &
```
第六步，运行deepseek-r1 1.5b：

`./ollama run deepseek-r1:1.5b --verbose`




