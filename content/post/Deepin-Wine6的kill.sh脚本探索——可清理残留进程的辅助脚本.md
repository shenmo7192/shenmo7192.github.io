---
title: Deepin Wine6的kill.sh脚本探索——可清理残留进程的辅助脚本
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
发布时间： 2022-05-30T18:26:37+08:00

对于QQ等退出会残留进程（没有窗口也没有托盘，还在后台跑）的流氓软件，deepin-wine也做了相应的调整，在启动时杀死，防止出错

<!--more-->


位置：/opt/deepinwine/tools/kill.sh

行为：
* 在没有任何参数时，杀死QQ进程
* 接收到参数时，会寻找第一个参数对应的容器名(在一系列骚操作下，懒得分析了，管他的，好用就完了)，找到进程，然后杀死
* 如果存在第二个参数，如果第二个参数为`block`，会检测是不是正在残留进程（如果被标注的bottle不活跃(没有Window，也没有托盘)则认为是残留；如果发现这个bottle有Window或者托盘，则认为这是活跃中的应用，不是残留进程），则尝试杀死。

用例：在`run_v4.sh`中，如果发现应用容器为`Deepin-WXWork"`，则执行`CallWXWork()`，代码片段如下

```bash
CallWXWork()
{
    if [ "autostart" == "$1" ]; then
        env WINEPREFIX="$WINEPREFIX" $WINE_CMD /opt/deepinwine/tools/startbottle.exe &
    else
        /opt/deepinwine/tools/kill.sh WXWork.exe block

        env WINEPREFIX="$WINEPREFIX" $WINE_CMD "c:\\Program Files\\WXWork\\WXWork.exe" &
    fi
}
```

如果是自动启动，则直接打开

如果不是，先杀死残留进程（如果有）再执行启动

以此原理，在spark_run_v4.sh中添加这样的`case`+Call启动，即可做到对星火wine应用的定制化启动，比如以后可以在星火的QQ启动脚本中添加此功能

