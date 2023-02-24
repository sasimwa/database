from main import Student

mystudent = Student.select()
for student in mystudent:
    print(student.student_name,student.student_id,student.student_class)