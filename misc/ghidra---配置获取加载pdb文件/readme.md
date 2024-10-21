# ghidra---配置获取加载pdb文件

在不配置"Symbol Server Config"的情况下，如果自己有pdb文件且和可执行程序在同一文件夹下，ghidra会自动加载相应pdb文件。  

分析Windows自身的可执行程序时，如果可以获取微软提供的符号文件，可以极大提高分析效率。  

打开一个可执行程序，界面操作 Edit -> Symbol Server Config：  
1. 给"Local Symbol Storage"选择一个文件夹用于存储pdb文件  
2. 在"Additional Search Paths"右侧点击加号图标，选择"Program's Import Location"，表示仍然尝试从导入文件的位置加载pdb  
3. 在"Additional Search Paths"右侧点击加号图标，选择"https://msdl.microsoft.com/download/symbols/"，表示前两步都没找到pdb时尝试从该地址获取pdb，这里不建议勾选"Trusted"，避免自己的程序也自动去微软服务器寻找pdb  

Analysis -> Auto Analyze...  
如果需要去微软服务器寻找pdb，点击"PDB Universal"，右侧勾选"Search untrusted symbol server"  
点击"Analyze"即可  

以vbscript.dll举例，分析之后entry函数内有"__DllMainCRTStartup"函数  
在之前选择的文件夹内可以找到vbscript.pdb文件夹  

Help -> Contents  
Ghidra Functionality -> Program Annotation -> PDB, 这里有详细的解释  


2024/9/3  
