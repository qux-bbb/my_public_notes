# perl相关

perl，一种脚本语言，一般linux发行版默认安装  
官网：https://www.perl.org/  

查看perl版本：`perl -v`  

cpan，Comprehensive Perl Archive Network，类似python的pip，安装模块示例：  
```
sudo cpan install Net::DNS
```
如果`make`出现错误，就安装make：`sudo apt install make`  
如果`make test`出现错误，可能是网络问题，试试直接进入`/root/.cpan/build`下找到对应文件夹，进入，执行：`make install`  


2020/12/19  
