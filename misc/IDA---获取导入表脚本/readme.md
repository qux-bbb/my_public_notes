# IDA---获取导入表脚本

idc脚本  
```c
//Imports.idc 列出当前程序的输入函数
//(c)  www.PEDIY.com 2000-2008

#include <idc.idc>

static GetImportSeg()
{
    auto ea, next, name;
    ea = FirstSeg();
    next = ea;
    while ( (next = NextSeg(next)) != -1) {
        name = SegName(next);
        if ( substr( name, 0, 6 ) == ".idata" ) break;
   }
   return next;
}

static main()
{
    auto BytePtr, EndImports;
    BytePtr = SegStart( GetImportSeg() );
    EndImports = SegEnd( BytePtr );
    Message(" \n" + "Parsing Import Table...\n");
    while ( BytePtr < EndImports ) {
        if (LineA(BytePtr, 1) != "") Message("\n" + "____" + LineA(BytePtr,1) + "____" + "\n");
        if (Name(BytePtr)!= "") Message(Name(BytePtr) + "\n");
        BytePtr = NextAddr(BytePtr);
    }
    Message("\n" + "Import Table Parsing Complete\n");
}

```


python脚本  
```python
#coding=utf-8
##《加密与解密》第四版
##code by zwfy
##http://bbs.pediy.com/thread-205578.htm

def GetImportSeg():
    ea=FirstSeg()
    next=ea
    count=0

    while next != BADADDR:  #判断是否为".idata"段
        next=NextSeg(next)
        name=SegName(next)
        if name[0:6]=='.idata':
            break
    return next

def main():
    BytePtr=SegStart(GetImportSeg()) #确定idata段VA
    EndImports=SegEnd(BytePtr)
    print('\n Parsing import table...') 
    while  BytePtr<EndImports:
        if LineA(BytePtr,1):
            print( '__'+LineA(BytePtr,1)+'__')
        if Name(BytePtr): 
            print(Name(BytePtr)+'\n')  #显示当前地址的函数名
        BytePtr=NextAddr(BytePtr)
    print('Import table parsing complete\n')

if __name__=='__main__':
    main()
```


来源：《加密与解密》  


2019/9/15  
