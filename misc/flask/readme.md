flask是一个轻量级的python web框架。  

官网: https://palletsprojects.com/p/flask/  
github地址: https://github.com/pallets/flask  
文档: https://flask.palletsprojects.com/  

跟着教程做一遍，可以了解大概用法: https://flask.palletsprojects.com/en/1.1.x/tutorial/#tutorial  
写完的项目是这样的: https://github.com/pallets/flask/tree/1.1.2/examples/tutorial  


安装：  
```
pip install Flask
```

示例：  
```python
# coding:utf8

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

```
跟tornado挺像的  