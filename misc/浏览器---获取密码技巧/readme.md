# 浏览器---获取密码技巧

这里只是一个思路，当你拿到一台电脑时，如果有谷歌或者火狐浏览器，很有可能保存了一些密码，这里简单说下如何提取密码  

谷歌，访问`chrome://settings/passwords`，可以看到保存密码的网站，如果有本地电脑密码，可以直接查看这些保存的密码，如果没有，可以通过访问对应登录页面，改表单的password属性获取密码  
火狐，在`隐私与安全`中找到`已保存的登录信息`，点击显示密码，即可得到密码。如果设置了主密码，需要输入主密码才能查看，这一点做的比谷歌好一点，在登录网站时，如果存有密码信息，就会提示输入主密码，然后会自动填充，打开浏览器只需要认证主密码一次，关闭浏览器再打开则需要重新认证主密码  


2018/6/3  
