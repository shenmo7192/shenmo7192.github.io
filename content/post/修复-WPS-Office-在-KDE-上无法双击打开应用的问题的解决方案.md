---
title: "修复 WPS Office 在 KDE 上无法双击打开应用的问题的解决方案"
date: 2026-03-15T14:45:01+08:00
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

这个问题是我在修 APM WPS 无法打开文件的时候发现的，在AOSC上有同样的问题

脚本内容：

```
`#!/usr/bin/env bash

# 自动进入文件所在目录再启动 WPS，支持本地路径、file://、KIO-Fuse(SMB/NAS)

log_file="/tmp/kde-open-wps.log"
echo "[$(date)] Arguments:" "$@" >> "$log_file"

# 如果没有参数，直接启动WPS

if [[ $# -eq 0 ]]; then
echo "[$(date)] 无参数，直接启动WPS" >> "$log_file"
exec wps
exit 0
fi

declare -a paths=()
declare -a fnames=()

for arg in "$@"; do
path="${arg#file://}"
if [[ ! -e "$path" && "$path" == *%* ]]; then
path=$(printf '%b' "${path//%/\\x}")
fi
if [[ -f "$path" ]]; then
paths+=("$(dirname "$path")")
fnames+=("$(basename "$path")")
else
echo "[$(date)] ⚠️ 文件不存在: $path" >> "$log_file"
fi
done

if [[ ${#paths[@]} -gt 0 ]]; then
cd "${paths[0]}" || { echo "[$(date)] ❌ 无法进入目录: ${paths[0]}" >> "$log_file"; exit 1; }
exec wps "${fnames[@]}"
else
echo "[$(date)] ❌ 没有找到可打开的文件" >> "$log_file"
exit 1
fi
`
```

把脚本保存为文件后，修改WPS的启动指令即可修复

星火和 APM 已修复并推送相关问题
