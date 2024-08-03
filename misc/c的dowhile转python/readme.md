# c的dowhile转python

python没有dowhile，可以用WhileTrue模拟，保持结构的一致性，避免转换出错。

C语言代码：
```c
#include <stdio.h>

int main() {
    int i = 0;
    do {
        printf("%d\n", i);
        i++;
    } while (i < 5);
    return 0;
}
```

python代码：
```python
i = 0
while True:
    print(i)
    i += 1
    if not (i < 5):
        break
```


2024/8/3
