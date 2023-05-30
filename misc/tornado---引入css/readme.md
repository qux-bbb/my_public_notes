# tornado---引入css

main.py中设置  
```python
ROOT_DIR = os.path.split(os.path.realpath(sys.argv[0]))[0]
settings = {
    "static_path": ROOT_DIR + "/../css",
    }
```

html文件里设置  
```html
<link rel="stylesheet" type="text/css" href="{{static_url('all.css')}}">
```


2017/9/2  
