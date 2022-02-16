# python---删除文件夹

```python
import os
import shutil

os.remove(path)  # 删除文件
os.removedirs(path)  # 删除空文件夹
os.rmdir(path)  # 删除空文件夹
shutil.rmtree(path)  # 递归删除文件夹，即：删除非空文件夹
```

原链接: https://blog.csdn.net/suibianshen2012/article/details/84303647  


2022/2/15  
