# ubuntu---修改时区

使用 tzselect 命令选择想要调整到的时区，最后会生成一条命令，类似：  
```r
TZ='Asia/Shanghai'; export TZ
```
将此命令写入 `~/.profile` 文件中  

使时区更改生效：  
```r
source ~/.profile
```


2018/10/18  
