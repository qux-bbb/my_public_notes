# python---获取上个星期五的日期

```python
from datetime import datetime, timedelta
 
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']
 
# 距离指定日期或当前日期最近的指定星期
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    targe_date = start_date - timedelta(days=days_ago)
    return targe_date.strftime('%Y%m%d')
```

原链接: https://blog.csdn.net/weixin_34110749/article/details/87195543  


2019/4/13  
