# Ghidra---使用python脚本

1. 下载脚本，放在一个文件夹里，如"D:\Ghidra_scripts"，建议不要放在Ghidra目录下，删除旧版本时可能会被删掉
2. Ghidra随便打开一个程序，即"CodeBrowser"窗口
3. 点击 Window -> Bundle Manager, 打开"Bundle Manager"窗口
4. 右键选择"Add bundle(s)"，添加包含脚本的文件夹

示例文件夹如下：  
```r
PS D:\> tree .\Ghidra_scripts\ /F /A
D:\GHIDRA_SCRIPTS
+---Ghidra_go_scripts
|       find_dynamic_strings.py
|       find_static_strings.py
|       go_func.py
|       README.md
|       type_extract.py
|
\---misc_scripts
        export_data_to_file.py
        SimpleStackStrings.py
```

添加Ghidra_go_scripts、misc_scripts文件夹后，"Bundle Manager"窗口多出2条记录：  
```r
D:/Ghidra_scripts/Ghidra_go_scripts
D:/Ghidra_scripts/misc_scripts
```

在"CodeBrowser"窗口点击 Window -> Script Manager, 打开"Script Manager"窗口  
在"Script Manager"窗口搜索相关脚本，右键选择"Run Script"即可执行  
如果脚本中包含"@menupath"，勾选脚本相应行最前面的可选框，就可以在相应菜单项执行脚本  
还可以右键选择"Assign Key Binding"，给脚本设置快捷键  

现在用到的一些脚本：  
```r
# 导出数据到文件
https://github.com/qux-bbb/ghidra-scripts/blob/master/export_data_to_file.py

# 给栈字符串添加注释
https://github.com/0x6d696368/ghidra_scripts/blob/master/SimpleStackStrings.py

# Golang相关脚本
https://github.com/getCUJO/ThreatIntel/tree/master/Scripts/Ghidra
```


2024/9/14  
