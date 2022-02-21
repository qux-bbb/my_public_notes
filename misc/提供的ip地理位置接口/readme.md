# 提供的ip地理位置接口

keywords: ip 位置  

## 淘宝
```r
http://ip.taobao.com/service/getIpInfo.php?ip=127.0.0.1
```

```php
public function getcountry()
{
    $ip = @file_get_contents("http://ip.taobao.com/service/getIpInfo.php?ip=".$this->ip);
    $ip = json_decode($ip,true);
    return $ip['data']['country'];
}
```

## 126
```r
http://ip.ws.126.net/ipquery
```

## sohu
```r
http://pv.sohu.com/cityjson
```

## ip138
```r
http://api.ip138.com/query/?datatype=string&callback=find&token=ec8b492b73763a2f8906aaf85d892872
```

## ipinfo.io
```r
https://ipinfo.io/json
```


---
2019/8/4  
