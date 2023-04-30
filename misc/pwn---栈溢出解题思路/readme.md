# pwn---栈溢出解题思路

1. 先定位可以栈溢出的函数
2. 确定栈溢出的长度
3. 确定保护机制(是否开启canary，是否开启NX)  
    a. 如果没有NX保护，直接在能确定地址的内存写shellcode，用ret2shellcode技术  
    b. 如果有NX保护，则需要使用ROP技术，可以使用相应的工具(ROPgadget)去寻找程序中基本的gadget，自行构造攻击链  
4. 攻击成功，寻找flag


2020/7/1  
