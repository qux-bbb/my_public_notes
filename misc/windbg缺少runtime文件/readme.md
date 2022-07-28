windbg缺少runtime文件  

api-ms-win-crt-runtime-l1-1-0.dll  

```
自己在安装完windbg 10版本后出现了api-ms-win-crt-runtime-l1-1-0.dll字眼的错误，后搜索发现这个问题是因为缺少最新的CRT 导致。

解决的办法自己知道的目前有两个：

1. 安装 VS2015。
    https://www.microsoft.com/en-in/download/details.aspx?id=48145

2. 去官网上下载 此项更新 ：https://support.microsoft.com/zh-cn/kb/2999226 重启，就OK
--------------------- 
作者：k91191 
来源：CSDN 
原文：https://blog.csdn.net/k91191/article/details/53005276 
版权声明：本文为博主原创文章，转载请附上博文链接！
```
