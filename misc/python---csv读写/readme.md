# python---csv读写

```python
# coding:utf8

import csv

DATA = (
    (9, "Web Client and Servers", "base64, urllib"),
    (10, "Web Programming: CGI & WSGI", "cgi, time, wsgiref"),
    (13, "Web Services", "urllib, twython"),
)

print("*** WRITING CSV DATA")
f = open("bookdata.csv", "w", newline="")
writer = csv.writer(f)
for record in DATA:
    writer.writerow(record)
f.close()

print("*** REVIEW OF SAVED DATA")
f = open("bookdata.csv", "r")
reader = csv.reader(f)
for chap, title, modpkgs in reader:
    print("Chapter %s: %r (featuring %s)" % (chap, title, modpkgs))
f.close()
```

csv文件太大时，使用csv模块处理速度较慢，可自行读取文件解析，提高处理速度  


2018/12/1  
