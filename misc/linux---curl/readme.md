# linux---curl

curl 是一个使用 url 发起请求, 获取响应的工具  
基础举例:  
```sh
curl https://www.baidu.com
```

-F 表单数据，默认使用 post 方式提交, 使用@可以提交文件, 举例:  
```sh
curl -F "file=@/home/hello/world.exe" -F "name=jack" -F "pass=love" https://helloworld.com/submit
```

-X 显式指定提交方式  
```sh
curl -X POST ...
```


2020/4/21  
