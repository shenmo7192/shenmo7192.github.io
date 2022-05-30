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

如果有DEEPIN_WINE_SCALE，则读取并按对应的值替换注册表键值
在`HKEY_CURRENT_USER\Control Panel\Desktop`和`HKEY_CURRENT_USER\Software\Wine\Fonts`中，以DWORD储存

![enter description here](https://xiaoshujiang-shenmo.oss-accelerate.aliyuncs.com/小书匠/1653895721239.png)
替换为指定的值

```bash
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

```

如果没有，则调用`spark-get-scale.sh`
* 如果发现是deepin/uos，这意味着是1.0缩放
* 如果不是，检查是否有已存在的配置文件，如果有，退出
* 如果不是且无配置文件，弹窗询问用户

