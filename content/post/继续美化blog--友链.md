---
title: 继续美化blog  友链
date: 2021-10-10T20:35:46+08:00
lastmod: 2021-10-10T20:35:46+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
cover: https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633871642677.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - 折腾博客
# nolastmod: true
draft: false
---
已经在QQ空间里发布了链接，互加友链的请求就来了。然而，我的博客主题不支持友链，也就是说，我还是需要手改主题......
<!--more-->


不过等等！在主题提供的`about`文件夹里，我可以使用一个帖子来写“关于我”

（话说不会有人不知道页面左上角的那个圆圈可以点吧？不会吧？）

Cris朋友给我一个模板，经过我的魔改（瞎写）后，成功启动了

效果差不多是这样的

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633869958478.png)

但是全在一个位置，另外两个元素很短，就显得很不平衡了

所以我决定，魔改社交链接post！
![](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633870101955.png)

这玩意就这么短

传统艺能：打开`/theme/dream/layouts/partials`找html

这回发现在`socials.html`里

找到最后一行

加一行分隔符

`<!--这里是手改的友链-->`

然后把码扔上去

```html
<div class="post-body"> 
<hr class="xsj_hr xsj_minus">
  <p class="xsj_paragraph xsj_paragraph_level_0" data-source-line="37" data-source-line-display="true">
<p><strong>友链</strong></p>
<!-- 上面的是分隔符 -->
   <div id="links"> 
    <style>
    .links-content
    {
      	margin-top:1rem;
      }
      .link-navigation::after
      {
      	content:" ";
      	display:block;
      	clear:both;
      }
      .card
      {
	      max-width:250px;
	      font-size:1rem;
      	border-radius:5px;
	      transition-duration:.15s;
	      margin-bottom:1rem;
	      display:flex;
	      padding:10px 25px;
      }
      .card:hover
      {
      	transform:scale(1.1);
      	box-shadow:0 2px 6px 0 rgba(0,0,0,0.12), 0 0 6px 0 rgba(0,0,0,0.04);
      }
      .card a
      {
      	border:none;
      }
      .card .ava
      {
      	width:3rem!important;
        height:3rem!important;
      	border-radius:4px;
      	margin:0 1em 0 0 !important;
      }
      .card .card-header
      {
      	font-style:italic;
      	overflow:hidden;
      	width:100%;
      }
      .card .card-header a
      {
      	font-style:normal;
      	color:#333;
      	font-weight:700;
      	text-decoration:none;
      }
      .card .card-header a:hover
      {
      	color:#79aeff;
      	text-decoration:none;
      }
      .card .card-header .info
      {
      	font-style:normal;
      	color:#a3a3a3;
      	font-size:14px;
      	min-width:0;
      	text-overflow:ellipsis;
      	overflow:hidden;
      	white-space:nowrap;
      }
      .card:nth-child(odd)
      {
      	float:left;
      }
      .card:nth-child(even)
      {
      	float:left;
      }
     </style> 
    <div class="links-content"> 
     <div class="link-navigation"> 
      <div class="card"> 
	  <img class="ava" src="https://img11.360buyimg.com/ddimg/jfs/t1/199313/28/4759/36424/6124e67aE6b16b6da/c23322e4a0242148.jpg" /> 
       <div class="card-header"> 
        <div> 
         <a href="https://www.cnblogs.com/maicss/">Maicss's Blog</a> 
        </div> 
        <div class="info">
         wonderful to have a beginner's mind.
        </div> 
       </div> 
      </div>
     </div> 
    </div> 
   </div> 
  </div>
  <div class="links-content"> 
     <div class="link-navigation"> 
      <div class="card"> 
	  <img class="ava" src="https://crisq.tk/images/logo@2x.png" /> 
       <div class="card-header"> 
        <div> 
         <a href="https://crisq.tk/">CRIS的小站</a> 
        </div> 
        <div class="info">
         Superbia.
		 </div>
		 </div>
		 </div>
		 </div>
		 
```
然后想起最右侧的CopyRight不支持自动换行
![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633870507462.png)

只能缩到一句话，很难受，直接找到源头`layouts\partials\back.html`

```
 <div class="sixteen wide mobile eight wide tablet four wide computer column dream-column">
    {{ if .Site.Copyright }}
    <article class="ui segment">

<!--原版的，注释了，万一我想要别的功能呢？
      {{ .Site.Copyright | safeHTML }}
-->

<p class="xsj_paragraph xsj_paragraph_level_0" data-source-line="9" data-source-line-display="true">本博客所有文章使用《知识共享 署名-非商业性使用-相同方式共享 4.0》(CC-BY-NC-SA-4.0)协议</p>
<p class="xsj_paragraph xsj_paragraph_level_0" data-source-line="11" data-source-line-display="true">这意味着你可以在署名并标明出处的情况下进行非商业转载（转载的文章也需要遵守CC-BY-NC-SA-4.0协议），但不可以进行商业转载</p>

    </article>
<!--这个article可以玩玩-->
    {{ end }}
  </div>
  
  ```


最后是这样的效果

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1633870658456.png)