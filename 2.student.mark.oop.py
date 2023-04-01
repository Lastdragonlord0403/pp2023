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
        return f"Mark: {self.__mark}"

student = []
course = []
mark = []


c = int(input("Number of course: "))
for j in range (c):
    crs = Course()
    course.append(Course.__str__(crs))
    print("\t")

s = int(input("Number of student: "))
for i in range (s):
    std = Students()
    student.append(Students.__str__(std))
    print("\t")
    for crs in course:
        m = Mark()
        mark.append(Mark.__str__(m)) 

n = 0
for idx, std in enumerate(student):
    print("--------------------------")
    print(f"{std}")
    for jdx, crs in enumerate(course):
        print(f"""{crs}
                {mark[n]}""")
        n +=1