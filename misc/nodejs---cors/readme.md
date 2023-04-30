# nodejs---cors

Cross-origin resource sharing (CORS)是一种机制，它允许一个网页上受限制的资源(例如字体)，从提供一手资源的域名以外的另一个域名请求跨来源资源共享。 一个网页可以自由地嵌入跨来源的图片、样式表、脚本、 iframe 和视频。 默认情况下，同源安全策略禁止某些“跨域”请求，特别是 Ajax 请求。  

cors是nodejs的中间件，用来允许来自其他源的请求。  

安装cors  
```
npm install cors
```

使用中间件并允许来自所有来源的请求:  
```js
const cors = require('cors')

app.use(cors())
```


2020/10/25  
