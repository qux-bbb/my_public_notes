# javascript---find和filter

find: 找到一个符合条件的即可，返回元素  
filter: 找到所有符合条件的，返回list  

举例  
```js
aa = [
  {
    id: 1, name: 'hello'
  },
  {
    id: 2, name: 'world'
  },
  {
    id: 3, name: 'hello'
  },
]

console.log(aa.find(a => a.name === 'hello'))
console.log(aa.filter(a => a.name === 'hello'))
```

结果  
```r
{ id: 1, name: 'hello' }
[ { id: 1, name: 'hello' }, { id: 3, name: 'hello' } ]
```


2020/11/10  
