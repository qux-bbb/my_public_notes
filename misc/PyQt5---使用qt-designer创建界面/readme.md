# PyQt5---使用qt-designer创建界面

安装模块：  
```r
pip install pyqt5-tools
```

启动qt designer：  
```r
qt5-tools designer
```

一般选择"Main Window"模板慢慢改。  
多个元素组合，合理使用"水平布局"和"垂直布局"，通过"Horizontal Spacer"和"Vertical Spacer"可以快速调整出整齐的界面。  
objectName命名有2种风格，比如: `pushButton_hello` 或者 `hello_pushButton`, 选一种风格保持统一即可。  
最后保存为.ui文件  

结果文件示例：  
[simple_file_edit.ui](./files/simple_file_edit.ui)  
[simple_file_edit.py](./files/simple_file_edit.py)  

参考来源：  
1. https://stackoverflow.com/questions/42090739/pyqt5-how-to-install-run-qt-designer
2. chatgpt  


2023/5/20  
