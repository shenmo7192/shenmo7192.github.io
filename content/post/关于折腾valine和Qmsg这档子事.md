---
title: 关于折腾Hugo和Valine和Qmsg这档子事
date: 2021-10-08T21:49:34+08:00
lastmod: 2021-10-08T21:49:34+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
cover: https://valine.js.org/images/valine.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - 折腾博客
# nolastmod: true
draft: false
---

经过了昨天的折腾，我总算选定了hugo作为我的博客生成器

原因很简单，在Windows上，Hexo需要装一整个nodejs环境，而hugo是go写成的，不仅执行效率高，而且文件小，单个文件不到100M，直接就可以使用




<!--more-->
首先就是尝试主题了

说实话，我一直不太能接受hugo的审美，试了几个经典的主题，比如even，还有各种衍生的，最终还是觉得wordpress一样的大列表比较适合我

结果找到了类似wordpress的主题，又觉得丑（话说我到现在也没弄明白wordpress怎么配置比较好。。。我好像确实不太适合整这个）

最后选定了dreams主题（现在的主题）作为我的博客主题

虽然有很多地方的本地化做的不好（其实是人家作者不需要），比如支持twitter,youtube,facebook,stackoverflow，但是不支持知乎，微博，b站。。。

只支持google分析，不支持百度分析/友盟+，而加了谷歌分析那国内就无法访问了

更别提gitee审核资格审核了一整天。。。

最后还是选定了dreams，可能是因为这是这几个主题里我唯一折腾得比较明白的了（低情商：功能少）

期间折腾了尝试用友盟替代google，然而友盟的官方统计方案是在页面后面添加一段html。。。

我用hugo怎么实现？

不好意思，没有教程:-(

尝试了手动添加分享按钮，不好意思，不会。。。

最后还是像我之前的wordpress博客一样，姑且是能用了，但是很多地方都是将就。。。

我最终选择了"dreams"作为我的hugo博客主题

但是，折腾才刚刚开始.....

首先我打开了Valine的官网[https://valine.js.org](https://valine.js.org/)

按照官方的“快速开始”进行了配置

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633701207218.png)

-----

首先进入LeanCloud，创建应用

按照官方的快速开始，我获取了appid和app key

接下来。。。怎么做？

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633701334953.png)

## ？？？

这个意思是想让我把这一段插到自己的网页里吗?

可是我使用的是hugo自动生成啊！怎么设置才能每次都插入啊？（刚才提到的友盟统计加不上去就是同样的原因）

然后呢？再往下一步

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633703302575.png)

## 这是什么东西？？？？？？

这是改源码？还是改网页？还是有什么我不知道的config？？？

下一步，有npm部署方式

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633703368039.png)

复制粘贴大法

`npm install valine --save`

然后

`nodejs`

复制粘贴

```
import Valine from 'valine';
```

报错。。。

复制粘贴
```

// Use import
import Valine from 'valine';
// or Use require
const Valine = require('valine');

new Valine({
    el:'#vcomments',
    // other config
})

```
报错。。。

这有什么用嘛！！！官方给出的快速部署，根本都不解释这个东西怎么用！

这是什么语言？在哪里执行？用什么方法部署？是连接到云上操作还是怎么样？

我感觉接下来给的这几步和获取api key根本没有关系啊！！！这都是什么鬼啊！！

HTML片段姑且是看懂了

接下来呢？配置？？？？

初始化对象是什么？

是，我是不知道，但是作为一个合格的新手指引，至少要告诉我们这个东西是在哪里执行的啊！

就且看直接百度“初始化对象”能搜到什么

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633703772779.png)

不同的语言都有结果

而且显然不是我所需要的

还有这个

```
1.3 成员变量的初始化和代码块的执行顺序,是由它们的声明顺序决定的,按顺序依次初始化或执行,但均在构造器方法之前执行。 在此例中,我们在创建Villa对象时,会先试着创建...
2.当有static成员时
3.静态成员变量只会被初始化一次,静态化代码块只会被执行一次,在该类第一次被JVM加载时
4.会先加载父类字节码,再加载子类字节码,如果有创建某类的实例对象,也是在该类的父类..
```

**这都什么跟什么啊！！！**

我需要准备什么环境？这是什么语言的术语？这是在shell里执行的命令吗？还是是nodejs执行的？需要写成脚本还是直接输入?

