import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.measurement_types = {
            "Mass": ["kg", "g", "ton", "pounds"],
            "Length": ["inch", "km", "m", "cm", "mm"],
            "Temperature": ["°C", "K", "°F"],
            "Digital volume": ["bit", "byte", "kilo byte", "mega byte", "Giga byte", "Tera byte"]
        }
        
        # Set up connections
        self.ui.Type_box.currentTextChanged.connect(self.update_boxes)
        self.ui.From_box.currentTextChanged.connect(self.update_to_box)
        self.ui.To_box.currentTextChanged.connect(self.update_to_box)
        self.ui.pushButton_3.clicked.connect(self.convert_units)

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
            self.ui.From_box.setCurrentIndex(
                self.ui.From_box.findText(self.ui.From_box.currentText()))
            self.ui.To_box.setCurrentIndex(
                self.ui.To_box.findText(self.ui.To_box.currentText()))
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
                # mass
                if from_unit == "kg":
                    if to_unit == "g":
                        result = input_value * 1000
                    elif to_unit == "ton":
                        result = input_value / 2240
                    elif to_unit == "pounds":
                        result = input_value * 2.20462
                elif from_unit == "g":
                    if to_unit == "kg":
                        result = input_value / 1000
                    elif to_unit == "ton":
                        result = input_value / 907184640
                    elif to_unit == "pounds":
                        result = input_value * 45359237
                elif from_unit == "ton":
                    if to_unit == "kg":
                        result = input_value * 907184640  
                    elif to_unit == "g":
                        result = input_value * 90718464000  
                    elif to_unit == "pounds":
                        result = input_value * 2000  
                elif from_unit == "pounds":
                    if to_unit == "kg":
                        result = input_value * 45359237 / 1000  
                    elif to_unit == "ton":
                        result = input_value / 2000  
                    elif to_unit == "g":
                        result = input_value * 45359237

                # length
                elif from_unit == "inch":
                    if to_unit == "km":
                        result = input_value / 39370.0787401575
                    elif to_unit == "m":
                        result = input_value / 39.3700787401575
                    elif to_unit == "cm":
                        result = input_value * 2.54
                    elif to_unit == "mm":
                        result = input_value * 25.4
                elif from_unit == "km":
                    if to_unit == "inch":
                        result = input_value * 39370.0787401575
                    elif to_unit == "m":
                        result = input_value * 1000
                    elif to_unit == "cm":
                        result = input_value * 100000
                    elif to_unit == "mm":
                        result = input_value * 1000000
                elif from_unit == "m":
                    if to_unit == "inch":
                        result = input_value * 39.3700787401575
                    elif to_unit == "km":
                        result = input_value / 1000
                    elif to_unit == "cm":
                        result = input_value * 100
                    elif to_unit == "mm":
                        result = input_value * 1000
                elif from_unit == "cm":
                    if to_unit == "inch":
                        result = input_value / 2.54
                    elif to_unit == "km":
                        result = input_value / 100000
                    elif to_unit == "m":
                        result = input_value / 100
                    elif to_unit == "mm":
                        result = input_value * 10
                elif from_unit == "mm":
                    if to_unit == "inch":
                        result = input_value / 25.4
                    elif to_unit == "km":
                        result = input_value / 1000000
                    elif to_unit == "m":
                        result = input_value / 1000
                    elif to_unit == "cm":
                        result = input_value / 10

                # temperature
                elif from_unit == "°C":
                    if to_unit == "K":
                        result = input_value + 273.15
                    elif to_unit == "°F":
                        result = (input_value * 9/5) + 32
                elif from_unit == "K":
                    if to_unit == "°C":
                        result = input_value - 273.15
                    elif to_unit == "°F":
                        result = (input_value - 273.15) * 9/5 + 32
                elif from_unit == "°F":
                    if to_unit == "°C":
                        result = (input_value - 32) * 5/9
                    elif to_unit == "K":
                        result = (input_value - 32) * 5/9 + 273.15
                    
                # Digital volume conversions
                elif from_unit == "bit":
                    if to_unit == "byte":
                        result = input_value / 8
                    elif to_unit == "kilo byte":
                        result = input_value / 8192
                    elif to_unit == "mega byte":
                        result = input_value / 819200
                    elif to_unit == "Giga byte":
                        result = input_value / 838860800
                    elif to_unit == "Tera byte":
                        result = input_value / 8589934592
                elif from_unit == "byte":
                    if to_unit == "bit":
                        result = input_value * 8
                    elif to_unit == "kilo byte":
                        result = input_value * 1024
                    elif to_unit == "mega byte":
                        result = input_value * 1048576
                    elif to_unit == "Giga byte":
                        result = input_value * 1073741824
                    elif to_unit == "Tera byte":
                        result = input_value * 1099511627776
                elif from_unit == "kilo byte":
                    if to_unit == "byte":
                        result = input_value * 1024
                    elif to_unit == "mega byte":
                        result = input_value * 1024
                    elif to_unit == "Giga byte":
                        result = input_value * 1024
                    elif to_unit == "Tera byte":
                        result = input_value * 1024
                    elif to_unit == "bit":
                        result = input_value * 8192
                elif from_unit == "mega byte":
                    if to_unit == "byte":
                        result = input_value * 1048576
                    elif to_unit == "kilo byte":
                        result = input_value / 1024
                    elif to_unit == "Giga byte":
                        result = input_value * 1024
                    elif to_unit == "Tera byte":
                        result = input_value * 1024
                    elif to_unit == "bit":
                        result = input_value * 8388608
                elif from_unit == "Giga byte":
                    if to_unit == "byte":
                        result = input_value * 1073741824
                    elif to_unit == "kilo byte":
                        result = input_value / 1024
                    elif to_unit == "mega byte":
                        result = input_value / 1024
                    elif to_unit == "Tera byte":
                        result = input_value * 1024
                    elif to_unit == "bit":
                        result = input_value * 8589934592
                elif from_unit == "Tera byte":
                    if to_unit == "byte":
                        result = input_value * 1099511627776
                    elif to_unit == "kilo byte":
                        result = input_value / 1024
                    elif to_unit == "mega byte":
                        result = input_value / 1024
                    elif to_unit == "Giga byte":
                        result = input_value / 1024
                    elif to_unit == "bit":
                        result = input_value * 85899345920

            self.ui.To_output.setText(
                f"{input_value} {from_unit} = {result:.4f} {to_unit}")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input",
                                "Please enter a valid number.")

    def reset_converter(self):
        self.ui.From_input.clear()
        self.ui.To_output.clear()
        self.update_boxes(self.ui.Type_box.currentText())


my_app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
my_app.exec()
