import math
import numpy as np
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class MarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.current_course = None

    def input_num_students(self):
        num_students = int(input("Enter the number of students in the class: "))
        for i in range(num_students):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (YYYY-MM-DD): ")
            student = Student(id, name, dob)
            self.students.append(student)

    def input_num_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for i in range(num_courses):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(id, name)
            self.courses.append(course)

    def select_course(self):
        print("Select a course:")
        for i, course in enumerate(self.courses):
            print(f"{i+1}. {course.name}")
        choice = int(input())
        self.current_course = self.courses[choice-1]

    def input_marks(self):
        print(f"Input marks for {self.current_course.name}")
        for student in self.students:
            mark = float(input(f"Enter mark for student {student.name}: "))
            student.add_mark(self.current_course.id, mark)

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"{course.id} - {course.name}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"{student.id} - {student.name}")

    def show_marks(self):
        print(f"Enter course ID for marks ({','.join([course.id for course in self.courses])}):")
        course_id = input()
        print(f"Marks for {course_id}:")
        for student in self.students:
            if course_id in student.marks:
                mark = student.marks[course_id]
                print(f"{student.name}: {mark}")
            else:
                print(f"{student.name}: -")
    def calculate_gpa(self, student):
        credits = []
        marks = []
        for course_id, mark in student.marks.items():
            course = next((c for c in self.courses if c.id == course_id), None)
            if course:
                credits.append(3) 
                marks.append(float(mark))
        if credits and marks:
            gpa = np.average(marks, weights=credits)
            return round(gpa, 2)
        else:
            return 0.0

    def list_students_by_gpa(self):
        students_by_gpa = sorted(self.students, key=self.calculate_gpa, reverse=True)
        print("List of students by GPA descending:")
        for student in students_by_gpa:
            print("Student ID:", student.id, "Name:", student.name, "GPA:", self.calculate_gpa(student))
 

system = MarkManagementSystem()
system.input_num_students()
system.input_num_courses()
system.select_course()
system.input_marks()
system.list_courses()
system.list_students()
system.show_marks()