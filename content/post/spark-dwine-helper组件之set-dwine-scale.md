---
title: Spark Dwine Helper组件之set-dwine-scale
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
发布时间： 2022-05-30T15:20:14+08:00



<!--more-->
需求：deepin-wine5不能读取DEEPIN_WINE_SCALE的设置，需要手动指定；ubuntu下没有人给指定缩放

解决：读取DEEPIN_WINE_SCALE并设置缩放；对于没有DEEPIN_WINE_SCALE的，如果是deepin/UOS，则返回1.0 ；如果不是，弹窗让用户选择缩放

方式：set-dwine-scale.sh

---


位置:  https://gitee.com/deepin-community-store/spark-wine/blob/master/spark-dwine-helper/pkg/opt/durapps/spark-dwine-helper/set-dwine-scale.sh

作用：设置wine容器的缩放

原理：修改注册表键值

如果有DEEPIN_WINE_SCALE，则把内容输出到`~/.config/spark-wine/scale.txt`


如果没有，则调用`spark-get-scale.sh`
* 如果发现是deepin/uos，这意味着是1.0缩放
* 如果不是，检查是否有已存在的配置文件(`~/.config/spark-wine/scale.txt`)，如果有，退出
* 如果不是且无配置文件，弹窗询问用户

获取后，输出到`~/.config/spark-wine/scale.txt`

然后通过`~/.config/spark-wine/scale.txt`的数值进行设置

当`$APPRUN_CMD`存在（也就是被spark_run_v4.sh调用时），利用wine的原生方式添加
```
case "$env_dwine_scale" in
       1.0)
            dpi="96"
            ;;
        1.25)
            dpi="120"
            ;;
        1.5)
            dpi="144"
            ;;
        2.0)
            dpi="192"
            ;;
	*)
		dpi="96"
		#可能不是Xorg或者是其他错误
		;;
    esac
echo "用$APPRUN_CMD执行指令"
echo "指令为"
echo "env WINEPREFIX="$CONTAINER_PATH" $APPRUN_CMD reg ADD 'HKCU\Control Panel\Desktop' /v LogPixels /t REG_DWORD /d $dpi /f"

env WINEPREFIX="$CONTAINER_PATH" $APPRUN_CMD reg ADD 'HKCU\Control Panel\Desktop' /v LogPixels /t REG_DWORD /d $dpi /f

```

读取并按对应的值替换注册表键值
在`HKEY_CURRENT_USER\Control Panel\Desktop`和`HKEY_CURRENT_USER\Software\Wine\Fonts`中，以DWORD储存

![enter description here](https://xiaoshujiang-shenmo.oss-accelerate.aliyuncs.com/小书匠/1653895721239.png)

替换为指定的值

```bash
echo "没有检测到APPRUN_CMD环境变量，执行sed替换。如果要使用wine原生提供的方法，请在环境变量中指定(export)"
case "$env_dwine_scale" in
       1.0)
            reg_text="\"LogPixels\"=dword:00000060"
            ;;
        1.25)
            reg_text="\"LogPixels\"=dword:00000078"
            ;;
        1.5)
            reg_text="\"LogPixels\"=dword:00000090"
            ;;
        2.0)
            reg_text="\"LogPixels\"=dword:000000C0"
            ;;
	*)
		reg_text="\"LogPixels\"=dword:00000060"
		#可能不是Xorg
		;;
    esac

#####根据scale设置dword值


LogPixels_line=(`sed -n -e "/"LogPixels"/=" $CONTAINER_PATH/user.reg`)
#####关键词行数取得
until [ "${#LogPixels_line[@]}" = "0" ];do


line_num=${LogPixels_line[0]}

sed -i "$line_num"c\ "$reg_text" "$CONTAINER_PATH/user.reg"
LogPixels_line=(${LogPixels_line[@]:1})
done

```