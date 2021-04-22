# 字符串拼接拆分

## 普通字符版
```cpp
#include <string.h>
#include <stdio.h>

int main()
{
	char content[420] = { 0 };
	strcat_s(content, "hello");
	strcat_s(content, ",");
	strcat_s(content, "world");

	printf("%s\n", content);

	char *token;
	char * pt;
	token = strtok_s(content, ",", &pt);
	while (token != NULL) {
		printf("%s\n", token);
		token = strtok_s(NULL, ",", &pt);
	}

	return 0;
}
```

## 宽字符版
```cpp
#include <Windows.h>
#include <stdio.h>

int main()
{
	WCHAR content[420] = { 0 };
	lstrcat(content, L"hello");
	lstrcat(content, L",");
	lstrcat(content, L"world");

	wprintf(L"%s\n", content);

	wchar_t *token;
	wchar_t * pt;
	token = wcstok_s(content, L",", &pt);
	while (token != NULL) {
		wprintf(L"%s\n", token);
		token = wcstok_s(NULL, L",", &pt);
	}

	return 0;
}
```

## 参考链接
1. https://www.cplusplus.com/reference/cwchar/wcstok/
2. https://www.cplusplus.com/reference/cstring/strtok/


2021/4/22  
