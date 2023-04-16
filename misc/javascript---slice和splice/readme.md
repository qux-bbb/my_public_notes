# javascript---slice和splice

slice: 切片  
splice: 铰接  

slice 和 splice 都可以用于添加或删除数组，前者不会改变原数组，后者会改变原数组。  

slice举例：  
```js
aa = [1, 2, 3]
bb = aa.slice(1)
console.log(aa)
console.log(bb)
```
结果：  
```r
[ 1, 2, 3 ]
[ 2, 3 ]
```

splice举例：  
```js
aa = [1, 2, 3]
bb = aa.splice(1)
console.log(aa)
console.log(bb)
```
结果：  
```r
[ 1 ]
[ 2, 3 ]
```

参考链接： https://www.w3school.com.cn/jsref/jsref_splice.asp  


2020/11/13  
