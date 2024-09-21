import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.rock.clicked.connect(partial(self.play,1))
        self.ui.paper.clicked.connect(partial(self.play,2))
        self.ui.scissors.clicked.connect(partial(self.play,3))
        self.ui.restart.clicked.connect(self.restart)
        self.ui.about.clicked.connect(self.about)

        self.choice={1:"Rock 🪨",
                     2:"Paper 📄",
                     3:"Scissors ✂️"}


    def ai_play(self):
        ai_choice=self.choice(random.randint(1,3))
        return ai_choice


    def play(self,user_push):
        try:
            user_choice=self.choice(user_push)
            cpu_choice=self.ai_play()
            


        except ValueError:
            QMessageBox.warning(self, "Invalid Input",
                                "Please enter a valid number.")


    def restart(self):
        self.ui.user_win.clear()
        self.ui.cpu_win.clear()
        self.ui.cpu_choice.clear()
        self.ui.user_choice.clear()
        msg_box = QMessageBox(
            text="Game restart!")
        msg_box.exec()

    def about(self):
        msg_box = QMessageBox(
            text="Rock Paper Scissors \n It's a game that: \n rock wins against scissors. \n scissors wins against paper. \n paper wins against rock. \n Let's play!")
        msg_box.exec()


my_app = QApplication(sys.argv)
my_window = MainWindow()
my_window.show()
my_app.exec()
