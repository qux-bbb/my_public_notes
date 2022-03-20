# 打包python项目

keywords: python 模块 库 打包  

打包python项目：  
https://packaging.python.org/tutorials/packaging-projects/  

安装必要的工具：  
```r
python -m pip install --user --upgrade setuptools wheel
```

生成发布包：  
```r
python setup.py sdist bdist_wheel
```

安装上传包需要的工具：  
```r
python -m pip install --user --upgrade twine
```

在 https://pypi.org 注册账号  

上传自己的包：  
```r
python -m twine upload --repository pypi dist/*
```

完成  

如果要更新包，需要把原来的build/dist文件夹删除，修改setup.py中的version字段，然后按上述步骤重新操作一遍。  
pypi不允许版本号不变的修改。  

vscode的这个扩展可以帮助写docstring：autoDocstring  


2020/11/26  
