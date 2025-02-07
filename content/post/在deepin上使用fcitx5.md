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

我照着这篇帖子 https://bbs.deepin.org/post/224852 配置了下，略微修改了些细节，替换了一些国内访问需要加速的链接，加上了后续的一些踩坑的经验，把图片换成文字

---

### 1\. 安装Fcitx5输入法

1. 卸载fcitx4：`sudo apt purge fcitx*`
2. 安装fcitx5：`sudo apt install fcitx5`
3. 启动器中设置Fcitx 5开机自启动，并注销重新登陆系统
4. 安装中文输入法：`sudo apt install fcitx5-chinese-addons`
5. 启动器中打开Fcitx 5配置
6. 在配置窗口的`输入法`tab下将拼音从右边添加到左边
![截图_fcitx5-config-qt_20210818105532](https://xiaoshujiang-shenmo.oss-accelerate.aliyuncs.com/小书匠/截图_fcitx5-config-qt_20210818105532.png)

7. 手动添加fcitx5中文输入法默认词库：从 https://kgithub.com/felixonmars/fcitx5-pinyin-zhwiki 下载.dict后缀的符合版权的词库文件，放到`~/.local/share/fcitx5/pinyin/dictionaries/`目录下，没有则创建目录
> 如果你加入了better dde源，你可以直接 `sudo apt install fcitx5-pinyin-zhwiki` 来安装词库


8. 在fcitx5配置窗口的附加组件tab下，点击拼音选项后面的齿轮按钮进入配置窗口，点击词典后面的齿轮按钮，打开另一个配置窗口，选择导入并选择在线浏览搜狗细胞词典，在打开的页面中选择对应的词典并点击立即下载，下载完成后会自动添加到拼音词典管理器中。
![截图_选择区域_20210819092158](https://xiaoshujiang-shenmo.oss-accelerate.aliyuncs.com/小书匠/截图_选择区域_20210819092158.png)
9. 启用表情符号：`sudo apt install fonts-noto-color-emoji`，安装后在fcitx5配置页面的`附加组件`tab下选择`拼音`后面的齿轮进入配置页面，勾选`启用颜文字`。
10. 启用云拼音：`sudo apt install fcitx5-module-cloudpinyin`，安装后在fcitx5配置页面的`附加组件`tab下选择`云拼音`，点击齿轮进入云拼音配置页面，后端选择Baidu。
11. 启用单行模式：打开fcitx5配置页面，选择`附加组件`tab，选择`拼音`并勾选`在程序中显示预编辑文本` （在一些应用中会有问题，不建议启用）

### 2\. 配置优化Fcitx5（修改完成后重启输入法生效）

1. 修改输入法：打开fcitx5配置页面，选择`附加组件`tab，选择`经典用户界面`后面的齿轮进入经典用户界面窗口，可以修改输入法主题，字体，字号，菜单字体等。或者在~/.confit/fcitx5/conf/classicui.conf中修改这些选项。
2. 推荐使用的皮肤：Fcitx5-Material-Color

`sudo aptss install fcitx5-material-color` 即可在经典用户界面窗口中设置此皮肤

> 因为deepin源中无此包，使用星火商店的cli安装指令
> 
> 使用此指令的前提是安装星火应用商店 
> 
> 你也可以使用spk链接来安装 [spk://store/themes/fcitx5-material-color](spk://store/themes/fcitx5-material-color)


3.  使用第三方皮肤，所有的皮肤都必须将文件夹放到目录~/.local/share/fcitx5/themes/下

* 使用搜狗输入法皮肤：下载[搜狗输入法皮肤](https://pinyin.sogou.com/skins/)和[搜狗输入法皮肤转换器](https://kgithub.com/fkxxyz/ssfconv) ，比如使用皮肤转换器通过这条命令
 ` ./ssfconv -t fcitx5 ～/Downloads/哪吒之魔童降世.ssf ～/Downloads/哪吒之魔童降世`
 将搜狗输入法皮肤转为fcitx5皮肤，将转换后的皮肤文件夹复制到`~/.local/share/fcitx5/themes/`下面
* 其他开源皮肤：将下载的主题包文件夹放到~/.local/share/fcitx5/themes/下面





### 3\. fcitx5中文输入法方括号和无法输入`·`问题的解决

`sudo deepin-editor /usr/share/fcitx5/punctuation/punc.mb.zh_CN`，把其中的的18、19行改为：

```
[ 【
] 】
```

并在尾部添加

```
` ·
```

这个文件的每一行第一个字符代表按键，第二个开始的所有字符代表该按键的Fcitx5中文输入法下的输出字符



### 4\. 其他常见问题

1. 修改候选词个数：Fcitx配置->拼音->页大小

