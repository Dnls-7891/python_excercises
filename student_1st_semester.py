from student import student


class student_1st_semester(student):
    def __init__(self, grades: vars(), id_number, name, lastname, age):
        super().__init__("1st", id_number, name, lastname, age)
        self.grades = grades

    def introduce_yourself(self):
        print(f"hi, my name is {self.name}")
        print("I amd a student of {} semester".format(self.semester))

    def tell_grades(self):
        print(f"my grades are: {self.grades}")