print("Hello World")
answer = 42
name = "PythonDeo"
print(answer)
def add_number(a:int, b:int) ->int:
    return a + b
print(add_number(10,20))

pi = 3.14
int(pi) == 3
print(pi)

name = 'deodat'
print(name.capitalize())

CSV = "Some|Value|CSV"
print(CSV)
print(CSV.split("|"))

name = 'PythonDeo'
machine = "Hal"
print("Nice to meet you {0}. I am {1}".format(name,machine))

# Boolean and None -- Always need to start with a Captital letter
python_course = True
java_course = False
int (python_course)  # Convert into 0 or 1
print(python_course)
aliens_found = None  # useful for place holder and evaluates to False in an IF STATEMENT

# If Statement
number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is not 5")

# Lists
student_name = ["Mark","Katherina","Jessica"]
student_name[0]
print(student_name[1])
student_name.append("Deodat")
print("Deodat" in student_name)
len(student_name)
print(len(student_name))
del student_name[-1]
print(student_name[-1])
student_name[1:] # List Slicing -- This is not changing the list data, just skipping
print(student_name[1:])

# Loops
for name in student_name:
    print("Student name is {0}".format(name))
# Python will automatically detect the length of the list
# Range function will accept 3 arguments
    # First is how many time to increment the list -- First Count
    # Second is the End point of the List
    # Third is the Skip value -- Example if I wanted to count by 2's -- Increments

# Break and Continue
for name in student_name:
    if name == "Katherina":
        print("Found him!" + name)
        break
    else:
        print("Currently testing " + name)

# While Loops
x = 0
while x < 10:
    print("Count is {0}".format(x))
    x += 1

# Exception Handhelding

Student = {
    "name": "Mark",
    "Student_id":15163,
    "feeback": None
}

try:
    lastname = Student["last_name"]
except KeyError as error:
    print(error)
    print("Error finding last_name")
except Exception as error:  # THis catch all exception.
    print("unkown error" + error)

# Other Data Types
# complex
# Use set and frozenset for removing dups and sorting data

# Functions == We will need to use def and name of function
