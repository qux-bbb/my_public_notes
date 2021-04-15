# linux---普通用户永久获取root权限

修改 `/etc/sudoers`, 在root下添加一行，如下：  
```conf
# User privilege specification
root    ALL=(ALL:ALL) ALL
alice    ALL=(ALL:ALL) ALL
```

原链接: http://www.360doc.com/content/14/1206/00/17673261_430872230.shtml  


2021/4/12  
