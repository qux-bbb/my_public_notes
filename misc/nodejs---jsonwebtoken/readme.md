# nodejs---jsonwebtoken

## 简单信息
JSON Web Token (JWT)  
使用json形式的字符串完成身份认证，方便之后的数据交互  

项目地址：  
https://github.com/auth0/node-jsonwebtoken  


## 基本流程
本地发起请求，通过验证后得到一个token，这个token
存到本地，每次调用需要验证的功能时，就在头里加这个token发送请求  

服务器在接收到用户名密码，验证成功后，生成token发给客户端，后续接收请求后，如果需要验证，就获取请求头里的token，验证通过之后再执行相关逻辑  


## 简单代码示例
最简单的token生成方式，可选过期时间，这里设为1小时：  
```js
// jwt.sign(payload, secretOrPrivateKey, [options, callback])
var jwt = require('jsonwebtoken');
var token = jwt.sign({
  data: 'foobar'
}, 'secret', { expiresIn: '1h' });
```

验证：  
```js
// jwt.verify(token, secretOrPublicKey, [options, callback])
var decoded = jwt.verify(token, 'secret');
console.log(decoded.data) // foobar
```

更具体使用见项目地址  


---
2020/11/11  
