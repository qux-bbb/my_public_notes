flask的认证基本上就是自己写一个装饰器  

这是官方示例的装饰器代码:   
```python
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
```
来自: https://flask.palletsprojects.com/en/1.1.x/tutorial/views/#require-authentication-in-other-views  


下面是自己搜的资源：  
这是一个api认证的示例: https://github.com/ericsopa/flask-api-key  

这是既有用户名密码，也有token的认证示例: http://www.pythondoc.com/flask-restful/third.html  