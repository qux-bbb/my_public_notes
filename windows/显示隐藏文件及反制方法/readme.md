# 显示隐藏文件及反制方法

Windows的文件管理器默认不会显示设置了隐藏属性的文件。  

## 显示隐藏文件
以Win7举例，打开文件管理器，"组织->文件夹和搜索选项->查看"  
勾选"隐藏受保护的操作系统文件(推荐)"和"隐藏文件和文件夹->显示隐藏的文件、文件夹和驱动器"  
这样就可以在文件管理器里看到隐藏的文件。  

## 禁止显示隐藏文件
但如果设置了这样的注册表项，就可以禁止通过上面的方式显示隐藏文件了：  
```r
[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\Folder\Hidden\SHOWALL]
"CheckedValue"=dword:00000000
```

## 命令行查看隐藏文件
打开命令行，切换到相应目录  
`dir /a` 命令可列出隐藏文件  
`attrib *` 命令可列出文件属性，显示更清晰  
`attrib -h <file_path>` 命令可以取消隐藏属性，attrib具体用法见 [attrib](../attrib/readme.md)  


---
2021/10/11  
