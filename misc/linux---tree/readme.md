tree可以把目录中的文件和文件夹以树的形式列出来。  

最简单命令：  
```
tree
```

限制层数为1：  
```
tree -L 1
```

举例：  
`tree -L 1`：  
```
.
├── bin
├── Desktop
├── Documents
├── Downloads
├── examples.desktop
├── Music
├── Pictures
├── Public
├── randomize_va_space~
├── Templates
└── Videos

9 directories, 2 files
```
`tree -L 2`：  
```
.
├── bin
├── Desktop
│   ├── exp.py
│   ├── level5
│   ├── peda-session-level5.txt
│   ├── pwninit
│   ├── ret2libc3
│   ├── static
│   └── static.c
├── Documents
├── Downloads
│   └── code_1.51.1-1605051630_amd64.deb
├── examples.desktop
├── Music
├── Pictures
├── Public
├── randomize_va_space~
├── Templates
└── Videos

9 directories, 10 files
```