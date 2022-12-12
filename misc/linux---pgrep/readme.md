# linux---pgrep

pgrep 可以通过名字获取进程id，可能有多个id。  
和 pidof 相比，只输入名字的一部分也可以获取进程id。  

```r
# 搜索进程名，可以是名字的一部分
pgrep python
# 使用"--full"可以搜索包括参数的部分，可以简写为"-f"
pgrep --full hello.py
```


2022/7/18  
