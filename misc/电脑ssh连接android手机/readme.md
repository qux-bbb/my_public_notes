将电脑和手机连到同一WiFi，手机安装termux  

在termux中操作如下：  
1. 安装ssh: `pkg install openssh`
2. 查看当前用户名: `whoami`, 假设用户名为 `hello`
3. 设置`hello`的密码: `passwd hello`, 假设密码为`hello_pass`
4. 启动ssh服务: `sshd`
5. 查看当前ip: `ip addr`, 假设ip为`1.2.3.4`

在电脑命令行下执行命令: `ssh hello@1.2.3.4 -p 8022`, 连接成功  