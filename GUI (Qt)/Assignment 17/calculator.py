import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def sum():
    ...


def minus():
    ...


def multiple():
    ...


def divide():
    ...


def percent():
    ...


def assign():
    ...


def cls():
    ...


def sin():
    ...


def cos():
    ...


def tan():
    ...


def cot():
    ...


def log():
    ...


def sqrt():
    ...


my_app = QApplication([])

loader = QUiLoader()
my_window = loader.load("mainwindow.ui")
my_window.show()


my_app.exec()
