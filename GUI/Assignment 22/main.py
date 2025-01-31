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
        # Clear existing widgets to prevent duplication
        while self.ui.GL_tasks.count():
            item = self.ui.GL_tasks.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        tasks = self.db.get_tasks()

        for i, task in enumerate(tasks):
            new_checkbox = QCheckBox()
            new_push = QPushButton(task[1])  # Title as button text
            new_checkbox_priority = QCheckBox()
            new_push_delete = QPushButton("❌")

            if task[5]:  # Priority is set
                new_checkbox_priority.setChecked(True)
                new_push.setStyleSheet("color: red; background-color: white;")
            else:
                new_push.setStyleSheet("color: white; background-color: #007bff;")
                
            
            if task[6]:  # Task is done
                new_checkbox.setChecked(True)
                new_push.setStyleSheet("text-decoration: line-through; color: black; background-color: white;")

            # Add widgets to layout
            self.ui.GL_tasks.addWidget(new_checkbox, i + 1, 0)
            self.ui.GL_tasks.addWidget(new_push, i + 1, 1)
            self.ui.GL_tasks.addWidget(new_checkbox_priority, i + 1, 2)
            self.ui.GL_tasks.addWidget(new_push_delete, i + 1, 3)

            # Connect actions with UI refresh
            new_checkbox.clicked.connect(lambda _, id=task[0]: [self.toggle_task_done(id), self.read_database()])
            new_push_delete.clicked.connect(lambda _, row=i + 1, id=task[0]: self.delete_task(row, id))
            new_push.clicked.connect(lambda _, id=task[0]: self.show_task_info(id))
            new_checkbox_priority.clicked.connect(lambda _, id=task[0]: [self.toggle_task_pri(id), self.read_database()])
    

    def toggle_task_done(self, task_id):
        task_info = self.db.set_task_data(task_id)
        if task_info:
            current_state = task_info[0]  # Fetch current state
            new_state = 0 if current_state else 1
            self.db.task_done(task_id,new_state)  # Toggle state

    def toggle_task_pri(self, task_id):
        task_info = self.db.set_task_data(task_id)
        if task_info:
            current_state = task_info[1]  # Fetch current state
            new_state = 0 if current_state else 1
            self.db.pri_task(task_id,new_state)  # Toggle state

    def delete_task(self, row, task_id):
        self.db.del_task(task_id)
        self.read_database()

    def show_task_info(self, task_id):
        task_info = self.db.task_data(task_id)
        if task_info:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Task Information")
            msg_box.setText(f"Description: {task_info[0]}\nTime: {task_info[1]}\nDate: {task_info[2]}")
            msg_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