怎么安装？安装到哪？是给出的云平台还是自己的电脑？云平台能执行什么？是读取什么部署的？

**我怎么知道啊**

我就算再敷衍，给人家指令的时候都要告诉他从终端输入啊！

这给了个什么啊！根本不知道再哪里输入，也不知道在哪里配置

这只能说

**懂得都懂，不懂的那就不懂吧！**

---
再次百度

`hugo valine`
结果出现了

https://www.bilibili.com/video/av84392015


bilibili上有“手把手”的教程，通过的是valine-admin

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633702293717.png)

问题来了

我使用的不是这个主题。。。

啊这

**However**

我在我的主题的config.toml中找到了相关的参数
```
#valine = true
   LEANCLOUD_APP_ID = ""
   LEANCLOUD_APP_KEY = ""
   VALINE_LANGUAGE = ""

```
相比教程，我使用的主题支持的选项少得多

先这样吧！

解除注释，添加appid

好的，然后呢？咋部署？

找百度找到了这个
[https://blog.csdn.net/u012208219/article/details/106883083/](https://blog.csdn.net/u012208219/article/details/106883083/)

![](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633702746095.png)

按照步骤一步步来

首先搞一个可爱的Qmsg酱（这个小姐姐一下把我的心情搞好了不少）

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633702805788.png)

然后

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633702827250.png)

获取api key

不得不说这个教程确实非常详细

看起来这个版本的admin面板功能很多啊！

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633704964783.png)
（这里只展示一部分）

**接下来是重头戏了**

**部署**

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633702900413.png)

当我复制粘贴到LeanCloud操作界面后点击部署

结果显示私有仓库需要ssh来操作

心里一凉

之前在gitee出现过类似的提示

除了私有仓库之外，还有一种可能，那就是

我忐忑地点开了链接

果不其然

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633703051508.png)

**404**

然后转到用户页

https://github.com/DreamyTZK

结果还是

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633703144061.png)

完了，这回完的很彻底了

不仅作者删库跑路

就连作者的主页都没了

跑了和尚，连庙都跑了！



没有Valine-admin，我怎么配置啊？官方的部署根本看不懂啊！

github搜索valine-admin，找到本家了

https://hub.fastgit.org/DesertsP/Valine-Admin

然而

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633704413016.png)

支持的太少了

QQ提醒没有，邮箱提醒模板没有，评论管理后端没有。。。

我连原版都没法deploy，自己根本不可能添加这些功能啊！

**但是**

之前有知乎大佬讲过，可以用gitee拉取github的仓库来加速下载

然而，有时候我pull了之后一直不删

也就是说

**有可能在码云有这个valine-admin-server的源码！**

找了半天，只找到了这个

https://gitee.com/xiaozhidage/Valine-Admin-Server

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633704724887.png)

这是一个私人定制魔改版

然而，能找到的只有这个了

硬着头皮上吧！fork！

https://gitee.com/shenmo7192/valin-admin

接着按教程走，又踩坑了！

后台管理设置

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633705030744.png)

备案域名......

我的shenmo.tech并没有备案。。。

打开xinnet

进行备案操作

结果需要备案服务号

之前工信部丧心病狂地对于备案反复横跳，现在变成了主机提供商备案

心里一凉

我是xinnet购买域名，在腾讯云有主机

而主机并不是我的名字，因为要白嫖学生机

所以不能在腾讯云备案

新网想要获取备案服务号，必须在新网有云主机或者付费企业邮箱......

理直气壮地拒绝备案啊！

我觉得这个规定就是不合理的！我想要用serverless的服务，不就是我买不起云主机的意思么。。。。。。


所以我就和没有自己域名一样，只能放弃后台管理了（后来发现原来魔改版魔改的部分主要就在于后台管理，正好让我把魔改的部分错过了）

终于部署完成了！

正好gitee来消息，我的gitee page审核通过了！

直接部署好吧

找一个文章直接回复就是这个

https://shenmo7192.gitee.io/posts/%E8%BF%99%E6%98%AF%E4%B8%80%E4%B8%AA%E6%B5%8B%E8%AF%95/

没错就是这个文章（现在你没看到评论是因为我在调试结束后删除了所有测试用的回复）

结果没有收到邮件

