---
title: 替换jsdelivr等迁移操作
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - 折腾博客
# nolastmod: true
draft: false
---
发布时间： 2022-05-19T14:40:18+08:00

这里输入的内容会出现在主页也在正文里

<!--more-->

`jsdelivr`挂了，于是开始替换

waifu相关暂时在gitee放，似乎`css`的mimetype需要改一下，暂时仅仅是迁移了位置
> 最后发现需要用gitee page才可以......不然都是text/plain
> 注意要改动桌宠的根位置
> 把不同的项目放到不同的仓库的gitee page防止访问过慢

>额外把桌宠的api放到了OSS，省gitee的带宽，也方便迁移。用别的平台会跨源。。。

npm相关替换到了unpkg

![enter description here](https://xiaoshujiang-shenmo.oss-accelerate.aliyuncs.com/小书匠/1652942510213.png)

http://www.360doc.com/content/22/0517/21/78411425_1031823645.shtml

---

测试了，`unpkg.zhimg.com`不行，换`unpkg.com`了