# python---随机1000必出5

```python
# coding:utf8

import random


class Random01:
    num_0_sum = 5
    num_1_sum = 995

    def get_num(self):
        if self.num_0_sum == 0 and self.num_1_sum == 0:
            self.num_0_sum = 5
            self.num_1_sum = 995
        r = random.randint(1, self.num_0_sum+self.num_1_sum)
        if r <= self.num_0_sum:
            self.num_0_sum -= 1
            return 0
        else:
            self.num_1_sum -= 1
            return 1

r01 = Random01()

f = open('result.txt', 'w')
for _ in range(1000):
    i = r01.get_num()
    f.write(str(i)+'\n')
f.close()
```


2019/11/25  
