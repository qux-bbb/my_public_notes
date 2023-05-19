# PyQt5简单了解

用PyQt5可以快速写出图形化程序。  

官方文档: https://www.riverbankcomputing.com/static/Docs/PyQt5/  
一个教程: https://zetcode.com/gui/pyqt5/  

安装：  
```r
pip install PyQt5
```

简单示例：  
```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt


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


2023/5/20  
