# dns---svchost

本来想通过火绒剑监控 DNS 请求，来定位相应进程的，但发现 DNS 请求都是从 svchost.exe 发出的。  

这是因为在 Windows 上，大多数 DNS 查询是由托管在 svchost.exe 中的 DNS 客户端服务进行的，所以通过 DNS 请求无法定位到相应进程。  

```r
服务名称 Dnscache
显示名称 DNS Client
启动类型 自动
执行命令 C:\Windows\system32\svchost.exe -k NetworkService
```

ping 一个域名，DNS 请求由 svchost.exe 发出  
nslookup 一个域名，DNS请求由 nslookup.exe 发出  


参考链接: https://social.technet.microsoft.com/Forums/en-US/074b50b5-f3e9-4302-951a-e335f0f838c4/dns-lookup-investigation  


2021/6/10  
