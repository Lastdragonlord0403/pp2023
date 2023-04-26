from domains.person import Person

class Student(Person):
    def __init__(self, name, id, dob):
        super().__init__(name, id, dob)

    def __str__(self):
        return f"""
                Student ID: {self.id} 
                Student name: {self.name} 
                Student DoB: {self.dob}"""
