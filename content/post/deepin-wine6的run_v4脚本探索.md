---
title: Deepin Wine6的run_v4脚本探索——更新系统
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - spark-dwine-helper文档
tags:
  - linux
# nolastmod: true
draft: false
---
发布时间： 2022-05-29T19:30:37+08:00



<!--more-->
## 结论：


### 更新条件
* 当获取到的版本号与已保存的版本号(`"$WINEPREFIX/PACKAGE_VERSION"`中)不同时，执行更新
* 在存在`files.md5sum`时，以md5sum当做版本号；如果不存在，则接收在启动脚本(一般为`run.sh`）中的`APPVER=`字段（逻辑上有一个`APPVER="@deb_version_string@"`，但是没有发现这个是怎么获取的，而且会在后续被这个逻辑覆盖）。在启动时检测，如果与`$WINEPREFIX/PACKAGE_VERSION`中的相符，则启动，跳过更新；如果不符，则执行更新并把新的`APPVER`写入`$WINEPREFIX/PACKAGE_VERSION`

### 更新行为
* 执行更新时，当容器名符合 `"Deepin-Intelligent" | "Deepin-QQ" | "Deepin-TIM" | "Deepin-WeChat" | "Deepin-WXWork" | "Deepin-Dding"`中的一个时，执行删除容器后解压（如果有配置文件，就一起没了）
* 执行更新时，当容器名不符合上述时，则把新的`files.7z`解压到`"${WINEPREFIX}.tmpdir"`，然后执行updater（源文件夹设置为`"${WINEPREFIX}.tmpdir"`，目的文件夹设置为`"${WINEPREFIX}"`）
#### updater的行为：
* 这可能是一个定制版的，可以定制保留策略的rsync
* 默认行为是同名文件用源文件夹中的覆盖目的文件夹的，如果目的文件夹的里面有但源文件夹里没有的(比如软件自己的配置文件)，则跳过
  *  举例：原来的软件在自己的目录放置了conf，而新的包里没有这个文件，这个文件会被跳过
* 对于某些文件需要保留的，或者源文件夹中某些文件不需要同步的（比如update.policy自己），则可以通过设置`update.policy`来精确配置保留哪个，







## 分析过程

----

这是一个deepin-wine6应用包（一般deepin官方提供的启动脚本叫run.sh，这里是qq.sh）

![enter description here](https://xiaoshujiang-shenmo.oss-accelerate.aliyuncs.com/小书匠/1653823906670.png)

fires.7z里面放的是容器，files.md5sum是md5值，用于版本更新判断

qq.sh里面是启动脚本

```bash
#!/bin/sh

#   Copyright (C) 2016 Deepin, Inc.
#
#   Author:     Li LongYu <lilongyu@linuxdeepin.com>
#               Peng Hao <penghao@linuxdeepin.com>

version_gt() { test "$(echo "$@" | tr " " "\n" | sort -V | head -n 1)" != "$1"; }

BOTTLENAME="Wine-QQ"
APPVER="9.6.0.1hf3"
EXEC_PATH="C:/Program Files/Tencent/QQ/Bin/QQ.exe"
START_SHELL_PATH="/opt/deepinwine/tools/run_v4.sh"
export MIME_TYPE=""
export DEB_PACKAGE_NAME="com.qq.im.dwine"
export APPRUN_CMD="deepin-wine6-stable"
DISABLE_ATTACH_FILE_DIALOG=""

export SPECIFY_SHELL_DIR=`dirname $START_SHELL_PATH`

ARCHIVE_FILE_DIR="/opt/apps/$DEB_PACKAGE_NAME/files"

export WINEDLLPATH=/opt/$APPRUN_CMD/lib:/opt/$APPRUN_CMD/lib64

export WINEPREDLL="$ARCHIVE_FILE_DIR/dlls"

if [ -z "$DISABLE_ATTACH_FILE_DIALOG" ];then
    export ATTACH_FILE_DIALOG=1
fi

if [ -n "$EXEC_PATH" ];then
    if [ -z "${EXEC_PATH##*.lnk*}" ];then
        $START_SHELL_PATH $BOTTLENAME $APPVER "C:/windows/command/start.exe" "/Unix" "$EXEC_PATH" "$@"
    else
        $START_SHELL_PATH $BOTTLENAME $APPVER "$EXEC_PATH" "$@"
    fi
else
    $START_SHELL_PATH $BOTTLENAME $APPVER "uninstaller.exe" "$@"
fi

```
可以知道，这里设定的`APPVER`是 `9.6.0.1hf3`，使用的启动脚本是`run_v4.sh`

启动时会把`APPVER`作为第二个参数传出去

设置完各种变量之后，执行`run_v4.sh`

---

run_v4会在启动时首先获取`APPVER`

首先会在开头获取一个`APPVER="@deb_version_string@"`，但是没看出这是用什么获取的，而且在587行被覆盖

587行的逻辑是：
```bash
if [ -f "$APPDIR/files.md5sum" ];then
    APPVER="$(cat $APPDIR/files.md5sum)"
else
    APPVER="$2"
fi

```

如果存在`files.md5sum`则使用此作为版本号（其实更接近于唯一版本标识符）
如果没有，则使用传入的第二个参数作为版本号，就是`run.sh`中指定的

随后，在执行更新APP时

```bash
UpdateApp()
{
	if [ -f "$WINEPREFIX/PACKAGE_VERSION" ] && [ "$(cat "$WINEPREFIX/PACKAGE_VERSION")" = "$APPVER" ]; then
		return
	fi
	if [ -d "${WINEPREFIX}.tmpdir" ]; then
		rm -rf "${WINEPREFIX}.tmpdir"
	fi

    case $BOTTLENAME in
        "Deepin-Intelligent" | "Deepin-QQ" | "Deepin-TIM" | "Deepin-WeChat" | "Deepin-WXWork" | "Deepin-Dding")
            rm -rf "$WINEPREFIX"
            DeployApp
            return
            ;;
    esac

	ExtractApp "${WINEPREFIX}.tmpdir"
	$SHELL_DIR/updater -s "${WINEPREFIX}.tmpdir" -c "${WINEPREFIX}" -v

    if UsePublicDir;then
        chgrp -R users "$WINEPREFIX"
        chmod -R 0775 "$WINEPREFIX"
    fi

	rm -rf "${WINEPREFIX}.tmpdir"
	echo "$APPVER" > "$WINEPREFIX/PACKAGE_VERSION"
}
```

首先是比对版本

比对位于`"$WINEPREFIX/PACKAGE_VERSION"`的版本号与获取到的`APPVER`（获取方法前文已经提及）。如果一致，则跳过；否则执行更新

然后检测是否是` "Deepin-Intelligent" | "Deepin-QQ" | "Deepin-TIM" | "Deepin-WeChat" | "Deepin-WXWork" | "Deepin-Dding"`其中的一个，如果是，可能因为updater无法处理的原因，则删除容器重新部署。对于其他的软件包，则执行`updater`

----
updater的行为分析：

首先执行updater，得知使用方法


```
shenmo@shenmo-PC:/opt/deepinwine/tools$ ./updater 
  -c string
        current prefix path to operate
  -s string
        source prefix path to operate
  -v    verbose mode
```

使用一个git仓库文件夹进行测试，得出以下结论：


* 这可能是一个定制版的，可以定制保留策略的rsync
* 默认行为是同名文件用源文件夹中的覆盖目的文件夹的，如果目的文件夹的里面有但源文件夹里没有的(比如软件自己的配置文件)，则跳过
  *  举例：原来的软件在自己的目录放置了conf，而新的包里没有这个文件，这个文件会被跳过
* 对于某些文件需要保留的，或者源文件夹中某些文件不需要同步的（比如update.policy自己），则可以通过设置`update.policy`来精确配置保留哪个，

---
### 关于update.policy

官方没有给出文档，在此附上一份样本，可以按需修改

这是来自Deepin-Wechat的policy文件，似乎默认会使用这个，因为发现其他星火的包都是这个策略，而在此之前大家都没发现这个更新系统，推测可能是默认生成的。当然，也可能是大家都基于这个容器打的包(

位置在~/.deepinwine/Deepin-WeChat/update.policy

```
[File]
;;=============================================================
;; Registry   - Mask this file is a registry file.
;; Keep       - Default. Use template file.
;; Override   - Use file in current prefix.
;; Replace    - If it's different type in current prefix and
;;              in template, use template one to replace it.
;; Ingore     - Ingore file when copy.

;; Ingore update.policy itself.
"^update.policy$" = "Ingore"
"^.update-timestamp$" = "Ingore"

;; System registry files.
"^(system|userdef|user).reg$" = "Registry"

;; Addtional assist files.
"^drive_c/Deepin" = "Keep"

;; Microsoft Office files.
"^drive_c/Windows/(?:control\.ini|hh\.dat|mapiuid\.ini|Reg Save Log\.txt)$" = "Override"



[Registry]
;;=============================================================
;; Keep       - Use template key section
;; Override   - Use user current key section
;; Merge      - Default. Merge two section, user current values
                override template

"^Software\\\\Wine\\\\DllOverrides$" = "Keep"
"^Software\\\\Wine\\\\Fonts\\\\Replacements$" = "Keep"

```