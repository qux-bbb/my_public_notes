# ssh实现免密码登陆

keywords: 免密登录  

免密码登陆用到rsa的体系，具体说就是在服务器上放自己的公钥，用自己的私钥来通过认证  

操作方法：  
在本机执行2条命令：
```bash
ssh-keygen  # 生成自己的密钥对，为了不麻烦，直接回车使用默认选项就好
ssh-copy-id -i ~/.ssh/id_rsa.pub 服务器ip或域名
```
第二条命令适合远程主机的 `~/.ssh/authorized_keys` 不存在或文件中没有内容时使用，否则需要自己复制公钥内容添加到此文件中  
第二条命令的 -i 选项需要跟公钥路径，不过跟私钥路径也可以，ssh-copy-id会自己找对应的公钥  


注意：  
authorized_keys 的权限必须是 600 或 700 才能连接，否则会拒绝  
```bash
chmod 600 ~/.ssh/authorized_keys
```


20171208  
20210109 增加 -i 参数说明  
