# 1.student.mark.py

# Input functions
def input_num_students():
    return int(input("Enter the number of students in the class: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth (DD/MM/YYYY): ")
    return (student_id, student_name, student_dob)

def input_num_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return (course_id, course_name)

def input_marks(course, students):
    marks = {}
    for student in students:
        mark = input(f"Enter mark for {student[1]} in {course[1]}: ")
        marks[student[0]] = mark
    return marks

# Listing functions
def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"{course[0]}: {course[1]}")

def list_students(students):
    print("List of students:")
    for student in students:
        print(f"{student[0]} - {student[1]} ({student[2]})")

def show_student_marks(course, students, marks):
    print(f"Marks for course {course[1]}:")
    for student in students:
        mark = marks.get(student[0])
        if mark:
            print(f"{student[1]}: {mark}")
        else:
            print(f"{student[1]}: N/A")

# Main program
students = []
num_students = input_num_students()
for i in range(num_students):
    student_info = input_student_info()
    students.append(student_info)

courses = []
num_courses = input_num_courses()
for i in range(num_courses):
    course_info = input_course_info()
    courses.append(course_info)

while True:
    print("\nOptions:")
    print("1. List courses")
    print("2. List students")
    print("3. Input marks for a course")
    print("4. Show student marks for a course")
    print("5. Exit")
    option = int(input("Enter option: "))

    if option == 1:
        list_courses(courses)
    elif option == 2:
        list_students(students)
    elif option == 3:
        course_id = input("Enter course ID: ")
        course = next((c for c in courses if c[0] == course_id), None)
        if course:
            marks = input_marks(course, students)
            course.append(marks)
        else:
            print("Course not found.")
    elif option == 4:
        course_id = input("Enter course ID: ")
        course = next((c for c in courses if c[0] == course_id), None)
        if course:
            marks = course[2]
            show_student_marks(course, students, marks)
        else:
            print("Course not found.")
    elif option == 5:
        break
    else:
        print("Invalid option.")
