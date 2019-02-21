# python convention is to use Capital letters for classes and lower case for function and variables.

students = []


class Student:
    def __init__(self, name, student_id = 332):
        student = {"name": name, "student_id": student_id}
        students.append(student)
    def __str__(self): # This is an overwrite function
        return "Student"


mark = Student("Mark")
print(students)