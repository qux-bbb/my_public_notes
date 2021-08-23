# AppImage

官网: https://appimage.org/  

可以把linux应用打包成单个文件，在大多数linux发行版运行。  

从源码打包XHash的示例脚本：  
```sh
#!/bin/sh

linuxdeploy=~/Downloads/linuxdeploy-x86_64.AppImage

mkdir linux_build
cd linux_build
qmake ../src
make -j$(nproc)
make install INSTALL_ROOT=AppDir
$linuxdeploy -d ../xhash.desktop -i ../src/xhash.png --appdir AppDir --output appimage --plugin qt
```

可能遇到的问题和解决方法：  
1. 图标尺寸问题
   ```
   ERROR: Icon hello.ico has invalid x resolution: 255 
   ERROR: Valid resolutions for icons are: 8x8, 16x16, 20x20, 22x22, 24x24, 28x28, 32x32, 36x36, 42x42, 48x48, 64x64, 72x72, 96x96, 128x128, 160x160, 192x192, 256x256, 384x384, 480x480, 512x512 
   ```
   解决方法：把图标尺寸调整为列出的一种即可  
2. 找不到可执行文件
   ```
   ERROR: Could not find suitable executable for Exec entry: hello
   ```
   解决方法：在hello.pro文件中把unix对应的 `target.path` 的值改成 `/usr/bin`
3. 找不到qt平台插件
   ```
   qt.qpa.plugin: Could not find the Qt platform plugin "xcb" in ""
   This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
   ```
   解决方法：需要下载linuxdeploy的qt插件，设置可执行权限，然后在linuxdeploy命令后添加`--plugin qt`即可


2021/7/19  
