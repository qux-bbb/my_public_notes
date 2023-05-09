# ImHex

ImHex是一个开源的多平台十六进制编辑器，可以解析PE/ELF等类型文件，和010Editor功能类似，支持Windows、MacOS、Linux。  

官网地址: https://imhex.werwolv.net/  
github地址: https://github.com/WerWolv/ImHex  

pattern可用来标注含义、上色，ImHex内置了多个pattern文件，这是一个简单的示例：  
```r
struct HEAD 
{
    char a;
    char b;
    char c[14];
    u8 d[0x10];
};

HEAD head @ 0x00;
char message[39] @ 0x4E;
```


2022/8/8  
