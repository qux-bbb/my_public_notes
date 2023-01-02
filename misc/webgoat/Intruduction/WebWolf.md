## 0x01 Introducing WebWolf
启动webwolf命令：  
`java -jar webwolf-<<version>>.jar [--server.port=9090] [--server.address=localhost]`  
java8或者更高版本启动命令：  
`java --add-modules java.xml.bind -jar ar webwolf-<<version>>.jar [--server.port=9090] [--server.address=jar`  
默认在9090端口  
浏览器访问：http://127.0.0.1:9090/WebWolf  
使用webgoat账号登录  


## 0x02 Uploading files
可以上传文件，让其他人来访问  


## 0x03 Your own mailbox
&& 需要启动webwolf  
一个邮箱，webwolf可以收到邮件  
邮箱地址'@'前必须是当前登录用户名，才能发送成功  

我写的邮箱地址为：webgoat@qq.com  
在webwolf收到邮件，code为：taogbew，填入即完成  
(图标没变绿，大概是bug吧)  

## 0x04 Landing page
&& 需要启动webwolf  
在webgoat访问密码重置页面，随意输入密码提交  
在webwolf的Incoming requests中会看到请求内容，将code填入webgoat即完成  
