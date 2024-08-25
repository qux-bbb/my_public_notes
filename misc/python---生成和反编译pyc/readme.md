# python---生成和反编译pyc

注意: 和python版本有关。  


## 生成pyc
```python
# 最终生成a.pyc
python -m a.py
```


## 反编译pyc

### uncompyle6
项目地址: https://github.com/rocky/python-uncompyle6  
```r
# pip安装  
pip install uncompyle6

# 简单使用  
# 可使用 -o 选项指定反编译结果的文件名
uncompyle6 a.pyc
```

### decompyle3
项目地址: https://github.com/rocky/python-decompile3/  
根据uncompyle6重构的工具，解决了一些问题，适用于3.7-3.8的python字节码反编译  
```r
# 安装
pip install decompyle3

# 简单使用
decompyle3 a.pyc
```

### pycdc
项目地址: https://github.com/zrax/pycdc  
需要自己编译，如果在linux下编译，需要安装cmake、g++  
编译安装示例：  
```bash
sudo apt update
sudo apt install cmake g++ git
git clone https://github.com/zrax/pycdc.git
cd pycdc
cmake .
make
sudo make install
```

注意：如果有元素互换，反编译逻辑可能会出错，需要特别注意  


## opcode
C:\Python27\Lib\opcode.py  


---
2019/10/10  
