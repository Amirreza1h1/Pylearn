import sys
import time
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.rock.clicked.connect(self.play)
        # self.paper.clicked.connect(self.play)
        # self.scissors.clicked.connect(self.play)
        self.ui.restart.clicked.connect(self.restart)
        self.ui.about.clicked.connect(self.about)

    def restart(self):
        self.player_status.clear()
        self.cpu_status.clear()
        self.result.clear()
        self.player_status.setText("Player WINs")
        self.cpu_status.setText("CPU WINs")

    def about():
        msg_box = QMessageBox(
            text="Rock Paper Scissors \n It's a game that: \n rock wins against scissors. \n scissors wins against paper. \n paper wins against rock. \n Let's play!")
        msg_box.exec()


my_app = QApplication(sys.argv)
my_window = MainWindow()
my_window.show()
my_app.exec()