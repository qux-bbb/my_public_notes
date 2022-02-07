# GetKeyboardLayout获取国家地区信息

返回值解释  
The return value is the input locale identifier for the thread. The low word contains a Language Identifier for the input language and the high word contains a device handle to the physical layout of the keyboard.  

```r
+---------------+----------------+---------------------+
| device handle | SubLanguage ID | Primary Language ID |
+---------------+----------------+---------------------+
31           16 15           10  9                     0   bit
```

举例：  
```cpp
#include <Windows.h>
#include <stdio.h>

int main()
{
	HKL inputLocaleIdentifier = GetKeyboardLayout(NULL);

	WORD languageIdentifier = (DWORD)inputLocaleIdentifier & 0xffff;
	BYTE primaryLanguageID = languageIdentifier & 0xff;

	printf("%d\n", primaryLanguageID);
	return 0;
}
```

参考链接：  
1. https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeyboardlayout
2. https://docs.microsoft.com/en-us/windows/win32/intl/language-identifiers
3. https://docs.microsoft.com/en-us/windows/win32/intl/language-identifier-constants-and-strings
4. https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/70feba9f-294e-491e-b6eb-56532684c37f 可以下载详细对应关系


2022/2/6  
