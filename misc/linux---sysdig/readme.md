# linux---sysdig

github地址: https://github.com/draios/sysdig  

Sysdig是linux系统下的进程监控工具，类似Windows的Process Monitor。  
Csysdig是curses版本的Sysdig，提供方便使用的UI。  

可以用Sysdig来捕获信息，Csysdig来查看过滤信息。  

ubuntu安装：  
```bash
sudo apt install sysdig
```

一些命令：  
```bash
# 直接运行sysdig，结果在终端输出
sudo sysdig

# 将结果保存到文件
sudo sysdig -w dumpfile.scap

# csysdig查看保存的结果
csysdig -r dumpfile.scap
```


初始信息来源: chatgpt  


2024/3/1  
