# 装win7系统致命系统错误

```
有人的电脑进不去系统了，我就拿了系统U盘过去（这系统盘是用cmd稍微设置了一下，然后把iso文件解压放进去的），本来安装一遍已经安装完了，但是重启之后就出现了这样的错误
STOP: c000021a {Fatal System Error}
The initial session process system process or system process terminated unexpectedly with a status of 0x00000000 (0xc00000001 0x001003f0).
The system has been shut down.
试了一遍又一遍，最后在一个boot选项里把 UEFI改成 legacy ，又重新装了一遍系统，才正常了，并不知道为什么，反正是好了

0x00000001  不正确的函数
0x001003f0  (没查到含义)
```


2017/1/20  
