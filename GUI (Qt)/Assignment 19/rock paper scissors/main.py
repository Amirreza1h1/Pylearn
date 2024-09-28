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
        self.number_user_win=0
        self.number_cpu_win=0


    def ai_play(self):
        ai_choice=self.choice[random.randint(1,3)]
        return ai_choice


    def play(self,user_push):
        try:
            user_choice=self.choice[user_push]
            cpu_choice=self.ai_play()

            if user_choice == cpu_choice:
                result = "It's a tie!"
            elif (user_choice == "Rock 🪨" and cpu_choice == "Scissors ✂️") or \
                 (user_choice == "Paper 📄" and cpu_choice == "Rock 🪨") or \
                 (user_choice == "Scissors ✂️" and cpu_choice == "Paper 📄"):
                result = "You wins!"
                self.number_user_win+=1
            else:
                result = "CPU wins!"
                self.number_cpu_win+=1


            self.ui.cpu_choice.setText(f"{cpu_choice}")
            self.ui.user_choice.setText(f"{user_choice}")

            msg_box = QMessageBox(text=result, icon=QMessageBox.Information)
            msg_box.exec()

            self.ui.user_win.setText(f"Player's wins : {self.number_user_win}")
            self.ui.cpu_win.setText(f"Cpu's wins : {self.number_cpu_win}")

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
