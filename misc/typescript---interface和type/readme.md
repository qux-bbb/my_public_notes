# typescript---interface和type

## 简介
interface 和 type 基本一样，都可以用来声明类型，但有些许不同。  


## 扩展为新的interface或type
两者都可以扩展为新的interface或type，如下：  

扩展一个interface  
```typescript
interface Animal {
  name: string
}

interface Bear extends Animal {
  honey: boolean
}

const bear = getBear() 
bear.name
bear.honey
```

通过相加扩展一个type  
```typescript
type Animal = {
  name: string
}

type Bear = Animal & { 
  honey: Boolean 
}

const bear = getBear();
bear.name;
bear.honey;
```


## 更新已存在的interface或type
interface可以更新，增加新字段，但type不可以，如下：  

向已有interface添加新字段  
```typescript
interface Window {
  title: string
}

interface Window {
  ts: import("typescript")
}

const src = 'const a = "Hello World"';
window.ts.transpileModule(src, {});
```

type创建后无法更改  
```typescript
type Window = {
  title: string
}

type Window = {
  ts: import("typescript")
}

// Error: Duplicate identifier 'Window'.
```


## 总结
interface更灵活一点，建议尽可能使用interface。  
如果无法使用interface表达某种类型，比如需要使用并集或元组类型，那就需要使用type。  

官网链接：https://www.typescriptlang.org/docs/handbook/advanced-types.html#interfaces-vs-type-aliases  


---
2020/11/19  
