# React---设置环境变量

命令行设置  
```
REACT_APP_API_KEY='t0p53hellop1k3world3' npm start // For Linux/macOS Bash
($env:REACT_APP_API_KEY='t0p53hellop1k3world3') -and (npm start) // For Windows PowerShell
set REACT_APP_API_KEY='t0p53hellop1k3world3' && npm start // For Windows cmd.exe
```

在项目根目录创建 .env 文件，内容如下：  
```
# .env

REACT_APP_API_KEY=t0p53hellop1k3world3
```

使用：  
```js
const api_key = process.env.REACT_APP_API_KEY
```


2020/8/24  
