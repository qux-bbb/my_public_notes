# Shc

Shc, Shell Script Compiler, 把shell脚本转成elf可执行文件，其实只是做了一层包裹，运行时会把脚本解密执行。  

## 安装
ubuntu下安装shc：  
```r
sudo add-apt-repository ppa:neurobin/ppa
sudo apt-get update
sudo apt-get install shc
```

## 使用
假设脚本是hello.sh：  
```r
#!/usr/bin/bash
echo "Hello World"
```

生成elf文件：  
```r
shc -f hello.sh -o hello
```

## 获取原始脚本
有一个项目: https://github.com/yanncam/UnSHc, 但不支持4.0.3及以上shc生成的文件处理。  

可以用gdb调试。  
实际脚本位置特征如下(一般实际脚本的长度比较长)：  
```r
fcn.00001547(0x4232, 1);
fcn.00001547(0x420c, 0x24);  // 这里是实际的脚本位置，该函数执行之后，第一个参数指向的地址(这里是0x420c)就是脚本内容
fcn.00001547(0x4234, 0x13);
fcn.0000144e(0x4234, 0x13);
fcn.00001547(0x41d7, 0x13);
```
调试时需要注意有一个条件跳转需要断下修改ip寄存器以实现不跳过，或者修改flags寄存器(比较麻烦，还没成功过)  
```r
0x00001b57      cmp     dword [var_2ch], 0  ; 1. 在这里下断点，断下后修改eip为 0x00001b61
0x00001b5b      je      0x1c6b
0x00001b61      mov     esi, 1     ; int64_t arg2
0x00001b66      lea     rdi, [0x00004052] ; int64_t arg1
0x00001b6d      call    fcn.00001547
0x00001b72      movzx   eax, byte [0x00004052]
0x00001b79      test    al, al
0x00001b7b      jne     0x1b99
0x00001b7d      lea     rdi, [0x0000429e] ; int64_t arg1
0x00001b84      call    fcn.0000163b
0x00001b89      test    eax, eax
0x00001b8b      je      0x1b99
0x00001b8d      lea     rax, [0x0000429e]
0x00001b94      jmp     0x1e27
0x00001b99      mov     esi, 1     ; int64_t arg2
0x00001b9e      lea     rdi, [0x00004232] ; int64_t arg1
0x00001ba5      call    fcn.00001547
0x00001baa      mov     esi, 0x24  ; '$' ; int64_t arg2  ; 脚本长度
0x00001baf      lea     rdi, [0x0000420c] ; int64_t arg1  ; 实际脚本位置
0x00001bb6      call    fcn.00001547
0x00001bbb      mov     esi, 0x13  ; int64_t arg2  2. 在这里下断点，断下后rdi指向的地址就是脚本地址，esi是脚本长度
```
最后使用dump命令保存脚本：  
```r
dump memory hello_sh.raw $edi $edi+$esi
```

如果确定了一些要下断和处理的地址，用gdb脚本也很方便：  
```r
file hello
break *0x40125D
run
set $rip=0x0401267
break *0x04012B7
continue
dump memory hello_sh.raw $edi $edi+$esi
```


---
2022/6/28  
