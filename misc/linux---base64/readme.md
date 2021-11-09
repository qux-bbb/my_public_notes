# linux---base64

字符串：  
```bash
# 加密
echo "hello" | base64
# 解密
echo "aGVsbG8K" | base64 -d
```

文件：  
```bash
# 加密
base64 a.txt
# 解密
base64 -d b.txt
```


2018/5/31  
