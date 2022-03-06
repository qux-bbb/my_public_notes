# vscode---搜索多个无顺序关键字

vscode没有搜索多个无顺序关键字的功能。  

有人提过，但是被官方否了，这里有链接：  
https://github.com/microsoft/vscode/issues/16488  

这里是一个命令的实现，用了正则，但感觉有些违背直觉：  
https://github.com/usernamehw/vscode-search  

&&&&&&& 初步的思路是逐个关键字在文件中搜索，把匹配到的结果像官方搜索那样列在侧边栏。  
能力不够，暂搁置。  


2022/3/6  
