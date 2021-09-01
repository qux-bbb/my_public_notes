# 获取磁盘大小

C盘大小：  
```cpp
#include <Windows.h>
#include <stdio.h>


int main()
{
	LPCSTR lpDirectoryName = "C:";
	LONG64 lpFreeBytesAvailable, lpTotalNumberOfBytes, lpTotalNumberOfFreeBytes;

	GetDiskFreeSpaceExA(lpDirectoryName, 
		(PULARGE_INTEGER)&lpFreeBytesAvailable, 
		(PULARGE_INTEGER)&lpTotalNumberOfBytes,
		(PULARGE_INTEGER)&lpTotalNumberOfFreeBytes);

	printf("lpTotalNumberOfBytes: %I64d\n", lpTotalNumberOfBytes);

	return 0;
}
```

所有盘大小：  
```cpp
#include <Windows.h>
#include <stdio.h>


int main()
{
	LONG64 totalBytes = 0;
	for (char i = 'C'; i <= 'Z'; i++) {
		char lpDirectoryName[3] = { i, ':', 0 };
		DWORD dwAttrib = GetFileAttributesA(lpDirectoryName);
		if (dwAttrib != INVALID_FILE_ATTRIBUTES) {
			LONG64 lpFreeBytesAvailable, lpTotalNumberOfBytes, lpTotalNumberOfFreeBytes;

			GetDiskFreeSpaceExA(lpDirectoryName,
				(PULARGE_INTEGER)&lpFreeBytesAvailable,
				(PULARGE_INTEGER)&lpTotalNumberOfBytes,
				(PULARGE_INTEGER)&lpTotalNumberOfFreeBytes);

			printf("%s lpTotalNumberOfBytes: %I64d\n", lpDirectoryName, lpTotalNumberOfBytes);
			totalBytes += lpTotalNumberOfBytes;
		}
	}
	printf("totalBytes: %I64d\n", totalBytes);

	return 0;
}
```


参考链接：  
1. https://www.tenouk.com/cpluscodesnippet/getdiskfreespacex.html
2. https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getdiskfreespaceexa
3. https://stackoverflow.com/questions/3828835/how-can-we-check-if-a-file-exists-or-not-using-win32-program