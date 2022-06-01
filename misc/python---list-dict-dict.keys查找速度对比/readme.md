# python---list,dict,dict.keys查找速度对比

结论:  
速度由快到慢为: dict, dict.keys, list  

相关代码和输出:  
```python
# coding:utf8

import time

aa = []
bb = {}
cc = set()
for a in range(10000):
    aa.append({
        'name': str(a),
        'value': a
    })
    bb[str(a)] = {
        'value': a
    }

# list
begin_time = time.time()
whatever = 0
for t in range(10000):
    for a in aa:
        if str(t) == a['name']:
            whatever = a['value']
            break
end_time = time.time()
print('list:')
print('    whatever: {}'.format(whatever))
print('    duration: {}'.format(end_time-begin_time))

# dict
begin_time = time.time()
whatever = 0
for t in range(10000):
    if str(t) in bb:
        whatever = bb[str(t)]['value']
end_time = time.time()
print('dict')
print('    whatever: {}'.format(whatever))
print('    duration: {}'.format(end_time-begin_time))

# dict.keys
begin_time = time.time()
whatever = 0
for t in range(10000):
    if str(t) in bb.keys():
        whatever = bb[str(t)]['value']
end_time = time.time()
print('dict.keys')
print('    whatever: {}'.format(whatever))
print('    duration: {}'.format(end_time-begin_time))
```

输出:  
```r
list:
whatever: 9999
duration: 16.9569997787
dict
whatever: 9999
duration: 0.00800013542175
dict.keys
whatever: 9999
duration: 1.89999985695
```


2020/3/9  
