# linux--mo和po文件

PO 是 Portable Object (可移植对象)的缩写形式；MO 是 Machine Object (机器对象) 的缩写形式。  

PO 文件是面向翻译人员的、提取于源代码的一种资源文件。当软件升级的时候，通过使用 gettext 软件包处理 PO 文件，可以在一定程度上使翻译成果得以继承，减轻翻译人员的负担。  

MO 文件是面向计算机的、由 PO 文件通过 gettext 软件包编译而成的二进制文件。程序通过读取 MO 文件使自身的界面转换成用户使用的语言。  

文件相互转换：  

```r
# po->mo
msgfmt  *.po -o *.mo

# mo->po
msgunfmt *.mo -o *.po
```


原地址: https://blog.csdn.net/here_c_my/article/details/44565479  


2018/7/5  
