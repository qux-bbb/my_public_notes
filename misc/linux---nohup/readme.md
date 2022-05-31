# linux---nohup

nohup, no hang up, 不挂起  
使用nohup可以在后台执行一个命令，即使用户退出也不影响，输出会重定向至nohup.out  

命令：  
```r
nohup python serve.py &
```

如果想把输出写入指定文件，可以使用重定向  
```r
nohup python serve.py > out.txt 2>&1 &
```


如果执行python脚本时，在nohup.out中看不到输出，应该是python输出的缓冲影响，可以通过`-u`参数取消python的输出缓冲，如下：  
```r
nohup python -u serve.py &
```


2017/11/16  
