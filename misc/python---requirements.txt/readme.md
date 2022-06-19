# python---requirements.txt

在 python 中，约定俗成将依赖模块信息保存在 requirements.txt 文件中(其它名字也可以)，内容举例如下：  
```r
black==22.3.0
Pillow==9.1.1
```

可以用 `pip freeze > requirements.txt` 生成 requirements.txt 文件，但最好手动管理  

如果需要根据不同系统指定不同依赖，可以使用 `platform_system` 指定，写成这种形式：  
```r
python-magic-bin==0.4.14;platform_system=="Windows"
python-magic==0.4.27;platform_system=="Linux"
```


参考链接: https://www.cnblogs.com/chnmig/p/12107199.html  


2022/6/19  
