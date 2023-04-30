# nodejs---express

## 简介
快速，简单，极简的Node.js Web框架  
http://expressjs.com/  

安装：  
```
npm install express
```

## 举例
hello world例子  
app.js  
```js
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
```

运行：  
```
node app.js
```


## 其他
### 获取get参数
`req.query`  


### 获取post数据
需要使用express json-parser 设置json转换  
```
app.use(express.json());
```
然后用 `req.body` 即可  


---
2020/10/24  
