from domains.students import Student
from domains.course import Course
from domains.mark import Mark
from domains.credit import Credit
from input import get_person_input, get_course_input, get_mark_input, get_credit_input
from output import print_student_info, print_course_info, print_mark_info, print_gpa

# Get course information from user
num_courses = int(input("Number of courses: "))
courses = []
credits = []
for i in range(num_courses):
    course_id, course_name = get_course_input()
    courses.append(Course(course_id, course_name))
    credits.append(Credit(get_credit_input()))

# Get student information from user
num_students = int(input("Number of students: "))
students = []
for i in range(num_students):
    name, id, dob = get_person_input()
    students.append(Student(name, id, dob))

# Get marks from user and calculate GPA for each student
for student in students:
    student_marks = []
    for course, credit in zip(courses, credits):
        mark = get_mark_input(course)
        student_marks.append(Mark(course, mark, credit))
    gpa = student.calculate_gpa(student_marks)
    print_student_info(student)
    for mark in student_marks:
        print_course_info(mark.course)
        print_mark_info(mark)
    print_gpa(gpa)
