# jest

## 简要信息
Jest是一个JavaScript测试框架，致力于简化测试。  

它适用于使用以下语言或框架的项目：Babel，TypeScript，Node，React，Angular，Vue等！  

官网  
https://jestjs.io/  

安装为开发依赖项  
```r
npm install --save-dev jest
```


## 官网示例
功能文件 sum.js  
```js
function sum(a, b) {
  return a + b;
}
module.exports = sum;
```

测试文件 sum.test.js   
```js
const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```

配置文件 package.json  
```json
{
  "scripts": {
    "test": "jest"
  }
}
```

测试命令  
```r
npm run test
```

指定描述或名称  
```r
npm run test -- -t 'hello'
```

指定测试文件名  
```r
# 这里需要注意文件路径不要用反斜杠
npm run test -- 'tests/blog_api.test.js'
```

还不清楚 `--` 代表什么  


2020/10/27  
