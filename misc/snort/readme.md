# snort

官网: https://www.snort.org  
官方文档: https://www.snort.org/documents  

snort是一个开源的IPS/IPS。  
IPS, Intrusion Prevention System, 入侵防御系统  
IPD, Intrusion Detection System, 入侵检测系统  

现在有2.x和3.x版本，2.x安装比较方便，支持windows，这里记录一下windows安装使用。  


## snort规则
规则构成：  
```r
[action][protocol][sourceIP][sourceport] -> [destIP][destport] ( [Rule options] )
```
直接看这个吧: https://snort-org-site.s3.amazonaws.com/production/document_files/files/000/000/116/original/Snort_rule_infographic.pdf  

匹配ping(ping属于ICMP)：  
```r
alert icmp any any -> any any (msg:"ICMP Test"; sid:6; rev:1;)
```


## 在windows安装使用
下载安装包，直接安装就好了，snort.exe在bin文件夹下，为方便使用，可以把bin文件夹路径添加到path。  

etc文件夹下的snort.conf是需要自己调整的配置文件(调整前做备份)，运行时也需要指定，举例：  
`snort -c c:\snort\etc\snort.conf`  
大概需要修改的点和思路：  
1. 改成正确的路径
2. 注释不需要的部分

直到运行上面的命令不出错，就基本改完了。  

### ping示例
1. 创建规则文件，如my.rules，写好规则后，把规则文件放在rules文件夹下  
2. 在snort.conf中添加一行`include $RULE_PATH/snort.rules`  
3. 执行命令: `snort -c c:\snort\etc\snort.conf`
4. 随便ping一个地址

这样就可以在log目录下的alert.ids文件里看到命中的记录了  
如果想让命中记录既保存在alert.ids文件又显示在命令行中，可以添加选项 `-A console -A full`  
如果在命令行中只想看到命令记录，可以添加选项 `-q`，表示安静一点  
&&&&&&& snort匹配windows下抓的包有些问题，请求包匹配不了，不清楚原因  

### pcap包读取  
```r
snort -c c:\snort\etc\snort.conf -A console -A full -r ping.pcap
```


## 在ubuntu安装使用
ubuntu安装snort比较复杂，参考该链接即可：  
https://upcloud.com/community/tutorials/install-snort-ubuntu/  

配置调整也是和windows类似的思路，指定配置执行，直到不出错: `/etc/snort/snort.conf`  


---
2021/10/21  
