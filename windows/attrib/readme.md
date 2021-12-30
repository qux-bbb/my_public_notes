# attrib

windows的attrib命令可以显示或更改文件属性。  
右键看文件属性也可以设置部分属性。  

添加隐藏，设置为系统文件：  
```bat
attrib +h +s hello.exe
```

`attrib /?`的输出：  
```r
ATTRIB [+R | -R] [+A | -A ] [+S | -S] [+H | -H] [+I | -I]
       [drive:][path][filename] [/S [/D] [/L]]
  + 设置属性。
  - 清除属性。
  R 只读文件属性。
  A 存档文件属性。
  S 系统文件属性。
  H 隐藏文件属性。
  I 无内容索引文件属性。
  [drive:][path][filename]
      指定 attrib 要处理的文件。
  /S 处理当前文件夹及其所有子文件夹中的匹配文件。
  /D 也处理文件夹。
  /L 处理符号链接和符号链接目标的属性。
```


2021/4/21  
