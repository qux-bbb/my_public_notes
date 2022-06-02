# python3---bytes和hex字符串互转

keywords: 16进制字符串 bytes 转换  

```python
# bytes转hex
a = b"hello"
b = a.hex()
print(b)

# hex转bytes
c = bytes.fromhex(b)
print(c)
```

输出：  
```r
68656c6c6f
b'hello'
```


2019/12/1  
