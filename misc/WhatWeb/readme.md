# WhatWeb

识别网站的ip、地域、使用的技术栈。  

官网: https://morningstarsecurity.com/research/whatweb  
github地址: https://github.com/urbanadventurer/WhatWeb  

最简单使用方法：  
```r
whatweb www.baidu.com
```

默认的请求有WhatWeb标识：  
```r
User-Agent: WhatWeb/0.5.5
```
可以指定User-Agent，如果指定为 `--user-agent ""`, User-Agent会变成"Ruby"  
举个指定的例子：  
```r
whatweb www.baidu.com --user-agent "Baiduspider+(+http://www.baidu.com/search/spider.htm)"
```


2017/9/2  
