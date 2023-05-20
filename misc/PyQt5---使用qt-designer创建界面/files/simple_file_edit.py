# coding:utf8

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QMainWindow,
    QLineEdit,
    QPushButton,
    QPlainTextEdit,
    QFileDialog,
    QApplication,
)


class SimpleFileEdit(QMainWindow):
    def __init__(self):
        super(SimpleFileEdit, self).__init__()
        uic.loadUi("simple_file_edit.ui", self)

        self.filepath_lineEdit.findChild(QLineEdit, "filepath_lineEdit")
        self.change_path_pushButton.findChild(QPushButton, "change_path_pushButton")
        self.load_file_pushButton.findChild(QPushButton, "load_file_pushButton")
        self.save_file_pushButton.findChild(QPushButton, "save_file_pushButton")
        self.content_plainTextEdit.findChild(QPlainTextEdit, "content_plainTextEdit")

        self.change_path_pushButton.clicked.connect(self.change_path)  # 绑定点击事件
        self.load_file_pushButton.clicked.connect(self.load_file)
        self.save_file_pushButton.clicked.connect(self.save_file)

        self.show()

    def change_path(self):
        file_dialog = QFileDialog()
        file_dialog.exec()
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            self.filepath_lineEdit.setText(selected_files[0])

    def load_file(self):
        file_path = self.filepath_lineEdit.text()
        the_file = open(file_path, "r", encoding="utf8")
        content = the_file.read()
        the_file.close()
        self.content_plainTextEdit.setPlainText(content)

    def save_file(self):
        content = self.content_plainTextEdit.toPlainText()
        file_dialog = QFileDialog()
        file_dialog.exec()
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            the_file = open(selected_files[0], "w", encoding="utf8")
            the_file.write(content)
            the_file.close()


app = QApplication(sys.argv)
window = SimpleFileEdit()
sys.exit(app.exec())
