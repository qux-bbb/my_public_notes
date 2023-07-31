# python2---执行系统命令

阻塞型：等待子进程结束再执行后面的语句  
非阻塞型：不等待子进程结束就执行后面的语句  

除了subprocess.Popen，其它都是阻塞型的  
1、2方法对带空格路径支持不好  

## 1
```python
import os

os.system("ls")  
```

如果有输出，会直接在终端输出，脚本不能直接获取执行结果  


## 2
```python
import os

result = os.popen("ls")
print result.read()
```

可以获取输出结果  


## 3
```python
# coding:utf8

import commands

a = commands.getstatus("a.py")
b = commands.getoutput("ls")
c = commands.getstatusoutput("ls")

print(a)
print(b)
print(c)
```

此方法在linux系统运行正常  
* commands.getstatus("a.py") 实质上执行的命令为 `ls -ld a.py`
* commands.getoutput("ls") 会将命令的输出返回
* commands.getstatusoutput("ls") 会返回命令执行是否成功，命令的输出

在windows上有bug  


## 4
一个比较强大的执行命令模块: subprocess，参数太多  

举例：  
```python
# coding:utf8

import subprocess

print "-----------------------------------------------"
a = subprocess.call(['ls', '-l'])
print "a: \n" + str(a)

print "-----------------------------------------------"
b = subprocess.check_call(['ls', '-l'])
print "b: \n" + str(b)

print "-----------------------------------------------"
c = subprocess.check_output(['ls', '-l'])
print "c: \n" + str(c)

print "-----------------------------------------------"
d = subprocess.Popen(['ls', '-l'])
print "d: \n" + str(d)
# d.wait() 可以等待子进程结束后再往下执行
```
结果：  
```r
λ python a.py
-----------------------------------------------
total 2
-rw-r--r-- 1 q 197121 577 12月 21 22:40 a.py
drwxr-xr-x 1 q 197121   0 12月 21 22:41 dir1
-rw-r--r-- 1 q 197121   8 12月 21 22:41 file1
a:
0
-----------------------------------------------
total 2
-rw-r--r-- 1 q 197121 577 12月 21 22:40 a.py
drwxr-xr-x 1 q 197121   0 12月 21 22:41 dir1
-rw-r--r-- 1 q 197121   8 12月 21 22:41 file1
b:
0
-----------------------------------------------
c:
total 2
-rw-r--r-- 1 q 197121 577 12鏈?21 22:40 a.py
drwxr-xr-x 1 q 197121   0 12鏈?21 22:41 dir1
-rw-r--r-- 1 q 197121   8 12鏈?21 22:41 file1
-----------------------------------------------
d:
<subprocess.Popen object at 0x000000000378B5F8>

D:\tmp
λ total 2
-rw-r--r-- 1 q 197121 577 12月 21 22:40 a.py
drwxr-xr-x 1 q 197121   0 12月 21 22:41 dir1
-rw-r--r-- 1 q 197121   8 12月 21 22:41 file1
```

2017/12/12  
