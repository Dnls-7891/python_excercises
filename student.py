from person import person

class student(person):
    def __init__(self, semester, id_number, name, lastname, age):
        super().__init__(name, lastname, age)
        self.semester = semester
        self.id_number = id_number

    def present_id(self):
        print("my id number is {}".format(self.id_number))

    def my_name_is(self):
        print("hi, I am a student, my name is {}".format(self.name))

    def introduce_yourself(self):
        print("I am a student.")