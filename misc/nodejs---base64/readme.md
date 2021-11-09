# nodejs---base64

```javascript
let a = Buffer.from('JavaScript').toString('base64');
console.log(a);

let b = Buffer.from(a, 'base64').toString();
console.log(b);
```

原链接：https://stackoverflow.com/questions/246801/how-can-you-encode-a-string-to-base64-in-javascript/26514148#26514148  


2021/3/7  
