# x64dbg---手动加载符号文件

```
Anyway I added the (currently) undocumented command symload which you can use like this:

symload app.exe, "C:\path\to\app.pdb"
symload app.exe, "C:\path\to\app.pdb", 1
The first command will load the PDB as normal from the disk (always manual now, it won't remember anything). The second command will load the PDB forced (if you know the PDB is right, but the validation data is missing or doesn't match).
```

第1种方法就是普通加载  
第2种方法是强制加载  

原链接: https://github.com/x64dbg/x64dbg/issues/2185  


2020/1/9  
