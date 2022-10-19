# golang---恢复符号

这样编译go程序，可以去除符号，加大逆向人员分析难度  
```bash
go build -o hello -ldflags '-s' hello.go
```
不过符号并不是真的删掉了，可以通过一些脚本恢复回来  

## for IDA
有2个好用的工具，可以都试试  
都是下载好直接用IDA加载脚本就好了，不需要放在插件文件夹里  

1. IDAGolangHelper  
https://github.com/sibears/IDAGolangHelper  

2. golang_loader_assist
https://rednaga.io/2016/09/21/reversing_go_binaries_like_a_pro/  
https://github.com/strazzere/golang_loader_assist/  

3. go_parser
https://github.com/0xjiayu/go_parser  
IDA加载go_parser.py即可，效果很好，如果有问题注意文件或者项目路径不包含中文试试  


## for Ghidra
使用步骤稍微多一点：  
复制脚本到 ghidra_scripts 目录(默认: `<HomeDirectory>/ghidra_scripts`). 用脚本管理器来加载脚本  

效果挺好的  

https://cujo.com/reverse-engineering-go-binaries-with-ghidra/  
https://github.com/getCUJO/ThreatIntel/tree/master/Scripts/Ghidra  


2021/9/5  
