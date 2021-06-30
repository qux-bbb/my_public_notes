# NTFS交换数据流

NTFS: New Technology File System, Windows默认的文件系统  
ADS: Alternate Data Streams, 交换数据流，或者更合适的翻译是备用数据流  

NTFS交换数据流可以理解成附在正常文件上的隐藏的文件内容  


## 已知的一个正常用途
在windows上，从网上下载的文件，都会有一个隐藏数据流，文件名为：`<filename>:Zone.Identifier`  
该文件会记录下载地址，这个功能也被系统用于判断文件是否从网络下载  

假如下载的文件是 `hello.txt`，则隐藏流文件名称为：`hello.txt:Zone.Identifier`  
意思就是说，假如我发现`hello.txt:Zone.Identifier`存在，那同一文件夹下的`hello.txt`就是从网上下载的  


## 一些操作
### 命令行
列出所有文件(包括隐藏流文件)的命令：  
```cmd
dir /r /a
```
使用记事本查看隐藏流文件(也可以用这种方法创建编辑流文件)：  
```cmd
notepad hello.txt:Zone.Identifier
```
暂时没找到命令行单独删除流文件的方法，删除原文件，流文件会一起被删除  

### 图形界面
如果不习惯命令行，AlternateStreamView软件可以用来查看和提取流文件  
用winrar在命令行下也可以提取隐藏流文件  

使用 AlternateStreamView 可以把这样的文件删掉  


2016/11/12  
