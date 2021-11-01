# hosts

windows下的hosts文件可以指定域名解析的ip地址，优先级最高，且访问相关域名不会产生dns流量。  

## 位置和形式
位置: `C:\Windows\System32\drivers\etc\hosts`  

形式: 每行 `ip + 至少一个空格 + 域名`，'#'是注释符，举例：  
```r
# comment
1.2.3.4 hello.world.com
```

## 修改方式
因为权限问题，直接记事本打开修改hosts文件无法保存。  
可以将hosts文件复制到桌面，修改之后再覆盖到原位置；也可以使用vscode直接修改原文件，然后以管理员权限保存。  

为确保生效，可以在命令行执行 `ipconfig /flushdns` 刷新dns缓存。  

可使用 `ping` 命令确认是否生效，该修改对 `nslookup` 命令无效。  


---
2021/11/1  
