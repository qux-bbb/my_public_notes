# kali---xshell-xming-eclipse显示不正常

显示不正常原因为缺少一个环境变量，在/etc/profile最后添加一行：  
```bash
export SWT_GTK3=0
```


2017/12/21  
