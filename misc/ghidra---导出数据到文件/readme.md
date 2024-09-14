# ghidra---导出数据到文件

Ghidra里没有比较方便的方法直接导出数据到文件，可以用python脚本实现。  

写了一个Ghidra用的脚本：  
https://github.com/qux-bbb/ghidra-scripts/blob/master/export_data_to_file.py  
可以直接用，下面内容可以不看  

核心就是指定数据起始位置和长度，这里根据使用场景给出4个代码示例。  

指定数据起始位置、长度：  
```python
# coding:utf8

data_start = 0x00400000
data_len = 0x40
filepath = "test_test_test_data"

data = getBytes(toAddr(data_start), data_len)

the_file = open(filepath, "wb")
the_file.write(data)
the_file.close()

```

指定数据起始位置、结束位置：  
```python
# coding:utf8

data_start = 0x00400000
data_end = 0x00400100
filepath = "test_test_test_data"

data_len = data_end - data_start
data = getBytes(toAddr(data_start), data_len)

the_file = open(filepath, "wb")
the_file.write(data)
the_file.close()

```

当前位置为起始地址、指定长度：  
```python
# coding:utf8

data_start = currentAddress
data_len = 0x40
filepath = "test_test_test_data"

data = getBytes(data_start, data_len)

the_file = open(filepath, "wb")
the_file.write(data)
the_file.close()

```

当前位置为起始地址、指定结束地址：  
```python
# coding:utf8

data_start = currentAddress
data_end = 0x00400100
filepath = "test_test_test_data"

data_len = data_end - data_start.getOffset()
data = getBytes(data_start, data_len)

the_file = open(filepath, "wb")
the_file.write(data)
the_file.close()

```


2023/3/21  
