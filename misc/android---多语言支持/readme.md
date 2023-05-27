# android---多语言支持

```
以android studio，中文为例
也就是跟随系统显示不同的语言，自己设两套资源，一套英文，一套中文
app会自己判断系统环境，来切换不同的语言

在res文件夹  右键-->New-->Values resource file

File name 写： strings
Available qualifiers 中选择 Locale  点击  >>
搜索  zh  找到中文对应，这时候   Directory name 会自动变成：values-zh-rCN

这样之后就可以对应着之前的 strings.xml中的字符串改成汉语的了
```


2017/9/2  
