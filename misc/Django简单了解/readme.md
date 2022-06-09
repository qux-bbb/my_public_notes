# Django简单了解

Django是一个高级Python web框架。  

官网: https://www.djangoproject.com/  
官方文档: https://docs.djangoproject.com/zh-hans/3.2/contents/ (可以在右下角切换语言和版本)  


安装：  
```r
pip install Django
```

创建一个项目  
```r
django-admin startproject mysite
```

启动开发服务器  
```r
python manage.py runserver
```

创建应用  
```r
python manage.py startapp blog
```

项目和应用的区别：  
```r
应用程序是执行某些操作的Web应用程序，例如，博客系统，公共记录数据库或小型民意调查应用程序。
项目是特定网站的配置和应用程序的集合。

一个项目可以包含多个应用。一个应用可以位于多个项目中。
```

创建或更改数据库表  
```r
# 创建更改的文件
python manage.py makemigrations
# 将生成的py文件应用到数据库
python manage.py migrate
```

创建超级用户
```r
python manage.py createsuperuser
```

DRY, Dont Repeat Yourself  

先记住几个东西吧  
```r
urls.py     路由，把url导向具体的处理
views.py    视图，具体的处理逻辑
models.py   模型，数据库表相关的东西

templates文件夹 存放html文件，视图会用数据来渲染这些html文件
```


2018/11/25  
