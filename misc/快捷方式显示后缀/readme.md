# 快捷方式显示后缀

系统默认状态是隐藏快捷方式后缀名的。你可以这样操作：  
管理员方式打开 cmd，执行以下命令：  
```bat
reg delete HKCR\lnkfile /v NeverShowExt /f
taskkill explorer
```

如果想恢复，把 `delete` 改成 `add`，重新执行一遍即可  


原链接：https://zhidao.baidu.com/question/135922638.html  


2020/6/30  
