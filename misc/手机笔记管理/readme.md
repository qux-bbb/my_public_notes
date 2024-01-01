# 手机笔记管理

termux结合markor，不是那么方便，勉强可用。  

shell用了fishshell，所以在 ~/.config/fish/config.fish 最后加了这样的命令别名，方便切换目录和更新  
```r
# for note
alias n='cd /data/data/com.termux/files/home/storage/shared/termux_share/my-public-notes'
alias nu='cd /data/data/com.termux/files/home/storage/shared/termux_share/my-public-notes && git pull'
```

markor可以收藏笔记相应路径，查看或写笔记  

上传新写的笔记麻烦些，要命令行 git add commit push, 所以一般手机只是临时搜索查看笔记  


2023/6/22  
