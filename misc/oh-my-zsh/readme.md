# Oh My Zsh

`Oh My Zsh` 是一个开源的管理zsh配置的工具，使终端显示更个性化，一些插件可提高使用效率(如自动预测命令)。  

github地址: https://github.com/robbyrussell/oh-my-zsh  

安装过程看github即可, 可以修改的配置文件: `~/.zshrc`  

现在用的主题: `ZSH_THEME="agnoster"`  
这些也不错：  
```r
bira
fino-time
fino
fox
gnzh
```

现在用的plugin：  
```r
plugins=(
    git
    zsh-autosuggestions  # 自动预测命令
    z  # 路径跳转，oh-my-zsh自带，启用即可，不需要安装
)
```

zsh-autosuggestions的github地址: https://github.com/zsh-users/zsh-autosuggestions  


修改之后可以重启终端，或使用该命令使修改生效：  
`source ~/.zshrc`  

手动更新：  
`omz update`  

卸载：  
`uninstall_oh_my_zsh`  


2019/11/7  
