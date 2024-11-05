# python便携版

embeddable版本的python就是便携版的，但是没有带pip，可以使用get-pip安装使用pip。  

以windows下的python举例：  
1. 打开链接: https://www.python.org/downloads/windows/
2. 下载 Windows embeddable package (64-bit) 版本
3. 解压后编辑 python313._pth (这里是3.13版本)，取消注释 `import site`
4. 下载 https://bootstrap.pypa.io/pip/get-pip.py 到python.exe所在文件夹
5. 执行命令: .\python.exe get-pip.py

这样就得到了带pip的便携版python，使用pip方法：  
```r
.\python.exe -m pip
```


信息来源: https://stackoverflow.com/a/48906746  


2024/11/5  
