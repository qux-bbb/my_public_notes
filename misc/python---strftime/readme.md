# python---strftime

keywords: 时间格式化  

```python
# coding:utf8

import time

print time.strftime('%Y-%m-%d %H:%M:%S')
# 2018-01-31 13:31:56
```

昨天  
```python
import datetime

def get_yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday.strftime('%Y%m%d')
```

今天|这周五|上周五  
```python
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

today = datetime.now()
this_friday = today + relativedelta(weekday=FR)
last_friday = today + relativedelta(weekday=FR(-1))

print 'today: ', today.strftime('%Y%m%d')
print 'this_friday: ', this_friday.strftime('%Y%m%d')
print 'last_friday: ', last_friday.strftime('%Y%m%d')
```

string时间转对象  
```python
start_day = datetime.datetime.strptime('2019-12-17', '%Y-%m-%d')
```

时间戳数字转格式化时间  
```python
import time

timeStamp = 1557502800
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)
# 2019-05-10 23:40:00
```


原链接: https://www.runoob.com/python3/python-timstamp-str.html  
