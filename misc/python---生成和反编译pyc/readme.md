# python---生成和反编译pyc

注意: 和python版本有关。  

## 生成pyc
```python
# 最终生成a.pyc
python -m a.py
```

## 反编译pyc
项目地址: https://github.com/rocky/python-uncompyle6  
pip安装  
`pip install uncompyle6`  
使用  
```r
# 可使用 -o 选项指定反编译结果的文件名
uncompyle6 a.pyc
```

opcode: `C:\Python27\Lib\opcode.py`  


2019/10/10  
