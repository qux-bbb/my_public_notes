# 样本反沙箱机制总结

1. 查找虚拟机特征，指定的文件，进程，注册表项等
2. CPUID返回结果
3. 屏幕分辨率
4. 机器内存大小，硬盘大小
5. 用户名
6. 检查鼠标键盘的活动频率
7. 检查系统是否有使用痕迹，比如最近使用文件是否为空，开机时间是否太短
8. 检查一下是不是正式磁盘只有C盘
9.  使用拟态按钮，使沙箱无法自动获取点击目标
10. 设置自启，重启才做敏感操作
11. 先休眠一段时间，然后再做真正敏感操作
12. 前期大量调用无用api，消耗大量时间后才做真正的敏感操作
13. 可以自己随意指定一个参数，只有参数个数或其他条件符合的时候，才执行敏感操作，参数也可以搞成密码，加解密资源或代码
14. 父进程文件名是否为explorer.exe


1-8是检测虚拟机特征，检测到了就不做敏感操作  
9-12是根据沙箱的运行机制做相应规避  
13比较通用吧，拿到一个单独的文件，默认条件下并不执行敏感操作  
14也比较通用，效果较好  


20201119  
20201227 增加参数影响逻辑  
20210113 增加盘符检测  
20210420 增加父进程名检测  
