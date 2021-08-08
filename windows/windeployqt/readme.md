# windeployqt

直接运行qt生成的release下的exe会提示缺少依赖，使用qt自带的windeployqt可以找到并复制相关依赖文件  

最简单方法：  
1. 复制exe文件到一个空文件夹，打开QT命令行  
   - 如果是32位的release，打开 `Qt 5.15.2 (MSVC 2019 32-bit)`  
   - 如果是64位的release，打开 `Qt 5.15.2 (MSVC 2019 64-bit)`  
2. 切换目录到上面的文件夹里，执行命令：`windeployqt <exe_name>`  

这样之后，exe就能正常运行了  


2021/8/8  
