# PyQt6简单了解

用PyQt6可以快速写出图形化程序。  

官方文档: https://www.riverbankcomputing.com/static/Docs/PyQt6/  
一个教程: https://zetcode.com/pyqt6/  

安装：  
```r
pip install PyQt6
```

简单示例：  
```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt


def main():
    app = QApplication(sys.argv)

    w = QMainWindow()
    w.resize(300, 200)
    w.move(300, 300)

    w.setWindowTitle("The Title")

    label = QLabel(w)
    label.setText("Hello World")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    w.setCentralWidget(label)
    w.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
```


2023/4/23  
