# fzf

fzf is a general-purpose command-line fuzzy finder.  
主要优点是可以实时过滤显示。  

github地址: https://github.com/junegunn/fzf  

ubuntu安装：  
```r
sudo apt install fzf
```

使用示例：  
```r
# 最简单过滤，只能选中1条
fzf
# -m, --multi 按Tab可以向下选中或取消选中多条，Shift+Tab可以向上选
fzf -m
# 预览文件内容，可以结合其它查看文件内容的命令，内容多时可以鼠标滚轮翻动内容，文件列表也可以鼠标滚轮翻动
fzf --preview "cat {}"
# ESC 退出
```


信息来源: https://www.bilibili.com/read/cv28317849  


2023/12/7  
