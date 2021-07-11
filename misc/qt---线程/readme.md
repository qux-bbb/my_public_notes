# qt---线程

qt的线程可以用QThread和QConcurrent  
QThread有run和moveToThread两种使用方法，官方建议后者  
QtConcurrent是一个更高层次的API，使用比较简单  

信息传递和函数调用都可以`信号-槽`的方式实现  

QtConcurrent和QThread具体区别可以看这里: https://stackoverflow.com/questions/30680358/multithreading-performance-of-qtconcurrent-vs-qthread-with-many-threads  

这里是一些使用视频和例子：  
1. 基本的QThread使用: https://www.youtube.com/watch?v=5zG6O1hkx-o  
2. moveToThread使用: https://www.youtube.com/watch?v=u1BwnIVuw0o  
3. 更完整的moveToThread使用: https://www.cnblogs.com/nanqiang/p/10818609.html  
4. QtConcurrent使用: https://www.youtube.com/watch?v=jPdgTdxklAY  


2021/7/11  
