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
        measurement_types = {
            "Mass": ["kg", "g", "mg"],
            "Length": ["m", "cm", "mm"],
            "Temperature": ["°C", "K", "°F"],
            "Volume": ["L", "ml", "t"]
        }
        self.From_box.clear()
        self.To_box.clear()
        self.update_boxes(self.Type_box.currentText(),measurement_types)


    def update_boxes(self,selected_type,measurement_types):
        self.From_box.clear()
        self.To_box.clear()

        if selected_type in measurement_types:
            units = measurement_types[selected_type]
            self.From_box.addItems(units)
            self.To_box.addItems(units)
        else:
            self.From_box.addItem("")
            self.To_box.addItem("")

my_app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
my_app.exec()