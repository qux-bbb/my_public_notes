# gdbgui

一个基于浏览器的gdb图形化前端，python实现，还行吧，起码有界面。  

官网: https://www.gdbgui.com  

官方建议的安装方法：  
```r
# 安装pipx(可以在隔离环境安装python应用)
python3 -m pip install --user pipx
python3 -m userpath append ~/.local/bin
# 用pipx安装gdbgui
pipx install gdbgui
```

升级和卸载：  
```r
# 升级
pipx upgrade gdbgui
# 卸载
pipx uninstall gdbgui
```

简单使用：  
```r
gdbgui --args ./test_program
```

&&&&&&& 有bug，好多数据都不显示，比如寄存器什么的  


2022/2/19  
