# 压缩壳定位OEP思路

keywords: 脱壳 OEP  

OEP, Original Entry Point, 原始入口点  
压缩壳一般可以完整脱壳，这里记一下找OEP的思路。  

## 栈相关
压缩壳一般会保证EP和OEP位置的栈保持一致。  
根据这一特性，可以用ESP定律，也可以观察特殊指令使用(pushad/popad)来定位OEP。  

## 跳转
压缩壳恢复原程序后，会跳转到OEP继续执行。  
根据这一特性，可以搜索结尾附近的跳转指令，或者`push ret`这样的形式，跳转距离较大的，一般就是跳到OEP了。  

## 特征API调用
命令行程序开头一般会调用 `GetVersion` `GetCommandlineA` 这样的API；  
图形化程序开头一般会调用 `GetVersion` `GetModuleHandleA` 这样的API。  

根据这一特性，可以下API断点，然后在上方附近找OEP。  

## 导入表相关
一些压缩壳会隐藏导入表，恢复导入表一般会用2个API `LoadLibrary` `GetProcAddress`。  
根据这一特性，对这2个API下断点，然后在上方附近找OEP。  

## 调用API观察
类似特征API调用，不过不局限于某个API。  
使用API Monitor监控程序运行，或者用带API记录功能的沙箱运行程序，这样可以得到程序使用的API，这样之后，挑一个像开头会调用的API,下API断点，也可能找到OEP。  

## .text节跳转
如果压缩壳保留了.text段，可以在该段下执行断点，当.text段被执行，应该就到OEP了。  


参考: 《恶意代码分析实战》  


2021/8/29  
