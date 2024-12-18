<img src='./src/assets/valine.png' width='200' align="right" />

# Valine

[![](https://data.jsdelivr.com/v1/package/npm/valine/badge)](https://www.jsdelivr.com/package/npm/valine)
[![version](https://img.shields.io/github/release/xCss/Valine.svg?style=flat-square)](https://github.com/xCss/Valine/releases)
[![npm downloads](https://img.shields.io/npm/dm/valine.svg?style=flat-square)](https://www.npmjs.com/package/valine)
[![build](https://img.shields.io/circleci/project/github/xCss/Valine/master.svg?style=flat-square)](https://circleci.com/gh/xCss/Valine)
[![donate](https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&style=flat-square)](#donate)

> A fast, simple & powerful comment system.
------------------------------
**[View Documentation](https://valine.js.org)**

## 比原版新增

- `博主`，`小伙伴`，`访客`标签
- 添加`浏览器`和`操作系统`图标，需`fontawesomeV5`支持
- 邮箱检测更严格
- `meta placeholder`可自定义

## 新增参数

| 参数 | 类型 | 说明 | 默认 | 示例 |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| tagMeta | Array | 标签要显示的文字 | ["博主","小伙伴","访客"] | ["博主","小伙伴","访客"] |
| master | Array/String | md5加密后的博主邮箱 | [] | ["fe01ce2a7fbac8fafaed7c982a04e229"] |
| friends | Array | md5加密后的小伙伴邮箱 | [] | ["fe01ce2a7fbac8fafaed7c982a04e229"] |
| metaPlaceholder | Object | meta placeholder内容 | {} | {"nick":"昵称/QQ号","mail":"邮箱(必填)"} |
| ~~verify~~(已弃用) | Boolean | 评论时是否需要验证 | false | true |

## Features
- High speed.
- Safe by default.
- No server-side implementation.
- Support for full markdown syntax.
- Simple and lightweight (~15kB gzipped).

See the [Quick start](https://valine.js.org) for more details.

## Contributors
- [Contributors](https://github.com/xCss/Valine/graphs/contributors)

## Donate
If you are enjoying this app, please consider making a donation to keep it alive, I will try my best to dedicate more time or even full time to work on it. 😉

| Alipay | Wechat |
| :------: | :------: |
| <img width="150" src="./src/assets/alipay.png"> | <img width="135" src="./src/assets/wechat.png"> |

If you are not available for this, simply spreading the word for us would help too!

## License
[GPL-2.0](https://github.com/xCss/Valine/blob/master/LICENSE)
