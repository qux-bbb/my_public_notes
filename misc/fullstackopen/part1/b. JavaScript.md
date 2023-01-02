JavaScript 标准的正式名称是ECMAScript  

### JavaScript 定义变量的方法  
```js
var x = 1
const y = 2
let z = 3
```
- var 是最古老的定义方式，不建议使用  
- const 实际上定义了一个常量，不能改变  
- let 定义的变量才是真正的变量  


### 数组和使用示例  
```js
const t = [1, -1, 3]

t.push(5)

console.log(t.length) // 4 is printed
console.log(t[1])     // -1 is printed

t.forEach(value => {
  console.log(value)  // numbers 1, -1, 3, 5 are printed, each to own line
})    
```
forEach 为数组中的每个元素调用了这个函数，并总是将这单个项作为参数传递。

在前面的示例中，使用了push方法将一个新元素添加到数组中。 在使用 React 时，经常使用函数式编程的技巧。 函数编程范型的一个特点，就是使用不可变的数据结构。 在React代码中，最好使用concat方法 ，因为它不向数组中添加元素，而是创建一个新数组，新数组中包含了旧数组和新的元素。  
```js
const t = [1, -1, 3]

const t2 = t.concat(5)

console.log(t)  // [1, -1, 3] is printed
console.log(t2) // [1, -1, 3, 5] is printed
```

map，对数组元素操作  
```js
const t = [1, 2, 3]

const m1 = t.map(value => value * 2)
console.log(m1)   // [2, 4, 6] is printed
```


### 对象
```js
const object3 = {
  name: {
    first: 'Dan',
    last: 'Abramov',
  },
  grades: [2, 3, 5, 3],
  department: 'Stanford University',
}
```

对象的属性可以使用“句点”号或括号进行引用  
```js
console.log(object1.name)         // Arto Hellas is printed
const fieldName = 'age' 
console.log(object1[fieldName])    // 35 is printed
```

可以使用句点符号或括号来动态地往对象中添加属性  
```js
object1.address = 'Helsinki'
object1['secret number'] = 12341
```


### 函数
**箭头函数**  
箭头函数的定义和使用  
```js
const sum = (p1, p2) => {
  console.log(p1)
  console.log(p2)
  return p1 + p2
}

const result = sum(1, 5)
console.log(result)
```

只有一个参数可去掉括号  
```js
const square = p => {
  console.log(p)
  return p * p
}
```

只包含一个表达式，可去掉大括号做精简  
```js
const square = p => p * p
```

精简的函数可以很方便地操作数组  
```js
const t = [1, 2, 3]
const tSquared = t.map(p => p * p)
// tSquared is now [1, 4, 9]
```

**function 函数**  
方式1  
```js
function product(a, b) {
  return a * b
}

const result = product(2, 6)
// result is now 12
```

方式2  
```js
const average = function(a, b) {
  return (a + b) / 2
}

const result = average(2, 5)
// result is now 3.5
```


### 类
简单了解  
```js
class Person {
  constructor(name, age) {
    this.name = name
    this.age = age
  }
  greet() {
    console.log('hello, my name is ' + this.name)
  }
}

const adam = new Person('Adam Ondra', 35)
adam.greet()

const janja = new Person('Janja Garnbret', 22)
janja.greet()
```
