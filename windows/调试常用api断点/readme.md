# 调试常用api断点

调试常用的api断点，持续收集中  
```r
# 写文件
Kernel32!WriteFile
Kernel32!WriteFileEx

# 复制文件
Kernel32!CopyFileA
Kernel32!CopyFileW
Kernel32!CopyFileExA
Kernel32!CopyFileExW

# 删除文件
Kernel32!DeleteFileA
Kernel32!DeleteFileW

# 网络请求
Wininet!InternetOpenUrlA
Wininet!InternetOpenUrlW
Ws2_32!getaddrinfo # 比较底层的api，和域名相关的都可以先用这个下断，然后看调用栈

# 执行命令
Shell32!ShellExecuteA
Shell32!ShellExecuteW
Shell32!ShellExecuteExA
Shell32!ShellExecuteExW

# 创建进程
Kernel32!CreateProcessA
Kernel32!CreateProcessW
```