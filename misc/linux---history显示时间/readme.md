# linux---history显示时间

默认情况下history只会显示历史命令，并不会附带时间。  
可以通过设置环境变量或添加选项使其附带时间，不同shell会有差别。  


## sh和bash
sh和bash都可以通过设置环境变量的方式使history附带时间  
`HISTTIMEFORMAT='%F %T ' history`  
结果类似：  
`2021-08-11 07:34:26 ls`  


## zsh
zsh不能通过HISTTIMEFORMAT实现，有自己的风格。  

添加选项  
```zsh
history -E
# example: 11.8.2021 07:17  ls
history -i
# example: 2021-08-11 07:17  ls
history -t '%F %T'
# example: 2021-08-11 07:17:09  ls
```


参考链接：  
1. https://blog.csdn.net/evil_wdpp/article/details/91873771
2. https://www.cyberciti.biz/faq/unix-linux-bash-history-display-date-time/
3. https://unix.stackexchange.com/questions/103398/how-to-view-datetime-stamp-for-history-command-in-zsh-shell


2021/8/11  
