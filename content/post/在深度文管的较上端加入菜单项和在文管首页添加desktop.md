---
title: 在深度文管的较上端加入菜单项和在文管首页添加desktop
date: 2021-12-21T18:51:40+08:00
lastmod: 2021-12-21T18:51:40+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
cover: https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1640084035324.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - linux
# nolastmod: true
draft: false
---

在官方给出的文档里，有`oem-extenshen`的写法（不会用请点[这里](https://gitee.com/shenmo7192/dde-file-manager-menu-oem)），但是这样插入的插件位置都比较靠下。那么，类似深度压缩的菜单项这样位置靠上的插件是怎么实现的呢？

<!--more-->

官方并没有相关的文档，但是万能的星火群友发现了位置

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1640084723774.png)

`/usr/share/applications/context-menus`

![enter description here](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1640084305977.png)


------


在这里添加`.conf`文件可以在较为靠上的位置添加菜单项，类似这样


![类似这样](https://gitee.com/shenmo7192/shenmo-map-bed/raw/master/小书匠/1640084386599.png)

附上`.conf`文件 *1，语法似乎和`.desktop`一致，参考开头的[https://gitee.com/shenmo7192/dde-file-manager-menu-oem](https://gitee.com/shenmo7192/dde-file-manager-menu-oem)大家魔改着用即可


------


文件名：`compressor-multicompress.conf`

```desktop
[Menu Entry]
Version=1.0
Actions=Zero:One:Two

[Menu Action Zero]
Exec=/usr/bin/deepin-compressor %F compress
Name=Compress
X-DFM-MenuTypes=MultiFiles:MultiDirs:FileAndDir
X-DFM-SupportSchemes=file
MimeType=*
PosNum=3
Separator=Top
Name[az]=Sıxmaq
Name[bo]=གནོད་བཙིར།
Name[ca]=Comprimeix
Name[de]=Komprimieren
Name[es]=Comprimir
Name[fi]=Pakkaa
Name[fr]=Compresser
Name[hu]=Tömörítés
Name[id]=Kompres
Name[it]=Comprimi
Name[nl]=Inpakken
Name[pl]=Kompresja
Name[pt]=Comprimir
Name[pt_BR]=Comprimir
Name[sq]=Ngjeshe
Name[sr]=Запакуј
Name[tr]=Sıkıştır
Name[ug]=پىرسلاش
Name[uk]=Стиснути
Name[zh_CN]=压缩
Name[zh_HK]=壓縮
Name[zh_TW]=壓縮

[Menu Action One]
Exec=/usr/bin/deepin-compressor %F compress_to_7z
Name=Add to "%d.7z"
X-DFM-MenuTypes=MultiFiles:MultiDirs:FileAndDir
X-DFM-SupportSchemes=file
MimeType=*
PosNum=4
Name[az]="%d.7z"ə əlavə edin
Name[bo]="%d.7z"ནང་སྣོན་པ།
Name[ca]=Afegeix a %d.7z
Name[de]=Zu „%d.7z“ hinzufügen
Name[es]=Añadir a "%d.7z"
Name[fi]=Lisää "%d.7z"
Name[fr]=Ajouter à "%d.7z"
Name[hu]=Hozzáadás a következőhöz: "%d.7z"
Name[id]=Tambahkan ke "%d.7z"
Name[it]=Aggiungi a "%d.7z"
Name[nl]=Toevoegen aan '%d.7z'
Name[pl]=Dodaj do "%d.7z"
Name[pt]=Adicionar a "%d.7z"
Name[pt_BR]=Adicionar a "%d.7z"
Name[sq]=Shtoje te "%d.7z"
Name[sr]=Додај у "%d.7z"
Name[tr]=Şuraya ekle "%d.7z"
Name[ug]="%d.7z" غا قوشۇش
Name[uk]=Додати до «%d.7z»
Name[zh_CN]=添加到"%d.7z"
Name[zh_HK]=添加到"%d.7z"
Name[zh_TW]=添加到"%d.7z"

[Menu Action Two]
Exec=/usr/bin/deepin-compressor %F compress_to_zip
Name=Add to "%d.zip"
X-DFM-MenuTypes=MultiFiles:MultiDirs:FileAndDir
X-DFM-SupportSchemes=file
MimeType=*
PosNum=5
Name[az]="%d.zip"ə əlavə edin
Name[bo]="%d.zip"ནང་སྣོན་པ།
Name[ca]=Afegeix a %d.zip
Name[de]=Zu „%d.zip“ hinzufügen
Name[es]=Añadir a "%d.zip"
Name[fi]=Lisää "%d.zip"
Name[fr]=Ajouter à "%d.zip"
Name[hu]=Hozzáadás a következőhöz: "%d.zip"
Name[id]=Tambahkan ke "%d.zip"
Name[it]=Aggiungi a "%d.zip"
Name[nl]=Toevoegen aan '%d.zip'
Name[pl]=Dodaj do "%d.zip"
Name[pt]=Adicionar a "%d.zip"
Name[pt_BR]=Adicionar a "%d.zip"
Name[sq]=Shtoje te "%d.zip"
Name[sr]=Додај у "%d.zip"
Name[tr]=Şuraya ekle "%d.zip"
Name[ug]="%d.zip" غا قوشۇش
Name[uk]=Додати до «%d.zip»
Name[zh_CN]=添加到"%d.zip"
Name[zh_HK]=添加到"%d.zip"
Name[zh_TW]=添加到"%d.zip"

```

---
## 文管首页添加desktop

放到`/usr/share/dde-file-manager/extensions/appEntry/`