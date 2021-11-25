# python---str.format

```python
print('hello{},{}'.format('friend', 'keke,hehe'))
print('hello{1},{0},{1}'.format('first', 'second'))
print('hello{ok},{good}'.format(ok='nooooo', good='badddddd'))
```
结果：
```
hellofriend,keke,hehe
hellosecond,first,second
hellonooooo,badddddd
```

精致用法  
```python
print('0x{0:0>8x}'.format(197072))
# 0x000301d0

'''
解释一下
a = '0:0>8x'
a[0]: '0'表示位置，第0个位置，这里可以省略
a[1]: ':'就是分隔符，不会输出
a[2]: '0'表示填充字符，可以是任意单个字符
a[3]: '>'表示对齐方式，这里表示右对齐
a[4]: '8'表示长度为8
a[5]: 'x'表示小写16进制输出

'''
```
还是挺方便的  

以","分割的数字：  
```python
a = 12345678
b1 = format(a, ',')
b2 = '{:,}'.format(a)
print(b1)
print(b2)

# 12,345,678
```


官方链接: https://docs.python.org/2/library/stdtypes.html?highlight=format#str.format  


2019/11/25  
