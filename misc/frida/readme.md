# frida

## 简单信息
官网: https://frida.re/  
github地址: https://github.com/frida/frida  

轻量级的hook框架，python和js结合  

安装：  
```r
pip install frida-tools
```

## 附加进程记录api
使用frida-trace附加目标进程记录一些api调用：  
```r
# -i FUNCTION, --include FUNCTION
#                       include [MODULE!]FUNCTION
frida-trace -i "CreateFileW" notepad.exe
```

然后会出现两个js路径，我们选 `C:\Users\alice\__handlers__\KERNEL32.DLL\CreateFileW.js`，编辑该文件  
修改 `log('CreateFileW()';` 为 `log('CreateFileW() - ' + args[0].readUtf16String());`  
保存之后，拖一个文件进notepad，就可以在命令行看到相应的文件路径  

## 一些常用命令
```r
# 创建新进程
frida -l hook.js -f 程序名称

# 附加到进程
frida -l hook.js 进程名
```

---
2020/9/2  
