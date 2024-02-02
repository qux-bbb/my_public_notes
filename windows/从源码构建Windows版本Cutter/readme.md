# 从源码构建Windows版本Cutter

https://cutter.re/docs/building.html#building-on-windows  

把系统语言切换成美国英文(所有能看到语言配置的地方都显式配置成美国英文，这样才能编译过)  

安装依赖工具  
注意点：  
1. 安装git
2. VS勾选VC++安装即可
3. CMake安装时注意选择添加到系统路径
4. Meson可以同时装Ninja了，不需要再另外装Ninja
5. 建议最后装QT，需要准备账号，而且安装太慢了，版本选择链接里提到的

安装代理(因为build的时候需要从github下载内容)  

执行如下面命令进行构建：  
```r
git config --global http.proxy http://127.0.0.1:10809
git config --global https.proxy http://127.0.0.1:10809
git clone --recurse-submodules https://github.com/rizinorg/cutter
cd cutter

# 注意Qt路径需要改成真实的路径
# First, set CMAKE_PREFIX_PATH to Qt5 intallation prefix
$Env:CMAKE_PREFIX_PATH = "C:\Qt\5.15.2\msvc2019_64\lib\cmake\Qt5"

# Then, add the following directory to your PATH
$Env:Path += ";C:\Qt\5.15.2\msvc2019_64\bin"

# Build Cutter
cmake -B build
cmake --build build
```

构建完成后，执行命令启动编译好的Cutter：  
```r
.\build\Debug\cutter.exe
```

当前构建版本必须设置环境变量才能正常执行Cutter，如果重新打开窗口，需要像构建时一样设置环境变量  

&&&&&&& 群里有人提到如果不设置环境变量，需要自己复制相关dll到文件夹里  

&&&&&&& 没有反编译器  


2024/1/22  
