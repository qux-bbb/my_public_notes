# pyplot---正弦函数

安装模块：  
```r
pip install matplotlib
```

```python
# coding:utf8

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 7, 0.01)
y = np.sin(x)
plt.plot(x, y)
plt.savefig("out.png")
plt.show()

```


2019/10/29  
