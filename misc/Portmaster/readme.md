# Portmaster

Portmaster是一个开源的网络管理工具，可以按应用(可以是前后缀)、域名、IP地址等进行网络管理(允许、拒绝)，支持Windows、Linux。

官网: https://safing.io/  
github地址: https://github.com/safing/portmaster

如果打开后发现域名都无法解析，可以这样配置：  
Global Settings -> Secure DNS -> Servers -> DNS Servers  
点击“Quick Settings”，切换不同的配置，或者在下方添加自定义的DNS服务器，直到域名能够正常解析即可

默认会阻断连入的网络连接，会影响Localsend、Python的http.server，可以针对应用允许连入或允许全部连入。

信息来源: https://mp.weixin.qq.com/s/EWt13kBJjBR4QGInO9ZvAA
