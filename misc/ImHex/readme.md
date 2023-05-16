# ImHex

ImHex是一个开源的多平台十六进制编辑器，可以解析PE/ELF等类型文件，和010Editor功能类似，支持Windows、MacOS、Linux。  

官网地址: https://imhex.werwolv.net/  
官方文档: https://docs.werwolv.net/documentation/  
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

struct SECTION
{
    // 可以指定颜色
    u32 x [[color("FF0000")]];
    // 也可以添加注释，会在光标指向"模式数据"相应位置时悬浮显示
    u32 y[2] [[color("00FF00"), comment("this is y")]];
    u32 z;
};

struct THE_FILE
{
    HEAD head;
    char info[48];
    // 结构体作为数组时，需要显式设置数量，sizeof($) 表示已加载的数据长度
    SECTION section[(sizeof($)-sizeof(head)-sizeof(info))/16];
};

THE_FILE the_file @ 0x00;
```

输出信息：  
```r
#include <std/io.pat>

std::print("data len: {}", sizeof($));
std::print("data len: 0x{:0x}", sizeof($));
```


2022/8/8  
