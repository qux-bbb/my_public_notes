# vs---判断是否为文件夹

```cpp
#include <stdio.h>
#include <Windows.h>


BOOL IsDirectory(LPCWSTR thePath) {
	HANDLE hFind;
	WIN32_FIND_DATA FindFileData;
	hFind = FindFirstFile(thePath, &FindFileData);
	if (INVALID_HANDLE_VALUE == hFind)
	{
		wprintf(L"[!] 4. error to open the file %s: GetLastError=0x%08x\n", thePath, GetLastError());
		return FALSE;
	}
	if (FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
		return TRUE;
	return FALSE;
}

int main() {
	LPCWSTR thePath = L"D:\\files\\vs2019\\sources\\CRecovery\\Release";
	if (IsDirectory(thePath))
		printf("TRUE\n");
	else
		printf("FALSE\n");
	return 0;
}
```


2020/12/11  
