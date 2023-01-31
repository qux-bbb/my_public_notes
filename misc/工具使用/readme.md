# 工具使用

一些工具的记录  


## CoagulaLight
**功能：** 可以将图片转为音频  
**用法：** 把编辑好的图片拖进去, 或者直接在里面新建图片，然后点击第二个齿轮按钮（Render image without blue/noise）（第一个齿轮按钮也可以，第二个效果好一些），另存为即得到隐写图片的音频文件  
官网及下载: https://www.abc.se/~re/Coagula/Coagula.html  

## audacity
**功能：** 可以分析音频文件，看波形图、频谱图  
**用法：** 打开音频文件，点击文件名右边的下三角，选择波形、频谱图选项即可  
官网及下载: http://www.audacityteam.org/  

## binwalk
**功能：** 分析提取隐藏文件  
**用法：** `binwalk -eM 文件名`  

## foremost
**功能：** 分析提取隐藏文件  
**用法：** `foremost 文件名`  

## strings
**功能：** 列出文件中字符串  
**用法：** `strings -n 字符串最小长度 文件名`  

## Steganography  
支持4种方法图片隐写：尾部追加、LSB替换、LSB-PM1、LSB水印  
我下载的少一张背景图片，自己根据提示随便加一张就可以了  
github项目链接: https://github.com/DaPangR/Steganography  

## everything
**功能：** 搜索电脑上的所有文件，比windows自己的文件搜索快多了  
官网及下载: http://www.voidtools.com  

## Snipaste
**功能：**  截图、贴图软件，神器  
**快捷键:** F1→截图，F2→贴图，文字转图片→全选后复制，F2即可贴图  
官网及下载: https://zh.snipaste.com  

## HxD
**功能：** 十六进制编辑工具，小巧免费  
官网及下载: https://mh-nexus.de/en/downloads.php?product=HxD20  

## Stegsolve
**功能：** 图层隐写查看，分析图片信息，LSB隐写分析工具  
下载地址: http://www.caesum.com/handbook/Stegsolve.jar  

## MP3Stego
**功能：**  MP3隐写工具  
`encode -E data.txt -P pass sound.wav sound.mp3`  
`decode -X -P pass sound.mp3`  
官网及下载: http://www.petitcolas.net/steganography/mp3stego/  


## john
**功能：** 密码hash破解软件，有彩虹表就很强大，根据`/etc/shadow`此文件的信息，可以破解出原密码  
`John -worlist=doc.txt shadow` (字典自己找)  
`john –show shadow` 查看破解的密码  

## alternatestreamview
**功能：**  ntfs流文件读取工具，检测可能存在流文件的文件夹即可  

## yafu
**功能：** 可以用来分解RSA算法中的n  
**用法：**  `factor(n)`  
下载地址: https://sourceforge.net/projects/yafu/  

## openssl
**功能：** 加密解密工具，可以用来生成RSA公钥私钥，加解密文件  
使用方法见: http://www.cnblogs.com/aLittleBitCool/archive/2011/09/22/2185418.html  

## libre office
**功能：** 跨平台，开源免费的类似office套件的软件集合，用起来卡，只建议在linux平台下使用......  
官网: http://www.libreoffice.org/  

## dnSpy
.net调试和反编译工具  
Github地址: https://github.com/dnSpyEx/dnSpy  

## jadx
Android反编译工具  
Github地址: https://github.com/skylot/jadx  

## OllyDbg
pe动态调试工具  
官网: http://www.ollydbg.de/  

## x64dbg
开源好用的pe动态调试工具  
官网: https://x64dbg.com/  

## nc
被誉为网络安全界的瑞士军刀  
windows版本下载网址: https://joncraton.org/blog/46/netcat-for-windows/  

## IceChat  
一款windows系统下IRC聊天客户端  
官网: http://www.icechat.net/site/  

## 7z
最简洁的压缩解压工具，附带的文件hash小工具也很方便  
官网: https://www.7-zip.org/  

## SpaceSniffer
磁盘空间占用情况查看，图形化，直观  
官网: http://www.uderzo.it/main_products/space_sniffer/index.html  


---
`更新于 20190418`  
2017/10/18  
