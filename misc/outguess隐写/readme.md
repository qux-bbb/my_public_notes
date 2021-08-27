# outguess隐写

Outguess是一种通用的隐写工具，允许将隐藏信息插入数据源的冗余位。数据源的性质与outguess的核心无关。该程序依赖于特定于数据的处理程序，这些处理程序将提取冗余位，并在修改后将其写回。  
目前只支持PPM(Portable Pixel Map)、PNM(Portable Any Map)和jpg图像格式，尽管只要提供了处理程序，outguess可以使用任何类型的数据。  

原github地址，已不维护: https://github.com/crorvick/outguess  
现在维护的地址: https://github.com/resurrecting-open-source-projects/outguess  

安装需要的工具：  
```
sudo apt install autoconf g++ make
```

根据说明编译：  
```sh
./autogen.sh
./configure --with-generic-jconfig
make
make install
```

google找到的使用方法：  
加密：  
```sh
outguess -k "my secret key" -d hidden.txt demo.jpg out.jpg
```
hidden.txt是要隐藏的文件, demo.jpg是用来隐藏信息的图片, out.jpg是有隐藏信息的图片  

解密：  
```
outguess -k "my secret key" -r out.jpg hidden.txt
```
解密之后，解密内容放在hidden.txt中，不一定是文本，什么信息都可以放  


参考网址: https://www.quora.com/How-do-you-use-the-OutGuess-steganography-program  


2017/3/18  
