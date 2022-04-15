# kali开wifi热点

电脑开wifi的前提，肯定要有两块网卡，一个用来上网，一个用来开wifi  

kali可以直接在wifi中设置，我插了一个无线网卡，通过点击`Turn On Wi-Fi Hotspot`，即可开启一个名为kali的热点  

kali做的事情: kali会将内置无线网卡作为热点开启，同时自动建立相关iptables规则，开启流量转发; 外置网卡则用来联网。  


2018/10/21  
