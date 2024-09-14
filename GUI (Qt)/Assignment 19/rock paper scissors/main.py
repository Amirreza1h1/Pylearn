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
        self.about.clicked.connect(self.about)

    def on_rock_click(self):
        pass

    def on_paper_click(self):
        pass

    def on_scissors_click(self):
        pass

    def on_restart_click(self):
        pass

    def about():
        msg_box = QMessageBox(
            text="Rock Paper Scissors \n It's a game that: \n rock wins against scissors. \n scissors wins against paper. \n paper wins against rock. \n Let's play!")
        msg_box.exec()

my_app = QApplication(sys.argv)
my_window = MainWindow()
my_window.show()
my_app.exec()