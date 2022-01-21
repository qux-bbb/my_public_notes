# linux---获取文件全路径

keywords: 绝对路径  

```sh
# readlink方法
readlink -f test.txt

# PWD方法
ls $PWD/test.txt
```

个人感觉第一种方法比较好  

原链接：https://www.aliyun.com/jiaocheng/123148.html  


2019/9/30  
