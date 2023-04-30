# Heroku

## 简要信息

官方介绍  
Heroku是一个云平台，可让公司构建，交付，监控和扩展应用程序--这是从构思到URL的最快方法，绕过了所有基础架构难题。  

其实意思就是按它的方式打包上传，自动化部署网站。  

官网  
https://www.heroku.com/  


## 简单使用
下载安装：https://devcenter.heroku.com/articles/getting-started-with-nodejs#set-up  

在项目根目录创建配置文件 Procfile，内容如下，告诉 Heroku 如何启动应用：  
```
web: npm start
```

把项目用git初始化一下，并在本地提交，.gitignore需要忽略node_modules  

推到heroku，即可根据地址正常访问  
```
git push heroku master
```

强制重新部署：  
```
git push heroku HEAD:master --force
```


---
2020/10/26  
