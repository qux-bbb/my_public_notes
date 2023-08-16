# oledump

keywords: oletools  

oledump可以直接解析office文档，获取宏代码  

下载: https://blog.didierstevens.com/programs/oledump-py/  

python2、python3均可  
依赖olefile库: `pip install olefile`  

使用举例：  
```bat
:: 直接查看文件
python oledump.py hello.xls
:: 选择解析出的第2个目标进行查看
python oledump.py hello.xls -s 2
:: VBA解压缩(可以解压缩的前面有一个M字符)
python oledump.py hello.xls -s 2 -v
```


2019/11/19  
