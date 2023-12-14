# gcc

一开始是 `GNU C Compiler` 的缩写，GNU C语言编译器  
后来改成 `GNU Compiler Collection` 的缩写，因为支持很多语言  

官网: https://gcc.gnu.org/  


最基本的使用：  
```bash
# 编译生成可执行文件，不指定输出文件名则默认为 a.out
gcc hello.c
# 指定输出文件名为 hello
gcc hello.c -o hello
```

部分选项说明：  
```r
# 指定输出文件名
-o file
Place the primary output in file file.  This applies to whatever sort of output is being produced, whether it be an executable file, an object file, an assembler file or preprocessed C code.
If -o is not specified, the default is to put an executable file in a.out, the object file for source.suffix in source.o, its assembler file in source.s, a precompiled header file in source.suffix.gch, and all preprocessed C source on standard output.

# 指定位数
-m32
-m64

# 压缩大小
-s
Remove all symbol table and relocation information from the executable.

# 生成dll
-shared
Produce a shared object which can then be linked with other objects to form an executable. Not all systems support this option. For predictable results, you must also specify the same set of options used for compilation (-fpic, -fPIC, or model suboptions) when you specify this linker option.[1]
pic, Position Independent Code, 位置无关代码

# 静态链接
-static

# 链接线程库
-pthread

# -l后加名字就是链接指定库的意思
# 链接数学库
-lm
```


2020/5/11  
