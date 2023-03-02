# windows---改文件创建和修改时间

keywords: 创建时间 修改时间 访问时间  

使用powershell命令可以方便地查看修改文件的时间属性。  

查看文件的所有属性：  
```powershell
Get-Item test.txt | Format-List *
<#
列举时间属性如下：  
...
CreationTime      : 2023/3/2 22:19:58
CreationTimeUtc   : 2023/3/2 14:19:58
LastAccessTime    : 2023/3/2 22:19:58
LastAccessTimeUtc : 2023/3/2 14:19:58
LastWriteTime     : 2023/3/2 22:19:58
LastWriteTimeUtc  : 2023/3/2 14:19:58
...
#>
```

修改时间属性举例：  
```powershell
(Get-Item test.txt).CreationTime = '2020/3/2 22:19:58'
```


2019/7/12  
