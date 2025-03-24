# 字符串反分析

keywords: 逆向

虽然对最终反编译结果没有影响，但可以对自动化字符串搜索造成困扰


## 正常写法
```c
#include <stdio.h>


int main()
{
	char domain[] = "www.baidu.com";
	printf("%s", domain);
	return 0;
}
```

生成这样的汇编代码：
```asm
mov     eax, cs:dword_14001B4E8
lea     rdx, [rsp+48h+var_28]
movsd   xmm0, cs:qword_14001B4E0
lea     rcx, unk_14001B4F0
mov     dword ptr [rsp+48h+var_28+8], eax
movzx   eax, cs:word_14001B4EC
mov     word ptr [rsp+48h+var_28+0Ch], ax
movsd   qword ptr [rsp+48h+var_28], xmm0
call    sub_140001010
```

反编译为：
```c
strcpy(v4, "www.baidu.com");
sub_140001010(&unk_14001B4F0, v4, envp);
```


## 反分析写法
```c
#include <stdio.h>


int main()
{
	char domain[] = {'w', 'w', 'w', '.', 'b', 'a', 'd', 'i', 'u', '.', 'c', 'o', 'm', '\0'};
	printf("%s", domain);
	return 0;
}
```

生成这样的汇编代码：
```asm
mov     dword ptr [rsp+48h+var_28], 2E777777h
lea     rcx, unk_14001B4E0
mov     dword ptr [rsp+48h+var_28+4], 64696162h
mov     dword ptr [rsp+48h+var_28+8], 6F632E75h
mov     word ptr [rsp+48h+var_28+0Ch], 6Dh ; 'm'
call    sub_140001010
```

反编译为：
```c
strcpy(v4, "www.baidu.com");
sub_140001010(&unk_14001B4E0, v4, envp);
```


---
2025/3/24
