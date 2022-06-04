# python---根据dict成员对list排序

```python
# coding:utf8

score_dict = [
    {
        "name": "a",
        "score": "55"
    },
    {
        "name": "b",
        "score": "33"
    },
    {
        "name": "c",
        "score": "99"
    },
]

score_dict.sort(key=lambda t: t["score"])
print(score_dict)
```

结果：  
```r
[{'name': 'b', 'score': '33'}, {'name': 'a', 'score': '55'}, {'name': 'c', 'score': '99'}]
```

2019/7/12  
