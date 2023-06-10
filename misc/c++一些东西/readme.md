# c++一些东西

```
#include <vector>   相当于动态数组
push_back(i)   // 把 i 放到最后

--------------------------------------------------------------------------------
#include <deque>   两端都可以进出的队列

--------------------------------------------------------------------------------
一些输出格式
#include <iomanip>


setprecision  设置精度
float n = 133.4657864345;
cout << setprecision(8) << n << endl;
这样输出结果是  133.46578
也就是不带小数点总共输出8位

fixed  和setprecision配合可以设置小数部分位数
float n = 133.4657864345;
cout << fixed << setprecision(3) << n << endl;
这样输出结果是   133.466
也就是小数点后保留3位，四舍五入

setw  设置输出宽度
setfill  设置填充
char a[] = "hello";
cout << setfill('q')<< setw(10) << a << endl;
输出结果  qqqqqhello
```


2017/9/2  
