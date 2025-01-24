import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_main import Ui_MainWindow
from database import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database()
        self.read_database()

        self.ui.add_btn.clicked.connect(self.new_task)

    def new_task(self):
        new_title = self.ui.new_title.text()
        new_description = self.ui.new_description.toPlainText()
        new_time = self.ui.new_time.text()
        new_date = self.ui.new_date.text()
        result = self.db.add_new_task(
            new_title, new_description, new_time, new_date)
        if result:
            self.read_database()
        else:
            msg_box = QMessageBox()
            msg_box.setText("there is a problem🤕")
            msg_box.exec()

    def read_database(self):
        tasks = self.db.get_tasks()
        for i in range(len(tasks)):
            new_checkbox = QCheckBox()
            new_push = QPushButton()
            new_checkbox_priority = QCheckBox()
            new_push_delete = QPushButton()
            self.ui.GL_tasks.addWidget(new_checkbox, i+1, 0)
            self.ui.GL_tasks.addWidget(new_push, i+1, 1)
            self.ui.GL_tasks.addWidget(new_checkbox_priority, i+1, 2)
            self.ui.GL_tasks.addWidget(new_push_delete, i+1, 3)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
