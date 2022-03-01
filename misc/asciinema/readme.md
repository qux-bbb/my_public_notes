# asciinema

官网: https://asciinema.org  
github地址: https://github.com/asciinema/asciinema/  

轻量级的、基于文本的终端记录方式。支持Linux、macOS和*BSD。  

ubuntu安装使用示例：  
```r
# 安装
sudo apt install asciinema

# 记录
$ asciinema rec hello.cast
asciinema: recording asciicast to hello.cast
asciinema: press <ctrl-d> or type "exit" when you are done
$ echo hello
hello
$ whoami
alice
$ exit
asciinema: recording finished
asciinema: asciicast saved to hello.cast

# 播放
$ asciinema play hello.cast
$ echo hello
hello
$ whoami
alice
$ exit
```


2022/3/1  
