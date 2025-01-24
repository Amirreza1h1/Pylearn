import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from functools import partial
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
            self.ui.new_title.setText("")
            self.ui.new_description.setText("")
        else:
            msg_box = QMessageBox()
            msg_box.setText("there is a problem🤕")
            msg_box.exec()

    def read_database(self):
        tasks = self.db.get_tasks()

        print(tasks)
        for i in range(len(tasks)):
            new_checkbox = QCheckBox()
            new_push = QPushButton()
            new_push.setText(tasks[i][1])
            new_checkbox_priority = QCheckBox()
            new_push_delete = QPushButton()

            if tasks[i][6]==True:
                new_checkbox_priority.setChecked(True)
                new_push.setStyleSheet("color: red; background-color: white;")

            if tasks[i][5]==True:
                new_checkbox.setChecked(True)

            new_push_delete.setText("❌")
            self.ui.GL_tasks.addWidget(new_checkbox, i+1, 0)
            self.ui.GL_tasks.addWidget(new_push, i+1, 1)
            self.ui.GL_tasks.addWidget(new_checkbox_priority, i+1, 2)
            self.ui.GL_tasks.addWidget(new_push_delete, i+1, 3)

            new_checkbox.clicked.connect(partial(self.db.task_done, tasks[i][0]))
            new_push_delete.clicked.connect(partial(self.db.del_task, tasks[i][0]))
            new_push.clicked.connect(partial(self.db.task_data, tasks[i][0]))
            new_checkbox_priority.clicked.connect(partial(self.db.pri_task, tasks[i][0]))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
