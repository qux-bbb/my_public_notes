# unidbg

unidbg 是一个基于 unicorn 的逆向工具，可以黑盒调用安卓和 iOS 中的 so 文件。  

github地址: https://github.com/zhkl0228/unidbg  

下载release文件，解压之后直接使用 IntelliJ IDEA 打开，  
打开后会自动执行maven构建，如果源是默认的会很慢，可以设置成国内源  
File -> Settings -> Build, Execution, Deployment -> Build Tools -> Maven -> User settings file  
勾选后面的"Override"，然后编辑对应的文件，在mirrors节点下添加如下内容保存即可(如果没有该文件直接创建文件把内容粘进去也行)：  
```xml
<mirror>
    <id>alimaven</id>
    <name>aliyun maven</name>
    <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
    <mirrorOf>central</mirrorOf>        
</mirror>
```

就先简单记一下，后面补充细节  


2023/2/12  
