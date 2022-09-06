---
title: Deepin Wine6的run_v4脚本探索——启动方式
date: 2022-05-30T21:33:21+08:00
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

终于搞懂`run_v4.sh`怎么启动了

<!--more-->


### 结论：

#### 情形1：三个参数
##### 用法：
`run_v4.sh $BOTTLENAME $APPVER "$EXEC_PATH" `

容器名，APP版本，启动路径

三号位的参数会被传到RunApp，然后转到CallApp，经过处理（如果没适配就是直接转，适配过的有的转有的就直接启动了）后转到CallProcess进行通用启动

* 如果容器不存在，会尝试解压。从APPDIR的APPTAR解压。APPDIR的位置是`/opt/apps/${DEB_PACKAGE_NAME}/files`。DEB_PACKAGE_NAME会从环境变量读取。这会在`run.sh`中设置。相关过程：ExtractApp()
* 如果容器存在，会在RunApp处对版本进行对比。如果所在的位置有`files.md5sum`，这个参数会被覆盖。更新行为请参看： https://blog.shenmo.tech/post/deepin-wine6%E7%9A%84run_v4%E8%84%9A%E6%9C%AC%E6%8E%A2%E7%B4%A2/
* 第三个参数是启动路径，会用从环境变量`APPRUN_CMD`中获取启动用的deepin-wine指令

所以，使用三个参数手动启动APP，首先要在环境变量中指定`DEB_PACKAGE_NAME`，然后`/opt/apps/${DEB_PACKAGE_NAME}/files`放好`files.7z`，再指定一个版本或者制作`files.md5sum`，然后指定启动脚本

很复杂对吧，而且路径写死了，因为这个并不是为平常使用设计的

##### 实践：用三个参数启动Spark-CloudMusic的最简方法
0. 先把软件包名和APPRUN_CMD export到环境变量
1. 容器名称打对了
2. APPVER请保证和容器中的一致。不一致就去尝试更新了。不过在这里，因为打包者写了md5sum文件，所以你写什么无所谓。对于没有提供md5sum文件的，请到`~/.deepinwine/$BOTTLENAME/PACKAGE_VERSION`读
3. 启动路径

实践开始，启动终端

* 首先执行
 ```bash
export DEB_PACKAGE_NAME=com.163.music.spark
export APPRUN_CMD="deepin-wine6-stable"

```
* 然后执行 `/opt/deepinwine/tools/run_v4.sh Spark-CloudMusic 我永远喜欢安柏 "c:/Program Files (x86)/Netease/CloudMusic/cloudmusic.exe"`

效果：
![enter description here](https://xiaoshujiang-shenmo.oss-accelerate.aliyuncs.com/小书匠/1653920318069.png)



---
#### 情形2：三个以上的参数

##### 2.1 第四个参数是"/Unix"
会执行lnk文件

需要在第五个参数处指明lnk位置

使用情景：在run.sh中指定的EXEC_PATH是一个lnk
在run.sh中会有处理
```bash
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

会用 "C:/windows/command/start.exe" 启动

##### 2.2 第四个参数不是/Unix

进入case阶段
```bash
case $4 in
	"-r" | "--reset")
		ResetApp
		;;
	"-c" | "--create")
		CreateBottle
		;;
	"-e" | "--remove")
		RemoveApp
		;;
	"-u" | "--uri")
        ParseArgs "$@"
		;;
	"-f" | "--file")
        ParseArgs "$@"
		;;
	"-h" | "--help")
		HelpApp
		;;
	*)
		echo "Invalid option: $4"
		echo "Use -h|--help to get help"
		exit 1
		;;
```

-r是重置，-c是创建，-e是删除，-u和-f都会转到参数分析
```bash
ParseArgs()
{
    if [ $# -eq 4 ];then
	    RunApp "$3"
    elif [ $# -eq 5 ];then
	    RunApp "$3" "$5"
    else
	    RunApp "$3" "$5" "$6"
    fi
}
```
嘛，反正就是把第四个跳过

这个更优雅的方法应该是把`$@`输入到一个列表里，然后再从里面删除一个元素，接着放这里

不过，又不是不能用....



### 源码片段：

```bash

BOTTLENAME="$1"
WINEPREFIX="$HOME/.deepinwine/$1"

if UsePublicDir;then
    WINEPREFIX="$PUBLIC_DIR/$1"
fi

APPDIR="/opt/apps/${DEB_PACKAGE_NAME}/files"
if [ -f "$APPDIR/files.md5sum" ];then
    APPVER="$(cat $APPDIR/files.md5sum)"
else
    APPVER="$2"
fi

debug_log "Run $*"

#执行lnk文件通过判断第5个参数是否是“/Unix”来判断
if [ "$4" == "/Unix" ];then
    RunApp "$3" "$4" "$5"
    exit 0
fi

if [ $# -lt 4 ]; then
	RunApp "$3"
	exit 0
fi
case $4 in
	"-r" | "--reset")
		ResetApp
		;;
	"-c" | "--create")
		CreateBottle
		;;
	"-e" | "--remove")
		RemoveApp
		;;
	"-u" | "--uri")
        ParseArgs "$@"
		;;
	"-f" | "--file")
        ParseArgs "$@"
		;;
	"-h" | "--help")
		HelpApp
		;;
	*)
		echo "Invalid option: $4"
		echo "Use -h|--help to get help"
		exit 1
		;;
esac
exit 0
```

完整脚本请看： https://gitee.com/deepin-community-store/spark-wine/blob/b1e08edfbe25c3e53716efe8039b1227d0e25989/spark-dwine-helper/dwine-helper-backup/run_v4.sh
