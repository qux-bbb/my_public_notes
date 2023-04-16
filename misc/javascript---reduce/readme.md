# javascript---reduce

reduce() 方法在数组的每个元素上执行由自己提供的reducer函数，从而产生单个输出值。  

JavaScript Demo: Array.reduce()  
```js
const array1 = [1, 2, 3, 4];
const reducer = (accumulator, currentValue) => accumulator + currentValue;

// 1 + 2 + 3 + 4
console.log(array1.reduce(reducer));
// expected output: 10

// 5 + 1 + 2 + 3 + 4
console.log(array1.reduce(reducer, 5));
// expected output: 15
```

原链接：https://developer.mozilla.org/en-US/docs/web/javascript/reference/global_objects/array/reduce  


2020/10/27  
