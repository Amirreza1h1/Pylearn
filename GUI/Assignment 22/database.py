import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("todo_list.db")
        self.cursor = self.connection.cursor()
        self.create_tasks_table()

    def get_tasks(self):
        query = "SELECT * FROM tasks"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks

    def add_new_task(self, new_title, new_description, new_time="00:00", new_date="1/1/1400"):
        try:
            # query = f"INSERT INTO tasks(title,description,time,date VALUES('{new_title}','{new_description}','{new_time}','{new_date}')"
            # self.cursor.execute(query)
            query = """INSERT INTO tasks(title, description, time, date)
                       VALUES (?, ?, ?, ?)"""
            self.cursor.execute(query, (new_title, new_description, new_time, new_date))
            self.connection.commit()
            return True
        except:
            return False
        
    def task_done(self,id):
        # self.cursor.execute(f"UPDATE tasks SET is_done = 1 WHERE id = ?", (id,))
        # self.connection.commit()
        self.cursor.execute(f"SELECT * FROM tasks WHERE id ='{id}'")
        task = self.cursor.fetchone()
        if task !=  None:
            self.cursor.execute(f"UPDATE tasks SET is_done ='1' WHERE id ='{id}'")
            self.connection.commit()

    def pri_task(self,id):
        self.cursor.execute(f"UPDATE tasks SET priority='1' WHERE id='{id}'")
        self.connection.commit()

    def del_task(self,id):
        # self.cursor.execute(f"DELETE FROM tasks WHERE id = ?", (id,))
        # self.connection.commit()
        self.cursor.execute(f"DELETE FROM tasks WHERE id = {id}")
        self.connection.commit()
        return True
    
    def task_data(self,id):
        self.cursor.execute(f"SELECT description,time,date FROM tasks WHERE id={id}")
        task=self.cursor.fetchone()
        return task

    def create_tasks_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            time TEXT DEFAULT '00:00',
            date TEXT DEFAULT '1/1/1400',
            is_done INTEGER DEFAULT 0,
            priority INTEGER DEFAULT 0
        )
        """
        self.cursor.execute(query)
