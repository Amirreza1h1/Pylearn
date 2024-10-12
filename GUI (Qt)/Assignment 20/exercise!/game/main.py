import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ro.clicked.connect(partial(self.play,1))
        self.ui.posht.clicked.connect(partial(self.play,2))
        self.ui.about.clicked.connect(self.about)

        self.choice={1:"✋on hand",
                     2:"back of hand🤚"}
        
        self.number_user_win=0
        self.number_cpu_1_win=0
        self.number_cpu_2_win=0
        self.round=1

    def ai_play(self):
        ai_choice=self.choice[random.randint(1,2)]
        return ai_choice
    
    def play(self,user_push):
        try:
            user_choice=self.choice[user_push]
            cpu_1_choice=self.ai_play()
            cpu_2_choice=self.ai_play()


            if user_choice == cpu_1_choice == cpu_2_choice:
                result_g = "It's a tie!"
                ms=result_g
            elif (user_choice == "✋on hand" and cpu_1_choice == "back of hand🤚" and cpu_2_choice == "back of hand🤚") or \
                 (user_choice == "back of hand🤚" and cpu_1_choice == "✋on hand" and cpu_2_choice == "✋on hand"):
                result_g = f"{cpu_2_choice}    /    {user_choice}    /    {cpu_1_choice}"
                ms="You win this round!"
                self.number_user_win+=1
            elif (user_choice == "✋on hand" and cpu_1_choice == "back of hand🤚" and cpu_2_choice == "✋on hand") or \
                 (user_choice == "back of hand🤚" and cpu_1_choice == "✋on hand" and cpu_2_choice == "back of hand🤚"):
                result_g = f"{cpu_2_choice}    /    {user_choice}    /    {cpu_1_choice}"
                ms="CPU 1 win this round!"
                self.number_cpu_1_win+=1
            else:
                result_g = f"{cpu_2_choice}    /    {user_choice}    /    {cpu_1_choice}"
                ms="CPU 2 win this round!"
                self.number_cpu_2_win+=1


            self.ui.result.setText(result_g)
            self.ui.user_win.setText(f"Wins : {self.number_user_win}")
            self.ui.cpu1_win.setText(f"Wins : {self.number_cpu_1_win}")
            self.ui.cpu2_win.setText(f"Wins : {self.number_cpu_2_win}")

            msg_box = QMessageBox(text=ms, icon=QMessageBox.Information)
            msg_box.exec()

            self.round+=1
            self.ui.turns_number.setText(f"Round: {self.round}")
            if self.number_cpu_1_win+self.number_cpu_2_win+self.number_user_win==5:
                self.restart()
            

        except ValueError:
            QMessageBox.warning(self, "Invalid Input",
                                "Please enter a valid number.")


    def restart(self):
        if self.number_user_win==3:
            msg_box = QMessageBox(
            text="You have won the game!🎊🎉✌️ \n Game restart!")
            msg_box.exec()
        elif self.number_cpu_1_win==3:
            msg_box = QMessageBox(
            text="CPU 1 has won the game!🎊🎉✌️ \n Game restart!")
            msg_box.exec()
        elif self.number_cpu_2_win==3:
            msg_box = QMessageBox(
            text="CPU 2 has won the game!🎊🎉✌️ \n Game restart!")
            msg_box.exec()
        elif self.number_cpu_1_win==2 and self.number_cpu_2_win==2 and self.number_user_win==1 :
            msg_box = QMessageBox(
            text="You have won the game!🎊🎉✌️ \n Game restart!")
            msg_box.exec()
        elif self.number_cpu_1_win==1 and self.number_cpu_2_win==2 and self.number_user_win==2 :
            msg_box = QMessageBox(
            text="CPU 1 won the game!🎊🎉✌️ \n Game restart!")
            msg_box.exec()
        elif self.number_cpu_1_win==2 and self.number_cpu_2_win==1 and self.number_user_win==2 :
            msg_box = QMessageBox(
            text="CPU 2 won the game!🎊🎉✌️ \n Game restart!")
            msg_box.exec()

        
        self.ui.user_win.clear()
        self.ui.cpu1_win.clear()
        self.ui.cpu2_win.clear()
        self.ui.turns_number.setText("Round: 1")
        self.number_user_win=0
        self.number_cpu_1_win=0
        self.number_cpu_2_win=0
        self.round=1
        

    def about(self):
        msg_box = QMessageBox(
            text="The game has 5 rounds without the tie rounds. who gets 3 wins, win the game. \n the winner of each round is the one who has diiferent choice. \n if two players get 2 win and the other one get one who get one win the game. \n enjoy the game. 🎉🎊✌️")
        msg_box.exec()


my_app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
my_app.exec()
