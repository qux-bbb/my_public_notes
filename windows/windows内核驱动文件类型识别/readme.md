# windows内核驱动文件类型识别

windows内核驱动文件一般都是.sys结尾的文件。  
如果没有文件名，通过file命令得到文件类型，如果以"PE32"开头并且包含"native"，也可以确定是内核驱动文件。  
```r
PE32+ executable (native) x86-64, for MS Windows
```


2020/11/20  
