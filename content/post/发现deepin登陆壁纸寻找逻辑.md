---
title: 发现deepin登陆壁纸寻找逻辑&/proc里面映射的主目录
date: 2021-11-11T00:47:27+08:00
lastmod: 2021-11-11T00:47:27+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
cover: https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1636563073612.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - Linux
# nolastmod: true
draft: false
---

书接上文的搜索`.jpg`，发现了更多好玩的东西

<!--more-->

P.S. 我首先是想要让几个壁纸循环更换，但是默认的壁纸我不喜欢（风格不一样），就去`/usr/share/wallpapers/deepin`删了个干净

结果问题来了：登陆界面的壁纸变成纯白了。。。

这个壁纸是不受壁纸设置控制的，不知道在哪，就只好恢复下原来的wallpapers,看看默认是哪个桌面壁纸被当成了登陆界面

是`desktop.jpg`

继续全删，再把想要的背景改名为desktop.jpg复制进去，注销，完美！

但是在我搜索jpg的时候，发现了这样一个东西

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1636564545651.png)

正是我的背景图

然而位置不对！这个位置是`/etc/alternatives`

打开一看，好家伙

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1636564585404.png)

原来dde的登陆界面读取的是这个了

等等，既然是alternative,也就是说有不是alternative的啊

然后我找到了这个东西

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1636564667182.png)

这里！这里才是真正的登陆背景来源！

而这个文件层层溯源，发现来自这里

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1636564803150.png)

又回到最初的起点～

所以逻辑已经明了了，是从`/usr/share/wallpapers/deepin`里读取`desktop.jpg`,然后软链接到`deepin-default-background`，接着链接到`default_background.jpg`，最终被读取到登录背景（不确定是不是dde-lock，如果是dde-lock理应可以被图形化设置背景啊）

吐槽一下：**为什么dde就是做不到把登陆背景和锁屏背景一致？？？？明明15.X根本没出现过相关问题！**

-----

在寻找jpg的时候我发现了大量的重复结果，这也导致了我的电脑风扇狂转~~以及我的电量见底，熄灯后专注写博客没注意已经只有15%了。。。~~

然后我打开某个重复内容，发现地址居然在`/proc`

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1636565205775.png)

顺藤摸瓜后发现，/proc里映射了我的完整主目录！（这怎么这么眼熟？参看上一篇[传送门](https://shenmo7192.gitee.io/post/%E5%81%B6%E7%84%B6%E5%8F%91%E7%8E%B0deepin%E6%96%B0%E7%94%A8%E6%88%B7%E9%BB%98%E8%AE%A4%E4%B8%BB%E7%9B%AE%E5%BD%95%E6%A8%A1%E6%9D%BF%E4%BD%8D%E7%BD%AE/)）

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1636565253341.png)

不太明白原理，希望有大佬帮忙解答

如果是稳定映射的话，是不是可以通过操作这个目录实现对主目录的操作？是不是就可以绕过UOS对于操作主目录的限制？（经过测试，读写操作都是可以进行的，而且会同步到主目录）

