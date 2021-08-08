# 写XHash用到的资料

XHash是一个模仿hash.exe的工具，一开始的目的是想做一个开源、跨平台的hash.exe，正好也想学习一下qt。  
做的过程发现qt生成的程序比较大，而且生成单个exe的方法不是太好，所以虽然有基本的功能，但是体积太大，权当练习qt了。  
链接在这里: https://github.com/qux-bbb/XHash  

下面是做的时候参考的资料：  
1. 剪贴板操作示例: https://doc.qt.io/qt-5/qclipboard.html  
2. 保存加载文件示例: https://doc.qt.io/qt-5/qtwidgets-tutorials-addressbook-part6-example.html  
3. 进度条: https://doc.qt.io/qt-5/qprogressbar.html  
4. 计算crc32，有点问题: https://www.programmersought.com/article/16751068617/  
5. 计算crc32，没什么问题，可以和上面的结合一下: https://github.com/nusov/qt-crc32  
6. 计算md5,sha1等hash: https://www.programmersought.com/article/90355271148/  
7. QtConcurrent和QThread比较: https://stackoverflow.com/questions/30680358/multithreading-performance-of-qtconcurrent-vs-qthread-with-many-threads  
8. 设置应用图标: https://doc.qt.io/qt-5/appicon.html linux的图标一般在/usr/share/icons/文件夹下，需要自己设置  
9. 这里写了构建单个exe应用，但是在执行qmake的时候失败了: https://wiki.qt.io/Build_Standalone_Qt_Application_for_Windows  
10. qt使用windeployqt和Enigma Virtual Box构建单个exe: https://www.cnblogs.com/mcumagic/p/5252777.html  
11. 拖拽文件: https://blog.csdn.net/Mr_robot_strange/article/details/112258570  
12. linux下用这个应该可以打包单个程序: https://appimage.org/  
13. linuxdeployqt，可用来生成AppImage: https://github.com/probonopd/linuxdeployqt  
14. linuxdeploy，可用来生成AppImage，据作者说比linuxdeployqt好一些: https://github.com/linuxdeploy/linuxdeploy  
15. qtinstaller: https://doc.qt.io/qtinstallerframework/  
16. qtinstaller各种变量: https://doc.qt.io/qtinstallerframework/scripting.html#predefined-variables  


2021/8/8  
