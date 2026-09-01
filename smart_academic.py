import sqlite3

class StudentManager:
    def __init__(self, db_name = "student.db"):
        self.db_name = db_name
    def get_connection(self):
        return sqlite3.connect(self.db_name)
    def create_table1(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS students(student_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        admission_number INTEGER NOT NULL, name TEXT NOT NULL, 
        grade INTEGER, stream TEXT )""")
        connection.commit()
        connection.close()
    def create_table2(self):
            connection = self.get_connection()
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS subjects(subject_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    subject_name TEXT NOT NULL)""")
            cursor.execute("""INSERT INTO subjects(subject_name) VALUES ('Pre_Technical_studies')""")
            connection.commit()
            connection.close()
    def create_table3(self):
                connection = self.get_connection()
                cursor = connection.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS marks(subject_id INTEGER, student_id INTEGER,student_mark INTEGER NOT NULL, 
                term TEXT NOT NULL, year INTEGER NOT NULL)""")
                cursor.execute("""INSERT INTO marks(subject_id, student_id, student_mark, term, year) VALUES (79, 19, 3, 'TWO', 2026 )""")
                
                connection.commit()
                connection.close()
class StudentInf:
    def __init__(self, student_id=None, admission_number="", name = "", grade = "10", stream = "N"):
            self.student_id = student_id
            self.admission_number = admission_number
            self.name = name
            self.grade = grade
            self.stream = stream
    def add_student(self):
          connection = sqlite3.connect("student.db")
          cursor = connection.cursor()
          cursor.execute(f"""INSERT INTO students(admission_number, name, grade, stream) VALUES ('{self.admission_number}', '{self.name}', '{self.grade}', '{self.stream}')""")
          connection.commit()
          connection.close()
    def view_student(self):
          connection = sqlite3.connect("student.db")
          cursor = connection.cursor()
          cursor.execute("""SELECT * FROM students""")
          all_students = cursor.fetchall()

          connection.commit()
          connection.close()
          return all_students
class StudentMarks:
    def __init__(self, student_id, subject_id, student_mark, term = 3, year=2027):
            self.student_id = student_id
            self.subject_id = subject_id
            self.student_mark = student_mark
            self.term = term
            self.year = year
    def add_marks(self):
          connection = sqlite3.connect("student.db")
          cursor = connection.cursor()
          cursor.execute("""INSERT INTO marks(subject_id, student_id, student_mark, term, year)
            VALUES (?, ?, ?, ?, ?)""", (self.subject_id, self.student_id, self.student_mark, self.term, self.year))
          connection.commit()
          connection.close()
          
        
            

def main():
      while True:
            print("\n___STUDENT MANAGEMENT___")
            print("1. Register student")
            print("2. View student")
            print("3. Enter Marks")
            print("4. Analyze performance")
            print("5. Generate report")
            print("6. Exit")

            choice = input("Select an option:")
            if choice == "1":
                admission_number = input("Enter student admission number:")
                name = input("Enter student name:")
                add_st = StudentInf(admission_number=admission_number, name=name)
                add_st.add_student()
                print("Student added succesfully")
            elif choice == "2":
                viewed_students = StudentInf().view_student()

                for data in viewed_students:
                        print(data)
            elif choice == "3":
                student_id = float(input("Enter student id:"))
                subject_id = float(input("Enter subject id:"))
                student_mark = float(input("Enter student mark:"))
                student_m = StudentMarks(student_id, subject_id, student_mark)
                student_m.add_marks()
                print("Marks added succesfully")

            else:
                  print("Invalid choice. Try again")

                  
            
            
main()







