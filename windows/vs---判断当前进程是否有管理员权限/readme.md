# vs---判断当前进程是否有管理员权限

```c
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
			printf("Failed to get Token Information, GetLastError=0x%08x\n", GetLastError());
		}
	}
	else {
		printf("Failed to get Process Token, GetLastError=0x%08x\n", GetLastError());
	}

	if (hToken)
	{
		CloseHandle(hToken);
		hToken = NULL;
	}
	return fIsElevated;
}
```

原链接：https://vimalshekar.github.io/codesamples/Checking-If-Admin  


20201209  
