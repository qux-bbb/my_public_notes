# volatility---基本用法

Keyword: forensic 取证  

1. 查看基本信息，根据查到的信息确定profile的值  
    ```bash
    volatility -f BOOM-6452e9b9.vmem imageinfo 
    ```
2. 指定profile，使用具体的命令  
   iehistory 是看浏览器的进程，pslist是ps命令(也可以用psscan)
    ```bash
    volatility -f BOOM-6452e9b9.vmem --profile=Win7SP1x64 iehistory 
    ```
3. 查找并dump相应进程的可执行程序  
    ```bash
    root@kali:~/Desktop# volatility -f mem.raw --profile=Win7SP1x86_BBA98F40 pslist | grep notepad
    Volatility Foundation Volatility Framework 2.5
    0x8398dad8 notepad.exe            3524   1636      2       61      1      0 2019-09-16 13:53:51 UTC+0000                                 
    root@kali:~/Desktop# volatility -f mem.raw --profile=Win7SP1x86_BBA98F40 procdump -p 3524 -D ./
    Volatility Foundation Volatility Framework 2.5
    Process(V) ImageBase  Name                 Result
    ---------- ---------- -------------------- ------
    0x8398dad8 0x00be0000 notepad.exe          OK: executable.3524.exe
    ```
4. 查找并dump进程内存  
    ```bash
    root@kali:~/Desktop# volatility -f mem.raw --profile=Win7SP1x86_BBA98F40 pslist | grep notepad
    Volatility Foundation Volatility Framework 2.5
    0x8398dad8 notepad.exe            3524   1636      2       61      1      0 2019-09-16 13:53:51 UTC+0000                                 
    root@kali:~/Desktop# volatility -f mem.raw --profile=Win7SP1x86_BBA98F40 memdump -p 3524 -D ./
    Volatility Foundation Volatility Framework 2.5
    ************************************************************************
    Writing notepad.exe [  3524] to 3524.dmp
    ```
5. 查找并dump文件  
    ```bash
    root@kali:~/Desktop# volatility -f mem.raw --profile=Win7SP1x86_BBA98F40 filescan | grep key
    Volatility Foundation Volatility Framework 2.5
    0x000000001e10a868      1      1 ------ \Device\NamedPipe\keysvc
    0x000000001e10a920      2      1 ------ \Device\NamedPipe\keysvc
    0x000000001e10aa90      1      1 ------ \Device\NamedPipe\keysvc
    0x000000001efb9370      1      0 R--rw- \Device\HarddiskVolume2\Users\lethal\Desktop\key
    root@kali:~/Desktop# volatility -f mem.raw --profile=Win7SP1x86_BBA98F40 dumpfiles -Q 0x000000001efb9370 -D ./
    Volatility Foundation Volatility Framework 2.5
    DataSectionObject 0x1efb9370   None   \Device\HarddiskVolume2\Users\lethal\Desktop\key
    ```


部分感觉有用的插件命令  
```
clipboard      	Extract the contents of the windows clipboard
cmdline        	Display process command-line arguments
cmdscan        	Extract command history by scanning for _COMMAND_HISTORY
consoles       	Extract command history by scanning for _CONSOLE_INFORMATION
deskscan       	Poolscaner for tagDESKTOP (desktops)
dumpcerts      	Dump RSA private and public SSL keys
dumpfiles      	Extract memory mapped and cached files
dumpregistry   	Dumps registry files out to disk 
editbox        	Displays information about Edit controls. (Listbox experimental.)
filescan       	Pool scanner for file objects
hashdump       	Dumps passwords hashes (LM/NTLM) from memory
imageinfo      	Identify information for the image
malfind        	Find hidden and injected code
memdump        	Dump the addressable memory for a process
notepad        	List currently displayed notepad text
procdump       	Dump a process to an executable file sample
pslist         	Print all running processes by following the EPROCESS lists 
psscan         	Pool scanner for process objects
pstree         	Print process list as a tree
psxview        	Find hidden processes with various process listings
timeliner      	Creates a timeline from various artifacts in memory 
truecryptmaster	Recover TrueCrypt 7.1a Master Keys
truecryptpassphrase	TrueCrypt Cached Passphrase Finder
truecryptsummary	TrueCrypt Summary
windows        	Print Desktop Windows (verbose details)
wintree        	Print Z-Order Desktop Windows Tree
```

官网: https://www.volatilityfoundation.org/  
github地址: https://github.com/volatilityfoundation/volatility  

2019/10/22  
