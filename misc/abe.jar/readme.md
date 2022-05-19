# abe.jar

https://github.com/nelenkov/android-backup-extractor  

Utility to extract and repack Android backups created with adb backup (ICS+). Largely based on BackupManagerService.java from AOSP.  

文件类型为 "Android Backup, Compressed, Not-Encrypted" 时，可以用这个工具提取内容  

用法：  
```r
java -jar abe.jar pack|unpack|pack-kk
```

举例：  
```r
# 提取，in_file为源文件，out_file为处理结果
java -jar abe-all.jar unpack in_file out_file
```


2019/11/12  
