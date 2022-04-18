# vim产生的swp文件恢复

使用vim编辑文件时，会生成临时交换文件(swap file)，如果意外退出，就可以使用交换文件恢复文件内容。  

假如编辑文件名为 `hello.txt`，则第一次生成的交换文件名为 `.hello.txt.swp`，第二次生成的交换文件名为 `.hello.txt.swo`，第三次生成的交换文件名为 `.hello.txt.swn`，以此类推。  

恢复命令: `vim -r hello.txt`  

参考链接: http://yyq123.blogspot.com/2012/03/vim-swap.html  


2022/4/19  
