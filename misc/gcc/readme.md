# gcc

一开始是 `GNU C Compiler` 的缩写，GNU C语言编译器  
后来改成 `GNU Compiler Collection` 的缩写，因为支持很多语言  


最基本的使用：  
```bash
gcc hello.c -o hello
```

部分选项说明：  
```
# 指定位数
-m32
-m64

# 压缩大小
-s
Remove all symbol table and relocation information from the executable.

# 生成dll
-shared
Produce a shared object which can then be linked with other objects to form an executable. Not all systems support this option. For predictable results, you must also specify the same set of options used for compilation (-fpic, -fPIC, or model suboptions) when you specify this linker option.[1]

# 静态链接
-static

# 链接线程库
-pthread

# -l后加名字就是链接指定库的意思
# 链接数学库
-lm
```

2020/5/11  
