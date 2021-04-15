ProcMon-for-Linux 是微软开源的linux下的process monitor，试了下，还不能正常用  

github地址: https://github.com/Sysinternals/ProcMon-for-Linux  

按照官方步骤，在ubuntu18上装好了，但启动之后没有信息，有错误日志输出，已经有人提了issue  

自己整理的下载编译安装脚本（卡住了）：  
```bash
#!/bin/bash

set -o errexit

# Install build dependencies
sudo apt-get -y install bison build-essential flex git libedit-dev libllvm6.0 llvm-6.0-dev libclang-6.0-dev python zlib1g-dev libelf-dev

# Build and install BCC
cd ~/Desktop
git clone --branch tag_v0.10.0 --recursive https://github.com/iovisor/bcc.git
mkdir -p bcc/build
cd bcc/build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
make
sudo make install

# Build Procmon
cd ~/Desktop
git clone https://github.com/Microsoft/Procmon-for-Linux
cd Procmon-for-Linux
mkdir -p build
cd build
cmake ..
make
```

git clone太慢的话，设个代理  

卡在这里了: `- Found Curses: /usr/lib/x86_64-linux-gnu/libcurses.so`  

&&&&&&& 待观望  


20210403  
