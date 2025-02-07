---
title: Python第一课：常见的数据类型
date: 2022-05-31T11:49:17+08:00
avatar: /img/avatar.jpeg
# authorlink: https://author.site
# cover: /img/Icey-view.png
# images:
#   - /img/cover.jpg
categories:
  - Python笔记
tags:
  - Python学习
# nolastmod: true
draft: false
---
猫猫上的第一节课

<!--more-->

## 变量类型
Python不支持设定变量类型，都是自动检测

例子：

```python
bool_1 = True
int_1 = 1
float_1 = 1.2
str_1 = "猫猫可不可爱？"
str_2 = '是的！'  # 单引号和双引号无区别
#字典
dict_1 = {"IsCatCute?": True, "IsMomoCute": True, "FuckU": False, 1: "One", "Two": 2}  # 冒号左边是索引，冒号右边是键值
#列表
list_1 = ["Cute", "Dog", "cat"]  # 索引从0开始计数

#元组
tuple_1 = (1,)  # 如果元组的长度为1，需要在后面加上逗号
tuple_1_fake = (1)  # 这是一个整数
```

* 布尔值：True或者False，True在被运算时看做1
* 整数值： 整数
* 浮点数：小数
* * 没有长短整形的区分，所有的数值型变量的范围都是一样的
* 字符串。python没有char，所有的字符都是字符串
* 在Python中，单双引号都是一样的意义
* 字典，储存项和值。格式：`"xxx":xxx,`
* 列表类似一维数组，只能存值
* 元组 元组是不能被删除元素的列表——如果长度为1，要在后面加上逗号，否则会被当成单个
* **元组的定义需要用`()`，而列表是`[]`**

## 获取类型
`print(type(变量))`


## 类型转换
```python
int_1 = int("114514")

```

用法：xxx=`类型(xxx)`
## 列表与字符串
* 字符串是特殊的列表
```python
str_1 = "猫猫可不可爱？"
list_2 = list(str_1)  # 强转字符串为列表
print(list_2)  # 字符串是特殊的列表

```

输出：`['猫', '猫', '可', '不', '可', '爱', '？']`


## 字典的操作
https://www.runoob.com/python3/python3-dictionary.html

