# 向程序添加资源文件并使用

向程序添加自定义类型的资源文件，取出使用  


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
	HRSRC hResource = FindResource(GetModuleHandle(NULL), MAKEINTRESOURCE(IDR_HELLO1), L"HELLO");
	//加载资源
	HGLOBAL hg = LoadResource(GetModuleHandle(NULL), hResource);
	//锁定资源
	LPVOID pData = LockResource(hg);
	//获取资源大小
	DWORD dwSize = SizeofResource(GetModuleHandle(NULL), hResource);

	printf("%s\n", pData);

	return 0;
}
```

编译执行就可以输出文件内容了  

不过这只是试出来的，不知道标准步骤是什么，暂时能用就行  


## 其它
各种资源类型: https://docs.microsoft.com/en-us/windows/win32/menurc/resource-types  

如果想获取dll中的资源，效果比较好的是直接获取模块句柄: `HMODULE helloModule = GetModuleHandle(L"hello.dll")`  
helloModule的值其实就是模块的加载地址，特征就是PE文件的开头: `MZ...`  


2021/4/17  
