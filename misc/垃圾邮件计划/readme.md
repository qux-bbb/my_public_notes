# 垃圾邮件计划

```python
# coding:utf8

# 垃圾邮件计划
# 添加url就可以了吧，用的时候改下email

import requests

urls = ["http://passport2.chaoxing.com/num/emailcode?email="]
email = "1@q.com"


for url in urls:
	try:
		res = requests.get(urls + email)
		print(res.status_code)
	except Exception as e:
		continue
```


2018/7/22  
