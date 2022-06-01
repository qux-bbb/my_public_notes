# pyinstaller---python转exe

## 简单信息

pyinstaller官网: http://www.pyinstaller.org/  
在线文档：https://pyinstaller.readthedocs.io/en/stable/  

注意版本问题：  
官网首页写的是：  
PyInstaller works with Python 3.5—3.7  

文档写的是：  
> Finally, this version drops support for Python 2.7, which is end-of-life since January 2020.. The minimum required version is now Python 3.5. The last version supporting Python 2.7 was PyInstaller 3.6.  

安装:  
```r
pip install pyinstaller
```

最简单使用  
拿我的md_pic举例:  
```r
pyinstaller --onefile md_pic.py
```

然后就生成了md_pic.exe, 把所在文件夹加到path, 就能全局调用了  

如果需要管理员权限执行，可使用如下命令：  
```r
pyinstaller --onefile md_pic.py --uac-admin
```


## 简单原理
收集脚本相关的依赖，放到一个文件夹或打包成一个文件  

运行就是设置python环境，import各种东西，运行python代码  
https://pyinstaller.readthedocs.io/en/stable/advanced-topics.html#the-bootstrap-process-in-detail  
https://pyinstaller.readthedocs.io/en/stable/operating-mode.html#how-the-one-folder-program-works  
https://pyinstaller.readthedocs.io/en/stable/operating-mode.html#how-the-one-file-program-works  


## 其他
**LoadLibrary: 参数错误**    
```r
PS D:\tmp\real_tmp\sangfor_scan\pyd_class_test_enc\dist\test> .\test.exe
Error loading Python DLL 'D:\tmp\real_tmp\sangfor_scan\pyd_class_test_enc\dist\test\python37.dll'.
LoadLibrary: 参数错误。
```

和upx有关系，加两个排除项，重新打包  
```r
pyinstaller.exe -D --upx-exclude=python37.dll --upx-exclude=vcruntime140.dll .\test.py
```

或者直接不要upx了  
```r
pyinstaller.exe -D --noupx .\test.py
```


**区分pyinstaller打包运行还是源程序运行**  
```python
import sys
if getattr(sys, 'frozen') and hasattr(sys, '_MEIPASS'):
    print('running in a PyInstaller bundle')
else:
    print('running in a normal Python process')
```


**hidden-import选项**  
隐式导入  
代码通过 `__import__`, `imp.find_module()`, `exec`, `eval` 导入模块，pyinstaller无法感知，这时需要指定 hidden-import 选项，导入相关模块  
https://pyinstaller.readthedocs.io/en/stable/when-things-go-wrong.html?highlight=hidden-import#listing-hidden-imports  


**key选项**  
使用AES256加密代码，key很容易被找到，并不能保证代码的安全性  

相关链接：  
https://pyinstaller.readthedocs.io/en/stable/operating-mode.html?highlight=key#hiding-the-source-code  
https://pyinstaller.readthedocs.io/en/stable/usage.html#encrypting-python-bytecode  


**hook**  
增强import的兼容性，增加依赖数据等。可以在hook脚本里写各种逻辑使import正常  
hook脚本文件名为 `hook-full.import.name.py`，以横杠拆分，举例 `import a.b` 对应的hook文件名为 `hook-a.b.py`  

可以在这个地址找到各种官方的hook：  
https://github.com/pyinstaller/pyinstaller/tree/develop/PyInstaller/hooks  

相关链接：  
https://pyinstaller.readthedocs.io/en/stable/hooks.html#understanding-pyinstaller-hooks  
https://pyinstaller.readthedocs.io/en/stable/hooks.html#how-a-hook-is-loaded  


**runtime-hook选项**  
指定自定义runtime-hook文件，可以改运行环境和模块  

相关资料：  
https://pyinstaller.readthedocs.io/en/stable/when-things-go-wrong.html#changing-runtime-behavior  


2020/1/19  
