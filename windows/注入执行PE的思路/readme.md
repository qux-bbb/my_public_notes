# 注入执行PE的思路

## 思路1
仅适用dll，直接写入，然后用 LoadLibrary 启动  

## 思路2
适用exe或dll，手动映射(解析各节内容，加载导入表等)，然后创建远程线程执行  


---
2023/5/5  
