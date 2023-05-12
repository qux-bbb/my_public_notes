# 一些漏洞类型

```r
1.    SQL注入（包括url和表单输入，也就是get和post）
2.    弱口令  （要有一份好的字典）
3.    文件上传漏洞     （主要是上传的文件可以解析的问题）
    content-type更改（Content-Type: Multipart/form-data  把开头m大写）
                                
4.    文件包含 （现在只知道php:filter=）


如果是页面编辑，试试改编请求方式，比如GET改成POST，OPTIONS等等
```

2016/7/3  
