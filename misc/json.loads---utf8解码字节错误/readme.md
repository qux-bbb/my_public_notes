# json.loads---utf8解码字节错误

```r
Traceback (most recent call last):
  File "test.py", line 83, in <module>
    downloaderwithjunksoft.auto_analysis()
  File "test.py", line 55, in auto_analysis
    report = json.loads(myzip.open('report.json').read().decode())
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xed in position 42867937: invalid continuation byte
```

如果确定编码是utf8, 那就需要指定一下解码错误的处理方式, 如下:  
```python
report = json.loads(report_file.read().decode(errors='ignore'))
```

可以把编码也指定一下:  
```python
report = json.loads(report_file.read().decode(encoding='utf8', errors='ignore'))
```


2020/1/2  
