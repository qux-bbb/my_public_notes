# VEH简单示例

VEH: Vectored Exception Handling 向量化异常处理  

```cpp
#include <Windows.h>
#include <stdio.h>

int b = 0;

long _stdcall ExceptionHandle(PEXCEPTION_POINTERS val) {
	//// 恶意代码经常会利用VEH来修改Eip，跳转到要执行的函数去
	//val->ContextRecord->Eip = 0x00402233;
	b = 1;
	MessageBoxA(NULL, "changed b", "change", MB_OK);
	return EXCEPTION_CONTINUE_EXECUTION;
}

#pragma optimize("", off)
int main() {
	AddVectoredExceptionHandler(1, ExceptionHandle);
	printf("a = 2 / 0;\n");
	b = 0;
	int a = 2 / b;
	printf("a: %d\n", a);
	printf("b: %d\n", b);
	getchar();

	return 0;
}
#pragma optimize("", on)
```

结果为：  
```r
a = 2 / 0;
a: 2
b: 1
```

参考链接: https://www.bilibili.com/video/BV1wS4y1m7c3  


2022/4/28  
