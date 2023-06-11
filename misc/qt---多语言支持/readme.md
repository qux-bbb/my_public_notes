# qt---多语言支持

keywords: 翻译 多语言  

可以翻译的有2种：  
1. 界面上的，默认都是会翻译的，如果不想翻译，可以取消勾选相应的"可翻译的"
2. 代码中出现的文本，如果需要翻译，可以用tr包裹，如: tr("hello")

准备好之后，工具 -> 外部 -> Qt语言家 -> 更新翻译，这样就可以在相应的ts文件中生成待翻译的项，举例：  
```xml
<message>
    <location filename="mainwindow.ui" line="53"/>
    <source>TextLabel</source>
    <translation type="unfinished"></translation>
</message>
```
翻译后的状态举例：  
```xml
<message>
    <location filename="mainwindow.ui" line="53"/>
    <source>TextLabel</source>
    <translation>TextLabel 测试</translation>
</message>
```

全部翻译完成后，工具 -> 外部 -> Qt语言家 -> 发布翻译，这样就可以生成相应的qm文件  

编译就可以自动显示相应语言版本的界面了。  


2021/7/27  
