# fishshell

官网: https://fishshell.com/  

fishshell和zsh类似，都比传统shell有更好的交互体验。  

ubuntu安装: `sudo apt install fish`  

fishshell自带命令预测功能。  
`Ctrl + F` 补全预测，`Alt + F` 接受部分预测，`F` 也可用右箭头代替  

fish配置文件路径: `~/.config/fish/config.fish`, 没有的话可以自己创建一个  

默认的主题不大好看，使用 `fish_config` 命令可以在浏览器以图形化方式配置主题，修改后记得点 `set *` 按钮保存  


## oh-my-fish
github地址: https://github.com/oh-my-fish/oh-my-fish  

oh-my-fish和oh-my-zsh类似，提供主题和插件管理功能  
安装: `curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish`  
使用 `omf search` 搜索插件，使用 `omf install` 安装插件  

安装切换路径插件 `z`: `omf install z`  
(autojump插件装完还得自己设置，这个更方便一点，一条命令搞定)  


## 添加命令别名
编辑 ~/.config/fish/config.fish, 在最后添加类似内容：  
```r
alias lll='ls -lha'
```


## 参考链接
https://kxcblog.com/post/terminal/1.fish-tutorial/  


---
2021/11/28  
