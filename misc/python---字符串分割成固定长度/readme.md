# python---字符串分割成固定长度

举例为2  
```r
import re

a = "hjhljkhjljlj"
b = re.findall(".{2}", a)
print(b)
# ['hj', 'hl', 'jk', 'hj', 'lj', 'lj']
```

原链接: https://blog.csdn.net/fengda2870/article/details/48657089  

2016/5/21  
