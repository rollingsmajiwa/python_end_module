import sqlite3
import tkinter as tk
from tkinter import messagebox
import pandas as pd

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
    def add_student(self, adm, name):
          connection = sqlite3.connect("student.db")
          cursor = connection.cursor()
          cursor.execute(f"""INSERT INTO students(admission_number, name, grade, stream) VALUES ('{adm}', '{name}', '{self.grade}', '{self.stream}')""")
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
    def view_subjects(self):
          connection = sqlite3.connect("student.db")
          cursor = connection.cursor()
          cursor.execute("""SELECT * FROM subjects""")
          all_subjects = cursor.fetchall()

          connection.commit()
          connection.close()
          return all_subjects
                              
                              
                    
                    
                    
          
                    
          
    def delete_student(self, name):
            connection = sqlite3.connect("student.db")
            cursor = connection.cursor()
            cursor.execute(f"""DELETE FROM students WHERE name = '{name}' """)
    
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

           
   
class MarksAnalyzer:

    def __init__(self, subject_id, student_id):
          self.student_id = student_id
          self.subject_id = subject_id
          
    def all_marks(self):
                  connection = sqlite3.connect("student.db")
                  cursor = connection.cursor()
                  cursor.execute(f"""SELECT topic_1_marks, topic_2_marks, topic_3_marks, topic_4_marks,topic_5_marks FROM marks WHERE student_id = '{self.student_id}'""")
                  get_marks = cursor.fetchall()
                
                  connection.commit()
                  connection.close()
                  return get_marks

    def get_names(self):
                      connection = sqlite3.connect("student.db")
                      cursor = connection.cursor()
                      cursor.execute(f"""SELECT topic_1, topic_2, topic_3, topic_4,topic_5 FROM subjects WHERE subject_id = '{self.subject_id}'""")
                      get_name = cursor.fetchone()
                    
                      connection.commit()
                      connection.close()
                      return get_name
    def get_student_names(self):
                          connection = sqlite3.connect("student.db")
                          cursor = connection.cursor()
                          cursor.execute(f"""SELECT name FROM students WHERE student_id = '{self.student_id}'""")
                          get_std_name = cursor.fetchone()
                        
                          connection.commit()
                          connection.close()
                          return get_std_name[0]
        
    
    
    
    
          
        
#TKINTER           

root = tk.Tk()
root.title("SMART ACADEMIC SYSTEM")
root.geometry("450x600")

#FEATURE FUNCTIONS

def open_register_window():
    win = tk.Toplevel(root)
    win.title("Register Student")
    win.geometry("300x200")

    tk.Label(win, text="Admission Number").pack(pady=5)
    adm_entry = tk.Entry(win)
    adm_entry.pack()

    tk.Label(win, text="Student Name").pack(pady=5)
    name_entry = tk.Entry(win)
    name_entry.pack()

    def submit():
        adm = adm_entry.get()
        name = name_entry.get()
        if adm and name:
            StudentInf().add_student(adm, name)
            messagebox.showinfo("Success", "Student registered successfully!")
            win.destroy()
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    tk.Button(win, text="Submit", command=submit).pack(pady=10)

def add_student_marks():
      win = tk.Toplevel(root)
      win.title("Enter Marks")
      win.geometry("300x550")

      tk.Label(win, text="Enter student ID").pack(pady=3)
      student_entry = tk.Entry(win)
      student_entry.pack(pady=3)

      tk.Label(win, text="Enter subject ID").pack(pady=3)
      subject_entry = tk.Entry(win)
      subject_entry.pack(pady=3)
            
            

        
            

      
    
      

      tk.Label(win, text="Enter marks scored in topi 1").pack(pady=3)
      topic1_entry = tk.Entry(win)
      topic1_entry.pack(pady=3)

      tk.Label(win, text="Enter marks scored in topic 2").pack(pady=3)
      topic2_entry = tk.Entry(win)
      topic2_entry.pack(pady=3)

      tk.Label(win, text="Enter marks scored in topic 3").pack(pady=3)
      topic3_entry = tk.Entry(win)
      topic3_entry.pack(pady=3)

      tk.Label(win, text="Enter marks scored in topic 4").pack(pady=3)
      topic4_entry = tk.Entry(win)
      topic4_entry.pack(pady=3)

      tk.Label(win, text="Enter marks scored in topic 5").pack(pady=3)
      topic5_entry = tk.Entry(win)
      topic5_entry.pack(pady=3)

      def confirm_add():
            std_id = student_id = student_entry.get().strip()
            sub_id = subject_id = subject_entry.get().strip()

            t1 = topic1= topic1_entry.get().strip()
            t2 = topic2 = topic2_entry.get().strip()
            t3 = topic3 = topic3_entry.get().strip()
            t4 = topic4 = topic4_entry.get().strip()
            t5 = topic5 = topic5_entry.get().strip()

            if not(std_id and sub_id and t1 and t2 and t3 and t4 and t5):
                  messagebox.showinfo("Error", "Please fill all fields")
                  return

            try:
                  student_id = float(std_id)
                  subject_id = float(sub_id)
                  topic1 = float(t1)
                  topic2 = float(t2)
                  topic3 = float(t3)
                  topic4 = float(t4)
                  topic5 = float(t5)
            except ValueError:
                    messagebox.showinfo("Error", "Please fill all fields")
                    return
                  
            StudentMarks(student_id, subject_id, topic1, topic2, topic3, topic4, topic5).add_marks()
            messagebox.showinfo("Success", "Marks added successfully")
            win.destroy()   

      tk.Button(win, text="Add Student", command=confirm_add).pack(pady=15)
                  


            
            
    
            


    


      


