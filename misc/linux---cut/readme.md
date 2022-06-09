# linux---cut

按列来切输入流或文件  

```r
# 切出第2列
cut -c 2 a.txt

# 切出第2,5-7列
cut -c 1,3-5 a.txt

# 按 “:” 切开，取第2部分
cut -d ":" -f 2 a.txt
```


2017/11/16  
