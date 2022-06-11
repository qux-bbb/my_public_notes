# vscode---ssh配置证书认证

生成证书：  
```r
ssh-keygen -t rsa -b 4096
```

复制公钥（`C:\Users\your-user\.ssh\id_rsa.pub`）内容到服务器的 `~/.ssh/authorized_keys` 文件中，如果没有，就创建一个，要注意 authorized_keys 的文件权限应该是 600 或 700  

重启ssh服务：  
```r
sudo service ssh restart
```

vscode 连接：  
```r
ssh -i C:/Users/your-user/.ssh/id_rsa name@host
```

然后保存配置就好了  


参考：  
1. https://code.visualstudio.com/docs/remote/troubleshooting#_configuring-key-based-authentication
2. https://blog.csdn.net/u010417914/article/details/96918562


2020/7/7  
