# Aegisub

字幕组一般用Aegisub做字幕，这是一个开源的工具，但最新一次release是在2014年，可以制作高级字幕，可以导出字幕。  

github地址: https://github.com/Aegisub/Aegisub  

便携版只有英文，安装版可以切换各种语言。  

## 一些快捷键
```r
A       向左卷动音频显示
F       向右卷动音频显示
S/Space 播放选择的音频
Q       播放所选部分之前500毫秒
W       播放所选部分之后500毫秒
E       播放所选部分头500毫秒
D       播放所选部分末500毫秒
G/Enter 提交所有在波形上对时间的更改(即确认当前段，开始下一段)
```

## 其它设置
音频，这里我将"显示频谱"改为"显示波形"，不熟练的话这个更容易识别边界  
计时->时间后续处理器，取消勾选"开始提前"，这样声音开始字幕就会出现  
查看->选项->音频->默认计时长度(毫秒)，这里的默认值是2000，感觉太短了，我设置成了16000  

## 自动化脚本
Aegisub的"自动化"功能可以用lua脚本处理字幕，用下面这两个示例改改就行了  
Add Italics to Selected Lines: https://unanimated.github.io/ts/lua/add_italics.lua  
Modify Font Size for Mocha: https://unanimated.github.io/ts/lua/font_refactor_simple.lua  

自动化->自动化->载入，就可以用了，如果修改了脚本，需要"重新载入"才生效  

## 参考链接
https://www.bilibili.com/video/BV1ps411b7as  
https://unanimated.github.io/ts/lua/ts-auto_tutorial.htm  


---
2022/2/8  
