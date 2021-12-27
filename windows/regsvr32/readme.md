# regsvr32

regsvr32用于注册动态链接库文件，实际是调用其中的DllRegisterServer函数。  

注册: `regsvr32 hello.dll`  
静默注册: `regsvr32 /s hello.dll`  
取消注册: `regsvr32 /U hello.dll`  

参考：  
1. https://docs.microsoft.com/zh-cn/windows-server/administration/windows-commands/regsvr32
2. https://baike.baidu.com/item/Regsvr32/749536


2021/12/27  
