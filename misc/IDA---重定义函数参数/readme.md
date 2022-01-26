# IDA---重定义函数参数

有时候恶意程序会设置不标准的传参方式，导致IDA识别函数参数错误。  
这时我们进到相关函数中，在函数名上右键选择"Set item type..."，然后可以重新定义函数的参数，下面是2个例子：  
```cpp
int __usercall call_about_RegSetValueExA@<eax>(int arg1@<ecx>, int arg2, int arg3)
char *__usercall dec_data@<eax>(unsigned int max_index@<edx>, int encrypted_data@<ecx>, int for_xor_bytes, int a4, int want_index)
```

建议修改前先备份原函数定义，以防万一。  


参考链接: https://www.hex-rays.com/products/decompiler/manual/interactive.shtml#08  


2022/1/26  
