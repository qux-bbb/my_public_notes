# PyQt5---使用qt-designer创建界面

## 安装模块
```r
pip install pyqt5-tools
```

## 拖放生成ui
启动qt designer：  
```r
qt5-tools designer
```

一般选择"Main Window"模板慢慢改。  
多个元素组合，合理使用"水平布局"和"垂直布局"，通过"Horizontal Spacer"和"Vertical Spacer"可以快速调整出整齐的界面。  
一些元素自带布局属性，如"Group Box"、"Scroll Area"，这时不需要额外的布局组件。  
objectName命名有2种风格，比如: `pushButton_hello` 或者 `hello_pushButton`, 选一种风格保持统一即可。  
窗体 -> 预览, 可以查看效果。  
最后保存为.ui文件  

结果文件示例：  
[simple_file_edit.ui](./files/simple_file_edit.ui)  


## 使用ui方式

### 方法1：直接使用ui文件
[simple_file_edit.py](./files/simple_file_edit.py)  

优点：  
1. 直接
2. 更新界面时方便

缺点：  
1. 速度稍慢，一般不影响
2. 开发时代码补全效果很差(可以显式声明类型，使用pycharm开发)

### 方法2：将ui转成python
```r
# -x 可以生成额外代码，执行运行可以查看界面
pyuic5 -x -o ui_mainwindow.py simple_file_edit.ui
```
[ui_mainwindow.py](./files/ui_mainwindow.py)  
[simple_file_edit_use_py_ui.py](./files/simple_file_edit_use_py_ui.py)  

优点：  
1. 加载速度较快
2. 开发时代码补全效果很好

缺点：  
1. 更新界面时不太方便


## 参考来源
1. https://stackoverflow.com/questions/42090739/pyqt5-how-to-install-run-qt-designer
2. chatgpt  


---
2023/5/20  
