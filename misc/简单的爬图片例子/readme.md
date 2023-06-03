# 简单的爬图片例子

说是爬图片的例子，其实也就是访问资源保存在本地，注意记得加 try except，防止中途崩溃  
requests.get中加入 timeout,防止因某资源请求不到消耗过多时间  
```python
# !python3
# coding:utf8

import requests
import re

# http://img.mmjpg.com/2017/1046/1.jpg
# 后来发现了问题，并不只是2017，，还有2016,2015，不过有顺序，所以直接找到分界点，分成三段就好了
# 851-1049	2017
# 486-850	2016
# 1-485		2015

# 加headers，绕过反爬虫机制
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
"Referer": "http://www.baidu.com",
}

url = "http://img.mmjpg.com/2015/"


for i in xrange(485,0,-1):
	print("#######################################################")
	print(i)
	res = requests.get("http://www.mmjpg.com/mm/" + str(i), headers=headers, timeout=5)
	try:
		maxnum = re.findall(r'(.{2})</a><em class="ch all" id="opic" onclick="openall\(1\);">全部图片</em>',res.content)[0]
	except Exception as e:
		pass
	print("num: " + maxnum)
	for j in range(1,int(maxnum)+1):
		imgurl = url + str(i) + "/" + str(j) + ".jpg"
		try:
			ires = requests.get(imgurl, headers=headers, timeout=5)
			img_name = str(i) + "_" + str(j) + ".jpg"
			open(img_name,"wb").write(ires.content)
			print(img_name)
		except Exception as e:
			pass
```

来个多线程的例子，理论上是可以的，有可能ip被封了，，  
```python
# !python3
# coding:utf8

import requests
import re
import threading

# http://img.mmjpg.com/2017/1046/1.jpg
# 后来发现了问题，并不只是2017，，还有2016,2015，不过有顺序，所以直接找到分界点，分成三段就好了
# 851-1049	2017
# 486-850	2016
# 1-485		2015

# 加headers，绕过反爬虫机制
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
"Referer": "http://www.baidu.com",
}

url = "http://img.mmjpg.com/"

def downImg(year, low_num, high_num):
	for i in xrange(low_num, high_num):
		print(i)
		try:
			res = requests.get("http://www.mmjpg.com/mm/" + str(i), headers=headers, timeout=3)
			maxnum = re.findall(r'(.{2})</a><em class="ch all" id="opic" onclick="openall\(1\);">全部图片</em>',res.content)[0]
		except Exception as e:
			pass

		for j in range(1,int(maxnum)+1):
			imgurl = url + str(year) + "/" + str(i) + "/" + str(j) + ".jpg"
			try:
				ires = requests.get(imgurl, headers=headers, timeout=3)
				img_name = str(i) + "_" + str(j) + ".jpg"
				open(img_name,"wb").write(ires.content)
			except Exception as e:
				pass


if __name__ == '__main__':
	t1 = threading.Thread(target=downImg, args=(2015, 1,486,))
	t2 = threading.Thread(target=downImg, args=(2016, 486,851,))
	t3 = threading.Thread(target=downImg, args=(2017, 851,1050,))
	t1.start()
	t2.start()
	t3.start()
	t1.join()
	t2.join()
	t3.join()
```


2017/9/2  
