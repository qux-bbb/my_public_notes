# virustotal的api使用

virustotal集成了大部分静态杀毒引擎和一些沙箱，可以快速检测文件、ip、域名等信息。  

官网: https://www.virustotal.com  

网站提供的api使得自动化和大批量操作成为可能，这里简单记录一下api使用经验。  

官方提供了各种api说明，可以在这里查看: https://developers.virustotal.com/reference/overview  
- Introduction, 简单介绍
- API Objects, 返回信息的字段含义介绍
- Universal API Endpoints, api接口的介绍和使用示例
- VT Enterprise, 企业(商业)用户可以使用的高级api接口介绍和使用示例
- VT Hunting, 威胁狩猎相关api接口介绍和使用示例
- VT Feed, 周期性获取威胁信息的api接口介绍和使用示例
- VT Augment, 集成到第三方程序的推荐方式介绍，包含部分api接口介绍和使用示例
- VT Monitor, 分析白文件，减少可能的误报，包含api接口介绍和使用示例
- VT Alerts, 监测到不正常行为时发起警告，包含api接口介绍和使用示例

官方提供了各种语言的库，使开发更容易，这是python的库：  
https://github.com/VirusTotal/vt-py  

如果找不到要请求的url，在页面打开相关内容，删除url的前半部分"https://www.virustotal.com/gui", 剩下的就是要请求的url  


2022/2/14  
