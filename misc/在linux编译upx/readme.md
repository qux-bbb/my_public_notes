# 在linux编译upx

准备upx源码
----------
https://github.com/upx/upx  
下载upx源码  
```
git clone https://github.com/upx/upx.git
```

准备ucl
-------
http://www.oberhumer.com/opensource/ucl/  
下载ucl  
http://www.oberhumer.com/opensource/ucl/download/ucl-1.03.tar.gz  
编译  
```
./configure
make
```
导出环境变量  
```
export UPX_UCLDIR=$HOME/local/src/ucl-1.03  
```

准备lzma-sdk
--------
进入upx的src目录  
https://github.com/upx/upx-lzma-sdk  
下载并重命名  
```
git clone https://github.com/upx/upx-lzma-sdk.git
mv upx-lzma-sdk lzma-sdk
```

upx编译
-------
在upx的Makefile文件所在目录下  
设置脚本可执行  
```
chmod +x src/stub/scripts/check_whitespace.sh
```
编译  
```
make all
```

src下的upx.out即为编译好的可执行文件  


2020/8/14  
