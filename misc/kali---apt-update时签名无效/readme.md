# kali---apt-update时签名无效

执行 apt update 时，报错：  
```
下列签名无效： EXPKEYSIG ED444FF07D8D0BF6 Kali Linux Repository <devel@kali.org>
```

可以用下面的命令解决：  
```bash
wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add
```


2018/3/22  
