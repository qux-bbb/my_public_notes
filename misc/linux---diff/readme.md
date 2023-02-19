# linux---diff

diff 命令可以用来按行比较两个文件  
文件a.txt  
```r
i am a
hello
yes
xixi
```
文件b.txt  
```r
i am b
hello
no
xixi
```

比较结果：  
```r
└─$ diff a.txt b.txt
1c1
< i am a
---
> i am b
3c3
< yes
---
> no
```

```r
└─$ diff -u a.txt b.txt
--- a.txt       2023-02-19 19:05:15.208436100 +0800
+++ b.txt       2023-02-19 19:05:28.260234700 +0800
@@ -1,4 +1,4 @@
-i am a
+i am b
 hello
-yes
+no
 xixi
```


2016/5/22  
