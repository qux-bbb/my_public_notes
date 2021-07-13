# 翻译---ubuntu---ftp服务器

原链接：https://help.ubuntu.com/lts/serverguide/ftp-server.html  

- [翻译---ubuntu---ftp服务器](#翻译---ubuntu---ftp服务器)
- [FTP 服务器](#ftp-服务器)
  - [vsftpd - FTP 服务器安装](#vsftpd---ftp-服务器安装)
  - [匿名 FTP 配置](#匿名-ftp-配置)
  - [认证 FTP 配置](#认证-ftp-配置)
  - [安全 FTP](#安全-ftp)
  - [引用](#引用)


# FTP 服务器
FTP, File Transfer Protocol, 文件传输协议是一种用于在计算机之间下载文件的 TCP 协议。以前 FTP 协议 也用于上传，但由于该协议不使用加密，明文的用户凭证和数据很容易被截获。如果想要找一种可以安全上传下载文件的方式，可以参阅 [远程管理](https://help.ubuntu.com/lts/serverguide/remote-administration.html) 中的 OpenSSH 部分。  

FTP 以 `客户端/服务端 `模式运作。服务端组件被称为 FTP 守护进程（FTP daemon），它会持续监听来自客户端的FTP请求。在收到请求时，它会验证登录并设置连接。在会话期间，它会执行FTP客户端发送的任何命令。  

可以设置两种 FTP 服务器的访问方式：  
1. 匿名
2. 认证

在匿名模式下，客户端可以使用名为 `anonymous `或 `ftp` 的默认账户访问FTP服务器，使用邮件地址作为密码。在认证模式下，用户必须有账户和密码。认证模式实际很不安全（凭证和数据明文传输），除非情况特殊，否则不应该使用。如果想要安全传输文件，可以参阅 OpenSSH-Server 中的 SFTP。用户对 FTP 服务器目录和文件的访问权限取决于登录时的帐户拥有的权限。通常情况下，FTP 守护进程将隐藏 FTP 服务器的根目录，转而使用 FTP 主目录。这样可以在远程会话中隐藏文件系统的其余部分。  


## vsftpd - FTP 服务器安装
vsftpd 是 Ubuntu 中常用的 FTP 守护进程，很容易安装、设置和维护。要安装 vsftpd，可以运行以下命令：
```sh
sudo apt install vsftpd
```


## 匿名 FTP 配置
默认情况下，vsftpd 配置为不允许匿名下载。如果要启用匿名下载，可以编辑 `/etc/vsftpd.conf`：
```
anonymous_enable=Yes
```
在 vsftpd 安装过程中，会创建一个名为 `ftp` 的用户，该用户的主目录为 `/srv/ftp`，这是默认的 FTP 目录。  
如果要修改默认 FTP 目录，比如说改成 `/srv/files/ftp`，只需要创建这个目录并更改 ftp 用户的主目录：
```
sudo mkdir /srv/files/ftp
sudo usermod -d /srv/files/ftp ftp 
```
修改之后重启 vsftpd 使配置生效：
```sh
sudo systemctl restart vsftpd.service
```
现在，就可以把想要分享的任何文件或文件夹复制到 ftp 用户的主目录下，小伙伴们就可以通过匿名 FTP 访问了。  


## 认证 FTP 配置
默认情况下，vsftpd 配置为用户经过身份验证才可以下载文件。如果希望用户能够上传文件，可以编辑 `/etc/vsftpd.conf`：
```
write_enable=YES
```
需要重启 vsftpd 使配置生效：
```sh
sudo systemctl restart vsftpd.service
```
现在，当用户登录到 FTP 时，就可以在他们的主目录中做下载、上传、创建目录等操作了。  
默认情况下，vsftpd 不允许匿名用户将文件上传到 FTP 服务器。要修改该设置，应取消注释配置文件中的以下行，并重新启动vsftpd：
```
anon_upload_enable=YES
```
**允许匿名 FTP 上传会有很大的安全风险。如果服务器可以直接从 Internet 访问，最好不要启用匿名上传。**  

配置文件包含很多配置参数。每个参数的相关信息在配置文件中都有说明。也可以查询 man page，`man 5 vsftpd.conf`，了解每个参数的详细信息。  


## 安全 FTP
`/etc/vsftpd.conf` 配置文件中有一些选项可以让 vsftpd 更安全。例如，可以通过取消以下行的注释来限制用户只能访问主目录：
```
chroot_local_user=YES
```

还可以限制特定用户列表只能访问其主目录：
```
chroot_list_enable=YES
chroot_list_file=/etc/vsftpd.chroot_list
```
取消上述两行的注释后，创建一个 `/etc/vsftpd.chroot_list` 文件，每行写一个用户名，然后重新启动 vsftpd：
```sh
sudo systemctl restart vsftpd.service
```

此外， `/etc/ftpusers`文件可以记录不允许访问 FTP 的用户列表。默认列表包括 `root`、`daemon`、`nobody` 等。要禁用其他用户的 FTP 访问权限，只需将它们添加到列表中。  

FTP 也可以使用 FTPS 进行加密。与 SFTP 不同，FTPS 是基于安全套接字层 （SSL，Secure Socket Layer）的 FTP。SFTP 所指的 FTP 像一个建立在加密SSH连接上的会话。一个主要区别是 SFTP 的用户需要在系统上具有一个shell帐户，而不是 nologin shell。向所有用户提供 shell 可能不是某些环境（如共享 Web 主机）的理想选择。不过，还是可以将此类帐户限制为仅 SFTP 并禁用 shell 交互的，有关详细信息，可以参阅 OpenSSH-Server。  
要配置FTPS，可以编辑 `/etc/vsftpd.conf`，在末尾添加：
```
ssl_enable=Yes
```
还需要添加证书和密钥相关的选项：
```
rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
```
默认情况下，这些选项会被设置为 ssl-cert 包提供的证书和密钥。在生产环境中，这些证书应替换为为特定主机生成的证书和密钥。有关证书的详细信息，可以参阅 [证书](https://help.ubuntu.com/lts/serverguide/certificates-and-security.html)。  
现在重新启动 vsftpd，非匿名用户将被强制使用 FTPS：
```sh
sudo systemctl restart vsftpd.service
```

为了允许具有 `/usr/sbin/nologin` shell 的用户访问 FTP，但不允许访问 shell，可以编辑 `/etc/shells` 添加 nologin shell：
```
# /etc/shells: valid login shells
/bin/csh
/bin/sh
/usr/bin/es
/usr/bin/ksh
/bin/ksh
/usr/bin/rc
/usr/bin/tcsh
/bin/tcsh
/usr/bin/esh
/bin/dash
/bin/bash
/bin/rbash
/usr/bin/screen
/usr/sbin/nologin
```
这是必需的，因为默认情况下，vsftpd 使用 PAM 进行身份验证，并且 `/etc/pam.d/vsftpd` 配置文件包含：
```
auth    required        pam_shells.so
```
shells PAM 模块会限制对 `/etc/shell` 文件中列出的 shell 的访问。  


大多数流行的 FTP 客户端可以配置为使用 FTPS 进行连接。lftp命令行 FTP 客户端也能够使用 FTPS。  


## 引用
1. 更多详细信息，可以参阅 [vsftpd 网站](http://vsftpd.beasts.org/vsftpd_conf.html)。
2. 了解更详细的 /etc/vsftpd.conf 选项，可以参阅 [vsftpd.conf man page](http://manpages.ubuntu.com/manpages/bionic/en/man5/vsftpd.conf.5.html)。


2020/3/28  
