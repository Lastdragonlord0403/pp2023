from domains.course import Course
class Mark: 
    def __init__(self, course, mark):
        self.course = course
        self.mark = mark

    def __str__(self):
        return f"{self.course} mark: {self.mark}"
