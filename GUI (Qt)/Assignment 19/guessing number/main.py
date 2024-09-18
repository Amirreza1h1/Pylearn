import sys
import random
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.computer_number=random.randint(0,100)

        self.ui.about.clicked.connect(self.about)
        self.ui.restart.clicked.connect(self.restart)
        self.ui.guess.clicked.connect(self.play)


    def about(self):
        msg_box = QMessageBox(
            text="A random number between 0 and 100 is selected by cpu and you have to guess the number. \n if your guess is correct, you win.")
        msg_box.exec()

    def play(self):
        ...

    def restart(self):
        msg_box = QMessageBox(
            text="the number which is chosen by the cpu will change and the number of your guessing set to zero!")
        msg_box.exec()
        self.computer_number=random.randint(0,100)
        self.ui.counter.clear()






my_app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
my_app.exec()