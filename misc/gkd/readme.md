# gkd

gkd 是一个基于 无障碍 + 高级选择器 + 订阅规则 的自定义屏幕点击 Android APP。  

官网: https://gkd.li/  
github地址: https://github.com/gkd-kit/gkd  

github介绍功能：  
- 点击跳过任意开屏广告/点击关闭应用内部任意弹窗广告, 如关闭百度贴吧帖子广告卡片/知乎回答底部推荐广告卡片
- 一些快捷操作, 如微信电脑登录自动同意/微信扫描登录自动同意/微信自动领取红包

类似李跳跳的手机自动点击工具，而且是开源的，很好用。  

官方不维护订阅，有一些第三方订阅：  
https://github.com/topics/gkd-subscription  
我用的AIsouler订阅: https://github.com/AIsouler/GKD_subscription  


信息来源: https://www.bilibili.com/video/BV1X94y1E7k8  


## 自己写订阅

写订阅前先把官方文档通读一遍，  
https://gkd.li/guide/what-is-gkd  

根据该仓库步骤搭建环境、写规则  
https://github.com/gkd-kit/subscription-template  

大概过程是：  
1. 搭建环境
2. 获取广告相关快照
3. 使用审查工具分析快照: https://i.gkd.li/
4. 写规则
5. 发布订阅

写规则可以参考其他第三方订阅。  


---
2023/12/7  
