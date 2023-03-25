# AndroidStudio---无法实例化appComponentFactory

&&&&&&& 遗留问题，不知道怎么解决  

模拟器安装apk运行找不到androidx.core.app.CoreComponentFactory  
```r
2020-05-20 09:16:07.811 4394-4394/com.example.how_debug E/LoadedApk: Unable to instantiate appComponentFactory
    java.lang.ClassNotFoundException: Didn't find class "androidx.core.app.CoreComponentFactory" on path: DexPathList[[zip file "/data/app/com.example.how_debug-ASm76H8kKxCrB6vuA2aHlg==/base.apk"],nativeLibraryDirectories=[/data/app/com.example.how_debug-ASm76H8kKxCrB6vuA2aHlg==/lib/x86, /data/app/com.example.how_debug-ASm76H8kKxCrB6vuA2aHlg==/base.apk!/lib/x86, /system/lib, /system/product/lib]]
```

9.0 10.0 都不行，换成低版本的可以，试过 4.4 5.0  


2020/5/20  
