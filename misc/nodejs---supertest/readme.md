# nodejs---supertest

https://github.com/visionmedia/supertest  

用来测试http api  

安装为开发依赖  
```
npm install supertest --save-dev
```

使用示例  
```js
const request = require('supertest');
const express = require('express');

const app = express();

app.get('/user', function(req, res) {
  res.status(200).json({ name: 'john' });
});

request(app)
  .get('/user')
  .expect('Content-Type', /json/)
  .expect('Content-Length', '15')
  .expect(200)
  .end(function(err, res) {
    if (err) throw err;
  });
```


2020/10/28  
