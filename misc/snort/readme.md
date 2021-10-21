# snort

官网: https://www.snort.org  
官方文档: https://www.snort.org/documents  

snort是一个开源的IPS/IPS。  
IPS, Intrusion Prevention System, 入侵防御系统  
IPD, Intrusion Detection System, 入侵检测系统  

现在有2.x和3.x版本，2.x安装比较方便，支持windows，这里记录一下windows安装使用。  


## snort规则
&&&&&&& 补充规则介绍  


## 在windows安装使用
下载安装包，直接安装就好了，snort.exe在bin文件夹下，为方便使用，可以把bin文件夹路径添加到path。  

etc文件夹下的snort.conf是需要自己调整的配置文件(调整前做备份)，运行时也需要指定，举例：  
`snort -c c:\snort\etc\snort.conf`  
大概需要修改的点和思路：  
1. 改成正确的路径
2. 注释不需要的部分

直到运行上面的命令不出错，就基本改完了。  

&&&&&&& 补充ping示例和pcap包读取  

---
2021/10/21  
