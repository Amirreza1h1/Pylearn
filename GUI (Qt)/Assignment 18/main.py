import random
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox, QRadioButton
from PySide6.QtUiTools import QUiLoader

player_current="X"
player_turn="O"
game_mode=1

def about():
    msg_box = QMessageBox(
        text="At first choose the opponent!(default vs cpu)\n who makes the first line of his symbol in a vertical, horizontal or diagonal.\n win the game")
    msg_box.exec()


def new_game():
    global player_current,player_turn
    player_current="X"
    player_turn="O"
    for i in range(3):
        for j in range(3):
            cells[i][j].setText("")


def restart():
    global player_current,player_turn
    # print("Restarting game...")
    msg_box = QMessageBox(
        text="every thing get back to default when the app was starting! \n")
    msg_box.exec()
    player_current="X"
    player_turn="O"
    for i in range(3):
        for j in range(3):
            cells[i][j].setText("")
    my_window.vs_player.setChecked(True)




def play(row, col):
    global player_current,player_turn
    button = cells[row][col]
    my_window.turn_status.setText(f"it's {player_turn} turn \n")

    if button.text() == "":
        button.setText(player_current)
        check_win_condition()

        # Switch player turn
        player_current = "O" if player_current == "X" else "X"
        player_turn="X" if player_turn == "O" else "O"
    else:
        # print("Cell already occupied")
        msg_box = QMessageBox(
        text="Cell already occupied! \n")
        msg_box.exec()


def ai_play():
   
    empty_cells = [(i, j) for i in range(3) for j in range(3) if cells[i][j].text() == ""]
    if empty_cells:
        chosen_cell = random.choice(empty_cells)
        cells[chosen_cell[0]][chosen_cell[1]].setText("O")

def check_win_condition():
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

my_window.about.clicked.connect(lambda: about())
my_window.new_game.clicked.connect(new_game)
my_window.restart.clicked.connect(restart)

# mode = my_window.findChild(QRadioButton, "vs_player")

# .player-X-turn #turnIndicator {
#     background-color: #1E90FF; /* Light Blue Background when X's turn */
# }

# .player-O-turn #turnIndicator {
#     background-color: #FFA500; /* Orange Background when O's turn */
# }
my_window.vs_player.setChecked(True)

my_window.show()


my_app.exec()
