# inetsim

keywords: https明文 https解密  

## 简介
官网：https://www.inetsim.org/  

INetSim是一个软件套件，用于在实验环境中模拟常见的Internet服务，例如用于分析未知恶意软件样本的网络行为。  
是用Perl写的。  


## 安装
ubuntu安装（不推荐按官方文档手动逐个依赖安装，依赖东西有点多）：  
```bash
su
echo "deb http://www.inetsim.org/debian/ binary/" > /etc/apt/sources.list.d/inetsim.list
wget -O - http://www.inetsim.org/inetsim-archive-signing-key.asc | apt-key add -
apt update
apt install inetsim
```


## 一些位置
init.d配置文件: /etc/default/inetsim  
主配置文件: /etc/inetsim/inetsim.conf  
请求响应文件: /var/lib/inetsim/  
日志和报告文件: /var/log/inetsim/  


## 简单使用
官方说明比较简洁，看一遍好了。  

默认会启动服务，可以这样控制：  
```bash
* Usage: /etc/init.d/inetsim {start|stop|restart|force-reload|status}
```

手动执行，使用默认配置，指定 绑定地址  
```bash
inetsim --bind-address=127.0.0.1
```
手动执行，指定配置  
```bash
# 最简单修改：将`service_bind_address`和`dns_default_ip`取消注释，值改成本机ip  
inetsim --conf inetsim.conf
```

win7(受监控机器)网络设置如下：  
```r
ip: win7ip
子网掩码: 255.255.255.0
默认网关: ubuntu ip

DNS服务器: ubuntu ip
```

然后在win7发起网络请求，ubuntu就会返回虚假结果。  
ubuntu会记录win7的网络请求，停止后会保存到一个report文件里，如果中途要查看，可以看`/var/log/inetsim/service.log`  


## 支持https
下载安装burp社区版: https://portswigger.net/burp/freedownload/  
执行下载的脚本即可  

准备自己数据的目录(也可以直接用系统默认的，这个不重要)  
```bash
mkdir -p analysis/test-analysis
cp /etc/inetsim/inetsim.conf analysis/test-analysis
sudo cp -r /var/lib/inetsim analysis/test-analysis/data
cd analysis/test-analysis
sudo chmod -R 777 data
```

禁止dns服务  
```bash
sudo systemctl disable systemd-resolved.service
sudo service systemd-resolved stop
```

更新配置analysis/test-analysis/inetsim.conf的https端口为8443: `https_bind_port 8443`  

启动inetsim: `inetsim --data data --conf inetsim.conf`  

启动Burpsuite  `BurpSuiteCommunity`  
Proxy->Intercept，点击`Intercept is on`，切换为`Intercept is off`，这样就不会拦截请求了  
Proxy->Options，添加listener，如下配置：  
```r
Binding tab
    Bind to port: 443
    Bind to address: all interfaces
Request handling tab:
    Redirect to host: 本机ip
    Redirect to port: 8443
Check Support invisible proxying
```
继续添加listener(该listener只是为了下载证书，用完了就可以删掉)：  
```r
Binding tab
    Bind to port: 8080
    Bind to address: all interfaces
```
浏览器访问 http://本机ip:8080，右上角下载证书  
下载证书后使用普通用户转换证书格式: `openssl x509 -in ~/Downloads/cacert.der -inform DER -out burp.crt`  
设置证书为ca证书并使其生效：  
```bash
sudo cp burp.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates
```

win7(被监控的机器)如果用的是firefox，需要这样信任证书：  
1. 把burp.crt复制到win7
2. Firefox->选项->隐私和安全->证书->查看证书->证书颁发机构->导入
3. 选择burp.crt，信任选项全部勾选，确定即可

这样之后，win7的firefox访问任何https网站都是绿色小锁了  

win7(被监控的机器)如果用的是IE，需要将burp.crt安装到受信任的根证书列表里，这样IE访问https网站不会提示证书错误  

确认inetsim不支持任意ip直接访问网页  


## 参考链接
1. https://www.freebuf.com/articles/system/177601.html （下面链接的翻译）  
2. https://blog.christophetd.fr/malware-analysis-lab-with-virtualbox-inetsim-and-burp/#INetSim  
3. https://blog.csdn.net/weixin_30885111/article/details/94977815  


20201216  
20201220 补充安装方式  
20201221 补充inetsim配置简单修改    
