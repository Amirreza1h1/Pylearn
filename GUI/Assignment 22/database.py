import sqlite3

class Database:
    def __init__(self):
        self.connection=sqlite3.connect("todo_list.db")
        self.cursor=self.connection.cursor()


    def get_tasks(self):
        query="SELECT * FROM tasks"
        result=self.cursor.execute(query)
        tasks=result.fetchall()
        return tasks
    
    def add_new_task(self, new_title, new_description,new_time="00:00",new_date="1/1/1400"):
        try:
            query=f"INSERT INTO tasks(title,description,time,date VALUES('{new_title}','{new_description}','{new_time}','{new_date}')"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            return False