---
title: 发行测评：GXDE V15.12：接近好用水准的混合桌面环境
date: 2024-08-15T19:38:57+08:00
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: https://gitee.com/GXDE-OS/GXDE/raw/master/icon.svg
# images:
#   - /img/cover.jpg
categories:
  - Linux测评
tags:
  - Linux
# nolastmod: true
draft: false
---

发行测评：GXDE V15.12：接近好用水准的混合桌面环境

<!--more-->

Hola大家好哦，这里是shenmo的发行版/桌面测评系列～（上一波：[TrinityDE：一款字面意义上复古的桌面环境](https://blog.shenmo.tech/post/q4os_evaluation/)）

今天是deepin 23发布的日子，标志着deepin 20结束支持。**当一个故事要结束的时候，我们总会想起它的开始....<a href="https://music.163.com/#/song?id=2026565329" target="_blank">(音乐起)</a>


> 题外话：如果各位v23正式版镜像下载非常慢的话，可以用镜像站下载～
> 
> [https://mirror.iscas.ac.cn/deepin-cd/23/](https://mirror.iscas.ac.cn/deepin-cd/23/)

---

作为直播间在逃人员，一边听着张磊总讲deepin的历史，一边码字。今天要给大家带来的是，deepin 15.11的精神延续——GXDE 15.12的评测

准备好时光机了吗？我们要回到统信还没成立的那个年代了，让我们开始——

# GXDE OS v15.12 测评

## 外观——回归经典

![图片.png](https://storage.deepin.org/thread/202408150931274834_图片.png "熟悉的登陆界面")

熟悉的登陆界面——v15时代的设计风格和20/23很不一样，是围绕高斯模糊和半透明设计的，至少在锁屏壁纸的处理上，我认为比后来的阴间滤镜好得多——尤其是使用人物或者动漫人物作为壁纸的时候，莫名其妙的颜色滤镜观感会非常差。同时，高斯模糊处理还可以起到一定的隐私保护作用（咳咳壁纸也太牙白了吧～）


![图片.png](https://storage.deepin.org/thread/202408150939519002_图片.png)

换回15时代的经典壁纸。

选装的旧版终端——自然要使用呀～相比于新版的粗标题栏+大圆角+默认不透明，旧版终端的窄标题栏+小圆角+半透明明显更加清新

![图片.png](https://storage.deepin.org/thread/202408150936145746_图片.png)

有那味了的壁纸和桌面——图中展示了曾经是deepin最具特色的侧边控制中心，从上到下无极滑动，依然使用高斯模糊+半透明设计，清新优雅，易于学习，但展示字数太多的时候这份优雅带来的阅读困难就变得比较难绷了，比如下图的版本协议界面，字小难读


![图片.png](https://storage.deepin.org/thread/202408150952255094_图片.png)

deepin 15到20到23的后台dbus接口做了大量变换，能让v15的控制中心控制这个混合桌面环境，作者是下了大功夫的

## 体验——博采众长


![图片.png](https://storage.deepin.org/thread/202408150940175089_图片.png)

怀旧的任务栏和启动器，配上Debian 12的新应用，让deepin 15复活在现代


![图片.png](https://storage.deepin.org/thread/202408151031198623_图片.png)

微信完全没有问题


![图片.png](https://storage.deepin.org/thread/202408150946094728_图片.png)


![图片.png](https://storage.deepin.org/thread/202408151032081939_图片.png)


![图片.png](https://storage.deepin.org/thread/20240815104320576_图片.png)



图中展示了运行最新的QQ,微信Linux,星火应用商店和v20后期才引入的剪贴板，都可以正常使用

GXDE OS同时兼容dtk2和dtk5应用。dtk2应用和原生应用使用小圆角，dtk5应用使用大圆角（但是版本有点低啊，还是两个点的版本）。可以看出开发者对二者风格融合的尝试，在后续的图片中可以看到一些widget被替换成了20/23时代的样式

GXDE并非全盘照搬deepin 15,而是把很多v20和23才有的功能融入了桌面，部分20时代更新了的组件采用20的新版。除此之外还加入了很多特色功能，这让GXDE OS更具风味，不再是一个复刻

![图片.png](https://storage.deepin.org/thread/202408151033293860_图片.png)

自带了远程协助功能


![图片.png](https://storage.deepin.org/thread/202408151035503237_图片.png)

gtk主题可在控制中心更改


![图片.png](https://storage.deepin.org/thread/20240815103638495_图片.png)

集成dde-top-bar和plank，一键切换风格


![图片.png](https://storage.deepin.org/thread/20240815103735953_图片.png)


![图片.png](https://storage.deepin.org/thread/202408151038355466_图片.png)

Wifi热点功能


![图片.png](https://storage.deepin.org/thread/202408151040501137_图片.png)

支持Live系统安装，遥遥领先（自行配音）

系统集成了Wine运行器来提供windows应用支持，星火应用商店来提供生态支持

---

## 缺点——小问题不断

然而，虽然融合的不错，但是现在仍有些影响体验的bug,距离完美还需要努力

* 图形安装器在UEFI下仅支持实体机安装，VM需使用Debian CLI安装器安装后手动切换语言到中文
* 截图录屏启动后概率崩溃
* 如果使用旧版deepin终端，默认启动位置为/tmp而不是~，在文件夹中右键启动不影响，默认使用的新版deepin终端无问题
* 未自带音乐播放器等部分组件（这个见仁见智了，可能有人会喜欢这种精简风格）
* nmbd服务自带了，但是无法使用也没有禁用，导致开机较为缓慢，需要启动后手动禁用
* 连接Wifi时需要输入两次密码，且密码错误后需手动处理
* 热区可以设置但是无法生效（这里建议作者可以考虑用第三方热区 https://gitee.com/Limexb/oh-my-dde/tree/master/omd-requ 可以自定义效果。柚子的YoyoOS的遗产也可以作为后续开发的参考）
* 缺少AI功能等v23新加入的能力，缺少深度邮箱和深度浏览器等闭源应用

这些问题都不是很大，可以解决，但是需要一点经验，建议有一定踩坑经验的同学入坑～

* 直接在实体机器上安装或在VM上使用LegacyBIOS启动
* 使用Flameshot等第三方截图工具
* 使用新终端，或者等待开发者修复（已经反馈）
* 安装自己喜欢的音乐播放器
* sudo systemdctl disable nmbd
* 使用nmtui操作



## 总结

GXDE v15.12是一个很好的桌面环境，为我们展示了一个新的可能性，尽管现在仍不完美，但已经达到可用的水准，日常使用完全不会有问题，期待后续的进一步改善

如果您有更好的改进建议，或者感兴趣加入研发，请访问： https://gitee.com/gxde-os
