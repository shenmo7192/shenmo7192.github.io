---
title: 使用 Pdf.js 来展示PDF
date: 2025-02-08T00:18:13+08:00
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - 笔记
# nolastmod: true
draft: false
---

转载自 https://www.cnblogs.com/Dongmy/p/17215879.html

<!--more-->


1. pdfjs库简介

PDF.js 是由Mozilla 主导推出的可以将PDF文件转换为H5页面进行展示的工具。相比较目前前端可以用的pdf节点方案，pdfjs是非常合适的。它有这么几个优点：1.完全js开发，不依赖其他js库，不使用flash插件。2.代码分层做的较好，官方提供了可以直接使用的封装组件，无需额外开发。3.兼容性也不错，支持canvas和svg渲染，pc和手机端都可以使用。

用于演示的图片：


![](https://shenmo7192.atomgit.net/imgs/2233/69723292_p0.jpg)

2. 使用方法：

* 方式1：通过链接方式，在viewer.html页面中独立独立查看【通过文件路径】

实现方法：通过`<a/>`标签链接到`viewer.html`页面，需要传递一个重要的参数`file`，设置为要显示的pdf文件的路径

`<a href="https://blog.shenmo.tech/external/pdf-viewer/web/viewer.html?file=https://shenmo7192.atomgit.net/imgs/demo.pdf">点击查看pdf内容</a>`

<a href="https://blog.shenmo.tech/external/pdf-viewer/web/viewer.html?file=https://shenmo7192.atomgit.net/imgs/demo.pdf">点击查看pdf内容</a>

* 方式2：嵌入在网页中

实现方法：通过`iframe`实现。需要传递`file`参数，设置pdf文件的路径

```html

    <iframe src="https://blog.shenmo.tech/external/pdf-viewer/web/viewer.html?file=https://shenmo7192.atomgit.net/imgs/demo.pdf" width="100%" height="400px;"></iframe>

```

<iframe src="https://blog.shenmo.tech/external/pdf-viewer/web/viewer.html?file=https://shenmo7192.atomgit.net/imgs/demo.pdf" width="100%" height="400px;"></iframe>

--->跨域设置

iframe涉及到跨域问题。如果PDF文件与网站部署在一起，则不存在跨域。如果PDF在网站之外，则涉及到跨域问题。打开viewer.js文件，注释掉以下内容。

![](https://shenmo7192.atomgit.net/imgs/1892002-20230314181059128-172520878.png)

