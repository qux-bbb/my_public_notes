# javascript---uuid

用来创建一个随机的UUID  
github地址：https://github.com/uuidjs/uuid  

安装：  
```r
npm install uuid
```

使用：  
```js
// ES6 module syntax
import { v4 as uuidv4 } from 'uuid';
uuidv4(); // ⇨ '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d'
```

```js
// CommonJS syntax
const { v4: uuidv4 } = require('uuid');
uuidv4(); // ⇨ '1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed'
```


2020/11/19  
