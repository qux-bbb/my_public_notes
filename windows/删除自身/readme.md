# 删除自身

DeleteFile api不能删除自身，因为被占用，但用ShellExecuteA执行删除的命令可以把自身删掉。  

```cpp
#include <Windows.h>
#include <stdio.h>

int main() {

	// 获取当前程序名称
	char exeFilePath[100 + 1] = { 0 };
	GetModuleFileNameA(GetModuleHandle(NULL), exeFilePath, 100);

	char commandStr[101] = { 0 };
	// sprintf不安全，所以用sprintf_s
	sprintf_s(commandStr, "/C DEL /F /Q %s >> NUL", exeFilePath);

	ShellExecuteA(NULL, "open", "cmd.exe", commandStr, NULL, SW_HIDE);

	return 0;
}
```


参考链接: https://blog.csdn.net/qq_43080331/article/details/83506474  


2021/6/3  
