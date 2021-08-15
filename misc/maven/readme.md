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


2021/8/15  
