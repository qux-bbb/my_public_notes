# 使用redux保存应用状态

redux可以用来全局保存应用状态  

安装依赖  
```
npm install redux
npm install react-redux
```

项目中和redux有关的文件：  
```
.
├── reducers
│   ├── blogReducer.js
│   ├── currentUserReducer.js
│   └── notificationReducer.js
└── store.js
```

不同的reducer提供各种信息的保存和修改方法  
store.js提供实例和状态的整合  

实际使用时，使用useSelecter获取状态，useDispatcher的实例dispatch方法来调用reducer提供的各种方法  


2020/11/9  
