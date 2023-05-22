# main.py
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.change_path_pushButton.clicked.connect(self.change_path)  # 绑定点击事件
        self.load_file_pushButton.clicked.connect(self.load_file)
        self.save_file_pushButton.clicked.connect(self.save_file)

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


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