def view_all_students():
    students = StudentInf().view_student()
    if students:
        display_text = "\n".join([f"ID: {s[0]} | Adm: {s[1]} | Name: {s[2]}" for s in students])
        messagebox.showinfo("Registered Students", display_text)
    else:
        messagebox.showinfo("Registered Students", "No students found.")

def view_all_subjects():
    subject = StudentInf().view_subjects()
    if subject:
          display_subject = "\n".join([f"ID: {s[0]} | Learning Area: {s[1]} | sub-strand 1: {s[2]} | sub-strand 2: {s[3]} | sub-strand 3: {s[4]} | sub-strand 4: {s[5]} | sub-strand 5: {s[6]}" for s in subject])
          messagebox.showinfo("Learning Areas", display_subject)
    else:
          messagebox.showinfo("Learning Areas", "No Learning Areas Found" )


def open_delete_window():
    win = tk.Toplevel(root)
    win.title("Delete Student")
    win.geometry("300x150")

    tk.Label(win, text="Enter Student Name to Delete").pack(pady=10)
    name_entry = tk.Entry(win)
    name_entry.pack()

    def confirm_delete():
        name = name_entry.get()
        if name:
            StudentInf().delete_student(name)
            messagebox.showinfo("Success", f"Deleted student: {name}")
            win.destroy()

    tk.Button(win, text="Delete", command=confirm_delete).pack(pady=10)


def analyze():
    try:
        student_id = float(student_entry.get())
        subject_id = float(subject_entry.get())
    except ValueError:
        output_label.config(text="Please enter valid numeric IDs.")
        return

    analyz = MarksAnalyzer(subject_id, student_id)
    every_marks = analyz.all_marks()
    student_report = []
    if every_marks:
        std_name = analyz.get_student_names()
        tpic_names = analyz.get_names()

        results_text = f"Student Name: {std_name}\n"

        for student_data in every_marks:
            analyzed_marks = student_data[:5]

            if tpic_names:
                for i, (tpic_name, mark) in enumerate(zip(tpic_names, analyzed_marks)):
                    if mark >= 20:
                        comment = "Exceeding Expectation"
                    elif mark >= 15:
                        comment = "Meeting Expectation"
                    elif mark >= 10:
                        comment = "Approaching Expectation"
                    else:
                        comment = "Below Expectation"
                    student_report.append(
                          {
                                "Student Name" : std_name if i ==0 else "",
                                "Topic" : tpic_name,
                                "Mark" : mark,
                                "Performance" : comment
                          }
                    )
                    results_text += f"{tpic_name} - {mark} - {comment}\n"
        df = pd.DataFrame(student_report)
        myFile = f"Student_analysis_{student_id}.xlsx"
        df.to_excel(myFile)
        messagebox.showinfo("Success", "Report exported successfully")
        

        output_label.config(text=results_text)
    else:
        output_label.config(text="No data found for this Student/Subject ID.")


#BUTTONS & INPUTS

tk.Label(root, text="STUDENT MANAGEMENT", font=("Arial", 12, "bold")).pack(pady=10)

tk.Button(root, text="Register Student", width=25, command=open_register_window).pack(pady=4)
tk.Button(root, text="View All Students", width=25, command=view_all_students).pack(pady=4)
tk.Button(root, text="Delete Student", width=25, command=open_delete_window).pack(pady=4)
tk.Button(root, text="View All Learning Areas", width=25, command=view_all_subjects).pack(pady=4)
tk.Button(root, text="Add marks", width=25, command=add_student_marks).pack(pady=4)

tk.Label(root, text="PERFORMANCE ANALYSIS", font=("Arial", 10, "bold")).pack(pady=10)

tk.Label(root, text="Enter Student ID").pack()
student_entry = tk.Entry(root)
student_entry.pack(pady=2)

tk.Label(root, text="Enter Subject ID").pack()
subject_entry = tk.Entry(root)
subject_entry.pack(pady=2)

tk.Button(root, text="Analyze Marks", width=25, command=analyze).pack(pady=10)

output_label = tk.Label(root, text="", justify="left")
output_label.pack(pady=10)



root.mainloop()








