在windows下，可以通过一些方式实现程序自启动  
使用SysinternalsSuite套件中的Autoruns.exe可以查看所有自启动项，这里列举其中一些  

1. StartUp文件夹  
   - winxp: `C:\Documents and Settings\Administrator\「开始」菜单\程序\启动`  
   - win7 win10: `C:\Users\<User>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`  
2. 各种注册表项自启动  
   下面是2个常见的注册表项  
   - `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`  
   - `HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run`  
3. 任务计划程序  
   win+R，输入: `taskschd.msc`, 回车可以打开任务计划程序，可以设置可执行程序的启动时间和频率  
4. 自启动服务  
   win+R，输入: `services.msc`, 回车可以打开服务列表，在这里可以设置已有任务的运行状态和启动类型  
   `sc.exe`是用来与服务控制管理器和服务进行通信的命令行程序，可以查看、创建、删除服务  

