# outguess隐写

Outguess是一种通用的隐写工具，允许将隐藏信息插入数据源的冗余位。数据源的性质与outguess的核心无关。该程序依赖于特定于数据的处理程序，这些处理程序将提取冗余位，并在修改后将其写回。  
目前载体只支持PPM(Portable Pixel Map)、PNM(Portable Any Map)和jpg图像格式，不支持png，需要密码。  
隐藏信息不限制类型。  

原github地址，已不维护: https://github.com/crorvick/outguess  
现在维护的地址: https://github.com/resurrecting-open-source-projects/outguess  

安装需要的工具：  
```r
sudo apt install autoconf g++ make
```

根据说明编译：  
```r
./autogen.sh
./configure --with-generic-jconfig
make
make install
```

google找到的使用方法：  
```sh
# 加密 隐藏
# hidden.txt是要隐藏的文件, demo.jpg是用来隐藏信息的图片, out.jpg是有隐藏信息的图片  
outguess -k "my secret key" -d hidden.txt demo.jpg out.jpg
# 解密 提取
outguess -k "my secret key" -r out.jpg hidden.txt
```
解密之后，解密内容放在hidden.txt中，不一定是文本，什么信息都可以放  


参考网址: https://www.quora.com/How-do-you-use-the-OutGuess-steganography-program  


2017/3/18  
