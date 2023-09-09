# linux---交叉编译windows可执行文件

安装编译工具:  
```sh
sudo apt install mingw-w64
```

生成exe:  
```sh
# pe32
i686-w64-mingw32-gcc -m32 -o hello_x86.exe hello.c

# pe32+
x86_64-w64-mingw32-gcc -m64 -o hello_x64.exe hello.c
```

生成dll模板:  
```sh
# x86
i686-w64-mingw32-gcc -m32 -shared -s -o TemplateDll_x86.dll TemplateDll.c TemplateDll.def
# x64
x86_64-w64-mingw32-gcc -m64 -shared -s -o TemplateDll_x64.dll TemplateDll.c TemplateDll.def
```

部分选项解释:  
```r
# 指定位数
-m32
-m64

# 压缩大小
-s
Remove all symbol table and relocation information from the executable.

# 生成dll
-shared
Produce a shared object which can then be linked with other objects to form an executable. Not all systems support this option. For predictable results, you must also specify the same set of options used for compilation (-fpic, -fPIC, or model suboptions) when you specify this linker option.[1]
```


参考资料:  
1. https://blog.csdn.net/zuihaobushi/article/details/90167362  
2. https://github.com/cuckoosandbox/monitor/blob/master/Makefile  
3. https://cuckoo-monitor.readthedocs.io/en/latest/requirements.html  
4. https://www.systutorials.com/docs/linux/man/1-i686-w64-mingw32-gcc/  


20200406  
