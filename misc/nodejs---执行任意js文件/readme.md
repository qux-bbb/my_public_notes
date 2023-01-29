# nodejs---执行任意js文件

keywords: 直接运行 javascript typescript js ts  

hello.js  
```js
console.log('Hello World!')
```

命令行执行：  
```r
node hello.js
```

typescript文件（比如hello.ts）不能直接运行，可以先用 `tsc hello.ts` 转译为javascript，然后再用上面的方式运行。  


2020/11/28  
