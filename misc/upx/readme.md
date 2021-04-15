# upx

## 简介
upx, the Ultimate Packer for eXecutables, 是一个支持多平台的压缩可执行文件的工具，下载解压即可使用  

网站: https://upx.github.io/  


## 使用说明
```
Usage: upx [-123456789dlthVL] [-qvfk] [-o file] file..

Commands:
  -1     compress faster                   -9    compress better
  -d     decompress                        -l    list compressed file
  -t     test compressed file              -V    display version number
  -h     give more help                    -L    display software license
Options:
  -q     be quiet                          -v    be verbose
  -oFILE write output to 'FILE'
  -f     force compression of suspicious files
  -k     keep backup files
file..   executables to (de)compress

Type 'upx --help' for more detailed help.

UPX comes with ABSOLUTELY NO WARRANTY; for details visit https://upx.github.io
```


## 使用示例
```bash
# 生成加壳文件 hello_upx.exe
upx -o hello_upx.exe hello.exe

# 脱壳
upx -d hello_upx.exe
# 脱壳 保留原文件
upx -k -d hello_upx.exe
```


## 报错
NotCompressibleException 错误原因: UPX无法处理40Kb以下的二进制文件。  

原链接: https://blog.csdn.net/whatday/article/details/104045395  
