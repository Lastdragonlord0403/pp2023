def get_person_input():
    name = str(input("Student name: "))
    id = int(input("Student ID: "))
    dob = str(input("Student DoB: "))
    return name, id, dob

def get_course_input():
    id = int(input("Course ID: "))
    name = str(input("Course name: "))
    return id, name

def get_mark_input(crs):
    mark = float(input(f"{crs} mark: "))
    return mark

def get_credit_input():
    credit = int(input("Credit: "))
    return credit
