# vs---判断文件是否存在

```cpp
#include <Windows.h>

BOOL IsFileExists(LPCWSTR filePath)
{
	WIN32_FIND_DATA FindFileData;
	HANDLE handle = FindFirstFile(filePath, &FindFileData);
	if (handle != INVALID_HANDLE_VALUE) {
		FindClose(handle);
		return TRUE;
	}
	else {
		return FALSE;
	}
}
```


20201211  
