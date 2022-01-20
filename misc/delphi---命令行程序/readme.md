# delphi---命令行程序

delphi安装，因为只是测试，随便在网上找一个delphi7的破解版装虚拟机里试一下  
要输注册码搜一下就行，比如这个  
SN:6AMD-PDJ686-APME9D-9CDR KEY：YVX-27C  

如果新建工程出错，尝试管理员启动Delphi，应该就可以了  

写个简单的Hello World，File -> New -> Other -> Console Application，然后保存到一个地方，粘下面的代码，编译运行即可  
```r
program Project2;

{$APPTYPE CONSOLE}

uses
  SysUtils;

begin
  { TODO -oUser -cConsole Main : Insert code here }
  writeln('Hello world');
  readln;
end.
```

参考链接：https://www.cnblogs.com/volcanol/archive/2016/03/24/5314059.html  


delphi生成的exe程序，前3个字节都是"MZP"  


20201206  
