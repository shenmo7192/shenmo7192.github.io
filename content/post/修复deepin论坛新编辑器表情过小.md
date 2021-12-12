---
title: 修复deepin论坛新编辑器表情过小
date: 2021-11-02T21:12:40+08:00
lastmod: 2021-11-02T21:12:40+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
cover: https://storage.deepin.org/thread/202111011923273518_%E6%B7%B1%E5%BA%A6%E6%88%AA%E5%9B%BE_%E9%80%89%E6%8B%A9%E5%8C%BA%E5%9F%9F_20211101192310.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - Linux
# nolastmod: true
draft: false
---

以下为解决方法

<!--more-->

来源： https://bbs.deepin.org/zh/post/227501?offset=2&postId=1273565

安装stylus插件，导入样式（火狐/Chrome系都有）

```
@-moz-document domain("bbs.deepin.org") {
.vditor-panel {
	max-width: 500px!important;
	width: 500px!important;
}

.vditor-emojis button {
	height: 60px!important;
	width: 60px!important;
	margin: 10px!important;
}

.vditor-emojis img {
	height: 60px!important;
	width: 60px!important;
}
}

```

