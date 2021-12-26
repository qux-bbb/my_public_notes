# sysmon相关

sysmon, System Monitor, 可用来监控异常或敏感事件(进程操作、文件操作、注册表操作、网络请求等)，在SysinternalsSuite套件中。  

官方介绍: https://docs.microsoft.com/zh-cn/sysinternals/downloads/sysmon  
Freebuf介绍: https://www.freebuf.com/sectool/122779.html  


## 简单用法
```r
Install:                 sysmon -i [<configfile>]
Update configuration:    sysmon -c [<configfile>]
Uninstall:               sysmon -u [force]
```
查看使用说明: `sysmon ?`  
获取配置帮助: `sysmon -? config`  


## 监控日志
搜索"Event Viewer"，该路径 "Applications and Services Logs/Microsoft/Windows/Sysmon/Operational" 有对应的日志记录  
对应的中文 "事件查看器"，"应用程序和服务日志/Microsoft/......"  

日志文件：C:\Windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx  


## 配置相关
一个通过powershell脚本配置sysmon规则的工具  
https://github.com/darkoperator/Posh-Sysmon  

一个配置示例介绍  
https://github.com/SwiftOnSecurity/sysmon-config  

### 配置示例1  
需要注意ProcessTerminate虽然看起来是匹配，但没有任何过滤器，所以其实是不匹配任何进程终止事件(该性质可以用来快速获取或拒绝某一类信息)  
```xml
<Sysmon schemaversion="4.20">
    <!-- Capture all hashes -->
    <HashAlgorithms>*</HashAlgorithms>
    <EventFiltering>
        <!-- Log all drivers except if the signature -->
        <!-- contains Microsoft or Windows -->
        <DriverLoad onmatch="exclude">
            <Signature condition="contains">microsoft</Signature>
            <Signature condition="contains">windows</Signature>
        </DriverLoad>
        <!-- Do not log process termination -->
        <ProcessTerminate onmatch="include" />
        <!-- Log network connection if the destination port equal 443 -->
        <!-- or 80, and process isn't InternetExplorer -->
        <NetworkConnect onmatch="include">
            <DestinationPort>443</DestinationPort>
            <DestinationPort>80</DestinationPort>
        </NetworkConnect>
        <NetworkConnect onmatch="exclude">
            <Image condition="end with">iexplore.exe</Image>
        </NetworkConnect>
    </EventFiltering>
</Sysmon>
```

### 配置示例2  
该示例主要说明Group的用法  
```xml
<Sysmon schemaversion="4.20">
    <!-- Capture all hashes -->
    <HashAlgorithms>*</HashAlgorithms>
    <EventFiltering>
        <RuleGroup name="group 1" groupRelation="and">
            <ProcessCreate onmatch="include">
                <Image condition="contains">timeout.exe</Image>
                <CommandLine condition="contains">100</CommandLine>
            </ProcessCreate>
        </RuleGroup>
        <RuleGroup groupRelation="or">
            <ProcessTerminate onmatch="include">
                <Image condition="contains">timeout.exe</Image>
                <Image condition="contains">ping.exe</Image>
            </ProcessTerminate>
        </RuleGroup>
        <ImageLoad onmatch="include"/>
    </EventFiltering>
</Sysmon>
```

### 配置示例3  
sysmon默认是不记录注册表项和文件操作的，该示例增加对关心的注册表项和文件的监控  
```xml
<Sysmon schemaversion="4.81">
  <!-- Capture all hashes -->
  <HashAlgorithms>*</HashAlgorithms>
  <EventFiltering>
    <RegistryEvent onmatch="include">
      <Image condition="contains">msra</Image>
    </RegistryEvent>
    <FileCreate onmatch="include">
      <Image condition="contains">msra</Image>
    </FileCreate>
    <FileDelete onmatch="include">
      <Image condition="contains">msra</Image>
    </FileDelete>
    <FileDeleteDetected onmatch="include">
      <Image condition="contains">msra</Image>
    </FileDeleteDetected>
  </EventFiltering>
</Sysmon>
```


---
2019/6/14  
