# nodejs---morgan中间件

Node.js的HTTP请求记录器中间件  

https://github.com/expressjs/morgan  

example：  
```js
var express = require('express')
var morgan = require('morgan')

var app = express()

app.use(morgan('combined'))

app.get('/', function (req, res) {
  res.send('hello, world!')
})
```


2020/10/24  
