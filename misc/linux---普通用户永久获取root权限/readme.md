# linux---普通用户永久获取root权限

keywords: 获取sudo权限  

## 查看或验证是否有sudo权限
```bash
sudo -l -U alice
```

## 设置方法1：添加组
切换到root帐户：  
```bash
su -
```

添加到sudo组：  
```bash
/sbin/addgroup alice sudo
```

添加组的另一种命令：  
```bash
usermod -aG sudo alice
```

注销重新登录即可  


## 设置方法2：修改sudoers文件
建议通过visudo修改 /etc/sudoers 文件  
```bash
# 切换到root帐户
su -
# 执行visudo命令
visudo
```

在root下添加一行，如下：  
```conf
# User privilege specification
root    ALL=(ALL:ALL) ALL
alice    ALL=(ALL:ALL) ALL
```


## 参考链接
1. http://www.360doc.com/content/14/1206/00/17673261_430872230.shtml
2. https://zhuanlan.zhihu.com/p/640865629


---
2021/4/12  
