# linux---通过进程恢复被删除文件

linux下的恶意程序有时候会删除自身，可以通过这种方法回复被删除的文件。  

```r
cat /proc/$PID/exe > recoverd_file
```

原链接：  
挖矿木马自助清理手册 https://cloud.tencent.com/developer/article/1834731  


2023/3/5  
