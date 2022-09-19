---
title: 在deepin上使用fcitx5
date: 2022-09-19T17:04:15+08:00
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

这里输入的内容会出现在主页也在正文里

<!--more-->


### 1\. 安装Fcitx5输入法

1.  卸载fcitx4：`sudo apt purge fcitx*`
2.  安装fcitx5：`sudo apt install fcitx5`

1.  启动器中设置Fcitx 5开机自启动，并注销重新登陆系统
2.  安装中文输入法：`sudo apt install fcitx5-chinese-addons`（fcitx5-pinyin只安装拼音和双拼，fcitx5-table只安装五笔、自然码、晚风、二笔、电报码、仓颉等，fcitx5-rime和fcitx5-chinese-addons类似，中文默认繁体），在托盘位置右键输入法图标并选择重新启动
3.  启动器中打开Fcitx 5配置
4.  在配置窗口的`输入法`tab下将拼音从右边添加到左边

![](https://cdn.nlark.com/yuque/0/2021/png/667108/1629255447588-054a9707-23e0-43cf-81f4-41eed4a42cca.png)

7.  手动添加fcitx5中文输入法默认词库：从 https://kgithub.com/felixonmars/fcitx5-pinyin-zhwiki 下载.dict后缀的符合版权的词库文件，放到`~/.local/share/fcitx5/pinyin/dictionaries/`目录下，没有则创建目录 
9.  在fcitx5配置窗口的附加组件tab下，点击拼音选项后面的齿轮按钮进入配置窗口，点击词典后面的齿轮按钮，打开另一个配置窗口，选择导入并选择在线浏览搜狗细胞词典，在打开的页面中选择对应的词典并点击立即下载，下载完成后会自动添加到拼音词典管理器中。 
    ![](https://cdn.nlark.com/yuque/0/2021/png/667108/1629336138623-64365ba8-33a3-4d51-9c6e-983cdcf02d2d.png)

1.  启用表情符号：`sudo apt install fonts-noto-color-emoji`，安装后在fcitx5配置页面的`附加组件`tab下选择`拼音`后面的齿轮进入配置页面，勾选`启用颜文字`。
2.  启用云拼音：`sudo apt install fcitx5-module-cloudpinyin`，安装后在fcitx5配置页面的`附加组件`tab下选择`云拼音`，点击齿轮进入云拼音配置页面，后端选择Baidu。
3.  启用单行模式：打开fcitx5配置页面，选择`附加组件`tab，选择`拼音`并勾选`在程序中显示预编辑文本`

### 2\. 配置优化Fcitx5（每次修改完成后重启输入法）

1.  修改输入法：打开fcitx5配置页面，选择`附加组件`tab，选择`经典用户界面`后面的齿轮进入经典用户界面窗口，可以修改输入法主题，字体，字号，菜单字体等。或者在~/.confit/fcitx5/conf/classicui.conf中修改这些选项。
2.  修改托盘拼音图标：替换/usr/share/icons/hicolor/48x48/apps/org.fcitx.Fcitx5.fcitx-pinyin.png成你自己的图片
3.  使用第三方皮肤，所有的皮肤都必须将文件夹放到目录~/.local/share/fcitx5/themes/下，然后按照第13的方法修改主题即可

*   使用搜狗输入法皮肤：下载[搜狗输入法皮肤(https://pinyin.sogou.com/skins/)](https://pinyin.sogou.com/skins/)和[搜狗输入法皮肤转换器(https://gitee.com/zzgkly/ssfconv.git)](https://gitee.com/zzgkly/ssfconv.git) ，比如使用皮肤转换器通过这条命令./ssfconv -t fcitx5 ～/Downloads/哪吒之魔童降世.ssf ～/Downloads/哪吒之魔童降世 将搜狗输入法皮肤转为fcitx5皮肤，将转换后的皮肤文件夹复制到~/.local/share/fcitx5/themes/下面
*   其他开源皮肤：比如win10风格输入法主题（https://github.com/hosxy/Fcitx5-Material-Color） ，将下载的主题包文件夹放到~/.local/share/fcitx5/themes/下面

1.  修改候选词个数：Fcitx配置->拼音->页大小
2.  修复快捷键无法打开截图和录屏：`sudo apt install qdbus-qt5`
3.  修改按键输出字符：`sudo dedit /usr/share/fcitx5/punctuation/punc.mb.zh_CN`，每一行第一个字符代表按键，第二个开始的所有字符代表该按键的Fcitx5中文输入法下的输出字符

> dedit支持在安装此应用后可使用

[spk://store/office/tech.shenmo.dedit](spk://store/office/tech.shenmo.dedit)


### 3\. fcitx5中文输入法方括号问题的解决

把`/usr/share/fcitx5/punctuation/punc.mb.zh_CN`的18、19行改为：


> [ 【
> ] 】

and add 
>` ·

in the end 

