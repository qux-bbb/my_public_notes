# AFL简单使用

使用AFL进行fuzz  
回顾早期的软件漏洞，在攻防之间的较量相当精彩。现在IT公司和安全实验室会使用强大的Fuzz工具寻找软件缺陷或挖掘漏洞。新防御技术提出的同时，反防御技术也随之出现。在这篇文章中，我们将了解软件漏洞利用的整个过程：从使用[American Fuzzy Lop(AFL)](http://lcamtuf.coredump.cx/afl/)来进行fuzz，到使用[gdb-peda](https://github.com/longld/peda)和[pwntools](https://github.com/Gallopsled/pwntools)调试编写漏洞利用脚本。为此，我们编写一个有明显缓冲区溢出漏洞的64位程序，然后对其进行fuzz，找到漏洞，分析结果，并为其编写漏洞利用脚本。这里也提供了[视频资源](https://youtu.be/nZD9oe5TUKs)。  

## 安装AFL
我们使用Ubuntu64位系统，通过以下命令即可成功安装AFL：  
```sh
wget http://lcamtuf.coredump.cx/afl/releases/afl-latest.tgz
tar -xvf afl-latest.tgz
cd afl-2.52b/
make
sudo make install
```

## 用afl-gcc编译有漏洞的vuln1程序
虽然可以在网上找一个有漏洞的程序，但为了完全了解细节，我们还是自己写一个简单的C程序。这个程序使用了2个字符串缓冲区，每个缓冲区的长度为32字节，分别用于存放`username`和`password`。为了获取用户输入，我们使用不安全的[gets()](http://www.cplusplus.com/reference/cstdio/gets/)函数，它不会去检查边界，这会导致缓冲区溢出。  
```c
#include <stdio.h>
#include <string.h>
 
int main(void)
{
	char login[32];
	char passwd[32];
	
	printf("Login: \n");
	gets(login);
	printf("Password: \n");
	gets(passwd);
	
	if (strcmp(login, "root") == 0) {
		if (strcmp(passwd, "1qazxsw2") == 0) {
			printf("Access Granted.\n");
			return 0;
		}
	}
	
	printf("Access Denied.\n");
	return 1;
}
```
执行该程序，会要求输入`username`和`password`。输入被存放到`login`和`passwd`变量中。然后使用[strcmp()](http://www.cplusplus.com/reference/cstring/strcmp/)和正确的值比较，如果输入值为"root"和"1qazxsw2"，控制台会输出"Access Granted."，否则输出"Access Denied."。  

我们使用afl-gcc编译器来构建目标程序。AFL编译器会在源码周围添加代码，最大限度地扩大覆盖率。使用以下命令进行编译：  
```sh
afl-gcc -fno-stack-protector -z execstack vuln1.c -o vuln1
```
-fno-stack-protector 该选项会禁止[stack canary](https://en.wikipedia.org/wiki/Stack_buffer_overflow#Stack_canaries)保护  
-z execstack 允许堆栈可执行  

生成的目标程序会用于下文的fuzz。  

## 使用afl-fuzz来fuzz程序
fuzz的一个关键点是创建好的测试用例，通过分析目标程序的所有潜在路径来最大化输入的覆盖率。vuln1程序很简单，只有3条路径：  
1. `username`无效；
2. `username`有效，但`password`无效；
3. `username`和`password`都有效。

创建3个文件作为测试用例来覆盖3条路径，每个文件都包含2行。如下：  
| test1.txt | test2.txt | test3.txt |
| --------- | --------- | --------- |
| a         | root      | root      |
| a         | a         | 1qazxsw2  |
AFL会读取每个文件的内容，将每一行输入到vuln1的标准输入中。创建一个名为testcase的目录，并在其中创建3个表示这些情况的文件。文件名并不重要。  

创建3个文件之后，再创建一个和testcase同级的名为results的目录，该目录会保存fuzz结果。  

最后一步准备工作：切到root用户，修改`core_pattern`文件内容为`core`：  
```sh
echo core > /proc/sys/kernel/core_pattern
```

使用以下命令开始fuzz：  
```sh
afl-fuzz -i ./testcases/ -o ./results/ ./vuln1
```
开始fuzz之后，右上角的`uniq crashes`会很快出现变化，当`total paths`到达3时，已经达到了我们想要的效果。使用Ctrl-C终止程序。在真实环境下，我们一般无法知道一共有多少种路径，AFL提供颜色变化来帮助你判断是否已有结果。最需要关注的就是`uniq crashes`，如果它的值不为0，表明已经有输入导致了程序崩溃，在results/crashes文件夹里存有相应文件：  
```
id:000000,sig:11,src:000000,op:havoc,rep:128
id:000001,sig:11,src:000000+000001,op:splice,rep:64
README.txt
```
每个id开头的文件都包含使程序崩溃的输入，这样就可以复现崩溃，并查看崩溃是否可以利用，以下命令展示了简单的复现：  
```sh
cat out/crashes/id\:000000\,sig\:11\,src\:000000\,op\:havoc\,rep\:128 | ./vuln1
Login: 
Password: 
段错误
```


## 总结
这篇文章介绍了AFL并fuzz了一个简单的程序。AFL是一个强大的fuzz工具，可用于源代码和二进制文件的漏洞查找，这通常是发现漏洞的第一步。  



原文：http://thecyberrecce.net/2017/03/20/software-exploit-development-fuzzing-with-afl/  


---
2019/4/19  
