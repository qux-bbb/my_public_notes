# x64系统编译运行调试arm64程序

需要用到gcc跨平台编译，qemu用户模式运行，gdb多架构调试。  

以ubuntu为例介绍步骤。  

hello.c如下：  
```c
#include <stdio.h>

int main() {
    int inputNumber;

    printf("Please enter an integer: ");
    scanf("%d", &inputNumber);

    printf("The integer you entered is: %d\n", inputNumber);

    return 0;
}
```

安装编译运行调试：  
```bash
# 安装gcc交叉编译器
sudo apt-get install gcc-aarch64-linux-gnu
# 安装qemu用户模式工具
sudo apt-get install qemu-user
# 安装gdb-multiarch
sudo apt-get install gdb-multiarch

# 编译
aarch64-linux-gnu-gcc -o hello hello.c

# 运行 -L指定ELF解释器相关文件路径
qemu-aarch64 -L /usr/aarch64-linux-gnu/ ./hello

# 调试
# 启动程序，-g指定gdb调试端口
qemu-aarch64 -L /usr/aarch64-linux-gnu/ -g 1234 ./hello
# 新开一个窗口，切换到同目录下，gdb调试，-ex执行一些命令
gdb-multiarch -ex "set architecture aarch64" -ex "target remote localhost:1234" -ex "file ./hello"
```

参考资料：  
1. https://blog.csdn.net/qq_41202237/article/details/118188924
2. chatgpt


2023/4/22  
