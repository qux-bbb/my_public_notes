# PySide

keywords: pyqt

Python bindings for the Qt cross-platform application and UI framework

PySide 由 Qt 公司（当时是诺基亚）亲自开发

pypi地址: https://pypi.org/project/PySide6/

安装：
```bash
pip install pyside6
```

打开Qt Designer设计页面
```bash
pyside6-designer
```

转换ui为python代码
```bash
pyside6-uic my_window.ui -o ui_my_window.py
```

主程序代码
```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
# 导入生成的 UI 类
from ui_my_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 创建 UI 对象
        self.ui = Ui_MainWindow()
        # 将 UI 设置到当前窗口
        self.ui.setupUi(self)
        
        # 现在可以通过 self.ui 来访问你在 Designer 中创建的部件了
        # 例如，连接信号
        self.ui.pushButton.clicked.connect(self.handle_button_click)
    
    def handle_button_click(self):
        print("按钮在生成的 UI 中被点击了！")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```


来源: DeepSeek


2025/10/13
