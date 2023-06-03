# windbg---工作布局

大神分享的工作布局  
https://bbs.pediy.com/thread-100391.htm  

也可以自己参照 windbg preview 的布局设置之后保存，拖窗口确实有点痛苦  
保存的工作在注册表里，可以导出  
`计算机\HKEY_CURRENT_USER\Software\Microsoft\Windbg\Workspaces`  

在 windbg 里设置保存的工作布局没有默认布局，按上面的方法导出布局之后，可以把想要设默认的布局复制一份出来，然后改一下路径，就有默认布局了，就像这样，第一个 Default 就是复制第二个的，改一下中括号的路径就好  
```r
[HKEY_CURRENT_USER\Software\Microsoft\Windbg\Workspaces]
"Default"=hex:57,44,57,53,01,00,00,00,44,00,00,00,10,00,04,00,01,00,00,00,00,\

[HKEY_CURRENT_USER\Software\Microsoft\Windbg\Workspaces\Explicit]
"Default"=hex:57,44,57,53,01,00,00,00,44,00,00,00,10,00,04,00,01,00,00,00,00,\
```


2020/7/18  
