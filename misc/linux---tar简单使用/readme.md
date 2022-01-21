# linux---tar简单使用

tar用来打包、压缩、解压缩。  

```bash
# 打包，以 gzip 压缩   
tar -zcvf a.tar.gz a.txt   
# 查看tar中有哪些文件  
tar -ztvf a.tar.gz   
# 解压  
tar -zxvf a.tar.gz   
# 解压压缩包中指定文件
tar -zxvf a.tar.gz a_folder/b_folder/c.txt  
```

**缩写解释**    
```r
z  gzip，使用gzip  
v  verbose，显示更多信息  
f  file，文件名  
c  create，创建文件  
t  list，列出文件  
x  extract，提取文件  
```

**注意事项：**  
`-f` 选项一定要放在最后，tar的 `-f` 之后就要跟文件名  


---
2019/1/9  
