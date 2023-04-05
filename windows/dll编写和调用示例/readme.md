# dll编写和调用示例

keywords: 写dll  

## SampleDLL Project

SampleDLL.h  
```cpp
// File: SampleDLL.h
//
extern __declspec(dllexport) void HelloWorld();
```

SampleDLL.cpp  
```cpp
// SampleDLL.cpp

#include "pch.h"
#include "sampleDLL.h"

BOOL APIENTRY DllMain(HANDLE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved)
{
	switch (ul_reason_for_call)
	{
		case DLL_PROCESS_ATTACH:
		{
			// 加载的时候调一下看看效果，正常使用不需要
			HelloWorld();
			break;
		}

		case DLL_THREAD_ATTACH:
		case DLL_THREAD_DETACH:
		case DLL_PROCESS_DETACH:
			break;
	}
	return TRUE;
}

void HelloWorld()
{
	MessageBox(NULL, TEXT("Hello World"),
		TEXT("In a DLL"), MB_OK);
}
```

如果头文件里只是简单的函数声明而没有`extern __declspec(dllexport)`前缀, 那还可以使用.def文件来导出函数  

SampleDLL.def  
```r
LIBRARY "SampleDLL"

EXPORTS
   HelloWorld
```

上方的形式是按函数名导出，还可以设置其他形式：  
```r
# 按序号导出
   HelloWorld @2

# 按序号导出且没有名字
   HelloWorld @3 NONAME
```

注意：只有def文件声明的导出才能用rundll32.exe调用  
测试执行命令：  
```bat
:: ","后可以有空格
:: 随便给一个函数名都可以执行DllMain
rundll32.exe SampleDll.dll,WrongFunc
:: 调用HelloWorld函数
rundll32.exe SampleDLL.dll,HelloWorld
```


## SampleApp Project

方法1---动态调用  
SampleApp.cpp  
```cpp
// SampleApp.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <Windows.h>

typedef VOID(*DLLPROC) ();

int main()
{

	HINSTANCE hinstDLL;
	DLLPROC HelloWorld;
	BOOL fFreeDLL;

	hinstDLL = LoadLibrary(TEXT("SampleDLL.dll"));

	if (hinstDLL != NULL)
	{
	    // 以函数名的方式获取
		HelloWorld = (DLLPROC)GetProcAddress(hinstDLL, "HelloWorld");
		// 以序号的方式获取
		// HelloWorld = (DLLPROC)GetProcAddress(hinstDLL, MAKEINTRESOURCEA(1));

		if (HelloWorld != NULL)
			HelloWorld();

		fFreeDLL = FreeLibrary(hinstDLL);
	}
}
```

方法2---静态调用  
需要先将SampleDLL.h/SampleDLL.lib/SampleDLL.dll复制到SampleApp.cpp所在文件夹  
```cpp
#include <Windows.h>
#include "SampleDLL.h"
#pragma comment(lib,"SampleDLL.lib")


int main()
{
	if (HelloWorld != NULL)
		HelloWorld();
}

```

## 用法
分别编译两个项目，将编译生成的dll和exe放在同一目录下，执行exe即可  

直接看这个好了，是一个总的导入导出用法链接： https://docs.microsoft.com/en-us/cpp/build/importing-and-exporting?view=vs-2019  


参考资料:  
1. http://www.tutorialspoint.com/dll/dll_writing.htm
2. https://docs.microsoft.com/en-us/cpp/build/walkthrough-creating-and-using-a-dynamic-link-library-cpp?view=vs-2019
3. https://docs.microsoft.com/en-us/cpp/build/exporting-from-a-dll-using-def-files?view=vs-2019
4. https://docs.microsoft.com/en-us/cpp/build/exporting-from-a-dll-using-declspec-dllexport?view=vs-2019
5. https://docs.microsoft.com/en-us/cpp/build/exporting-functions-from-a-dll-by-ordinal-rather-than-by-name?view=vs-2019


2020/3/31  
