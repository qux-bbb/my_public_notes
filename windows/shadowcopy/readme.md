# shadowcopy

ShadowCopy用来备份Windows磁盘文件数据。  


## 删除ShadowCopy的方法
### 使用vssadmin
```cmd
vssadmin.exe Delete Shadows /All /Quiet
```

### 使用diskshadow  
```cmd
diskshadow.exe /s a.txt
```
a.txt内容为：  
```
delete shadows all
exit
```

来源：DoppelPaymer勒索软件  


2021/7/1  
