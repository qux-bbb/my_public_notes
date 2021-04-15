遍历磁盘输出所有路径  

```c++

// wprintf: https://www.cplusplus.com/reference/cwchar/wprintf/
// FindFirstFileA function (fileapi.h): https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-findfirstfilea
// Listing the Files in a Directory: https://docs.microsoft.com/en-us/windows/win32/fileio/listing-the-files-in-a-directory

#include <stdio.h>
#include <Windows.h>
#include <wchar.h>
#include <strsafe.h>

#define MAX_PATH 1024


int PrintAllPath(LPCWSTR folderPath) {

	HANDLE hFind;
	WIN32_FIND_DATA FindFileData;
	wchar_t searchPath[MAX_PATH];
	StringCchCopy(searchPath, MAX_PATH, folderPath);
	StringCchCat(searchPath, MAX_PATH, TEXT("\\*"));

	hFind = FindFirstFile(searchPath, &FindFileData);

	if (INVALID_HANDLE_VALUE == hFind)
	{
		printf("error to open the file: GetLastError=%08x\n", GetLastError());
		return 1;
	}

	do
	{
		if (wcscmp(FindFileData.cFileName, L".") == 0 || wcscmp(FindFileData.cFileName, L"..") == 0) {
			continue;
		}

		wchar_t newPath[MAX_PATH];
		StringCchCopy(newPath, MAX_PATH, folderPath);
		StringCchCat(newPath, MAX_PATH, L"\\");
		StringCchCat(newPath, MAX_PATH, FindFileData.cFileName);
		if (FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
			PrintAllPath(newPath);
		}
		else {
			wprintf(L"The file found is %s\n", newPath);
		}
	} while (FindNextFile(hFind, &FindFileData)!=0);

	return 0;
}


int main() {

	wchar_t buf[256] = { 0 };
	int usedLen = GetLogicalDriveStrings(sizeof(buf)/2, buf);
	for (int i = 0; i < usedLen; i+=4)
	{
	    buf[i + 2] = 0; // 清除 "\\"
		//wprintf(L"%s\n", &buf[i]);
		PrintAllPath(&buf[i]);
	}
	
	return 0;
}
```


20201211  
