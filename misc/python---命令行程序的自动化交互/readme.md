# python---命令行程序的自动化交互

keywords: python 命令行程序 自动化 交互  

以这个python程序为例: [want_right.py](files/want_right.py)  

用脚本调用want_right.py，并自动输出  'Rignt!'，使用 subprocess 实现: [main.py](files/main.py)  

执行 `python main.py`, 输出：  
```r
input 5:
'5'
input 0:
'0'
Right!
```


感谢 zl  


&&&&&&& 问题：针对python程序是没问题的，但针对exe和elf就获取不到输出了，暂时还不知道为什么，以后慢慢解决  


2020/5/25  
