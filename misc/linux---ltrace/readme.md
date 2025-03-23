# linux---ltrace

ltrace - A library call tracer.  

官网: https://www.ltrace.org/  
gitlab地址: https://gitlab.com/cespedes/ltrace  
手册地址: https://man7.org/linux/man-pages/man1/ltrace.1.html

默认可以看程序的库函数调用，还没找到合适的例子。  

使用"-S"选项可以看系统调用，示例：  
```bash
ltrace -S ./hello
```

2024/2/28  
