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

        self.rock.clicked.connect(self.play)
        self.paper.clicked.connect(self.play)
        self.scissors.clicked.connect(self.play)
        self.restart.clicked.connect(self.restart)
        self.about.clicked.connect(self.about)

        self.outcomes = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

    def play(self):
        player_choice = self.sender().objectName().lower()  # change it because of gpt
        cpu_choice = random.choice(list(self.outcomes.keys()))

        player_score = 0
        cpu_score = 0

        if player_choice == cpu_choice:
            self.update_ui(player_choice, cpu_choice, "draw")
        elif self.outcomes[player_choice] == cpu_choice:
            player_score += 1
            self.update_ui(player_choice, cpu_choice, "win")
        else:
            cpu_score += 1
            self.update_ui(player_choice, cpu_choice, "lose")

        self.update_scores(player_score, cpu_score)

    def update_ui(self, player_choice, cpu_choice, result):
        self.player_status.setText(f"{self.ui.player_status.text()} {result}")
        self.cpu_status.setText(f"{self.ui.cpu_status.text()} {result}")
        self.result.setText(
            f"Player chose: {player_choice}\nCPU chose: {cpu_choice}")

    def update_scores(self, player_score, cpu_score):
        self.ui.player_status.setText(f"Player Score: {player_score}")
        self.ui.cpu_status.setText(f"CPU Score: {cpu_score}")

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