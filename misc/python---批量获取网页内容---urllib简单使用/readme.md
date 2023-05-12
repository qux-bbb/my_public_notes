# python---批量获取网页内容---urllib简单使用

```python
# -*- coding:utf-8 -*-
#! usr/bin/python

import urllib
url = "http://chinalover.sinaapp.com/web11/sql.php?id="
for i in range(1019,1030):
    wp=urllib.urlopen(url+str(i))
    print url+str(i)
    content=wp.read()
    print content
```


2016/5/29  
