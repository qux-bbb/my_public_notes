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

maven构建完成后，在一些测试文件里的类声明处或者主函数处的左边会有绿色的执行箭头，点击执行可以查看效果  
举例: unidbg-android/src/test/java/com/bytedance/frameworks/core/encrypt/TTEncrypt.java  
```r
...
00E0: A0 E0 3B 4D AE 2A F5 B0 C8 EB BB 3C 83 53 99 61    ..;M.*.....<.S.a
00F0: 17 2B 04 7E BA 77 D6 26 E1 69 14 63 55 21 0C 7D    .+.~.w.&.i.cU!.}
^-----------------------------------------------------------------------------^
Find native function Java_com_bytedance_frameworks_core_encrypt_TTEncryptUtils_ttEncrypt => RX@0x40000f19[libttEncrypt.so]0xf19
```

就先简单记一下，后面补充细节  


2023/2/12  
