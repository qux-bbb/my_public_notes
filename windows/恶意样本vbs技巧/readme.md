# 恶意样本vbs技巧

部分文档样本为了逃避静态自启动检测，会用这样的形式：  
```vbs
Private Sub _
Document_open()
xiotteeslieh
End Sub
```

在 vbs 里，当一行过长时，下划线可以用作续行符  


---
2020/7/29  
