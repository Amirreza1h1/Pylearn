import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

# Global variables
current_value = 0
pending_operation = None


def update_display(value):
    my_window.input_box.setText(str(value))


def sum():
    global current_value, pending_operation
    current_value = float(my_window.input_box.text())
    pending_operation = 'sum'
    my_window.input_box.clear()


def minus():
    global current_value, pending_operation
    current_value = float(my_window.input_box.text())
    pending_operation = 'minus'
    my_window.input_box.clear()


def multiple():
    global current_value, pending_operation
    current_value = float(my_window.input_box.text())
    pending_operation = 'multiple'
    my_window.input_box.clear()


def divide():
    global current_value, pending_operation
    current_value = float(my_window.input_box.text())
    pending_operation = 'divide'
    my_window.input_box.clear()


def percent():
    global current_value
    current_value = float(my_window.input_box.text()) / 100
    update_display(current_value)


def assign():
    global current_value
    current_value = float(my_window.input_box.text())
    current_value *= -1
    update_display(current_value)


def cls():
    my_window.input_box.clear()
    my_window.history_box.clear()


def sin():
    result = math.sin(math.radians(float(my_window.input_box.text())))
    update_display(result)


def cos():
    result = math.cos(math.radians(float(my_window.input_box.text())))
    update_display(result)


def tan():
    result = math.tan(math.radians(float(my_window.input_box.text())))
    update_display(result)


def cot():
    result = 1 / math.tan(math.radians(float(my_window.input_box.text())))
    update_display(result)


def log():
    result = math.log10(float(my_window.input_box.text()))
    update_display(result)


def sqrt():
    result = math.sqrt(float(my_window.input_box.text()))
    update_display(result)


def result():
    global current_value, pending_operation
    second_value = float(my_window.input_box.text())
    if pending_operation == 'sum':
        current_value += second_value
    elif pending_operation == 'minus':
        current_value -= second_value
    elif pending_operation == 'multiple':
        current_value *= second_value
    elif pending_operation == 'divide':
        current_value /= second_value
    update_display(current_value)
    pending_operation = None


my_app = QApplication([])

loader = QUiLoader()
my_window = loader.load("mainwindow.ui")
my_window.show()

my_window.minus.clicked.connect(minus)
my_window.plus.clicked.connect(sum)
my_window.multiple.clicked.connect(multiple)
my_window.percent.clicked.connect(percent)
my_window.assign.clicked.connect(assign)
my_window.clear.clicked.connect(cls)
my_window.result.clicked.connect(result)
my_window.sin.clicked.connect(sin)
my_window.cos.clicked.connect(cos)
my_window.tan.clicked.connect(tan)
my_window.cot.clicked.connect(cot)
my_window.log.clicked.connect(log)
my_window.sqrt.clicked.connect(sqrt)

my_app.exec()
