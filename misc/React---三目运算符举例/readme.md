# React---三目运算符举例

```js
const notesToShow = showAll
  ? notes
  : notes.filter(note => note.important === true)
```

定义如下：  
```
const result = condition ? val1 : val2
```
解释如下：  
```
如果 condition 为真，则 result变量将设置为val1值。 如果 condition为 false，则result 变量将设置为 val2
```


2020/8/24  
