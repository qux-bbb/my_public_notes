# DLL注入的实现方法

向某个进程注入DLL时主要使用以下三种方法：  
1. 创建远程线程（CreateRemoteThread() API）
2. 使用注册表（AppInit_DLLs值）
3. 消息钩取（SetWindowsHookEx() API）


2019/3/8  
