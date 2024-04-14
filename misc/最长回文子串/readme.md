# 最长回文子串

一道简单的题目，只写了暴力解法和中点扩散解法。  


## 题目要求
```r
求一个字符串的最长回文子串

题目描述
给定一个字符串 s，找到 s 中最长的回文子串。​

示例1：​
输入: "babad"​
输出: "bab"​
注意: "aba"也是一个有效。​

示例2：​
输入: "cbbd"​
输出: "bb"​
```


## 简单粗暴解法
```python
"""
列举所有可能的字符串，逐个字符串判断是否为回文字符串，比较长度得到最长的回文字符串
"""


def is_palindrome_str(the_str):
    the_str_len = len(the_str)
    # 如果长度1，是回文字符串，后面的逻辑也可以处理这种情况，但这样更直接一点
    if the_str_len == 1:
        return True
    mid_len = the_str_len // 2
    for i in range(mid_len):
        if the_str[i] != the_str[-1 - i]:
            return False
    return True


def get_longest_palindrome_substr(raw_str):
    result_str = ""
    raw_str_len = len(raw_str)
    for i in range(0, raw_str_len):
        for j in range(i + 1, raw_str_len + 1):
            tmp_str = raw_str[i:j]
            if is_palindrome_str(tmp_str) and len(tmp_str) > len(result_str):
                result_str = tmp_str

    return result_str


raw_str_list = ["babad", "cbbd", "a", "abcba"]
for raw_str in raw_str_list:
    result_str = get_longest_palindrome_substr(raw_str)
    print(raw_str, result_str)

"""
babad bab
cbbd bb
a a
abcba abcba
"""
```


## 中点扩散
```python
"""
遍历每个位置
每个位置考虑奇数长度回文字符串和偶数长度回文字符串

找可能的奇数长度回文字符串
    当前字符作为中心字符，向左右扩展字符，当左右字符不一致时停止

找可能的偶数长度回文字符串
    初始状态没有字符，当前字符作为右边的字符，向左右扩展字符，当左右字符不一致时停止
"""


def get_longest_palindrome_substr(raw_str):
    result_str = ""
    raw_str_len = len(raw_str)
    if raw_str_len <= 1:
        return raw_str
    for i in range(0, raw_str_len):
        # 奇数长度字符串
        extend_num = 0
        while True:
            next_num = extend_num + 1
            if i - next_num < 0 or i + next_num >= raw_str_len:
                break
            if raw_str[i - next_num] != raw_str[i + next_num]:
                break
            extend_num = next_num
        tmp_str = raw_str[i - extend_num : i + extend_num + 1]
        if len(tmp_str) > len(result_str):
            result_str = tmp_str

        # 偶数长度字符串
        extend_num = 0
        while True:
            next_num = extend_num + 1
            if i - next_num < 0 or (i - 1) + next_num >= raw_str_len:
                break
            if raw_str[i - next_num] != raw_str[(i - 1) + next_num]:
                break
            extend_num = next_num
        tmp_str = raw_str[i - extend_num : i + extend_num]
        if len(tmp_str) > len(result_str):
            result_str = tmp_str

    return result_str


raw_str_list = ["babad", "cbbd", "a", "abcba"]
for raw_str in raw_str_list:
    result_str = get_longest_palindrome_substr(raw_str)
    print(raw_str, result_str)

```


---
2024/4/14  
