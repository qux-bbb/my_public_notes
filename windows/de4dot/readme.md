# de4dot

de4dot是一个.NET程序反混淆工具，已经很久不维护了。  

github地址: https://github.com/de4dot/de4dot  


## 获取可执行文件方法
fork项目，在 .github/workflows/build.yml 添加"workflow_dispatch"，前后对比如下：  
```r
name: GitHub CI
on:
  push:
    branches:
```

```r
name: GitHub CI
on:
  workflow_dispatch:
  push:
    branches:
```

这样就可以在 Actions 页面手动运行 workflow，运行之后在 Artifacts 下方可以看到生成的文件：  
```r
de4dot-net35
de4dot-net45
de4dot-netcoreapp2.1
de4dot-netcoreapp3.1
```

我下载的是 de4dot-net45  

其实任意代码提交都会触发build逻辑，README.md随便改点什么都可以  


## 常用命令
```r
# 直接解混淆，一般效果还行，结果文件命名为"file1-cleaned"
de4dot.exe file1
# 可以一次处理多个文件
de4dot.exe file1 file2 file3
# 递归搜索.NET文件，处理后输出到output文件夹，-r表示recursively
de4dot.exe -r c:\my\files -ro c:\my\output
# -f指定输入文件，-o指定输出文件
de4dot.exe file1 -f file2 -o file2.out -f file3 -o file3.out

# 使用delegate(委托)的方式调用解密函数来解密字符串，最后使用解密后的字符串替换调用解密函数的逻辑，06012345、060ABCDE是解密函数的Token值
# !最好在沙箱或虚拟机中执行，因为会运行代码
de4dot.exe file1.dll --strtyp delegate --strtok 06012345 --strtok 060ABCDE
# 使用emulate(调用解密函数，模拟指令)的方式解密字符串
# !最好在沙箱或虚拟机中执行，因为会运行代码
de4dot.exe file1 --strtyp emulate --strtok 06000002

# Detect obfuscators and exit
de4dot.exe -d file1
# 对于未知的混淆工具，如果变量名、方法名等不符合相应正则，则重命名
# 可以处理变量名是一堆中文字符的情况
de4dot.exe --un-name "^[a-zA-Z_<{$][a-zA-Z_0-9<>{}$.`-]*$" file1
```


## mobile46/de4dot
mobile46给de4dot添加了一些自动反混淆的功能，效果不错，但可能自动运行代码，所以最好在虚拟机中运行  

github地址: https://github.com/mobile46/de4dot  


---
2023/11/20  
