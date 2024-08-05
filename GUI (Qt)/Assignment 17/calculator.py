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
    pending_operation = '+'
    my_window.input_box.clear()


def minus():
    global current_value, pending_operation
    current_value = float(my_window.input_box.text())
    pending_operation = '-'
    my_window.input_box.clear()


def multiple():
    global current_value, pending_operation
    current_value = float(my_window.input_box.text())
    pending_operation = '*'
    my_window.input_box.clear()


def divide():
    global current_value, pending_operation
    current_value = float(my_window.input_box.text())
    pending_operation = '/'
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
    input_value = float(my_window.input_box.text())
    result = math.sin(math.radians(float(my_window.input_box.text())))
    update_display(result)
    my_window.history_box.setText(my_window.history_box.text() + f"\nsin({input_value})")


def cos():
    input_value = float(my_window.input_box.text())
    result = math.cos(math.radians(float(my_window.input_box.text())))
    update_display(result)
    my_window.history_box.setText(my_window.history_box.text() + f"\ncos({input_value})")



def tan():
    input_value = float(my_window.input_box.text())
    result = math.tan(math.radians(float(my_window.input_box.text())))
    update_display(result)
    my_window.history_box.setText(my_window.history_box.text() + f"\ntan({input_value})")



def cot():
    input_value = float(my_window.input_box.text())
    result = 1 / math.tan(math.radians(float(my_window.input_box.text())))
    update_display(result)
    my_window.history_box.setText(my_window.history_box.text() + f"\ncot({input_value})")



def log():
    input_value = float(my_window.input_box.text())
    result = math.log10(float(my_window.input_box.text()))
    update_display(result)
    my_window.history_box.setText(my_window.history_box.text() + f"\nlog_10({input_value})")



def sqrt():
    input_value = float(my_window.input_box.text())
    result = math.sqrt(float(my_window.input_box.text()))
    update_display(result)
    my_window.history_box.setText(my_window.history_box.text() + f"\nsqrt({input_value})")



def result():
    global current_value, pending_operation
    second_value = float(my_window.input_box.text())
    operation_phrase = f"{current_value} {pending_operation} {second_value}"
    
    if pending_operation == '+':
        current_value += second_value
    elif pending_operation == '-':
        current_value -= second_value
    elif pending_operation == '*':
        current_value *= second_value
    elif pending_operation == '/':
        current_value /= second_value

    my_window.history_box.setText(str(operation_phrase))
    update_display(current_value)
    pending_operation = None

def num(x):
    text = my_window.input_box.text()
    my_window.input_box.setText(text + x)


loader = QUiLoader()
my_app = QApplication([])
my_window = loader.load("mainwindow.ui")

# Connecting buttons to functions
my_window.n0.clicked.connect(lambda: num("0"))
my_window.n1.clicked.connect(lambda: num("1"))
my_window.n2.clicked.connect(lambda: num("2"))
my_window.n3.clicked.connect(lambda: num("3"))
my_window.n4.clicked.connect(lambda: num("4"))
my_window.n5.clicked.connect(lambda: num("5"))
my_window.n6.clicked.connect(lambda: num("6"))
my_window.n7.clicked.connect(lambda: num("7"))
my_window.n8.clicked.connect(lambda: num("8"))
my_window.n9.clicked.connect(lambda: num("9"))
my_window.minus.clicked.connect(minus)
my_window.plus.clicked.connect(sum)
my_window.multiple.clicked.connect(multiple)
my_window.divide.clicked.connect(divide)
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

my_window.show()
my_app.exec()