查看日志出现smtp错误。。。只有Qmsg成功发送

行吧，我就把smtp从网易邮箱换成了域名邮（就是我的shenmo@spark-app.store）

反正是自己给自己发邮件

折腾完了，准备再发一个评论测试，发现还有一点不对


**为什么我没有收到QQ消息？**

明明日志里面显示成功发送了！

一看Qmsg控制台

好家伙
![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633705580284.png)

只要有链接就算是恶意推广。。。

咨询站长

只要是捐赠版Qmsg就可以无视这个规则

获取捐赠版的Qmsg需要自有QQ号（怪不得没有审查，自己提供QQ嘛）和捐赠200+RMB
好家伙，我有200块直接租一个wordpress不香吗？我为什么用gitee page你心里没点ac数吗？

只好尝试改代码把url屏蔽

假期的时候曾经改过miari色图插件的json（星火的应用详情也是json），也算是对改这类字符串拼接的东西有点经验（色图+链接确实容易被冻结）

但是说实话，对一个自己都不知道啥语言的代码直接手撸，之前没有过

提交记录如下

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633705883629.png)

改完好家伙，直接挂。。。

无论我发什么，都不会有任何邮箱或者QQ发送

甚至都没有尝试！

在日志里只记录了回复者的ip和未找到屏蔽词，根本没有尝试发送邮件/QQ的log！！！

马上回滚代码！

没用！还是没有尝试

百度，无用，这个valine-admin-server作者都删库跑路了，哪有什么相关的东西？

直接百度valine，出来的博客园和csdn都是千篇一律的东西

插一句，我就很奇怪了，这是有kpi考核吗还是什么？为什么同一篇文章持续不断地被人转载以至于塞满整个搜索结果？为什么从几年前一直到最近都有人发布？而且有的转载甚至连排版都有问题！有的转载甚至有明显的不属于他的博客系统的内容！

这都什么？

更蛋疼的是，给出的配置文件位置都是适配hexo的。。。

现在我尝到当时选定方案不成熟时的苦果了，人家hexo的生态好，就像现在wordpress的占有率仍然吊打一众博客生成器，人家来的早功能全，还有wordpress大学等一系列社区支持，选择一个小众的博客生成器，那没有相关文档就是必然的了

更何况我好死不死用了一个已经弃坑甚至连文档也只有一篇博客的admin-server.....


反复刷新，尝试找valine的代码，找不到。valine-admin-server的仓库里找不到valine的release本体。。。我不清楚这个评论系统到底是怎么被部署的。。。

一筹莫展的时候，我突然发现，本地开的hugo服务器上回复的内容，会被处理！

赶紧看Qmsg，果然有被拦截的消息！

刷新手机，果然在垃圾箱找到了邮件提醒

回滚到手改代码版本，成功了！

看来我改的没问题

那问题出在哪？

我的目光逐渐盯到了“域名白名单”，也就是"web安全域名"

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633706861957.png)

我在本地调试的时候显然是localhost，这就是白名单之内的

那在码云端调试的时候，既然无法触发，那就是这里设置有误！

**神末式解决问题方法：既然这个东西暂时没用，而且影响到了问题的解决，那就砍掉！**

于是清空整个白名单，转为全部放行

刷新，回复，无效

只有接收到评论的log，没有Email/QQ

这时候看到了这个

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633707038726.png)

三分钟，等就是了

半个小时过去了

疯狂刷新中。。。

没有任何作用！！！

心里烦躁，真心难受

到底是哪里出了问题？？？怎么调都调不通！还没有代码可以看！到底这狗b玩意是怎么部署到服务器的啊！

这时候我突然发现，在线的页面和本地页面有一个细微的不同

在线页面的回复框的邮箱处，填写了我的真实邮箱

而本地的是瞎写的

等等，我似乎在代码里看到.....

赶紧打开码云
```
// 提醒站长
exports.notice = (comment) => {
  // 站长自己发的评论不需要通知
```

虽然不知道怎么实现的，但是确实

**站长的评论回复是不会通知的！**

在线上更改了个瞎写的邮箱后

正常通知了！

然而，心里一点都没有高兴，没有茅塞顿开，也没有柳暗花明又一村

只有

**抓狂**

这么长时间干了啥？一点用也没有啊！瞎打转！

出去吃完饭，平复心情，已经八点多了。。。

