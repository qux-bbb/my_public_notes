# 竞争提权思路

```
初始条件
普通用户，内核有uaf漏洞

触发uaf漏洞，使内核分配地址和用户态地址在physmap 重合，控制buffer，执行自己想要的逻辑

设置sid uid为0，开tty，获取root权限
```


2019/9/9  
