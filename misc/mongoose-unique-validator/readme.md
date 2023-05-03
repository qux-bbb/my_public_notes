# mongoose-unique-validator

mongoose-unique-validator是一个插件，可为Mongoose模式中的唯一字段添加预保存验证。  

这使错误处理变得更加容易，因为当您尝试违反唯一约束时，您将得到一个Mongoose验证错误，而不是MongoDB中的E11000错误。  

github地址：  
https://github.com/blakehaswell/mongoose-unique-validator  

安装：  
```
npm install mongoose-unique-validator
```

使用示例：  
```js
var mongoose = require('mongoose');
var uniqueValidator = require('mongoose-unique-validator');

// Define your schema as normal.
var userSchema = mongoose.Schema({
    username: { type: String, required: true, unique: true },
    email: { type: String, index: true, unique: true, required: true },
    password: { type: String, required: true }
});

// Apply the uniqueValidator plugin to userSchema.
userSchema.plugin(uniqueValidator);
```


2020/10/29  
