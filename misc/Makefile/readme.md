Makefile是make命令的默认配置文件，执行`make`相当于执行`make -f Makefile`  

代码hello.c  
```c++
#include <stdio.h>

int main(){
    printf("Hello World!\n");
    return 0;
}
```

一个例子：  
Makefile  
```Makefile
.PHONY: clean
hello: hello.c
	gcc -o hello hello.c
    
clean:
	rm hello
```

`.PHONY` 表示伪目标，不指具体生成的文件  

基本格式是：  
```
目标文件: 依赖文件
<制表符>要执行的命令
```
命令前必须是制表符  

只执行make，会选取第一个目标对应的命令执行  

注释以"#"开头  

命令或注释前加"@"则不会输出到终端  


参考链接:  
http://www.ruanyifeng.com/blog/2015/02/make.html  
https://www.gnu.org/software/make/manual/make.html  