# 汇编---test指令

test eax, ebx  
test会将一些标志位置为相应值，这里只关注ZF标志位  
eax 和 ebx 做与操作，如果结果为0，将ZF设为1，否则设为0  

```asm
mov eax, 0xA
test eax, eax
je 0x400000
```
test eax, eax 的结果不为零，所以后续不会跳转


2020/11/17  
