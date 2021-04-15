最长公共子串 python实现 抄的  

```python
# coding:utf8
# python3

def find_lcsubstr(str1, str2):
    matrix = [[0 for i in range(len(str2)+1)]
         for j in range(len(str1)+1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    max_len = 0  # 最长匹配的长度
    p = 0  # 最长匹配对应在s1中的最后一位
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                matrix[i+1][j+1] = matrix[i][j]+1
                if matrix[i+1][j+1] > max_len:
                    max_len = matrix[i+1][j+1]
                    p = i+1
    return str1[p-max_len:p], max_len  # 返回最长子串及其长度


result = find_lcsubstr('abcdfg', 'abdfg')
print(result)

result = find_lcsubstr('hahshelloadfa', 'worldhello')
print(result)
```

原链接: https://blog.csdn.net/wateryouyo/article/details/50917812  
