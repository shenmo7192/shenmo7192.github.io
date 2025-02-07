---
title: UOS 免开发者模式安装第三方应用工具（UOS安装应用）
date: 2021-11-23T15:21:08+08:00
lastmod: 2021-11-23T15:21:08+08:00
author: shenmo
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - 啥都有
tags:
  - Linux
# nolastmod: true
draft: false
---

早在去年UOS发布证书认证工具的时候我就想这样了，但是想到星火商店专门为UOS单独开发版本，还要收集用户的证书就很难受，遂作罢。然而QQ群里一位神人向我亲自演示了这东西可行，我就想搞一个脚本来处理，反正也没什么事可做

<!--more-->

[https://gitee.com/deepin-community-store/uos-self-signer](https://gitee.com/deepin-community-store/uos-self-signer)

链接镇楼

原理很简单，就是利用cert-tool生成证书再签名，安装

原本想着要图形化获取用户名什么的，现在开发停滞做不到

但是如果秉持`又不是不能用`的准则，命令行打开脚本的话

完全够了！

于是直接开搞  
下载地址： https://gitee.com/deepin-community-store/spark-store-uos/blob/master/ussinstall

以下为脚本内容

```bash
#!/bin/bash
reset
if [ -f "/usr/bin/deepin-deb-installer" ]
then 
echo "深度软件包安装器已安装，开始检测证书"
else
echo "未安装深度软件包安装器，拒绝执行"
echo "UOS需要深度软件包安装器来认证签名"
echo "如果你用的是UOS，你能卸载这玩意说明你已经开了开发者模式......悄悄告诉你，放屁是不用脱裤子的！"
echo "如果你用的不是统信系发行版......所以你为什么要打开这个脚本？"
exit 1
fi

if [ -f "/usr/share/ca-certificates/deepin/private/priv.crt" ]

	then 
	echo "检测到已经生成过证书，直接跳过询问"

else

until [ -f "/usr/bin/cert-tool" ]
#强制未安装证书工具的不通过
do

echo "该工具的原理是利用UOS的自签名安装包免开发者的特性，需要您的UOS ID账号和密码，请在使用工具前确保在应用商店中已安装过“证书工具”这个应用"
echo "如果没有安装，则无法使用。请确认安装后再进行下一步操作"
echo "如果你确认已经安装了该应用，请按回车"
read renyijian

#检测是否在说谎签名文件
if [ -f "/usr/bin/cert-tool" ]
then
echo "成功检测到cert-tool存在，开始检测证书\n"
else
echo "没有检测到该应用，请您再次确认“证书工具”已经安装！"
sleep 3
clear

fi
done



until [ -f "/usr/share/ca-certificates/deepin/private/priv.crt" ]
do 
	echo "没有检测到证书，准备调用证书工具生成证书，请输入您的UOS账号/密码。本脚本不会上传任何信息"
	echo "请在此行输入您的UOS账号用户名/电话号/邮箱"
	read account
	echo "请在此行输入您的UOS账号密码"
	read passwd
	echo "即将安装证书，请在弹出的窗口安装"
	cert-tool -username="$account" -password="$passwd"

done
echo "检测到已经生成过证书，准备签名"

fi
#这个if是判断是否已经有证书


unset account
unset passwd
unset renyijian

debpath=""
cd /tmp

until [ -f "$debpath" ]
do
if [ ! $1 ]
    then 
    echo "没有检测到参数，以交互式安装运行"
    echo "请输入deb文件的绝对路径或直接拖入deb文件(仅限支持的文件管理器，比如深度文管），结束后回车"
    echo "生成的签名过的deb将保存在/tmp/signed_deb"
    read debpath
else
    echo "参数存在，直接开始签名\n生成的签名过的deb保存在/tmp/signed_deb"
    debpath="$1"
    echo "读取到的deb路径为：$debpath"
fi
debpath=`echo "$debpath" | sed $'s/\'//g'`
echo "去除可能的单引号后得到：$debpath"


if [ -f $debpath ]
then
echo "文件有效，开始签名"
deepin-elf-sign-deb "$debpath"
echo "签名结束，启动深度软件包管理器"
else
echo "路径出错,请确认你输入了正确的路径！"
sleep 3
clear
fi
done
file_name=$(basename "$debpath")

deepin-deb-installer "/tmp/signed_deb/$file_name"


```