# de4dot

de4dot是一个.NET程序反混淆工具，已经很久不维护了。  

github地址: https://github.com/de4dot/de4dot  


## 获取可执行文件方法
fork代码，在 .github/workflows/build.yml 添加"workflow_dispatch"，前后对比如下：  
```r
name: GitHub CI
on:
  push:
    branches:
```

```r
name: GitHub CI
on:
  workflow_dispatch:
  push:
    branches:
```

这样就可以在 Actions 页面手动运行workflow，运行之后在 Artifacts 下方可以看到生成的文件：  
```r
de4dot-net35
de4dot-net45
de4dot-netcoreapp2.1
de4dot-netcoreapp3.1
```

我下载的是 de4dot-net45  

其实任意代码提交都会触发build逻辑，README.md随便改点什么都可以  


---
2023/11/20  
