# gdb---结合python自动化调试

gdb支持通过python自动化调试，实现循环、读写内存、保存内容等复杂逻辑，不需要安装模块。  
核心函数：  
```python
gdb.execute(command [, from_tty [, to_string]])
```

脚本示例 test.py：  
```python
import gdb

gdb.execute("break *0x12345678")
gdb.execute("continue")
# 指定 to_string=True 可以让脚本接收输出并做后续处理，这是能让gdb和脚本交互的重要参数
the_line = gdb.execute("info registers eip", to_string=True)
gdb.execute("dump memory /root/memory.dump $ebx $ebx+0x100")
```

启动gdb，执行如下命令调用脚本：  
```r
source ./test.py
```

或者直接启动时指定脚本  
```r
gdb -x test.py
```


参考链接：  
1. https://segmentfault.com/a/1190000005718889
2. https://sourceware.org/gdb/onlinedocs/gdb/Basic-Python.html#Basic-Python


2023/5/3  
