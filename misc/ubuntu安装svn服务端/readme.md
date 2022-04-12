# ubuntu安装svn服务端

### 安装

ubuntu 安装 subversion  
```r
apt install svn
```

查看 svn 版本  
```r
 svn --version
```

### 创建
创建版本库 runoob  
```r
svnadmin create /opt/svn/runoob
```

### 配置文件示例
1. svn服务配置文件svnserve.conf  
    ```r
    [general]
    anon-access = none
    auth-access = write
    password-db = /home/svn/passwd
    authz-db = /home/svn/authz
    realm = tiku 
    ```

2. 用户名口令文件passwd  
    格式  
    ```r
    <用户名> = <口令>
    ```
    示例  
    ```r
    [users]
    admin = admin
    thinker = 123456
    ```

3. 权限配置文件
    由svnserve.conf的配置项authz-db指定，默认为conf目录中的authz。该配置文件由一个`[groups]`配置段和若干个版本库路径权限段组成。  
    
    `[groups]`配置段中配置行格式如下：  
    ```r
    <用户组> = <用户列表>
    ```
    版本库路径权限段的段名格式如下：  
    ```r
    [<版本库名>:<路径>] 
    ```
    示例  
    ```r
    [groups]
    g_admin = admin,thinker
    
    [admintools:/]
    @g_admin = rw
    * =
    
    [test:/home/thinker]
    thinker = rw
    * = r
    ```

### 启动服务  
```r
svnserve -d -r 目录 --listen-port 端口号
-r: 配置方式决定了版本库访问方式。

--listen-port: 指定SVN监听端口，不加此参数，SVN默认监听3690
```

1. 方式一：-r直接指定到版本库(称之为单库svnserve方式)  
    ```r
    svnserve -d -r /opt/svn/runoob
    ```
    对应 authz 配置  
    ```r
    [groups]
    admin=user1
    dev=user2
    [/]
    @admin=rw
    user2=r
    ```
    使用类似这样的URL：svn://192.168.0.1/　即可访问runoob版本库  
2. 方式二：指定到版本库的上级目录(称之为多库svnserve方式)  
    ```r
    svnserve -d -r /opt/svn
    ```
    对应 authz 配置  
    ```r
    [groups]
    admin=user1
    dev=user2
    [runoob:/]
    @admin=rw
    user2=r
    
    [runoob01:/]
    @admin=rw
    user2=r
    ```
    使用类似这样的URL：svn://192.168.0.1/runoob　即可访问runoob版本库。

### 停止服务
最粗暴的方式，`ps aux | grep svn`，然后 kill 进程  

还有一个 kill 所有相关进程的命令  
```r
killall svnserve
```

完全来自： https://www.runoob.com/svn/svn-tutorial.html  


2020/7/9  
