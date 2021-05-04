# linux---dd

man手册描述：  
```
dd - convert and copy a file
Copy a file, converting and formatting according to the operands.
```

生成linux安装系统用的U盘启动盘：  
```bash
dd if=kali-linux-2016.2-amd64.iso of=/dev/sdb bs=1M
```

生成一个1G的全0文件：  
```bash
dd if=/dev/zero of=/tmp/zero.img bs=1M count=1024
```

选项解释  
```
if, 输入文件
of, 输出文件
count, 写的次数
bs, BYTES, 一次写的量
    c=1
    w=2
    b=512
    kB=1000, K=1024
    MB=1000*1000, M=1024*1024
    GB=1000*1000*1000, G=1024*1024*1024
    后面还可以是 T, P, E, Z, Y
```

参考man手册  


2021/5/4  
