使用site.ip138.com获取ip的大致位置  

```python
# coding:utf8
# python3

import re
import requests


def get_ip_location(ip):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
    }

    url = 'https://site.ip138.com/{}/'.format(ip)

    res = requests.get(url, headers=headers)
    res_text = res.text

    # s = re.search(r'<h3>(.+)</h3>', res_text)
    # if s:
    #     print(s.group(1))

    s = re.search(r'data-location="(.+?)"', res_text)
    if s:
        return s.group(1)
    else:
        return None

ips = [
    '42.159.204.116',
    '110.242.68.3',
    '202.89.233.100',
    '199.96.62.21',
]

for ip in ips:
    result = get_ip_location(ip)
    print('{}: {}'.format(ip, result))
```