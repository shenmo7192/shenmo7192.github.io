---
title: 关于折腾Valine第三期：完全的自定义
date: 2021-10-10T16:06:14+08:00
lastmod: 2021-10-10T16:06:14+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
cover: https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633853103267.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - 折腾博客
# nolastmod: true
draft: false
---

之前尝试了修改`bilibili-img.js`来添加更多表情包，成功了

但是，当尝试更多参数（比如说placeholder和QQ解析）时，出现了奇怪的症状

<!--more-->

进入网页的时候，还是没有任何参数的原版

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633849839328.png)

然而，当我点击了一个已有评论再点击回复之后

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633849901651.png)

成功启动了

因此，我猜测，是主题自己的Valine设置先加载了，点击回复之后才加载了我的自定义设置

然而，主题所提供的接口很少，只有appID、appKey和一个已经弃用的lang参数

根本没有自定义能力

所以我决定，直接找主题源文件，也就是之前大佬博客说的：手改主题！（把主题文件拷贝到根目录可以无损修改）
[传送门](https://blog.ohmykreee.top/article/music-player-in-hugo-page/)

没装ide，不想装，于是挨个文件用Notepad.exe打开，Ctrl+F 搜索Valine

终于在`layout/_default/single.html`找到了（我一直再找post....我以为名字会和帖子有关的）


```
{{ if .Site.Params.valine }}
<script src='//unpkg.com/valine/dist/Valine.min.js'></script>
{{ end }}

{{ end }}

```

也就是说，这里判断有这个参数之后，从这里引入Valine.min.js
然而...其实我们可以使用官方CDN

当然也包括魔改版！

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633850507231.png)

我准备完全废弃主题提供的配置方式，于是

```
!-- 这里是引入Valine.min.js，为了引入魔改版，把官方版的屏蔽-->
<!--
{{ if .Site.Params.valine }}
<script src='//unpkg.com/valine/dist/Valine.min.js'></script>
{{ end }}
-->

<script src='//cdn.jsdelivr.net/gh/HCLonely/Valine@latest/dist/Valine.min.js'></script>

<!--上面这一行为魔改版本，来自https://www.jianshu.com/p/205aaa14dff3 -->
```

（其实最开始我在每一行前面加了`//`，然后发现报错，才知道html的注释格式比较清奇）

继续往下搜索Valine，看到了这个

```html
  {{ if .Site.Params.valine }}
    <article class="ui segment" data-html2canvas-ignore>
      <div id="vcomments"></div>
    </article>
	
```
	
虽然我完全不懂html，但是这一段似乎在说把valine正确放到评论区的内容

之前出现过强行插入结果评论区蔓延了整个页面的情况，因此我决定不动它

```
<!-- 这一段疑似为启动vcomments的关键段落，这里确认插入vcomment的地点。由于本人不会html，怕改错，所以保留并在config中启用valine以使用-->

    {{ if .Site.Params.valine }}
    <article class="ui segment" data-html2canvas-ignore>
      <div id="vcomments"></div>
    </article>

<!-- 结束 --->
```

接下来看到了关键

```
<script>
      new Valine({
        el: '#vcomments',
        appId: {{ .Site.Params.LEANCLOUD_APP_ID }},
        appKey: {{ .Site.Params.LEANCLOUD_APP_KEY }},
        lang: {{ .Site.Params.VALINE_LANGUAGE }}
      })
    </script>
	
```
这就是熟悉的Valine配置文件了

这是叫短代码么？这个地方显然是在读取config中的内容

但是我自己不会写，回头找源文件也是蛋疼

干脆就地注释

```
<!--以下为原版读取config内容，不敢改，直接注释，万一挂了也能恢复-->
<!-- 开始注释
    <script>
      new Valine({
        el: '#vcomments',
        appId: {{ .Site.Params.LEANCLOUD_APP_ID }},
        appKey: {{ .Site.Params.LEANCLOUD_APP_KEY }},
        lang: {{ .Site.Params.VALINE_LANGUAGE }}
      })
    </script>

注释结束 -->

```

然后取消config里面引用bilibili-img.css

直接复制粘贴到这里

