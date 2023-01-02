# 使用010editor增加空节区

```r
下载EXETemplate2.bt来解析

首先查看需要用到的2个值SectionAlignment和FileAlignment，即节对齐、文件对齐
ImageSize应为SectionAlignment的整数倍
SizeOfRawData应为FileAlignment的整数倍
struct IMAGE_NT_HEADERS FileHeader -> struct IMAGE_OPTIONAL_HEADER32 OptionalHeader -> DWORD SectionAlignment: 00100000(0x1000)
struct IMAGE_NT_HEADERS FileHeader -> struct IMAGE_OPTIONAL_HEADER32 OptionalHeader -> DWORD FileAlignment: 00020000(0x200)

空节区大小定为0x400字节(即SizeOfRawData，为FileAlignment的2倍)

更改总节区数：
struct PeHeader PEHead -> int16 NumSections: 0500 --> 0600
也就是将节区数加1

更改ImageSize：
struct OptionalHeader OptionalHead -> int32 ImageSize: 00100100 --> 00200100
0x011000 --> 0x012000

添加节区头：
struct SectionTable sec[5] -> char Name[8]: 2E68656C6C6F0000
struct SectionTable sec[5] -> int32 VirtualSize: 23010000
struct SectionTable sec[5] -> int32 VirtualAddress: 00100100
struct SectionTable sec[5] -> int32 SizeOfRawData: 00040000
struct SectionTable sec[5] -> int32 PointerToRawData: 00D00000
struct SectionTable sec[5] -> int32 PointerToRelocations: 00000000
struct SectionTable sec[5] -> int32 PointerToLinenumbers: 00000000
struct SectionTable sec[5] -> int16 NumberOfRelocations: 0000
struct SectionTable sec[5] -> int16 NumberOfLinenumbers: 0000
struct SectionTable sec[5] -> int32 Characteristics: 40000042
一个节区头大小为40字节，直接在最后一个节区头后面的0字节上修改
Name表示节区名，这里写的是 .hello
VirtualSize表示加载到内存时该节区实际数据的大小，经过测试发现，应该需要满足VirtualSize+VirtualAddress <= ImageSize，这里值为0x123，符合条件
VirtualAddress表示加载到内存时该节区相对于image base的起始地址，该地址应为上一节区的VirtualAddress+对齐之后的VirtualSize，上一节区的2个值分别为0x10000、0xE40，后者按SectionAlignment对齐为0x1000，最终VirtualAddress为0x11000
SizeOfRawData表示在磁盘中该节区大小，应为FileAlignment的整数倍，这里设置为0x400，因为这是最后一个节区，所以实际上不是整数倍也没关系，只要与实际大小相同即可
PointerToRawData表示在磁盘中该节区的起始地址，应为FileAlignment的整数倍，具体值应为上一节区的PointerToRawData+SizeOfRawData，为0xD000
PointerToRelocations、PointerToLinenumbers、NumberOfRelocations、NumberOfLinenumbers暂不关注，设为0即可
Characteristics设置了该节区的一些属性，比如可读、可写、可执行等，与上一节区设置相同即可

添加具体节区：
因为添加的是空节区，所以直接在最后加相应的0字节即可，这里在0xD000后添加了0x400个0字节

大功告成
```


2019/1/9  
