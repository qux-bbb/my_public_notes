# linux---tr

tr, translate, 用来转换或删除字符，只处理标准输入  

### 替换
字符 a 替换成 c（-t 可省略）：  
```r
tr -t a c < a.txt
```
小写替换成大写：  
```r
tr [a-z] [A-Z] < a.txt
```


### 压缩
就是把 “aaa” 替换成“a”这样的操作：  
```r
tr -s a < a.txt
```


### 删除
删除所有a字符：  
```r
tr -d a < a.txt
```


### 填充
把所有不是a的字符填充为b：  
```r
tr -c a b < a.txt
```


---
2017/11/16  
