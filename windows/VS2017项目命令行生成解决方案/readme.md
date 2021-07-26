# VS2017项目命令行生成解决方案

搜索 `VS 2017的开发人员命令提示符` 打开，转到项目目录下，生成和清理命令如下：  
```bat
:: 生成解决方案
devenv hello.sln /Build

:: 清理解决方案
devenv hello.sln /Clean
```

可指定解决方案配置(Release或Debug)和平台(x86或x64)，命令举例如下：  
```
:: 生成解决方案
devenv hello.sln /Build "Release|x86"

:: 清理解决方案
devenv hello.sln /Clean "Release|x86"
```

参考链接：  
1. https://docs.microsoft.com/en-us/cpp/build/building-on-the-command-line?view=msvc-160
2. https://stackoverflow.com/questions/498106/how-do-i-compile-a-visual-studio-project-from-the-command-line


2021/7/22  
