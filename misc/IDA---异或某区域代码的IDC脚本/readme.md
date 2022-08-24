# IDA---异或某区域代码的IDC脚本

```c
//encrypted.idc
//(c)  www.PEDIY.com 2000-2008

#include <idc.idc>
static decrypt(from, size, key ) { 
   auto i, x; 
   for ( i=0; i < size; i=i+1 ) { 
      x = Byte(from); 
      x = (x^key); 
      PatchByte(from,x); 
      from = from + 1;
   } 
 Message("\n" + "Decrypt Complete\n");
} 
```

来源: 《加密与解密》  


2019/9/15  
