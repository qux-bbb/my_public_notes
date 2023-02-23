# 在多个平台运行的程序

一次编译，可以在以下平台运行：  
```r
Linux + Mac + Windows + FreeBSD + OpenBSD + NetBSD + BIOS  
```
大概原理是把各种格式巧妙地拼在一起  

```r
wget https://justine.lol/cosmopolitan/cosmopolitan-amalgamation-2.2.zip
unzip cosmopolitan-amalgamation-2.2.zip
printf 'main() { printf("hello world\\n"); }\n' >hello.c
gcc -g -Os -static -nostdlib -nostdinc -fno-pie -no-pie -mno-red-zone \
  -fno-omit-frame-pointer -pg -mnop-mcount -mno-tls-direct-seg-refs -gdwarf-4 \
  -o hello.com.dbg hello.c -fuse-ld=bfd -Wl,-T,ape.lds -Wl,--gc-sections \
  -include cosmopolitan.h crt.o ape-no-modify-self.o cosmopolitan.a
objcopy -S -O binary hello.com.dbg hello.com
```

原链接: https://justine.lol/cosmopolitan/index.html  
github地址: https://github.com/jart/cosmopolitan  

感谢B站 AHelloWorldA  


2023/2/23  
