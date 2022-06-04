# python2---cgi简单使用

目录如下:  
```r
.
├── cgi-bin
│   └── friendsA.py
└── friends.htm
```

在当前目录执行命令:  
```r
chmod +x cgi-bin/friendsA.py
python -m CGIHTTPServer
```

在浏览器访问: `http://127.0.0.1:8000/friends.htm`  

相关源码  
friendsA.py  
```python
# coding:utf8

import cgi

reshtml = '''Content-Type: text/html\n\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Friends CGI Demo (dynamic screen)</title>
</head>
<body>
    <h3>Friends list for: <i>%s</i></h3>
    Your name is: <b>%s</b>
    <p>You have <b>%s</b> friends.</p>
</body>
</html>'''

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print(reshtml % (who, who, howmany))
```

friends.htm  
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Friends CGI Demo (static screen)</title>
</head>
<body>
    <h3>Friends list for: <i>NEW USER</i></h3>
    <form action="cgi-bin/friendsA.py">
        <b>Enter you Name:</b>
        <input type="text" name="person" value="NEW USER" size="15">
        <p>
            <b>How many friedns do you have?</b>
            <input type="radio" name="howmany" value="0" checked> 0
            <input type="radio" name="howmany" value="10" checked> 10
            <input type="radio" name="howmany" value="25" checked> 25
            <input type="radio" name="howmany" value="50" checked> 50
            <input type="radio" name="howmany" value="100" checked> 100
        </p>
        <input type="submit">
    </form>
</body>
</html>
```


2018/11/18  
