# python---解析单独的.net资源文件

安装模块：  
```r
pip install pythonnet
```

使用dnspy.Console.exe反编译.net文件，得到资源文件  

解析资源文件示例  
```python
import clr  # 引入clr才可以使用System模块
from System.Resources import ResourceReader

res = ResourceReader('a/b/files.resources')
the_dict = res.GetEnumerator()
while the_dict.MoveNext():
    data = None
    dataType = None
    _, dataType, data = res.GetResourceData(the_dict.Key, dataType, data)
    print(the_dict.Key)
    real_data = bytes(data)[4:]  # 前4位表示数据总长度
```

参考链接：  
1. https://docs.microsoft.com/zh-cn/dotnet/api/system.resources.resourcereader?view=net-6.0
2. https://pythonnet.github.io
3. https://github.com/pythonnet/pythonnet/wiki/Troubleshooting-on-Windows,-Linux,-and-OSX


2022/3/4  
