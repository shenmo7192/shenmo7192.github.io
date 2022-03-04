---
title: 通过热区唤出侧边栏的折腾实践
date: 2021-10-08T12:29:20+08:00
lastmod: 2021-10-08T12:29:20+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
cover: https://z3.ax1x.com/2021/10/02/4bdqJK.gif
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - Linux
# nolastmod: true
draft: false
---
最开始把Linux当做主力系统是deepin 15.9，本人是非常习惯热区操作的
什么是热区呢？就是屏幕四个角用鼠标戳的时候进行某些操作

<!--more-->

deepin的一个经典操作就是猛戳右下角出控制中心

然而，后来在某些客户的要求下，热区被关闭了

一直到后来某个版本开始，甚至每次启动dde-kwin都会强制覆盖kwinrc文件来防止手动开启热区……

现在主力换成uk之后，发现麒麟的侧边栏设计比dde的侧边栏控制中心好很多，侧边栏只保留一个通知栏，下方有好用的widget和剪贴板（这个剪贴板操作手感比dde的那个强太多了）

相比于dde单独拉出一个窗口放剪贴板，单独做一个通知列表，我个人认为ukui的设计是更好的

我查了下快捷键，win+a是唤出侧边栏，心中狂喜

然后踩坑了。。。

不知为何ukui的快捷键很不灵敏，甚至包括win键单独按，很多时候就是不能唤起

我在想要拉起侧边栏的时候，总是输入一个a……

总是拉不起来，这是很难受的

而如果可以通过热区来唤起，是不是会非常方便呢？直接把鼠标华丽地甩到右下角，突突！侧边栏出来了

既然dde-kwin实现了，那ukui-kwin没道理不能实现啊

所以第一步，拿出我们的老朋友

`sudo apt install systemsettings`

下载kde系统设置

![](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633670043825.png)

打开后找到

工作空间行为——>屏幕边缘

![](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633670043845.png)

右下角戳一下，随便选一个效果，然后apply

你猜怎么着？起效了！

接下来我要做的很简单了，找到~/.config/kwinrc，找到对应行并修改即可

接下来踩到了第一个坑

根本没有这个文件！

随后发现ukui把kwin的config文件改名为ukui-kwinrc了。。。（汗）

更改后

```
[ElectricBorders]
Bottom=None
BottomLeft=None
BottomRight=ukui-sidebar
Left=None
Right=None
Top=None
TopLeft=None
TopRight=None

```

满怀激动地

`pkill kwin`

然后

`kwin`

报告未找到命令…..

啊这？进程名叫kwin，可执行难道是ukui-kwin？

`ukui-kwin`

启动了…（你说你改这个干啥啊你？）

再次满怀激动地戳右下角。。。没有反应

这是为什么呢？我启动了终端，直接在里面输入了

`ukui-sidebar`

结果如下

```
21-10-02 17:09:53.105 [139927504697600] DEBUG - |PID:47799|main.cpp:69(int main(int, char**))|"ukui-sidebar is already running!"
21-10-02 17:09:53.107 [139927504697600] WARN - |PID:47799|QFileSystemWatcher::removePaths: list is empty
21-10-02 17:09:53.107 [139927504697600] WARN - |PID:47799|QFileSystemWatcher::removePaths: list is empty`

```

> 
> 
> `ukui-sidebar is already running!`
> 
> 

看来ukui的侧边栏和dde-control-center一样，是常驻的，需要用参数调出

这里踩了第二个坑

`ukui-sidebar --help`
```
21-10-02 17:09:53.105 [139927504697600] DEBUG - |PID:47799|main.cpp:69(int main(int, char**))|"ukui-sidebar is already running!"
21-10-02 17:09:53.107 [139927504697600] WARN - |PID:47799|QFileSystemWatcher::removePaths: list is empty
21-10-02 17:09:53.107 [139927504697600] WARN - |PID:47799|QFileSystemWatcher::removePaths: list is empty

