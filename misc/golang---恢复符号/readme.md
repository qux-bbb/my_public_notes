# golang---恢复符号

这样编译go程序，可以去除符号，加大逆向人员分析难度  
```r
go build -o hello -ldflags '-s' hello.go
```
不过符号并不是真的删掉了，可以通过一些脚本恢复回来  

## for IDA
有好用的工具，可以都试试  
都是下载好直接用IDA加载脚本就好了，不需要放在插件文件夹里  

1. IDAGolangHelper  
https://github.com/sibears/IDAGolangHelper  

2. golang_loader_assist
https://rednaga.io/2016/09/21/reversing_go_binaries_like_a_pro/  
https://github.com/strazzere/golang_loader_assist/  

3. go_parser
https://github.com/0xjiayu/go_parser  
IDA加载go_parser.py即可，效果很好，如果有问题注意文件或者项目路径不包含中文试试  

相关文章：  
```r
Go二进制文件逆向分析从基础到进阶——综述
https://www.anquanke.com/post/id/214940

Go二进制文件逆向分析从基础到进阶——MetaInfo、函数符号和源码文件路径列表
https://www.anquanke.com/post/id/215419

Go二进制文件逆向分析从基础到进阶——数据类型
https://www.anquanke.com/post/id/215820

Go二进制文件逆向分析从基础到进阶——itab和strings
https://www.anquanke.com/post/id/218377

Go二进制文件逆向分析从基础到进阶——Tips与实战案例
https://www.anquanke.com/post/id/218674
```

## for Ghidra
使用步骤稍微多一点：  
如果是python脚本，复制到 Ghidra\Features\Python\ghidra_scripts 目录  
Window -> Script Manager, 搜索脚本名称，选中一个，点击右上图标"Run Script"即可  
注意一次只能运行一个脚本  

效果挺好的  

https://cujo.com/reverse-engineering-go-binaries-with-ghidra/  
https://github.com/getCUJO/ThreatIntel/tree/master/Scripts/Ghidra  


2021/9/5  
