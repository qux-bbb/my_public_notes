# python---pipx

使用pipx可以在隔离环境安装运行python应用，避免依赖冲突问题。  

网站: https://pypa.github.io/pipx/  
github地址: https://github.com/pypa/pipx  

Windows安装：  
```r
python -m pip install --user pipx
# 确保可以直接在命令行中使用应用(不是自动补全，如果需要自动补全，需要把相应路径添加到path，如: C:\Users\hello\.local\bin)
pipx ensurepath
```

简单使用：  
```r
# 安装pycowsay
pipx install pycowsay
# 指定pip参数安装
pipx install pycowsay --pip-args="-i https://pypi.mirrors.ustc.edu.cn/simple"
# 运行(如果添加了path变量，可以直接pycowsay)
pipx run pycowsay "Hello"
```


2022/8/8  
