# python3---setuptools

setuptools用来处理包相关的东西, 功能有`构建`, `安装`, `卸载`, `开发`等  

示例:  
```python
# setup.py
from setuptools import setup, find_packages

setup(
    name='x_analyzer',
    version='0.1',
    packages=find_packages(),
    package_data={
        'x_analyzer': ['data/UserDB.TXT'],
    },
    author='hahaha',
    description='Analzyer for files and urls',
    long_description=open('README.md', 'r').read(),
    entry_points={
        'console_scripts': [
            'x_analyzer = x_analyzer.main:main',
        ],
    },
    install_requires=open('requirements.txt', 'r').read().split('\n'),
)
```

setup.py中的`packages=find_packages()`的作用和单独的`MANIFEST.in`文件类似  

`package_data`用于包含其他数据  

查看更多帮助:  
`python setup.py --help-commands`  

开发模式安装:  
`python setup.py develop`  


参考资料:  
https://www.jianshu.com/p/692bab7f8e07  
https://setuptools.readthedocs.io/en/latest/index.html  


2020/1/18  
