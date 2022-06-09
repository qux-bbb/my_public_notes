# linux---包含ip文件排序top10

## 0x00 问题描述
给一个文件，一行有三列：序号 ip url  ,中间用逗号分隔，比如：  
```r
1,1.1.1.1,hello World!
2,2.1.2.3,hello World!
3,2.1.3.3,hello World!
```
用linux命令找出访问数前10的ip  

## 0x01 问题分析
提取ip，排序，统计，再按出现次数多少排序，取出前10  

## 0x02 解决方法
比如文件名为a.txt  
命令：`cut -d ',' -f 2 a.txt | sort | uniq -c | sort -nr | head -10`  
解释：  
竖线就是用管道传输内容  
`cut -d ',' -f 2 a.txt`：提取每行的ip  
`sort`：对提取的ip排序，使相同的ip靠在一起  
`uniq -c`：统计每个ip出现次数（前提是相同ip需要靠在一起）  
`sort -nr`：-n是按照数字排序，-r是降序排列  
`head -10`：显示前10行  

## 0x03 生成测试文件脚本
```python
#coding:utf8

import random

str1 = ""

for i in range(1000):
	ip = str(random.randint(1,3)) + "." + str(random.randint(1,3)) + "." + str(random.randint(1,3)) + "." + str(random.randint(1,3))
	url = "hello World!"
	str1 += "%d,%s,%s\n"%(i, ip, url)

open("a.txt", 'w').write(str1)
```


---
2017/9/14  
