import random
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox, QRadioButton
from PySide6.QtUiTools import QUiLoader

player_current="X"
player_turn="O"

def about():
    msg_box = QMessageBox(
        text="At first choose the opponent!(default vs cpu)\n who makes the first line of his symbol in a vertical, horizontal or diagonal.\n win the game")
    msg_box.exec()


def new_game():
    global player_current,player_turn
    player_current="X"
    player_turn="O"
    if my_window.vs_cpu.isChecked():
        player_text="Player_1 = X"+"\n"+"Player_2 = cpu"+"\n"
        my_window.players.setPlainText(player_text)
    elif my_window.vs_player.isChecked():
        player_text="Player_1 = X"+"\n"+"Player_2 = O"+"\n"
        my_window.players.setPlainText(player_text)
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
    my_window.vs_cpu.setChecked(True)
    my_window.draw.clear()
    my_window.draw.setText(str(0))
    my_window.X_status.clear()
    my_window.X_status.setText(str(0))
    my_window.O_status.clear()
    my_window.O_status.setText(str(0))








def play(row, col):
    global player_current, player_turn
    button = cells[row][col]
    
    if button.text() == "":
        button.setText(player_current)
        check_win_condition()

        # Switch player turn if playing against another player
        if my_window.vs_player.isChecked():
            player_current = "O" if player_current == "X" else "X"
            player_turn = "X" if player_turn == "O" else "O"
            my_window.turn_status.setText(f"It's {player_current}'s turn")
        
        # If playing against CPU, make the AI move after player's move
        elif my_window.vs_cpu.isChecked():
            player_current = "O"
            ai_play()
            check_win_condition()  # Check if AI's move wins the game
            player_current = "X"  # Revert back to player for the next turn
            my_window.turn_status.setText("It's your turn")
    else:
        msg_box = QMessageBox(text="Cell already occupied!")
        msg_box.exec()


def ai_play():
   
    empty_cells = [(i, j) for i in range(3) for j in range(3) if cells[i][j].text() == ""]
    if empty_cells:
        chosen_cell = random.choice(empty_cells)
        cells[chosen_cell[0]][chosen_cell[1]].setText("O")

def check_win_condition():
    # Checking rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows
        if cells[i][0].text() == cells[i][1].text() == cells[i][2].text() != "":
            declare_winner(cells[i][0].text())
            return
        
        # Check columns
        if cells[0][i].text() == cells[1][i].text() == cells[2][i].text() != "":
            declare_winner(cells[0][i].text())
            return
    
    # Check diagonals
    if cells[0][0].text() == cells[1][1].text() == cells[2][2].text() != "":
        declare_winner(cells[0][0].text())
        return
    
    if cells[0][2].text() == cells[1][1].text() == cells[2][0].text() != "":
        declare_winner(cells[0][2].text())
        return
    
    # Check for draw
    if all(cells[i][j].text() != "" for i in range(3) for j in range(3)):
        declare_draw()
        return

def declare_winner(winner):
    msg_box = QMessageBox(text=f"Player {winner} wins!")
    msg_box.exec()
    update_status(winner)
    new_game()  # Reset the game after a win

def declare_draw():
    msg_box = QMessageBox(text="It's a draw!")
    msg_box.exec()
    update_status(winner="draw")
    new_game()  # Reset the game after a draw

def update_status(winner):
    if winner=="draw":
        value=int(my_window.draw.text())+1
        my_window.draw.clear()
        my_window.draw.setText(str(value))
        return
    elif winner=="X":
        value=int(my_window.X_status.text())+1
        my_window.X_status.clear()
        my_window.X_status.setText(str(value))
        return
    elif winner=="O":
        value=int(my_window.O_status.text())+1
        my_window.O_status.clear()
        my_window.O_status.setText(str(value))
        return

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

my_window.vs_cpu.setChecked(True)


my_window.show()


my_app.exec()