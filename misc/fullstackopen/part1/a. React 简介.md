### 创建一个名为 part1 的应用  
```
npx create-react-app part1
```

### 进入文件夹，启动应用  
```
npm start
```

### 一个最简单的 index.js  
```js
import React from 'react'
import ReactDOM from 'react-dom'

const App = () => (
  <div>
    <p>Hello world</p>
  </div>
)

ReactDOM.render(<App />, document.getElementById('root'))
```

上面用到了箭头函数，我们推荐用这种函数形式  

### 组件和调用示例（React 组件名称首字母必须大写）  
```js
const Hello = () => {
  return (
    <div>
      <p>Hello world</p>
    </div>
  )
}

const App = () => {
  return (
    <div>
      <h1>Greetings</h1>
      <Hello />
    </div>
  )
}

ReactDOM.render(<App />, document.getElementById('root'))
```

React 的核心理念，就是将许多定制化的、可重用的组件组合成应用。  
应用的组件树顶部都要有一个root 组件 叫做App。  

### 向组件传递数据  
```js
const Hello = (props) => {
  return (
    <div>
      <p>
        Hello {props.name}, you are {props.age} years old
      </p>
    </div>
  )
}

const App = () => {
  const name = 'Peter'
  const age = 10

  return (
    <div>
      <h1>Greetings</h1>
      <Hello name="Maya" age={26 + 10} />
      <Hello name={name} age={age} />
    </div>
  )
}
```

### React 组件的内容(通常)需要包含 一个根元素（div），可以用空代替  
```js
const App = () => {
  const name = 'Peter'
  const age = 10

  return (
    <>
      <h1>Greetings</h1>
      <Hello name="Maya" age={26 + 10} />
      <Hello name={name} age={age} />
      <Footer />
    </>
  )
}
```

### 打印到控制台（建议使用）  
```
console.log()
```
