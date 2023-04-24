# PyQt6---下拉切换窗口的输入布局格式

test.py  
```python
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QComboBox,
    QStackedWidget,
    QLabel,
)


class SwitchWindowLayoutDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle("下拉切换窗口的输入布局格式")

        self.layout = QVBoxLayout(self)

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("窗口1")
        self.comboBox.addItem("窗口2")
        self.comboBox.addItem("窗口3")

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.addWidget(self.createWindow("窗口1"))
        self.stackedWidget.addWidget(self.createWindow("窗口2"))
        self.stackedWidget.addWidget(self.createWindow("窗口3"))

        self.layout.addWidget(self.comboBox)
        self.layout.addWidget(self.stackedWidget)

        self.comboBox.currentIndexChanged.connect(self.stackedWidget.setCurrentIndex)

    def createWindow(self, text):
        window = QWidget(self)
        layout = QVBoxLayout(window)
        label = QLabel(text, window)
        layout.addWidget(label)
        return window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = SwitchWindowLayoutDemo()
    demo.show()
    sys.exit(app.exec())
```

结合vbs脚本可以做到无黑框执行：  
RUNME.vbs  
```vbs
Dim oShell
Set oShell = WScript.CreateObject ("WScript.Shell")
oShell.Run ".\venv\Scripts\python.exe test.py", 0, True
Set oShell = Nothing
```

来源: chatgpt  


2023/4/24  
