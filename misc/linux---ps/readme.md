ps，process status，显示进程状态  

部分选项解释：  
```sh
-e  所有用户
-f  格式化输出，可以看到进程所属用户名和启动时间
-F  比 -f 选项更详细一点
```

`ps -aux` 和 `ps aux` 的区别（摘自 man 手册，其实不用管，直接用 `ps -ef` 吧）：  
```
Note that "ps -aux" is distinct from "ps aux".  The POSIX and UNIX standards require that "ps -aux" print all processes owned by a user named "x", as well as printing all processes that would be selected by the -a option.  If the user named "x" does not exist, this ps may interpret the command as "ps aux" instead and print a warning.  This behavior is intended to aid in transitioning old scripts and habits.  It is fragile, subject to change, and thus should not be relied upon.

Commands options such as ps -aux are not recommended as it is a confusion of two different standards.  According to the POSIX and UNIX standards, the above command asks to display all processes with a TTY (generally the commands users are running) plus all processes owned by a user named "x".  If that user doesn't exist, then ps will assume you really meant "ps aux".
```

翻译如下：  
```
注意 "ps-aux" 不同于 "ps aux"。POSIX 和 UNIX 标准要求 "ps -aux" 输出名为 "x" 的用户拥有的所有进程，'-a' 选项确定输出所有进程。如果名为 "x" 的用户不存在，会将命令解释为 "ps aux" ，并输出警告。此行为旨在帮助转换旧脚本和习惯。但这样的转化是不确定的，随时可能发生变化，因此不应依赖它。  

不建议使用类似 `ps -aux` 的命令选项，因为这是两种不同标准的混淆。根据 POSIX 和 UNIX 标准，这个命令要求用 TTY（通常是用户正在运行的命令）显示名为 "x" 的用户拥有的所有进程。如果该用户不存在，那就会假定你的真正意思是 "ps aux"。
```


参考资料：  
https://www.computernetworkingnotes.com/linux-tutorials/ps-aux-command-and-ps-command-explained.html  
