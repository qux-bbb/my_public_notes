# pyc隐写工具---Stegosaurus

Stegosaurus可以在Python字节码（pyc或pyo）文件中隐藏信息。  
github地址: https://github.com/AngelKitty/stegosaurus  

要求python版本>=3.6, 测试3.10会报错  

使用示例：  
```r
# 测试可隐藏多少信息
python -m stegosaurus sample.py -r

# 隐藏信息，生成的__pycache__/sample.cpython-36-stegosaurus.pyc携带了隐藏的信息
python -m stegosaurus sample.py -s --payload "hello world"

# 提取信息
python -m stegosaurus __pycache__/sample.cpython-36-stegosaurus.pyc -x
```


2022/1/15  
