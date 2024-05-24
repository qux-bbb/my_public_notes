# APKLab

APKLab是一个vscode扩展，可以用来做APK逆向相关的事情。  

github地址: https://github.com/Surendrajat/APKLab  

github介绍：  
```
The ultimate Android RE experience right inside your VS Code.
APKLab seamlessly integrates the best open-source tools: Apktool, Jadx, uber-apk-signer, apk-mitm and more to the excellent VS Code so you can focus on app analysis and get it done without leaving the IDE.
```

机译汉语：  
```
VS Code内的终极Android RE体验。  
APKLab无缝集成了最好的开源工具：Apktool，Jadx，uber-apk-signer，apk-mitm等工具到VS Code，因此您可以专注于应用程序分析，而无需离开IDE即可完成。  
```

打开APK：  
Ctrl + Shift + P, 搜索选择"APKLab: Open an APK"  

重打包APK：  
打开apktool.yml，右键选择"APKLab: Rebuild the APK"，注意会自动签名，如果不要签名得单独用apktool操作  
打包时如果出现"error: attribute android:dataExtractionRules not found."错误，在AndroidManifest.xml中搜索删除"android:dataExtractionRules"属性重新打包即可  

基本使用方法详见: https://apklab.surendrajat.xyz/docs/user-guide/getting-started/  
