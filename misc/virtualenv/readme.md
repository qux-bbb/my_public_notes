# virtualenv

virtualenv是创建孤立的Python环境的工具

安装  
```r
pip install virtualenv
```

创建环境  
```r
virtualenv venv   # 这样会创建一个venv文件夹
```

指定Python版本创建环境（前提已经安装python3）  
```r
virtualenv -p /usr/bin/python3 venv
```

进入文件夹开启虚拟环境  
```r
source venv/bin/activate
```

退出虚拟环境  
```r
deactivate
```

---
**windows下不一样的地方**  
开启虚拟环境  
`your_env_dir\Scripts\activate`

---
**迁移**：  
virtualenv不能简单的复制迁移环境，迁移最好重新建一个虚拟环境，利用 `pip freeze > requirements.txt` 导出安装模块，`pip install -r requirements.txt`来搭建一个和原来一样的环境  
比这个更好的是自己手动管理一份requirements.txt  


---
**sudo**：  
如果要用到root权限，比如要用80端口，可以指定python具体路径，举例如下：  
`sudo venv/bin/python ./hello.py 0.0.0.0:80`  


---
2017/12/21  
