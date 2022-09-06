---
title: 开始折腾Valine美化第二期
date: 2021-10-09T12:01:32+08:00
lastmod: 2021-10-09T12:01:32+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
cover: https://images3.freesion.com/535/5d/5ddf6d8f1f0a571bac9cded203accd07.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - 折腾博客
# nolastmod: true
draft: false
---

首先我们看看刚才那个博文有用的地方（上一集传送门：[点我](https://shenmo7192.gitee.io/post/%E5%B0%9D%E8%AF%95%E6%8F%92%E5%85%A5%E9%9F%B3%E4%B9%90%E6%97%B6%E7%9A%84%E7%81%B5%E6%84%9F/)）

<!--more-->

首先是这里

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633749575679.png)

我们可以知道，在博客根目录的文件比同目录下theme里面的文件读取优先级更高，也就是说我们可以直接从theme复制出来并修改，不需要直接更改theme

这是个很好的设计（以后可以抄一下

重点在于，这里的baseof.html就是博客所有页面的基础html

也就是说，如果我想要添加看板娘，只需要在这里添加html即可！

之前已经测试过了，这个方法是可行的

但是首先，我觉得要测试下Valine官方的教程能不能用

找到这里

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633749740609.png)

emmmm，应该是塞到baseof里面的，但是主题提供的配置直接可以启动

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633749793209.png)

也就是说，引入Valine框架的工作，我们不需要自己做

那就不做（

反正做了容易出错，如果出现两个不一样的评论区还是挺难受的

接下来看自定义表情包

就是前天我吐槽的（吐槽我是不会收回的，这玩意怎么加载，就是应该说一下的）

```
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

这段，扔到js/custom.js

成功加载！可以看到不一样的表情包了！直接override了主题提供的接口！

但是提示401错误，写错了appID

我一看，好家伙，我这还写着`<Your_APP_ID>`呢！
赶紧替换成`<这是真的_APP_ID>`

结果还是不行

401错误

什么情况这是？

难道是配置文件有问题？

把配置文件的Valine行注释掉

评论区消失了

手动手改baseof.html

出现了一个横跨整个页面的评论区（实在不想复现，就不截图了）

回滚

再打开主题自带的Valine开关

清除appID内容（我怀疑是这个appID和js的appid冲突？）

还是401错误

反复复制粘贴

错误

刷新

错误。。。

又开始抓狂了

从网上复制一段配置

可以看到表情变化了，还是401错误

难道是域名白名单？

于是域名白名单又惨遭毒手

没用。。。



突然发现

网上给的例子里

appID的格式是这样的

`appId:'xxxxxxxxxxxx'`

所以根本没有尖括号是吗？？？（虽然感谢这位兄弟点醒了我，但是把自己的appID露在外面风险是很大的）

去除尖括号后，成功！

抓狂！为什么会是这种问题？？？？

这也不能怪人家说的不明白，人家的单引号是在尖括号外面的。。。

唉，心塞