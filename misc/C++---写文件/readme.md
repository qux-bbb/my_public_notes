# C++---写文件

```cpp
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ofstream f("hello.txt", ios::out);
	if (f.fail()) {
		cout << "Error to open a file!\n";
		exit(0);
	}
	f << "Hello World!!!!!!!";
	f.close();
}
```

原链接: https://www.cnblogs.com/liaocheng/p/4371796.html  


2019/4/15  
