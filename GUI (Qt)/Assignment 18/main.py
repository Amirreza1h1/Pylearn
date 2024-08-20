import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox, QRadioButton
from PySide6.QtUiTools import QUiLoader


def about():
    msg_box = QMessageBox(
        text="At first choose the opponent!(default vs cpu)\n who makes the first line of his symbol in a vertical, horizontal or diagonal.\n win the game")
    msg_box.exec()


def restart():
    print("Restarting game...")


def play(row, col):
    ...


loader = QUiLoader()
my_app = QApplication(sys.argv)
my_window = loader.load("main.ui")

cells = [[my_window.r_c_11, my_window.r_c_12, my_window.r_c_13],
         [my_window.r_c_21, my_window.r_c_22, my_window.r_c_23],
         [my_window.r_c_31, my_window.r_c_32, my_window.r_c_33],]

for i in range(3):
    for j in range(3):
        cells[i][j].clicked.connect(partial(play, i, j))

my_window.new_game.clicked.connect(restart())
my_window.about.clicked.connect(lambda: about())

# mode = my_window.findChild(QRadioButton, "vs_player")

# .player-X-turn #turnIndicator {
#     background-color: #1E90FF; /* Light Blue Background when X's turn */
# }

# .player-O-turn #turnIndicator {
#     background-color: #FFA500; /* Orange Background when O's turn */
# }

my_window.show()
my_app.exec()
