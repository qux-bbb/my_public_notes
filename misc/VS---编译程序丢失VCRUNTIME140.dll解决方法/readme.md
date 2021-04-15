keywords: vs runtime `visual studio`  

VS编译C或C++程序丢失VCRUNTIME140.dll解决方法  
1. 更改版本为Release  
2. 项目->具体项目属性，配置属性->C/C++->代码生成->运行库，将该项改为多线程(/MT)  

重新编译即可  


来源: https://jingyan.baidu.com/article/a681b0de7a173c3b1843462b.html  


20181107  
