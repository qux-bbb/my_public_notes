# NTFS备用数据流

keywords: 交换数据流 ads  

NTFS: New Technology File System, Windows默认的文件系统  
ADS: Alternate Data Streams, 备用数据流，虽然很多地方都叫交换数据流，但通过`dir /?`是能看到官方翻译的  

NTFS备用数据流可以理解成附在正常文件上的隐藏的文件内容  


## 已知的一个正常用途
在windows上，从网上下载的文件，都会有一个备用数据流，名为：`<filename>:Zone.Identifier`  
该备用数据流会记录下载地址，这个功能也被系统用于判断文件是否从网络下载  

假如下载的文件是 `hello.txt`，则备用数据流名称为：`hello.txt:Zone.Identifier`  
意思就是说，假如我发现`hello.txt:Zone.Identifier`存在，那同一文件夹下的`hello.txt`就是从网上下载的  


## 一些操作
### 命令行
列出文件(包括文件的备用数据流)的命令：  
```cmd
dir /r
```
使用记事本查看备用数据流(也可以用这种方法创建编辑备用数据流)：  
```cmd
notepad hello.txt:Zone.Identifier
```
暂时没找到命令行单独删除备用数据流的方法，删除原文件，备用数据流会一起被删除  

### 图形界面
如果不习惯命令行，AlternateStreamView软件可以用来查看和提取备用数据流  
用winrar在命令行下也可以提取备用数据流  

使用 AlternateStreamView 可以单独把备用数据流删掉  


2016/11/12  
