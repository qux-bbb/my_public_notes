# 生成可在xp下运行的exe
使用IDE: VS2017  
vs2019不再支持xp，所以用vs2017  

步骤：  
1. 项目->具体项目属性，配置属性->常规->平台工具集  
    选择有xp的那一项: Visual Studio 2017 - Windows XP (v141_xp)  
    如果没有，工具->获取工具和功能->单个组件->编译器、生成工具和运行时，选中"对C++的Windows XP 支持"，安装重启应该就有了  
2. 项目->具体项目属性，配置属性->C/C++->语言->符合模式，修改为否  
3. 项目->具体项目属性，配置属性->C/C++->代码生成->运行库，修改为"多线程（/MT）"  


参考链接：  
1. https://docs.microsoft.com/en-us/cpp/build/configuring-programs-for-windows-xp?view=vs-2019
2. https://blog.csdn.net/ly1390811049/article/details/106392052


20210401  
