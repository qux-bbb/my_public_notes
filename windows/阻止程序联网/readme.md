用的是win10，想想怎么阻止一个程序联网。  

首先要看看哪些程序用了网络：  
Windows设置 --> 网络与Internet --> 数据使用量，可以查看各个网卡上程序使用流量情况  

然后用防火墙的出站规则阻止程序联网：  
搜索`高级安全 Windows Defender 防火墙`，选择`出站规则`，右键`新建规则`，按步骤禁用某一程序外连即可。  


整个过程确实有些繁琐，不像Android那样直接，比如在小米手机里，设置某应用的`联网控制`，取消选中`WLAN`和`数据`即可。  
Fab可以简化这个过程，可以很方便地通过文件、文件夹、进程来控制程序是否联网。  
Fort也可以，而且开源。  
