# VS---宽字符串和普通字符串声明

keywords: visual studio 宽字符 unicode(虽然是个错的关键字)  

LPCSTR 类型为`const char *`  
LPCWSTR 类型为`const wchar_t *`  

还有其它的类型，暂时没用到，现在这些就够用了  

举个例子：  
```cpp
#include <stdio.h>
#include <Windows.h>
#include <tchar.h>


int main() {
	LPCSTR a = "hello";
	LPCWSTR b = L"hello";
	puts(a);
	_tprintf(b);
	return 0;
}
```

LPCSTR拆分解释  
LP: Long Pointer, Long型指针  
C: Constant, 常量  
STR: String, 字符串  

LPCWSTR拆分解释  
LP: Long Pointer, Long型指针  
C: Constant, 常量  
WSTR: Wide character String, 宽字符串  

参考链接：https://www.codeproject.com/articles/76252/what-are-tchar-wchar-lpstr-lpwstr-lpctstr-etc  


20201210  
20201227 增加拆分解释  
