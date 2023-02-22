# initialize empty dictionaries to store information
students = {}
courses = {}
marks = {}
# input functions
def input_num_students():
    num_students = int(input("Enter the number of students in the class: "))
    return num_students

def input_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth (dd/mm/yyyy): ")
    students[student_id] = {"name": student_name, "dob": student_dob}

def input_num_courses():
    num_courses = int(input("Enter the number of courses: "))
    return num_courses

def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    courses[course_id] = {"name": course_name, "marks": {}}

def input_student_marks():
    course_id = input("Enter course ID: ")
    for student_id in students:
        marks = float(input(f"Enter marks for student {students[student_id]['name']} (ID: {student_id}): "))
        courses[course_id]["marks"][student_id] = marks

# listing functions
def list_courses():
    print("List of courses:")
    for course_id in courses:
        print(f"{course_id}: {courses[course_id]['name']}")

def list_students():
    print("List of students:")
    for student_id in students:
        print(f"{student_id}: {students[student_id]['name']}")

def show_student_marks():
    course_id = input("Enter course ID: ")
    print("Marks for students in course", courses[course_id]["name"])
    for student_id in students:
        if student_id in courses[course_id]["marks"]:
            print(f"{students[student_id]['name']} (ID: {student_id}): {courses[course_id]['marks'][student_id]}")

# main program
num_students = input_num_students()
for i in range(num_students):
    input_student_info()

num_courses = input_num_courses()
for i in range(num_courses):
    input_course_info()

while True:
    print("Select an option:")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a course")
    print("5. Exit")
    option = int(input())
    if option == 1:
        input_student_marks()
    elif option == 2:
        list_courses()
    elif option == 3:
        list_students()
    elif option == 4:
        show_student_marks()
    elif option == 5:
        break
    else:
        print("Invalid option. Please try again.")
