## 介绍
.net是一个开源的开发平台，可以用来开发不同平台的应用（Windows、Linux、MacOS）。  
官网: https://dotnet.microsoft.com/  
官方文档: https://docs.microsoft.com/zh-cn/dotnet/fundamentals/  


## 写程序
用Visual Studio就可以写.net了。  
.net framework只支持Windows，可以生成单个exe。  
.net core支持多平台，但还不知道怎么生成单个exe。  


## 反编译工具
https://github.com/dnSpyEx/dnSpy  

dnspy除了反编译，也可以调试。  


## 混淆工具
https://github.com/yck1509/ConfuserEx  


## 反混淆工具
https://github.com/de4dot/de4dot  

举例：  
```
de4dot.exe -r c:\my\files -ro c:\my\output
de4dot.exe file1 file2 file3
de4dot.exe file1 -f file2 -o file2.out -f file3 -o file3.out
de4dot.exe file1 --strtyp delegate --strtok 06000123
```
最后的解密字符串操作最好在沙箱或虚拟机中执行，因为会运行代码  
