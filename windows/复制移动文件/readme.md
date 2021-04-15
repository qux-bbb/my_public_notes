复制移动文件api使用  

```c++
#include <Windows.h>
#include <stdio.h>


int main()
{
	LPCWSTR filePath = L"good.txt";
	LPCWSTR filePathCopied = L"good_copied.txt";
	LPCWSTR filePathMoved = L"good_moved.txt";
	CopyFile(filePath, filePathCopied, FALSE);  // TRUE 存在则失败, FALSE 存在则覆盖
	MoveFile(filePath, filePathMoved);

	getchar();

	return 0;
}
```


参考链接：  
1. https://docs.microsoft.com/en-us/previous-versions/ms959899(v=msdn.10)
2. https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-movefile


20210401  
