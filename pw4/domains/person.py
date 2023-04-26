class Person:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob

    def __str__(self):
        return f"{self.name} {self.id} {self.dob}"
