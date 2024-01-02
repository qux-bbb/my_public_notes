# gdb---结合python自动化调试

gdb支持通过python自动化调试，实现循环、读写内存、保存内容等复杂逻辑，不需要安装模块。  

官方文档: https://sourceware.org/gdb/current/onlinedocs/gdb.html/Python.html  
官方文档直接看不太容易理解，可以结合chatgpt、文心一言等工具使用。  


## 简单使用
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


## 获取寄存器值和内存数据的方法
hello.c  
```c
// gcc -o hello hello.c
#include <stdio.h>

int main(){
    printf("Hello World!\n");
    return 0;
}
```

python脚本
```python
# gdb -x test.py
import gdb

gdb.execute("file hello")
gdb.execute("break main")
gdb.execute("run")
gdb.execute("nexti 2")

# 获取当前被调试程序的栈帧
frame = gdb.selected_frame()
# 获取寄存器'rax'的值
rax = frame.read_register("rax")
# 打印寄存器的值
print("rax的值是: 0x%x" % rax)

# 获取当前GDB中的被调试程序（也称为“下级”）
inferior = gdb.selected_inferior()
# 从地址rax开始读取32个字节（即0x20字节）的内存数据
the_mem = inferior.read_memory(rax, 0x20)
# 打印内存数据
print("the_mem: ", the_mem.tobytes())
```


## 参考链接
1. https://segmentfault.com/a/1190000005718889
2. https://sourceware.org/gdb/onlinedocs/gdb/Basic-Python.html#Basic-Python
3. 文心一言
4. chatgpt


---
2023/5/3  