从下午开始，已经快6个小时了。。。其中多长时间是被这个破玩意耽误了呢？

回来之后，开始下一项工作：Valine美化

------

别人家的博客：有看板娘，有特色鼠标光标，可以用各种表情包

我的博客：朴素，简陋，只能发经典表情包

---
百度很多的好玩的插件都是在html后面或者前面挂一段代码。。。

我不会啊！谁能告诉我hugo应该怎么配置才能这样做？？？

那自定义表情包呢？

不是我不想，但是Valine的官方文档长这样

举例：bilibili自定义表情包
```
举个栗子

比如我们要用Bilibili的表情包(效果可以在评论区查看):

new Valine({
    el:'#vcomment',
    appId:'<Your_APP_ID>',
    appKey:'<Your_APP_KEY>',

    // 设置Bilibili表情包地址
    emojiCDN: '//i0.hdslb.com/bfs/emote/', 
    // 表情title和图片映射
    emojiMaps: {
        "tv_doge": "6ea59c827c414b4a2955fe79e0f6fd3dcd515e24.png",
        "tv_亲亲": "a8111ad55953ef5e3be3327ef94eb4a39d535d06.png",
        "tv_偷笑": "bb690d4107620f1c15cff29509db529a73aee261.png",
        "tv_再见": "180129b8ea851044ce71caf55cc8ce44bd4a4fc8.png",
        "tv_冷漠": "b9cbc755c2b3ee43be07ca13de84e5b699a3f101.png",
        "tv_发怒": "34ba3cd204d5b05fec70ce08fa9fa0dd612409ff.png",
        "tv_发财": "34db290afd2963723c6eb3c4560667db7253a21a.png",
        "tv_可爱": "9e55fd9b500ac4b96613539f1ce2f9499e314ed9.png",
        "tv_吐血": "09dd16a7aa59b77baa1155d47484409624470c77.png",
        "tv_呆": "fe1179ebaa191569b0d31cecafe7a2cd1c951c9d.png",
        "tv_呕吐": "9f996894a39e282ccf5e66856af49483f81870f3.png",
        "tv_困": "241ee304e44c0af029adceb294399391e4737ef2.png",
        "tv_坏笑": "1f0b87f731a671079842116e0991c91c2c88645a.png",
        "tv_大佬": "093c1e2c490161aca397afc45573c877cdead616.png",
        "tv_大哭": "23269aeb35f99daee28dda129676f6e9ea87934f.png",
        "tv_委屈": "d04dba7b5465779e9755d2ab6f0a897b9b33bb77.png",
        "tv_害羞": "a37683fb5642fa3ddfc7f4e5525fd13e42a2bdb1.png",
        "tv_尴尬": "7cfa62dafc59798a3d3fb262d421eeeff166cfa4.png",
        "tv_微笑": "70dc5c7b56f93eb61bddba11e28fb1d18fddcd4c.png",
        "tv_思考": "90cf159733e558137ed20aa04d09964436f618a1.png",
        "tv_惊吓": "0d15c7e2ee58e935adc6a7193ee042388adc22af.png",
        // ... 更多表情
    } 
})

```
# 这是啥？在哪用？写在哪？？？

完全没有任何可操作性！

只好问百度

基本上也是这样的

**难道错的是我自己吗。。。**

但是

有一个美化

也就是添加评论widget背景

是一个css

我突然想起，在好久之前，我的config.toml好像有一句.....


就是这个！

`customCSS = ["css/custom.css"]`

找到custom.css，在后面复制粘贴，改链接

成功！

于是我目前唯一的装饰就是

当当当当！

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633708738761.png)

折腾了好久，要熄灯了，就先告一段落吧！










P.S.今天写博客的时候感觉室友甚是聒噪，想要使用耳塞，却发现耳塞之前睡觉的时候丢了一个。。。把耳机戴上，快写完博客的时候也快12点了，正好转到这首歌，心里突然软了一下

------

这是我的旅行

这是我的冒险

这是我的伙伴

这是我们一起走过来的一年

明明是代码和图片...情感却是真实的！

在门的另一端，故事还没写完......

**Yeye Tomo!**

**Odomu dada!**

**mosi mita !!!**

**祝各位旅行者一周年快乐！**

<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=1880127698&auto=0&height=66"></iframe>


