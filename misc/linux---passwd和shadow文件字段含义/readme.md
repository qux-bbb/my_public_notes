# linux---passwd和shadow文件字段含义

## passwd
/etc/passwd, 存储账户、密码等信息，每行都包含7个字段，以":"分隔。  
使用命令查看解释：  
```r
man 5 passwd
```

简单记录如下：  
```r
1. login name
2. optional encrypted password
    可能为空
    以"!"开头则表示密码锁定，无法登录
    如果值为"x"，则加密后的密码保存在shadow文件中
3. numerical user ID
4. numerical group ID
5. user name or comment field
6. user home directory
7. optional user command interpreter
    举例如: "/bin/bash"
```


## shadow
/etc/shadow, 存储账户、密码等信息，每行都包含9个字段，以":"分隔。  
使用命令查看解释：  
```r
man shadow
```

简单记录如下：  
```r
1. login name
    必须是一个有效的存在的账户名
2. encrypted password
    可能为空
    以"!"开头则表示密码锁定，无法登录
3. date of last password change
4. minimum password age
5. maximum password age
6. password warning period
7. password inactivity period
8. account expiration date
9. reserved field
    保留字段，以后用
```


2022/12/18  
