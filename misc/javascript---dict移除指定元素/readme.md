# javascript---dict移除指定元素

```js
const aa = {
  hello: 'hello',
  world: 'world'
}

const removeHello = (object) => {
  const {hello, ...rest} = object
  return rest
}

console.log(removeHello(aa))
```

原链接：https://stackoverflow.com/questions/56155922/how-to-delete-property-from-spread-operator  


2020/11/5  
