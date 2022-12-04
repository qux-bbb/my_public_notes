# 花指令示例

```r
.text:00425C8E 33 C0                   xor     eax, eax              ; Logical Exclusive OR
.text:00425C90 85 C0                   test    eax, eax              ; Logical Compare
.text:00425C92 74 03                   jz      short near ptr loc_425C96+1 ; Jump if Zero (ZF=1)
.text:00425C94 75 00                   jnz     short $+2             ; Jump if Not Zero (ZF=0)
.text:00425C96
.text:00425C96                         loc_425C96:                   ; CODE XREF: .text:00425C94↑j
.text:00425C96                                                       ; .text:00425C92↑j
.text:00425C96 E8 B8 44 01 00          call    near ptr byte_43A12C+27h ; Call Procedure
```

`75 00 E8` 永远不会执行，可以设置为 nop（0x90）  


2020/8/15  
