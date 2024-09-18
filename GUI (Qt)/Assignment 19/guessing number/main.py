import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



my_app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
my_app.exec()