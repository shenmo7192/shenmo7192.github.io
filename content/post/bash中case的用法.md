---
title: Bash中case的用法
date: 2022-02-27T22:43:21+08:00
lastmod: 2022-02-27T22:43:21+08:00
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

转载自：https://www.cnblogs.com/J1ac/p/10988210.html

<!--more-->

> 需求来自看懂zty199的提交 and 看懂 abcfy的压制脚本。我自己还是习惯用if。路过大佬能否讲解下if差在哪里

-------

zty199的提交： https://gitee.com/deepin-community-store/spark-store/commit/3bfc183c895718a669e673be6b4678a2f87727c3  
abcfy的脚本： https://gitee.com/abcfy2/simple_video_compress_build

## 转载内容：

看到一些很实用的脚本，由于之前对于bash脚本的积累都比较离散，没有一个全面的了解，在这里记录一下：

bash的case语句用法

case语句的语法规则是：

```bash
case $变量名 in
 模式1）
 命令序列1
 ;;
 模式2）
 命令序列2
 ;; 
 *）
 默认执行的命令序列     
 ;; 
esac 

```

注意的是, case比较的是pattern，然后既然是通配符，那么：

1.  切记通配符本身不能用引号括起来。
2.  而对于变量VAR是否使用双引号括起来都可以。
3.  另外要记住通配符(pattern)和规则表达式(regular expression)的区别。
4.  匹配模式中可是使用方括号表示一个连续的范围，如[0-9]；使用竖杠符号“|”表示或。 最后的“*）”表示默认模式，当使用前面的各种模式均无法匹配该变量时，将执行“*）”后的命令序列。

case语句实例：由用户从键盘输入一个字符，并判断该字符是否为字母、数字或者其他字符， 并输出相应的提示信息。


```bash
#!/bin/bash
read -p "press some key ,then press return :" KEY
case $KEY in
[a-z]|[A-Z])
echo "It's a letter."
;;
[0-9]) 
echo "It's a digit."
;;
*)
echo "It's function keys、Spacebar or other ksys."
esac

```

case/esac的标准用法大致如下: 
```bash
 case $arg in 
     pattern | sample) # arg in pattern or sample 
     ;; 
     pattern1) # arg in pattern1 
     ;; 
     *) #default 
     ;; 
 esac 
 ```
 
 arg是您所引入的参数，如果arg内容符合pattern项目的话，那麽便会执行pattern以下的程式码，而该段程式码则以两个分号";;"做结尾。 
 可以注意到"case"及"esac"是对称的，如果记不起来的话，把"case"颠倒过来即可。 

case语句匹配的是通配符，如果加上双引号后就不是按通配符处理，而是按文本处理。

使用双引号后通配符就不再生效 ，只是作为普通字符对待。

----
分号&:and功能，满足其中任一条件即可
例子：
```bash
#!/bin/bash
read -p "你喜欢编程么：（y/n）：" ans
case $ans in
    y);&
    Y) echo "我也是";;
    n);&
    N) echo "sorry,跟你没什么好谈的";;
esac

```
