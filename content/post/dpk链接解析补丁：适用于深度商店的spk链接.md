---
title: Dpk链接解析补丁：适用于深度商店的spk链接
date: 2022-02-28T22:08:19+08:00
lastmod: 2022-02-28T22:08:19+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - linux
# nolastmod: true
draft: false
---

我在 `ccc-app-manager`这个应用中发现这个应用居然支持“在应用商店中显示”

<!--more-->


经查看代码得知，`deepin-app-store`现在可用dbus拉起对应应用链接

代码链接： https://gitee.com/ct243768648/ccc-app-manager/blob/main/appmanagermodel.cpp

```
QString cmd = QString("qdbus com.home.appstore.client "
                      "/com/home/appstore/client "
                      "com.home.appstore.client.openBusinessUri "
                      "\"app_detail_info/%1\"")
                  .arg(pkgName);
```

---

于是我搞了这个东西  
星火dpk链接补丁  
![store.spark-app.spark-dpk-patch.png](https://storage.deepin.org/thread/202202282137396831_store.spark-app.spark-dpk-patch.png)

参照spk为深度商店制作了dpk以直接进入应用详情  
可以做到点击链接后直接拉起应用商店的对应APP详情页！  

目前官方api提供的功能有两个：`app_detail_info`和`searchApp`  
所以目前dpk链接支持直接进入应用详情或者进行应用搜索  
提供两个示例  

1. [dpk://app_detail_info/net.hmcl.huangyuhui](dpk://app_detail_info/net.hmcl.huangyuhui)
2. [dpk://searchApp/hmcl](dpk://searchApp/hmcl)

体验dpk/spk链接和下载补丁：点击下方链接  

https://www.shenmo.tech/2022/02/28/dpk%e9%93%be%e6%8e%a5%e8%a1%a5%e4%b8%81/

> 补丁开源地址是 https://gitee.com/shenmo7192/spark-dpk-patch/releases/

----------
芭比Q了，原来官方已经有了。。。

不需要装dpk助手就可以拉起了，链接格式是  
`appstore://deepin-home-appstore-client?app_detail_info/cc.modao.mockitt`

参考dpk的方法使用即可