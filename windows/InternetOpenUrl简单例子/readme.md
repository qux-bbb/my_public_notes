# InternetOpenUrl简单例子

使用 InternetOpen、InternetOpenUrl、InternetReadFile 请求url，获取结果。  

```cpp
#include <stdio.h>
#include <windows.h>
#include <wininet.h>
#pragma comment(lib,"Wininet.lib")


int main()
{
	CHAR szUrl[] = "http://www.baidu.com/";
	//CHAR szUrl[] = "http://14.215.177.38";
	CHAR szAgent[] = "";
	HINTERNET hInternet1 =
		InternetOpen(NULL, INTERNET_OPEN_TYPE_PRECONFIG, NULL, NULL, NULL);
	if (NULL == hInternet1)
	{
		InternetCloseHandle(hInternet1);
		return FALSE;
	}
	HINTERNET hInternet2 =
		InternetOpenUrlA(hInternet1, szUrl, NULL, NULL, INTERNET_FLAG_NO_CACHE_WRITE, NULL);
	if (NULL == hInternet2)
	{
		InternetCloseHandle(hInternet2);
		InternetCloseHandle(hInternet1);
		return FALSE;
	}
	DWORD dwMaxDataLength = 4096;
	PBYTE pBuf = (PBYTE)malloc(dwMaxDataLength * sizeof(CHAR));
	if (NULL == pBuf)
	{
		InternetCloseHandle(hInternet2);
		InternetCloseHandle(hInternet1);
		return FALSE;
	}
	DWORD dwReadDataLength = NULL;
	BOOL bRet = TRUE;
	do
	{
		ZeroMemory(pBuf, dwMaxDataLength * sizeof(CHAR));
		bRet = InternetReadFile(hInternet2, pBuf, dwMaxDataLength, &dwReadDataLength);
		printf("%s", pBuf);
	} while (NULL != dwReadDataLength);

	free(pBuf);

	getchar();

	return 0;
}
```

原链接: https://www.cnblogs.com/likebeta/archive/2012/04/01/2428189.html  


2021/6/28  
