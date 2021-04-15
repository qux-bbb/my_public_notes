调试-->打开配置，如下添加参数：  
```json
"configurations": [
    {
        "name": "Python: Current File",
        "type": "python",
        "request": "launch",
        "program": "${file}",
        "args": [
            "-m",
            "spirit"
        ]
    },

```
例子加了2个参数： -m spirit  
参数需要用双引号  
