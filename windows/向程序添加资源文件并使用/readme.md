# 向程序添加资源文件并使用

向程序添加自定义类型的资源文件，取出使用  

解释一下FindResource的参数含义：  
```cpp
HRSRC FindResource(
  HMODULE hModule,        // 模块句柄
  LPCWSTR lpName,         // 资源名称
  LPCWSTR lpType          // 资源类型
);

// hModule：指定包含资源的模块的句柄。如果该参数为NULL，则默认搜索当前应用程序的模块。
// lpName：指定资源的名称。可以是一个整数ID，也可以是一个指向以NULL结尾的字符串的指针。
// lpType：指定资源的类型。可以是一个整数ID，也可以是一个指向以NULL结尾的字符串的指针。常见的资源类型包括RT_ICON、RT_BITMAP、RT_STRING等。
```


## 步骤
准备资源文件 greet.txt  
```
Hello World!
Good Morning!
```

使用VS2019创建控制台应用，可以把greet.txt放在项目文件夹中，以免丢失  

单击 "解决方案资源管理器"里的"资源文件"，右键 添加 -> 资源 -> 导入  
右下角把文件类型设置为`所有文件(*.*)`，找到greet.txt，打开，资源类型可以是任意字符串，确定保存即可  

代码这么写：  
```cpp
#include <stdio.h>
#include <Windows.h>
#include "resource.h"

int main() {
	// 参考: https://blog.csdn.net/weixin_30378623/article/details/98292897
	// 参数: 模块句柄, 资源ID, 资源类型
	HMODULE hModule = GetModuleHandle(NULL);
	HRSRC hResource = FindResource(hModule, MAKEINTRESOURCE(IDR_STRING1), L"STRING");
	//加载资源
	HGLOBAL hg = LoadResource(hModule, hResource);
	//锁定资源
	LPVOID pData = LockResource(hg);
	//获取资源大小
	DWORD dwSize = SizeofResource(hModule, hResource);

	printf("%s\n", pData);

	return 0;
}
```

编译执行就可以输出文件内容了  


## 其它
各种资源类型: https://docs.microsoft.com/en-us/windows/win32/menurc/resource-types  

如果想获取dll中的资源，效果比较好的是直接获取模块句柄: `HMODULE helloModule = GetModuleHandle(L"hello.dll")`  
helloModule的值其实就是模块的加载地址，特征就是PE文件的开头: `MZ...`  


2021/4/17  
