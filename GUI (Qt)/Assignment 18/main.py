import sys
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def restart():
    ...



loader = QUiLoader()
my_app = QApplication(sys.argv)
my_window = loader.load("main.ui")

my_window.new_game.clicked.connect(restart())
my_window.r_c_11.clicked.connect()
my_window.r_c_11.clicked.connect()
my_window.r_c_11.clicked.connect()
my_window.r_c_11.clicked.connect()
my_window.r_c_11.clicked.connect()
my_window.r_c_11.clicked.connect()
my_window.r_c_11.clicked.connect()
my_window.r_c_11.clicked.connect()
my_window.r_c_11.clicked.connect()
my_window.r_c_11.clicked.connect()




my_window.show()
my_app.exec()