# java---获取文件hash

```java
Path path = new File("D:\\hello.pdf").toPath();

String hashTypeList[] = {"MD5", "SHA1", "SHA256"};

byte[] b = Files.readAllBytes(path);
for(String hashType : hashTypeList) {
    byte[] hash = MessageDigest.getInstance(hashType).digest(b);
    String fx = "%0" + (hash.length * 2) + "x";
    String hashResult = String.format(fx, new BigInteger(1, hash));
    System.out.println(hashResult);
}
```
结果：  
```
25ac711a5e8d9d02e064d03133281a07
8febdc13e4c71b51690f45d5f6db64fd310c7ffa
5bc75ba4fc99233cfa0b07ddf4a53299fcca0338194109b9e4f76d21806975ab
```


原链接: https://stackoverflow.com/questions/304268/getting-a-files-md5-checksum-in-java  


2021/4/29  
