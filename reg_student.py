from main import Student


try:
    student_name = input("Enter Student Name \n")
    student_id = input("Enter Student id \n")
    student_class = input("Enter Student Class \n")


    Student.create(student_name = student_name,student_id = student_id,student_class = student_class)
    print("Student Created Successfully")

except:
    print("Failed To Create Student Use a Different id")