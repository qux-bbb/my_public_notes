# gdb---调试python程序


1. ubuntu安装环境  
```bash
sudo apt-get install gdb python2.7-dbg
```

2. 启动python应用  
    - 交互式  
    ```bash
    $ gdb python
    (gdb) run <programname>.py <arguments>
    ```
    - 自动  
    ```
    $ gdb -ex r --args python <programname>.py <arguments>
    ```
    - 通过PID接入已经运行的进程  
    ```
    # 方法1
    $ gdb python <pid of running process>
    # 方法2
    $ gdb attach <pid of running process>
    ```
3. 调试进程  
    - 查看python调用栈  
    ```
    (gdb) py-bt
    ```
    - 上一帧，下一帧  
    ```
    py-up
    py-down
    ```
    - python栈跟踪(不可用)  
    ```
    (gdb) pystack
    ```
    - 获取栈帧python变量(不可用)  
    ```
    (gdb) pystackv
    ```
    - 查看当前线程python运行位置处代码  
    ```
    (gdb) py-list
    # 可指定显示代码范围
    (gdb) py-list START
    (gdb) py-list START,END
    ```
    - 查找一个python名字并输出值  
    ```
    (gdb) py-print self
    # 查找顺序：locals、globals、buildins
    ```
    - 查找选中线程的当前python帧中的所有locals，输出  
    ```
    (gdb) py-locals
    ```
    - 查看线程  
    ```
    (gdb) info threads
    # 当前所在线程前面会标星号
    ```
    - 切换当前线程  
    ```
    # 切换到线程5
    thread 5
    ```
    
    - 对所有线程操作  
    ```
    (gdb) thread apply all <command>
    # 可简写为 t a a <command>
    ```


---


可能遇到的问题：unable to read python frame information  
可能解决的办法，用python-dbg启动程序，然后用gdb attach  
```
$ python-dbg ./cc_py_gdb.py

$ ps -ef | grep cc_py_gdb
root 1287 1092 0 18:18 pts/0 00:00:00 python-dbg ./cc_py_gdb.py

$ gdb -q python-dbg -p 1287
```

---

参考资料：  
https://wiki.python.org/moin/DebuggingWithGdb  
https://fedoraproject.org/wiki/Features/EasierPythonDebugging  
https://blog.alswl.com/2013/11/python-gdb/  
https://blog.csdn.net/wangzuxi/article/details/42317827  

2018/7/4  