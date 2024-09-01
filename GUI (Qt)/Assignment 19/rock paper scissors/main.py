import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
my_app = QApplication(sys.argv)
my_window = loader.load("main.ui")

my_window.show()
my_app.exec()