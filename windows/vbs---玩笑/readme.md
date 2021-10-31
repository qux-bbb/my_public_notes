# vbs---玩笑

如果有汉字，需要记事本保存，编码选为ANSI  

```vb
Rem 无限循环小窗口，任务管理器关闭，使用记事本保存，选择 ANSI格式
do
msgBox "系统出现严重错误!"
loop
```

```vb
Rem 无限弹光驱
set wmp=createobject("wmplayer.ocx") 
set cd=wmp.cdromcollection.item(0) 
do 
cd.eject 
loop 
```

```vb
Rem 双击电脑爆炸    骗别人电脑爆炸，语音挺有意思的
Set s = CreateObject("sapi.spvoice") 
s.speak "你的电脑10秒后将会爆炸" 

i=10
do while i >= 0
s.speak i 
i=i-1 
loop 

s.speak "轰隆隆隆哈哈哈"
```

```vb
Rem  QQ消息轰炸 需要先打开一个聊天窗口，名字就是窗口上面的名字
Dim wsh,name,n
set wsh=createobject("wscript.shell") 
name = inputbox("请打开一个聊天窗口，输入窗口名字")
n = inputbox("请输入发送次数")

for i=1 to n  
wsh.AppActivate(name)
wsh.sendKeys i 
wsh.sendKeys "%s"
next 
```


2017/9/4  
