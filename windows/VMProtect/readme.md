# VMProtect

官网：https://vmpsoft.com/  

VMProtect通过在一个非标准架构的虚拟机里执行程序，使软件很难被分析和破解。除此之外，VMProtect还有生成验证序列号，限制免费升级等功能。  

一个很厉害的虚拟机壳，可以在 吾爱破解 下载研究学习。  

## 简单使用
VMProtect的使用方式：  
1. 将相关的dll或其它库文件放到项目中
2. 在相关函数前后添加标志函数
3. 正常编译
4. 将编译后的文件用VMProtect打开，选择要保护的函数、资源等，编译即可

第3步生成的编译文件和第4步VMProtect编译后的文件即加壳前文件和加壳后文件  

VMProtect提供了各种版本的示例程序，可根据示例程序导入自己项目需要的dll或其它库文件  

## 一个例子
使用IDE：VS2017  

在Test.cpp同目录下放3个文件：  
```
VMProtectSDK.h
VMProtectSDK32.dll
VMProtectSDK32.lib
```

Test.cpp内容：  
```cpp
#include <stdio.h>
#include "VMProtectSDK.h"
#pragma comment(lib,"VMProtectSDK32.lib")

int main()
{
	VMProtectBegin("Hello");
	printf("Hello World!\n");
	return 0;
	VMProtectEnd();
}
```

选 Release x86，生成解决方案  

将生成的Test.exe使用VMProtect.exe打开编译即可，默认会生成Test.vmp.exe  


2021/4/25  
