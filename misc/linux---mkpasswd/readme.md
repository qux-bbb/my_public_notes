# linux---mkpasswd

mkpasswd可以生成shadow文件中保存的密码hash。  
密码hash一般格式为：  
```r
$<hash_type>$<salt>$<base64_hash_value>
```
使用 `man 5 crypt` 可以查看详细说明  

命令示例：  
```r
# 指定算法为md5，盐为12345678，密码为my_pass
mkpasswd --method=md5crypt --salt=12345678 my_pass
# $1$12345678$JklvlbDlb5LHHuzwbBK7f1
```


2022/6/29  
