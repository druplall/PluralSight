students = []

def  get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def  print_students_titlecase():
    student_titlecase = get_students_titlecase()
    print(student_titlecase)


def add_student (name,student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


#def var_args (name,**kwargs):
#   print(name)
#  print(kwargs["descriptions"], kwargs["feedback"])

# Read from file
def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read the files")


# Write to the file
def save_file(student):
    try:
        f = open("students.txt","a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save to file")


#add_student(name="Mark", student_id=15)

#var_args("Mark",descriptions="Loves python",feedback=None,pluralsight_subscriber=True)

## Continue to add student until user types "NO" exit and print

#flag = True
#while(flag == True):
#    student_name = input("Enter the student name: ")
#    student_id = input("Enter student ID: ")
#    input_Flag = input("Would you like to Enter another name? Yes or No: ")
#    add_student(student_name,student_id)
#    if input_Flag == "No":
#        break

read_file()
print_students_titlecase()

student_name = input("Enter the student name: ")
student_id = input("Enter student ID: ")
add_student(student_name,student_id)
save_file(student_name)

