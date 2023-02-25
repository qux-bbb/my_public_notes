# 将特定后缀文件恢复为未知打开方式

1. 备份注册表：按下“WIN+R”快捷键，运行“regedit”命令，打开"注册表编辑器",选中对应的注册表，点击右键，将其导出，误删时，可以用其恢复。  

2. 删除以下注册表项以及子项（左边导航框的整个项，而不是右边的一些值）：  
    ```r
    HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\[.文件后缀]
    HKEY_CURRENT_USER\Software\Classes\[文件后缀]_auto_file
    HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\[.文件后缀]
    HKEY_USERS\[SID]\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\[.文件后缀]
    ```
3.重启计算机。  


原链接: https://blog.csdn.net/xiao_song_shu/article/details/60871194  


2019/4/3  