```


好嘛！干脆不鸟我

那如果和dde-control-center一样用--show呢？

还是不行

于是我决定用我的三脚猫功夫去扒优麒麟的代码，像Linus说的，Read the fucking source

在这里

<https://gitee.com/ubuntukylin/ukui-sidebar/blob/Debian/src/main.cpp>

看这行
```
QCommandLineParser parser ; QCommandLineOption debugOption ({ “d” , “debug” }, QObject :: tr ( “Display debug information” )); QCommandLineOption showSidebar ({ “s” , “show” }, QObject :: tr ( “show sidebar widget” ));
```

也就是说，应该是

`ukui-sidebar -s`

尝试在终端执行，好耶！拉起来了！！！

于是快乐地把ukui-kwinrc改成这样了

```
[ElectricBorders]
Bottom=None
BottomLeft=None
BottomRight="ukui-sidebar -s"
Left=None
Right=None
Top=None
TopLeft=None
TopRight=None
```

重启kwin后，发现

还是没有卵用….

难道是我用的不对？

改成绝对路径
```
[ElectricBorders]
Bottom=None
BottomLeft=None
BottomRight=sh -c "/usr/bin/ukui-sidebar -s"
Left=None
Right=None
Top=None
TopLeft=None
TopRight=None
```

仍旧卵用没有

上百度查kwinrc的手册

没有

bing

也没有

Google

也没有……

于是现在只剩下一种解决方法了

那就是

抄deepin的作业

下载deepin 15.11版本，这是最后一个经典版本了，还是用的dde-kwin，这正是我想要的

挂一下squashfs，chroot进live

看一下os-release，目录切到deepin live了没错

这时候出了问题

从15.9开始，dde不再默认启动热区

也就是说，我必须启动kwin，利用dde的设置启动热区，然后查看kwinrc

尝试 `startx`，果然不能用……

于是重启进入Windows环境，打开livecd

下一个坑来了：deepin 15.10开始，不再支持livecd试用。。。只能直接安装

谁等你啊？？？

于是我尝试切tty2，在deepin 20.1以上版本，这个方法被封死了，live用户也有了登录密码

直接输入startx

进入桌面成功

设置热区，测试可以拉起（OHHHHHHH）

然后我查看了kwinrc

看到了这一段
```
[Script-runcommandaction]
Border3Program=sh -c “dde-control-center –show”
BorderActivate=,3
Enabled=true
```
这啥玩意？“Script-runcommandaction”

尝试复制到ukui-kwinrc

果真不能用

接下来全局搜索deepin live cd下script关键词

发现kwin scripts目录

打开一看，看不懂….尝试复制粘贴到ukui同一目录

重启ukui-kwin，无效…..

查看deepin-kwin文档

deepin团队为了适配dde做了一系列兼容工作

难不成….

这个热区执行命令的功能

tmd是deepin团队自己写的？

啊这。。。。

眼看着无望，这时候群聊“柚子的朋友们”出现新消息了，开发者放出截图，oh my dde（社区制作的dde美化+优化软件）新版本将加入热区功能

woc这难道是心有灵犀？

之前在我最想要动态壁纸的时候，也是这位突然做了一个一只动态壁纸，后来通过魔改dde-desktop成为deepin 20下第一个可用的动态壁纸（现在的动态壁纸方案是另一位开发者做的，原理不相同）

这也许就是心有灵犀把

当一个人的愿望强烈到一定程度时，神明的视线就会……启动原神（bushi

题外话少说，我当即问，dde-kwin已经锁死了kwinrc，你是怎么做的？

他回答是做了一个独立应用，专门用来检测鼠标位置来实现热区功能

而且不和oh my dde集成

这意味着我可以单独抽出这个应用，运行到其他桌面环境！

理论上，甚至包括Windows！

马上git clone，找到插件名称

omd-requ

吐个槽，这个显然是oh my dde 热区的缩写。。。但是我看了真的瞬间血压升高。。。

这缩写方式从未见过，英文拼音混输

人家热区 英文名是`ElectricBorders`

不管怎么说，直接拉出来就编译

`sudo apt install qt5-default g++`

编译一次通过，显然没有用到dtk依赖

启动后没有任何提示….

`./omd-requ --help`

没有任何提示….（不是你们这样真的好么？只能翻代码？？？）

翻widget.cpp，发现这东西的配置文件是config.qaq

.qaq……..这也太可爱了吧！！！！

就连接受配置文件的变量都叫qaq…..

改了下配置文件的位置为~/.config/omd-requ/config.bunny（兔兔伯爵，出击！）

管开发者要了份样本

```
[General]
LowerLeftShell=
LowerRightShell=
TopLeftShell=
TopRightShell=

```
修改为
```
[General]
LowerLeftShell=
LowerRightShell=ukui-sidebar -s
TopLeftShell=
TopRightShell=
```

启动

戳

成功！！！

然鹅，把鼠标戳过去之后不停往外跳sidebar….反复执行

反馈bug之后开发者快速修复并推送了

这回就完美了！

接下来我把配置文件位置修改为在可执行文件的位置即可

这样方便单独使用

于是，omd-requ单应用版改制完成！

后续：为了解决有时窗口无法置顶问题，开发者柚子尝试在kwinrulesrc加入内容

然后发现ukui很特，它的叫ukui-kwinrulesrc（你没事加这玩意干啥？？）

所以又开始新一轮踩坑了

------
华丽丽的分割线

我不准备接着踩坑了，因为我换回了deepin

主要是ukui灾难性的1.25缩放。。。还有怎么也调不明白的热区（在deepin下，oh my dde可以正常工作，热区也在运行，唯一问题就是没有侧边栏。。。）

ukui下的测试彻底失败了，现在我的omd-requ仓库中的版本根本没法运行，最后还是只有第一个release能用

最后还是拥抱了dde
 
 ----
 更新：现在dde-kwin也不识别`[Script-runcommandaction]`了
 
 允悲