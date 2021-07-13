# pkgfile数据库更新失败问题

使用manjaro的时候，把默认shell换成了zsh，然后基本每次关机都会出现这样的错误：  
```
Failed to start pkgfile database update
```

参考这个链接解决了问题: https://forum.manjaro.org/t/failed-failed-to-start-pkgfile-database-update/31731/47  
问题就是pkgfile开机更新的时候还没联网，所以解决方法就是开机等会儿再更新  

修改这个文件: `/usr/lib/systemd/system/pkgfile-update.timer`，diff如下：  
```bash
diff pkgfile-update.timer.bak pkgfile-update.timer
5,7c5,7
< OnCalendar=daily
< AccuracySec=6h
< Persistent=yes
---
> OnBootSec=15min
> OnUnitActiveSec=1d
> Persistent=no
```

&&&&&&& 观察一段时间  

改完之后，不需要做别的，下次关机就没问题了  


2021/7/10  
