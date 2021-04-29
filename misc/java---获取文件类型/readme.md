# java---获取文件类型

效果不太好，识别exe有问题  

```java
Path path = new File("D:\\hello.pdf").toPath();
String mimeType = Files.probeContentType(path);
System.out.println(mimeType);
```
结果：  
```
application/pdf
```


原链接: https://www.baeldung.com/java-file-mime-type  


2021/4/29  
