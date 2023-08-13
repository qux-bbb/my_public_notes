# inetsim

keywords: https明文 https解密  

官网：https://www.inetsim.org/  

INetSim是一个软件套件，用于在实验环境中模拟常见的Internet服务，例如用于分析未知恶意软件样本的网络行为。  
是用Perl写的。  

inetsim的各种服务需要root权限，burpsuite绑定443端口时需要root权限(端口小于1024就需要)  
全程使用root用户操作即可(sudo su)  


## 安装
ubuntu安装（不推荐按官方文档手动逐个依赖安装，依赖东西有点多）：  
```bash
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

配置并重启inetsim服务  
```bash
cp /etc/inetsim/inetsim.conf /etc/inetsim/inetsim.conf.bak
# 修改/etc/inetsim/inetsim.conf，将`service_bind_address`和`dns_default_ip`取消注释，值改成本机ip
systemctl restart inetsim
```

win7(受监控机器)网络设置如下：  
```r
ip: win7ip
子网掩码: 255.255.255.0
默认网关: ubuntu ip

DNS服务器: ubuntu ip
```

确保win7可以ping通ubuntu，然后在win7发起网络请求，ubuntu就会返回虚假结果。  
ubuntu会记录win7的网络请求，停止后会保存到一个report文件里，如果中途要查看，可以看`/var/log/inetsim/service.log`  


## 支持https

禁止dns服务  
```bash
systemctl disable systemd-resolved.service
service systemd-resolved stop
```

更新配置/etc/inetsim/inetsim.conf的https端口为8443: `https_bind_port 8443`  
重启inetsim服务  
```bash
systemctl restart inetsim
```

下载安装burp社区版: https://portswigger.net/burp/freedownload/  
执行下载的脚本即可  

启动Burpsuite  
```bash
BurpSuiteCommunity
```
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

&&&&&&& 现在按上面的操作，firefox会显示SEC_ERROR_BAD_SIGNATURE错误，IE会提示证书错误，还不知道怎么解决  

确认inetsim不支持任意ip直接访问网页  


## 自定义数据和配置路径，手动执行
停止并禁用服务  
```bash
systemctl stop inetsim
systemctl disable inetsim
```

手动执行，指定配置和数据  
```bash
cp -r /var/lib/inetsim data
cp /etc/inetsim/inetsim.conf inetsim.conf
# 可以任意修改数据和配置文件
inetsim --data data --conf inetsim.conf
```


## 参考链接
1. https://www.freebuf.com/articles/system/177601.html （下面链接的翻译）  
2. https://blog.christophetd.fr/malware-analysis-lab-with-virtualbox-inetsim-and-burp/#INetSim  
3. https://blog.csdn.net/weixin_30885111/article/details/94977815  


20201216  
20201220 补充安装方式  
20201221 补充inetsim配置简单修改  
