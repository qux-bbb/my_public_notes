# termux

termux是一个Android平台的Linux终端环境程序。  
官网: https://termux.com  

对我来说就是可以在Android上用linux的终端，而且生成或下载的文件可以用Android操作。  

# 获取手机存储访问权限
获取手机存储访问权限，执行命令: `termux-setup-storage`  

# 更新出现403错误

更新可以用 apt 或者 pkg  

如果出现403错误，执行 `rm -f ${PREFIX}/etc/apt/sources.list.d`，然后正常更新即可

原链接: https://www.zhihu.com/question/338094182  
