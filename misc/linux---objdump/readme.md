keywords: 反汇编  

objdump可以显示文件的一些信息  

输出可执行程序的汇编码  
```bash
objdump -d notepad.exe
```

查看GOT表的地址  
```bash
objdump -R hello.bin
```
