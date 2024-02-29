# ProcMon-for-Linux

ProcMon-for-Linux 是微软开源的linux下的process monitor  

github地址: https://github.com/Sysinternals/ProcMon-for-Linux  

支持Ubuntu 18.04 & 20.04，很久不更新了  

安装方式：  
```bash
wget -q https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb

sudo apt-get update
sudo apt-get install procmon
```


20210403  
