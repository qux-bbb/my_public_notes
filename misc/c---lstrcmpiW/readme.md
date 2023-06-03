# c---lstrcmpiW

keywords: 比较字符串  

```c++
#include "pch.h"
#include <iostream>
#include <Windows.h>

int main()
{
	LPCWSTR a = L"Hello";
	LPCWSTR b = L"World";
	LPCWSTR c = L"Hello";

	if (lstrcmpiW(a, b) == 0) {
		std::cout << "Yes\n";
	}
	else {
		std::cout << "No\n";
	}

	if (lstrcmpiW(a, c) == 0) {
		std::cout << "Yes\n";
	}
	else {
		std::cout << "No\n";
	}

}

```


2019/2/18  
