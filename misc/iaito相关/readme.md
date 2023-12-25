# iaito相关

官网: https://www.radare.org/n/iaito.html  
github地址: https://github.com/radareorg/iaito  

iaito是radare2的官方图形界面，是Cutter分叉之后的延续，还不太完善。  

iaido, いあいどう, 居合道的意思。  
iaito, いあいと, 居合刀的意思，一种用于居合道（iaido）训练的日本剑。  
(含义来源: chatgpt)  

因为基于radare，所以有wtf命令(write to file)可以保存部分内存数据，很方便。  
```r
# 当前位置开始，写20字节到hello.dat文件
wtf hello.dat 20
# 指定从地址0x8048300开始，写20字节到hello.dat文件
wtf hello.dat 20 @ 0x8048300
# iaito的Console支持重定向，所以这样也是没问题的
pr 20 @ 0x8048300 > hello.dat
```


2023/12/24  
