# python2---反斜杠x字符串转汉字

```python
def try_decode(argument):
    # '\xb5\xb1\xc7\xb0\xcf\xd4\xca\xbe\xa3\xba'
    try:
        return argument.decode("string-escape").decode('gbk')
    except:
        print('[!] decoding failure: %r' % argument)
        return argument

print(try_decode('\xb5\xb1\xc7\xb0\xcf\xd4\xca\xbe\xa3\xba'))
```

可能会是别的编码方式  


2020/9/21  
