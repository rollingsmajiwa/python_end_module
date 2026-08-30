import sqlite3

class StudentManager:
    def __init__(self, db_name = "student.db"):
        self.db_name = db_name
    def get_connection(self):
        return sqlite3.connect(self.db_name)
    def create_table(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS students(student_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        admission_number INTEGER NOT NULL, name TEXT NOT NULL, 
        grade INTEGER NOT NULL, stream TEXT NOT NULL )""")
        cursor.execute("""INSERT INTO students(admission_number, name, grade, stream) VALUES (101, 'Rollings Majiwa', 9, 'N')""")
        connection.commit()
        connection.close()

StudentManager().create_table()
print("Done")


