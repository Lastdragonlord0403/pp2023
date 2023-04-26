from domains.credit import Credit
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"""
                Course ID: {self.id} 
                Course name: {self.name}"""
