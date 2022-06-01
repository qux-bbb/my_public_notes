# python---修改系统时间为一个月之前

其实用的是系统的 date 命令  
```python
def change_time():
    """
    修改时间为一个月之前
    """
    now_time = datetime.datetime.now()
    oneday = datetime.timedelta(days=1)
    the_time = now_time - oneday * 30
    the_time_str = the_time.strftime('%Y/%m/%d')
    print('change time to: {}'.format(the_time_str))
    os.system('date {}'.format(the_time_str))
```

2020/12/8  
