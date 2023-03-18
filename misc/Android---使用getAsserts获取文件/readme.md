# Android---使用getAsserts获取文件

assets文件夹应该放在跟Java和res同级目录下  
```r
main/
├── AndroidManifest.xml
├── assets
│   ├── ming.txt
│   └── xing.txt
├── ic_launcher-web.png
├── java
│   └── com
└── res
    ├── drawable
    ├── drawable-v24
    ├── layout
    ├── mipmap-anydpi-v26
    └── values
```

相关代码：  
```java
AssetManager assetManager = getAssets();
InputStream is = assetManager.open(fileName);
int length = 0;
length = is.available();
byte[]  buffer = new byte[length];
is.read(buffer);
fileContent = new String(buffer, "utf8");
```

参考链接: http://www.07net01.com/2015/08/918160.html  


2016/10/1  
