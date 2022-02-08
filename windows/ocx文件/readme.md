# ocx文件

OCX, Object Linking and Embedding (OLE) Control Extension, 对象类别扩充组件  
包含关系(后者包含前者): ocx < dll < pe  

正常情况下导出表至少包含2项：  
```r
DllRegisterServer
DllUnregisterServer
```

可以使用regsvr32进行注册和取消注册。  


参考链接: https://baike.baidu.com/item/ocx/7155675  


2022/2/8  
