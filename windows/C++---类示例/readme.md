# C++---类示例

```cpp
// pointer to classes example
#include <iostream>
using namespace std;

class Rectangle {
	int width, height;
public:
	Rectangle(int x, int y) : width(x), height(y) {}
	int area(void) { return width * height; }
};


int main() {
	Rectangle obj(3, 4);
	Rectangle* foo, * bar, * baz;
	foo = &obj;
	bar = new Rectangle(5, 6);
	baz = new Rectangle[2]{ {2,5}, {3,6} };
	cout << "obj's area: " << obj.area() << '\n';
	cout << "*foo's area: " << foo->area() << '\n';
	cout << "*bar's area: " << bar->area() << '\n';
	cout << "baz[0]'s area:" << baz[0].area() << '\n';
	cout << "baz[1]'s area:" << baz[1].area() << '\n';
	delete bar;
	delete[] baz;
	return 0;
}
```

如果有默认构造函数（构造函数的每个参数都有值），比如 `Rectangle(int x=2, int y=1)...`  
那就可以这样声明 `Rectangle obj;`  

如果在delete之后，变量的作用域没有结束，最好手动设置空指针，比如在 `delete bar;` 之后添加 `bar=nullptr`  


参考链接: https://www.cplusplus.com/doc/tutorial/classes/  


2021/7/16  
