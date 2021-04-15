64位系统安装32位运行库和编译库  

## kali
```sh
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install lib32z1
sudo apt install lib32ncurses5
sudo apt install gcc-multilib
```
lib32ncurses5 这个库已经没有了，但好像不影响32位的功能  


## ubuntu
```sh
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install libc6:i386 libncurses5:i386 libstdc++6:i386
sudo apt install gcc-multilib
```
