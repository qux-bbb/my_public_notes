# 低版本VMP脱壳

## 基础信息
看看这篇分析文章：  
https://mp.weixin.qq.com/s/84S_pxD6TZeVpc1HC4VsTg  
https://xz.aliyun.com/t/13745  
想知道VMP是怎么脱壳的  

在X搜"from:@vxunderground SugarGh0st"就能找到相关信息了  
https://twitter.com/vxunderground/status/1757651384453787723?t=HseemS2k4TXoEiCiwPkbhg&s=19  
https://vx-underground.org/APTs/2024/2024.02.09%20-%20SugarGh0st%20RAT%20attacks%20Kazakhstan%20%E2%80%93%20State%20Technical%20Service  

DIE查看update.dll_DEDF98E7E085CED2D3266AFA9279E4C7，显示是VMP1.7  
保护器: VMProtect(1.70)[Max protection]  


## 脱壳思路
```r
思路灵感来自这里: https://bbs.kanxue.com/thread-246429.htm
这种旧版的VMP，开始在.vmp段运行，最后会跳到在.text段的oep执行，所以逻辑上只要在.text段第一次执行时断下就可以了
为什么不直接在.text段下一个内存执行断点呢？
因为程序会调用VirtualProtect修改.text段的权限，导致内存执行断点失效
```


## 具体步骤
x64dbg32位加载update.dll，查看.text段内存，我这里起始地址是0x00231000，建个快照  

方法1：  
1. 反汇编转到0x00231000，下硬件执行断点
2. 断下后，转到"调用堆栈"窗口，右键选择"显示可能的调用堆栈帧"，看到调试的dll最下层的返回地址是0x002343E2
3. 在反汇编窗口跳转到0x002343E2，Ctrl+A分析函数，Ctrl+HOME跳到函数开头，就是脱壳后dll入口点的地址，这里是0x00234392
4. 找到0x00234392之后，恢复快照，在0x00234392下硬件执行断点，运行断下之后保存脱壳后的dll进行分析即可

方法2：  
1. 在0x00231000下内存执行断点
2. 在VirtualProtect下断点，执行断下后，发现VirtualProtect操作的内存段以0x00231000开头时，Ctrl+F9执行完VirtualProtect，重新在0x00231000下内存执行断点
3. 触发内存执行断点后，程序就会停在OEP的位置，保存脱壳后的dll进行分析即可
