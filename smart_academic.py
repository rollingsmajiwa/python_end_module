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
                    subject_name TEXT NOT NULL, topic_1 TEXT NOT NULL, topic_2 TEXT NOT NULL, topic_3 TEXT NOT NULL, topic_4 TEXT NOT NULL, topic_5 TEXT NOT NULL )""")
            
            
            cursor.execute("""INSERT INTO subjects(subject_name,topic_1, topic_2, topic_3, topic_4, topic_5) VALUES ('Mathematics', 'Numbers', 'Algebra', 'Measurement', 'Geomentry', 'Data Handling and Probability')""")
          
           
            
            
            connection.commit()
            connection.close()
    def create_table3(self):
                connection = self.get_connection()
                cursor = connection.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS marks(subject_id INTEGER, student_id INTEGER, total_marks INTEGER NOT NULL, topic_1_marks INTEGER NOT NULL,topic_2_marks INTEGER NOT NULL, 
                topic_3_marks INTEGER NOT NULL, topic_4_marks INTEGER NOT NULL, topic_5_marks INTEGER NOT NULL,
                term TEXT NOT NULL, year INTEGER NOT NULL)""")
                cursor.execute("""INSERT INTO marks(subject_id, student_id, total_marks, topic_1_marks,topic_2_marks, 
                topic_3_marks, topic_4_marks, topic_5_marks, term, year) VALUES (1, 22, 85, 15, 20, 15, 10, 25, 'TWO', 2026 )""")
                
                
                
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
    def delete_student(self):
            connection = sqlite3.connect("student.db")
            cursor = connection.cursor()
            cursor.execute(f"""DELETE FROM students WHERE name = '{self.name}' """)
    
            connection.commit()
            connection.close()
class StudentMarks:
    def __init__(self, student_id, subject_id, topic_1_marks, topic_2_marks, topic_3_marks, topic_4_marks, topic_5_marks, term = "TWO", year=2027):
            self.student_id = student_id
            self.subject_id = subject_id
            self.total_marks = (topic_1_marks + topic_2_marks + topic_3_marks + topic_4_marks + topic_5_marks)
            self.topic_1_marks = topic_1_marks
            self.topic_2_marks = topic_2_marks
            self.topic_3_marks = topic_3_marks
            self.topic_4_marks = topic_4_marks
            self.topic_5_marks = topic_5_marks
            self.term = term
            self.year = year
    def add_marks(self):
          connection = sqlite3.connect("student.db")
          cursor = connection.cursor()
          
          
          cursor.execute(f"""INSERT INTO marks(subject_id, student_id, total_marks,topic_1_marks, topic_2_marks, topic_3_marks, topic_4_marks, topic_5_marks, term, year)
            VALUES ('{self.subject_id}', '{self.student_id}', '{self.total_marks}', '{self.topic_1_marks}', '{self.topic_2_marks}', '{self.topic_3_marks}', '{self.topic_4_marks}', '{self.topic_5_marks}', '{self.term}', '{self.year}')""")
          
          connection.commit()
          connection.close()
    
    
          
        
            

def main():
      while True:
            print("\n___STUDENT MANAGEMENT___")
            print("1. Register student")
            print("2. View student")
            print("3. Enter Marks")
            print("4. Delete student")
            print("5. Analyze performance")
            print("6. Generate report")
            print("7. Exit")

            choice = input("Select an option:")
            if choice == "1":
                admission_number = input("Enter student admission number:")
                name = input("Enter student name:")
                add_st = StudentInf(admission_number=admission_number, name=name)
                add_st.add_student()
                print("Student added succesfully")
            elif choice == "2":
                viewed_students = StudentInf().view_student()
                if viewed_students:

                    for data in viewed_students:
                        print(data)
                else:
                      print("Student list is empty!")
            
            elif choice == "3":
                student_id = float(input("Enter student id:"))
                subject_id = float(input("Enter subject id:"))
                
                topic_1_marks = float(input("Enter marks scored in topic 1:"))
                topic_2_marks = float(input("Enter marks scored in topic 2:"))
                topic_3_marks = float(input("Enter marks scored in topic 3:"))
                topic_4_marks = float(input("Enter marks scored in topic 4:"))
                topic_5_marks = float(input("Enter marks scored in topic 5:"))
                student_m = StudentMarks(student_id, subject_id, topic_1_marks, topic_2_marks, topic_3_marks, topic_4_marks, topic_5_marks)
                student_m.add_marks()
                print("Marks added succesfully")

            elif choice == "4":
                  name = input("Enter the full name of the student you want to delete:")
                  dlete_n = StudentInf(name=name)
                  dlete_n.delete_student()
                  print(dlete_n)
            elif choice == "7":
                  
                  print("Thank you!")
                  break
                

            else:
                  print("Invalid choice. Try again")

                  
            
            
main()








