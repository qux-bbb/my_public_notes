# maven

https://maven.apache.org/  

maven是一个项目构建管理工具。  

从这里可以搜各种包找到对应的maven依赖配置: https://search.maven.org/  


## Windows安装
安装之前需要确保JDK已安装并配置了java环境变量  

下载对应系统的压缩包，解压之后，把mvn所在文件夹路径添加到path即可  
验证安装：命令行执行`mvn --version`  


## IntelliJ IDEA使用
创建一个默认的Maven项目就好了，依赖在pom.xml中添加，举例：  
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" ...>
...
    <dependencies>
        <dependency>
            <groupId>com.j256.simplemagic</groupId>
            <artifactId>simplemagic</artifactId>
            <version>1.16</version>
        </dependency>
    </dependencies>
</project>
```

IntelliJ IDEA自带maven，也可以在设置中改成自己安装的maven。  

有时会遇到依赖无法下载的问题，原因是maven默认的库在国外，国内网络不好，可以把设置成国内的库  
File -> Settings -> Build, Execution, Deployment -> Build Tools -> Maven -> User settings file  
勾选后面的"Override"，然后编辑对应的文件，在mirrors节点下添加如下内容保存即可：  
```xml
<mirror>
    <id>alimaven</id>
    <name>aliyun maven</name>
    <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
    <mirrorOf>central</mirrorOf>        
</mirror>
```


参考链接: https://www.runoob.com/maven/maven-repositories.html  


2021/8/15  
