# MBR病毒利用系统中断

MBR, Master Boot Record, 主引导记录  
MBR病毒是会修改主引导记录的病毒，利用的中断是 `int 13h`  

BIOS Int 13H 调用是 BIOS 提供的磁盘基本输入输出中断调用，它可以完成磁盘(包括
硬盘和软盘)的复位，读写，校验，定位，诊断，格式化等功能。所以MBR病毒一般都是通过HOOK int 13h执行恶意代码。   

原链接：https://bbs.pediy.com/thread-121861.htm  


20201119  
