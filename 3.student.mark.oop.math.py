class Person:
    def __init__(self):
        self.name = str(input("Student name: "))
        self.id = int(input("Student ID: "))
        self.dob = str(input("Student DoB: "))
    def __str__(self):
        return f"{self.name} {self.id} {self.dob}" 

class Students(Person):
    def __init__(self):
        super().__init__()    
    def __str__(self):
        return f"""
                Student ID: {self.id} 
                Student name: {self.name} 
                Student DoB: {self.dob}"""
    
class Course:
    def __init__(self):
        self.__course_id = int(input("Course ID: "))
        self.__course_name = str(input("Course name: "))
    def __str__(self):
        return f"""
                Course ID: {self.__course_id} 
                Course name: {self.__course_name}"""
    
class Mark: 
    def __init__(self):
        self.__mark = float(input(f"""{crs} 
                                mark: """))
    def __str__(self):
        return f"{self.__mark}"

class Credit:
    def __init__(self):
        self.__credit = int(input("Credit: "))
    def __str__(self):
        return f"{self.__credit}"
    
student = []
course = []
mark = []
credit = []

c = int(input("Number of course: "))
for j in range (c):
    crs = Course()
    course.append(Course.__str__(crs))
    cr = Credit()
    credit.append(Credit.__str__(cr))
    print("\t")

s = int(input("Number of student: "))
for i in range (s):
    std = Students()
    student.append(Students.__str__(std))
    print("\t")
    for crs in course:
        m = Mark()
        mark.append(Mark.__str__(m)) 
import math
def round_down(n, decimals=0):
    multiplier = 10** decimals
    return math.floor(n*multiplier)/ multiplier      
import numpy as np
score = np.array([])
score = np.concatenate((score, mark))
student_score = np.array_split(score,s)
total_credit = sum(int(i) for i in credit)
GPA = []
for i in range (s):
    student_gpa = sum(float(i) for i in student_score[i])/total_credit
    # round_down(student_gpa,1)
    GPA.append(round_down(student_gpa,1))
    
n = 0
k = 0
for idx, std in enumerate(student):
    print("--------------------------")
    print(f"{std}")
    for jdx, crs in enumerate(course):
        print(f"""{crs}
                Mark: {mark[n]}""")
        n +=1
    print(f"GPA: {GPA[k]}")
    k+=1
# GPA_reversed = []
# GPA_reversed.append((GPA, student))
# print(np.sort(GPA_reversed))
# # for i in GPA_reversed:
# #     print(f"{GPA_reversed}")
        