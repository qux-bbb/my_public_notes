# 一个清理Neshta病毒的C语言脚本

```cpp
// Opening a File for Reading or Writing: https://docs.microsoft.com/en-us/windows/win32/fileio/opening-a-file-for-reading-or-writing
// GetFileSize function (fileapi.h): https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfilesize
// SetFilePointer function (fileapi.h): https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-setfilepointer
// 设置文件结尾：https://www.easefilter.com/kb/fileapi-setendOffile.htm
// wprintf: https://www.cplusplus.com/reference/cwchar/wprintf/
// FindFirstFileA function (fileapi.h): https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-findfirstfilea
// Listing the Files in a Directory: https://docs.microsoft.com/en-us/windows/win32/fileio/listing-the-files-in-a-directory
// C++SYSTEMTIME修改系统日期时间（非批处理）: https://blog.csdn.net/TweeChalice/article/details/96624308
// GetLocalTime function (sysinfoapi.h): https://docs.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlocaltime


#include <stdio.h>
#include <Windows.h>
#include <wchar.h>
#include <strsafe.h>
#include <locale.h> 


char virusSignature[] = { 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x25, 0x2c, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x28, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x24, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x20, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x1c, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x18, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x38, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x14, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x10, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x0c, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x08, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x04, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x48, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x44, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x40, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x54, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x50, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0x00, 0x51, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0xfc, 0x50, 0x41, 0x00, 0x8b, 0xc0, 0x53, 0x83, 0xc4, 0xbc, 0xbb, 0x0a, 0x00, 0x00, 0x00, 0x54, 0xe8, 0xa9, 0xff, 0xff, 0xff, 0xf6, 0x44, 0x24, 0x2c, 0x01, 0x74, 0x05, 0x0f, 0xb7, 0x5c, 0x24, 0x30, 0x8b, 0xc3, 0x83, 0xc4, 0x44, 0x5b, 0xc3, 0x8b, 0xc0, 0xff, 0x25, 0xf8, 0x50, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0xf4, 0x50, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0xf0, 0x50, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0xec, 0x50, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0xe8, 0x50, 0x41, 0x00, 0x8b, 0xc0, 0xff, 0x25, 0xe4, 0x50 };
LPCWSTR svchostComPath = L"C:\\Windows\\svchost.com";


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


// 是否有管理员权限 https://vimalshekar.github.io/codesamples/Checking-If-Admin
BOOL IsProcessElevated()
{
	BOOL fIsElevated = FALSE;
	HANDLE hToken = NULL;
	TOKEN_ELEVATION elevation;
	DWORD dwSize;

	if (OpenProcessToken(GetCurrentProcess(), TOKEN_QUERY, &hToken)) {
		if (GetTokenInformation(hToken, TokenElevation, &elevation, sizeof(elevation), &dwSize)) {
			fIsElevated = elevation.TokenIsElevated;
		}
		else {
			printf("[!] failed to get Token Information, GetLastError=0x%08x\n", GetLastError());
		}
	}
	else {
		printf("[!] failed to get Process Token, GetLastError=0x%08x\n", GetLastError());
	}

	if (hToken)
	{
		CloseHandle(hToken);
		hToken = NULL;
	}
	return fIsElevated;
}


BOOL IsInfectedFile(LPCWSTR filePath) {
	int filePathLen = lstrlen(filePath);
	if (filePathLen <= 4)
		return FALSE;
	if (lstrcmpi(&filePath[filePathLen - 4], L".exe") != 0)
		return FALSE;

	HANDLE hFile;
	hFile = CreateFile(filePath,               // file to open
		GENERIC_READ,          // open for reading
		FILE_SHARE_READ,       // share for reading
		NULL,                  // default security
		OPEN_EXISTING,         // existing file only
		FILE_ATTRIBUTE_NORMAL, // normal file
		NULL);                 // no attr. template

	if (hFile == INVALID_HANDLE_VALUE) {
		wprintf(L"[!] 1. error to open the file: GetLastError=%08x\n", GetLastError());
		return FALSE;
	}

	int theSize = GetFileSize(hFile, NULL);
	if (theSize <= 0xA200 || theSize > 10000000) {
		CloseHandle(hFile);
		return FALSE;
	}

	BYTE headBuffer[4] = { 0 };
	DWORD headBytesRead = 0;
	if (FALSE == ReadFile(hFile, headBuffer, 3, &headBytesRead, NULL)) {
		printf("[!] error to read the file: GetLastError=%08x\n", GetLastError());
		CloseHandle(hFile);
		return FALSE;
	}
	if (memcmp(headBuffer, "MZP", 3) != 0) {
		CloseHandle(hFile);
		return FALSE;
	}

	SetFilePointer(hFile,1000, NULL, FILE_BEGIN);
	BYTE theBuffer[0x100] = { 0 };
	DWORD dwBytesRead = 0;
	if (FALSE == ReadFile(hFile, theBuffer, 0x100, &dwBytesRead, NULL)) {
		printf("[!] error to read the file: GetLastError=%08x\n", GetLastError());
		CloseHandle(hFile);
		return FALSE;
	}
	if (memcmp(theBuffer, virusSignature, 0x100) != 0) {
		CloseHandle(hFile);
		return FALSE;
	}
	
	CloseHandle(hFile);
	return TRUE;
}


int RecoveryAnExe(LPCWSTR exePath) {
	HANDLE hFile;

	hFile = CreateFile(exePath,               // file to open
		GENERIC_READ | GENERIC_WRITE,          // open for reading and writing
		FILE_SHARE_READ,       // share for reading
		NULL,                  // default security
		OPEN_EXISTING,         // existing file only
		FILE_ATTRIBUTE_NORMAL, // normal file
		NULL);                 // no attr. template

	if (hFile == INVALID_HANDLE_VALUE) {
		wprintf(L"[!] 2. error to open the file %s: GetLastError=%08x\n", exePath, GetLastError());
		return 1;
	}

	int theSize = GetFileSize(hFile, NULL);

	SetFilePointer(hFile, theSize - 0xA200, NULL, FILE_BEGIN);

	DWORD dwBytesRead = 0;
	BYTE* theBuffer = (BYTE*)malloc((0xA210) * sizeof(BYTE));
	if (theBuffer == NULL) {
		printf("[!] error to malloc theBuffer: GetLastError=%08x\n", GetLastError());
		return 1;
	}
	if (FALSE == ReadFile(hFile, theBuffer, 0xA200, &dwBytesRead, NULL)) {
		printf("[!] error to read the file: GetLastError=%08x\n", GetLastError());
		CloseHandle(hFile);
		return 1;
	}

	int theOffset = 0xA200 - 0x9D2E;
	DWORD curNum;
	BYTE theByte;
	curNum = (theBuffer[theOffset+3] << 24) | (theBuffer[theOffset+2] << 16) | (theBuffer[theOffset+1] << 8) | theBuffer[theOffset];

	for (int i = 0; i < 1000; i++) {
		curNum = 0x8088405 * curNum + 1;
		theByte = (unsigned int)curNum * (unsigned __int64)0xFF >> 32;
		theBuffer[i] = (theBuffer[i] ^ theByte) & 0xFF;
	}
		

	SetFilePointer(hFile, 0, NULL, FILE_BEGIN);

	DWORD dwBytesWritten = 0;
	BOOL bErrorFlag = WriteFile(
		hFile,           // open file handle
		theBuffer,      // start of data to write
		0xA200,  // number of bytes to write
		&dwBytesWritten, // number of bytes that were written
		NULL);            // no overlapped structure

	if (bErrorFlag == FALSE)
	{
		wprintf(L"[!] error to write the file : %s GetLastError=%08x\n", exePath, GetLastError());
	}
	else {
		if (dwBytesWritten != 0xA200)
		{
			printf("[!] error: dwBytesWritten != dwBytesToWrite\n");
		}
		else
		{
			wprintf(L"[*] wrote 0x%x bytes to %s successfully.\n", dwBytesWritten, exePath);
		}
	}

	SetFilePointer(hFile, theSize-0xA200, 0, FILE_BEGIN);
	SetEndOfFile(hFile);
	CloseHandle(hFile);

	free(theBuffer);

	return 0;
}

int RecoveryFolderExes(LPCWSTR folderPath) {
	HANDLE hFind;
	WIN32_FIND_DATA FindFileData;
	wchar_t searchPath[MAX_PATH];
	StringCchCopy(searchPath, MAX_PATH, folderPath);
	StringCchCat(searchPath, MAX_PATH, TEXT("\\*"));

	hFind = FindFirstFile(searchPath, &FindFileData);

	if (INVALID_HANDLE_VALUE == hFind)
	{
		wprintf(L"[!] 3. error to open the file %s: GetLastError=%08x\n", folderPath, GetLastError());
		return 1;
	}

	do
	{
		if (wcscmp(FindFileData.cFileName, L".") == 0 || wcscmp(FindFileData.cFileName, L"..") == 0)
			continue;

		wchar_t newPath[MAX_PATH];
		StringCchCopy(newPath, MAX_PATH, folderPath);
		StringCchCat(newPath, MAX_PATH, L"\\");
		StringCchCat(newPath, MAX_PATH, FindFileData.cFileName);

		if (wcscmp(newPath, L"C:\\Windows") == 0 || wcscmp(newPath, L"C:\\Program Files") == 0)
			continue;

		if (FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
			RecoveryFolderExes(newPath);
		else {
			if (IsInfectedFile(newPath) && RecoveryAnExe(newPath) == 0)
				wprintf(L"    %s recoverd\n", newPath);
		}
	} while (FindNextFile(hFind, &FindFileData) != 0);

	return 0;
}

int RecoveryInfectedExes() {
	printf("[*] start recovering infected exe...\n");
	wchar_t buf[256] = { 0 };
	int usedLen = GetLogicalDriveStrings(sizeof(buf) / 2, buf);
	for (int i = 0; i < usedLen; i += 4)
	{
		buf[i + 2] = 0; // 清除 "\\"
		RecoveryFolderExes(&buf[i]);
	}
	printf("[*] all infected exe recovered.\n");
	return 0;
}

int ChangeYear(int addedYear) {
	SYSTEMTIME theSystemTime;
	GetLocalTime(&theSystemTime);

	theSystemTime.wYear += addedYear;
	SetLocalTime(&theSystemTime);
	printf("[*] change time to %04d/%02d/%02d\n", theSystemTime.wYear, theSystemTime.wMonth, theSystemTime.wDay);
	return 0;
}

int AboutSvchost() {
	if (IsFileExists(svchostComPath)) {
		DeleteFile(svchostComPath);
		CreateDirectory(svchostComPath, NULL);
		printf("[*] svchost.com: file deleted and folder created.\n");
	}
	return 0;
}


int DeleteReleatedFileAndFolder() {
	//    '%Temp%\\3582-490'
	//    '%Temp%\\tmp5023.tmp'
	//    'C:\\Windows\\directx.sys',
	//    'C:\\Windows\\svchost.com',
	wchar_t lpTempBuffer[MAX_PATH] = { 0 };
	DWORD dwRetVal = GetTempPath(MAX_PATH, lpTempBuffer);
	if (dwRetVal > MAX_PATH || (dwRetVal == 0))
	{
		printf("Failed to GetTempPath, GetLastError=0x%08x\n", GetLastError());
		return 1;
	}

	wchar_t tempPath1[MAX_PATH], tempPath2[MAX_PATH];
	StringCchCopy(tempPath1, MAX_PATH, lpTempBuffer);
	StringCchCat(tempPath1, MAX_PATH, L"3582-490");
	StringCchCopy(tempPath2, MAX_PATH, lpTempBuffer);
	StringCchCat(tempPath2, MAX_PATH, L"tmp5023.tmp");
	LPCWSTR thePaths[] = {
		tempPath1,
		tempPath2,
		L"C:\\Windows\\directx.sys",
		L"C:\\Windows\\svchost.com"
	};

	HANDLE hFind;
	WIN32_FIND_DATA FindFileData;
	for (int i = 0; i < 4; i++) {
		hFind = FindFirstFile(thePaths[i], &FindFileData);
		if (INVALID_HANDLE_VALUE == hFind)
		{
			//wprintf(L"[!] 4. error to open the file %s: GetLastError=0x%08x\n", thePaths[i], GetLastError());
			continue;
		}
		if (FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
			RemoveDirectory(thePaths[i]);
		else
			DeleteFile(thePaths[i]);
		wprintf(L"[*] %s removed\n", thePaths[i]);
		
	}

	return 0;
}

int RecoveryReg() {
	HKEY theKey;
	RegOpenKey(HKEY_CLASSES_ROOT, L"exefile\\shell\\open\\command", &theKey);
	RegSetValue(theKey, NULL, REG_SZ, L"\"%1\" %*", 7);
	RegCloseKey(theKey);
	printf("[*] exe open command registry entry reset.\n");
	return 0;
}

int main()
{
	if (IsFileExists(svchostComPath)) {
		if (IsProcessElevated()) {
			setlocale(LC_ALL, "chs");
			printf("[*] start cleaning...\n");
			ChangeYear(-1);
			AboutSvchost();
			RecoveryReg();
			RecoveryInfectedExes();
			DeleteReleatedFileAndFolder();
			ChangeYear(1);
			printf("[*] finished.");
		}
		else
			printf("[!] please run with administrator rights.\n");

	}
	else
		printf("[*] the computer is not infected.\n");

	printf("enter any key to exit.");
	char _ = getchar();
	return 0;
}
```


2020/12/11  
