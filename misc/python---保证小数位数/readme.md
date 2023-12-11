# python---保证小数位数

```python

number_tuple = (
    123.456,
    123.4,
    123
)

for number in number_tuple:
    # 默认四舍五入
    formatted_number = "{:.2f}".format(number)
    print(formatted_number)

"""
123.46
123.40
123.00
"""
```

来源: chatgpt  


2023/12/11  
