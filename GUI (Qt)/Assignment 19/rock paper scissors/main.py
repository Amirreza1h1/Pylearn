import sys
import time
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.rock.clicked.connect(self.on_rock_click)
        self.paper.clicked.connect(self.on_paper_click)
        self.scissors.clicked.connect(self.on_scissors_click)
        self.restart.clicked.connect(self.on_restart_click)
        self.about.clicked.connect(self.on_about_click)

    def on_rock_click(self):
        pass

    def on_paper_click(self):
        pass

    def on_scissors_click(self):
        pass

    def on_restart_click(self):
        pass

    def on_about_click(self):
        pass

my_app = QApplication(sys.argv)
my_window = MainWindow()
my_window.show()
my_app.exec()