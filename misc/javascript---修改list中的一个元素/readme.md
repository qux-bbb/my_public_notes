# javascript---修改list中的一个元素

```js
const person = persons.find(p => p.name === args.name)
if (!person) {
  return null
}

const updatedPerson = { ...person, phone: args.phone }
persons = persons.map(p => p.name === args.name ? updatedPerson : p)
return updatedPerson
```

map很适合list逐个修改或更新的情形。  


2020/11/17  
