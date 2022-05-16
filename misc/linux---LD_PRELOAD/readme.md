# linux---LD_PRELOAD

使用该技术，可以 hook 一些库函数，关键操作如下：  

time.c  
```c
static int t = 0x31337;

void sleep(int sec) {
    t += sec;
}

int time() {
    return t;
}
```

生成动态链接文件：  
```r
gcc --shared time.c -o time.so
```

运行命令：  
```r
LD_PRELOAD=./time.so ./patched.elf
```

这样就达到了替换 sleep 和 time 函数的效果  

在 gdb 中设置 LD_PRELOAD 的方法：  
```r
set environment LD_PRELOAD ./ptrace.so
```


原链接：https://ctf-wiki.github.io/ctf-wiki/reverse/linux/ld_preload-zh/  


2020/6/27  
