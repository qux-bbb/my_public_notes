# sizeof和strlen

sizeof和strlen都可以计算字符串长度

代码：  
```cpp
#include <Windows.h>
#include <stdio.h>


int main() {
	char theStr[] = "Hello\0World";
	
	int sizeofResult = sizeof(theStr);
	int strlenResult = strlen(theStr);

	printf("sizeofResult: %d\n", sizeofResult);
	printf("strlenResult: %d\n", strlenResult);

	return 0;
}
```

输出：  
```
sizeofResult: 12
strlenResult: 5
```

结论：  
sizeof 可计算包含0字节的字符串长度，计算长度会包含末尾0  
strlen 不可计算包含0字节的字符串长度，计算长度不包含末尾0  


2021/6/10  
