---
title: 以root身份发送通知(如使用notify Send)到现在运行的用户上
date: 2022-08-05T16:35:01+08:00
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - linux
# nolastmod: true
draft: false
---

百度只能搜到国内的收费的文档

<!--more-->


从`Stack Overflow`抄的

如果你要使用`notify-send`的脚本，把这个东西放到最前面，你就会发现可以发送到当前启动的用户桌面上了

```bash
function notify-send() {
    #Detect the name of the display in use
    local display=":$(ls /tmp/.X11-unix/* | sed 's#/tmp/.X11-unix/X##' | head -n 1)"

    #Detect the user using such display
    local user=$(who | grep '('$display')' | awk '{print $1}' | head -n 1)

    #Detect the id of the user
    local uid=$(id -u $user)

    sudo -u $user DISPLAY=$display DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$uid/bus notify-send "$@"
}

```

来源： https://stackoverflow.com/questions/28195805/running-notify-send-as-root