```
<script>
new Valine({
    el:'#vcomment',
placeholder: "期待你的回复哦ヽ(✿ﾟ▽ﾟ)ノ\n在邮件栏目填写QQ邮箱可以获取QQ头像哦~\n可以使用markdown哦～",
enableQQ:true,

    appId:'不会告诉你的',
    appKey:'不会告诉你的',

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
      "tv_打脸": "56ab10b624063e966bfcb76ea5dc4794d87dfd47.png",
      "tv_抓狂": "fe31c08edad661d63762b04e17b8d5ae3c71a757.png",
      "tv_抠鼻": "c666f55e88d471e51bbd9fab9bb308110824a6eb.png",
      "tv_斜眼笑": "911f987aa8bc1bee12d52aafe62bc41ef4474e6c.png",
      "tv_无奈": "ea8ed89ee9878f2fece2dda0ea8a5dbfe21b5751.png",
      "tv_晕": "5443c22b4d07fb1907ccc610c8e6db254f2461b7.png",
      "tv_流汗": "cead1c351ab8d79e9f369605beb90148db0fbed3.png",
      "tv_流泪": "7e71cde7858f0cd50d74b0264aa26db612a8a167.png",
      "tv_流鼻血": "c32d39db2737f89b904ca32700d140a9241b0767.png",
      "tv_点赞": "f85c354995bd99e28fc76c869bfe42ba6438eff4.png",
      "tv_生气": "26702dcafdab5e8225b43ffd23c94ac1ff932654.png",
      "tv_生病": "8b0ec90e6b86771092a498c54f09fc94621c1900.png",
      "tv_疑问": "0793d949b18d7be716078349c202c15ff166f314.png",
      "tv_白眼": "c1d59f439e379ee50eef488bcb5e5378e5044ea4.png",
      "tv_皱眉": "72ccad6679fea0d14cce648b4d818e09b8ffea2d.png",
      "tv_目瞪口呆": "0b8cb81a68de5d5365212c99375e7ace3e7891b7.png",
      "tv_睡着": "8b196675b53af58264f383c50ad0945048290b33.png",
      "tv_笑哭": "1abc628f6d4f4caf9d0e7800878f4697abbc8273.png",
      "tv_腼腆": "89712c0d4af73e67f89e35cbc518420380a7f6f4.png",
      "tv_色": "61822c7e9aae5da76475e7892534545336b23a6f.png",
      "tv_调侃": "4bc022533ef31544ca0d72c12c808cf4a1cce3e3.png",
      "tv_调皮": "b9c41de8e82dd7a8515ae5e3cb63e898bf245186.png",
      "tv_鄙视": "6e72339f346a692a495b123174b49e4e8e781303.png",
      "tv_闭嘴": "c9e990da7f6e93975e25fd8b70e2e290aa4086ef.png",
      "tv_难过": "87f46748d3f142ebc6586ff58860d0e2fc8263ba.png",
      "tv_馋": "fc7e829b845c43c623c8b490ee3602b7f0e76a31.png",
      "tv_鬼脸": "0ffbbddf8a94d124ca2f54b360bbc04feb6bbfea.png",
      "tv_黑人问号": "45821a01f51bc867da9edbaa2e070410819a95b2.png",
      "tv_鼓掌": "1d21793f96ef4e6f48b23e53e3b9e42da833a0f6.png"
        // ... 更多表情
    } 
})
</script>

```

结果失败了

取消注释前文的原版

可以显示

难道是。。。

对比发现后文的config中`el:'#vcomment'`少了一个s

更改后正常

等等....难道说

如果我的`bilibili-img.js`也加上s的话......

立即尝试

直接在single.html删除相关js

刷新页面，评论区消失

修改bilibili-img.js（并改名为valine-custom.js，现在它的用途更多了，当然也要改名），并在config中加入

显示倒是显示了，placeholder也正常了

就是。。。

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633852234913.png)

看来还是只能手改html了（笑）

这次折腾成功了，哈哈！

接着看番剧，冲着核爆神曲来的，没想到正在限免，开心！

https://www.bilibili.com/bangumi/play/ep324682