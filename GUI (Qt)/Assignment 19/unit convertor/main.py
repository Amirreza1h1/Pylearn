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
        self.measurement_types = {
            "Mass": ["kg", "g", "mg"],
            "Length": ["m", "cm", "mm"],
            "Temperature": ["°C", "K", "°F"],
            "Volume": ["L", "ml", "t"]
        }
        # self.From_box.clear()
        # self.To_box.clear()
        # self.update_boxes(self.Type_box.currentText(),measurement_types)
        # Set up connections
        self.ui.Type_box.currentTextChanged.connect(self.update_boxes)
        self.ui.From_box.currentTextChanged.connect(self.update_to_box)
        self.ui.To_box.currentTextChanged.connect(self.update_to_box)
        self.ui.pushButton_3.clicked.connect(self.convert_units)
        # self.ui.pushButton_2.clicked.connect(self.reset_converter)

        # Initialize boxes
        self.update_boxes(self.ui.Type_box.currentText())

    def update_boxes(self, selected_type):
        self.ui.From_box.clear()
        self.ui.To_box.clear()

        if selected_type in self.measurement_types:
            units = self.measurement_types[selected_type]
            self.ui.From_box.addItems(units)
            self.ui.To_box.addItems(units)
        else:
            self.ui.From_box.addItem("")
            self.ui.To_box.addItem("")

    def update_to_box(self):
        if self.ui.From_box.count() > 0 and self.ui.To_box.count() > 0:
            self.ui.To_box.setCurrentIndex(self.ui.To_box.findText(self.ui.From_box.currentText()))
        elif self.ui.From_box.count() == 0 or self.ui.To_box.count() == 0:
            self.ui.To_box.setCurrentIndex(-1)

    def convert_units(self):
        try:
            from_unit = self.ui.From_box.currentText()
            to_unit = self.ui.To_box.currentText()
            input_value = float(self.ui.From_input.text())
            
            if from_unit == to_unit:
                result = input_value
            else:
                # Simple conversion example (you might need to adjust this based on your actual conversion logic)
                if from_unit == "kg":
                    if to_unit == "g":
                        result = input_value * 1000
                    elif to_unit == "mg":
                        result = input_value * 1000000
                elif from_unit == "g":
                    if to_unit == "kg":
                        result = input_value / 1000
                    elif to_unit == "mg":
                        result = input_value * 1000
                elif from_unit == "mg":
                    if to_unit == "kg":
                        result = input_value / 1000000
                    elif to_unit == "g":
                        result = input_value / 1000
            
            self.ui.To_output.setText(f"{input_value} {from_unit} = {result:.4f} {to_unit}")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")

    def reset_converter(self):
        self.ui.From_input.clear()
        self.ui.To_output.clear()
        self.update_boxes(self.ui.Type_box.currentText())
my_app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
my_app.exec()