# shell脚本相关

keywords: bash脚本  

shell脚本，可以直接在linux下执行的脚本，因为linux应该都有shell。  
shell有很多种，这里只记一些Bash相关的脚本信息。  

官方文档: https://www.gnu.org/software/bash/manual/bash.html  


## 简单示例
这里的教程一般足够我用了: https://www.runoob.com/linux/linux-shell.html  
一个helloworld例子：  
```bash
#!/bin/bash
echo "Hello World !"
```

一个if举例：  
```bash
#!/bin/bash
echo "Guess the secret color"
read COLOR
if [ $COLOR = "purple" ]
then
    echo "You are correct."
else
    echo "You are wrong."
fi
```
很简单的if，最重要的是 `[ $COLOR = "purple" ]`  
方括号必须要有空格，等号两边必须要有空格  

## 出错即退出
如果想让某条命令执行出错后立即退出脚本，可以这样写：  
```bash
#!/bin/bash
set -o errexit

echo 1
ehco 2
echo 3
```
中间的`ehco 2`拼错了，而且设置了出错即退出，所以只会输出1  

参考链接: https://my.oschina.net/u/2409113/blog/490833  

## 变量声明 写文件
```bash
#!/bin/bash

set -o errexit

# 变量名和等号之间不能有空格
the_path="/home/hello/Desktop/log.txt"

date >> $the_path
echo -e "\n" >> $the_path
```

## 函数
```bash
#!/bin/bash

set -o errexit

greet() {
    echo "Hello ${1}"
}

greet World
```

参考链接: https://opensource.com/article/21/3/input-output-bash  

## 必须有sudo权限才执行
不一定是root用户执行，这里指的是root权限，只要有sudo权限就可以  
```bash
# check if start with root
if [ "$EUID" -ne 0 ]; then
   echo 'This script must be run as root'
   exit 1
fi
```

参考链接: https://github.com/doomedraven/Tools/blob/master/Virtualization/kvm-qemu.sh  
