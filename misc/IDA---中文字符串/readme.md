# IDA---中文字符串

keywords: 汉字  


## `显示中文字符串`
在 Options -> General... -> Strings 标签页下，鼠标左键点击"Default 8-bit"右侧的按钮，鼠标右键添加并选择合适的编码(可能是GBK之类的编码)  

设置之后再次尝试显示字符串，可能会有效果  


对单独的字符串设置方法：  
在已经设置为看起来乱码的字符串的情况下，点击字符串，然后 Options -> String Literals... Current选择不同的编码试试


## `IDA7.0中文字符搜索的实现方法`
```
标题：IDA7.0 中文字符搜索的实现方法	
作者：LOCKLOSE 

方法1:
1:保存Chinese.clt文件到IDA\CFG目录中.
将以下内容保存为clt文件,
u2000..u206F,
u2F00..u2FDF,
u3000..u303F,
u31C0..u31EF,
u3400..u4DBF,
u4E00..u9FFF,
uF900..uFAFF,
uFE30..uFE4F,
u20000..u2A6DF,
u2A700..u2BA7F,
u2B740..u2B81F,
u2F800..u2FA1F;

2:修改IDA.CFG文件中ENCODING_CULTURES项目.添加一条GB2312:Chinese, 注意格式别写错.这里的Chinese对应上面保存的clt文件.不需要.clt扩展名.

ENCODING_CULTURES =
        1250: Central_Europe,
        1251: Cyrillic,
        1252: Latin_1,
        1253: Greek,
        1254: Turkish,
        1255: Hebrew,
        1256: Arabic,
        1257: Baltic,
        1258: Vietnam,
        874: Thai,
        GB2312: Chinese, //这里是添加的.
        cp863: Latin_1 Greek;
```

原链接: https://bbs.pediy.com/thread-221591.htm  

2019/9/15  
