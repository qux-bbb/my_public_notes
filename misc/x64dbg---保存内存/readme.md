# x64dbg---保存内存

keywords: memory dump  

命令如下:  
```
savedata file_name, addr_start, data_size
```

举例如下:  
```
savedata memory_unity,0x00007FF7E0180000,0xa2000  
```

注意：  
dump命令是内存窗口显示指定地址内存: `dump edi` `dump 0x401010`  
sdump命令是栈窗口显示指定地址的栈信息: `sdump esp-0x10` `sdump 0x586640`  


20200410  
