---
title: 关于preinst等维护者脚本被唤起时可能会获得的参数或状态提示总结
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
发布时间： 2022-05-29T17:33:40+08:00



<!--more-->
https://www.debian.org/doc/debian-policy/ch-maintainerscripts.html#summary-of-ways-maintainer-scripts-are-called

用例：

需求：星火维护的某wine应用，希望在卸载时自动删除用户目录下的容器，而直接在postrm写入则会在升级时也删除容器。需要判断到是在卸载或者完全卸载时再删除

相关内容：链接中：
>The postrm script may be called in the following ways:
postrm remove
postrm purge
old-postrm upgrade new-version
disappearer's-postrm disappear overwriter overwriter-version

所以在postrm前加入判断

`if [ "$1" = "remove" ] || [ "$1" = "purge" ];then`

即可实现在升级的时候不删除，在卸载时删除

代码例子：

```
#!/bin/bash

if [ "$1" = "remove" ] || [ "$1" = "purge" ];then

echo "清理卸载残留"
for username in `ls /home`  
    do
      echo /home/$username
        if [ -d /home/$username/.deepinwine/Wine-QQ ]
        then
        rm -rf /home/$username/.deepinwine/Wine-QQ
        fi
        if [ -d /home/$username/.deepinwine/Wine-QQ.tmpdir ]
        then
        rm -rf /home/$username/.deepinwine/Wine-QQ.tmpdir
        fi
    done
else
echo "非卸载，跳过清理"
fi
```

代码来源：spk://store/chat/com.qq.im.dwine

即将更新的9.6.0.1hf3版本会解决运行卡顿的问题。暂时没有上线spark_run_v4.sh，需要在更新时删除旧的容器体验
