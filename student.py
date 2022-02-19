from person import person


class student(person):
    def __init__(self, id_number, semester, name, lastname, age):
        super().__init__(name, lastname, age)
        self.id_number = id_number
        self.semester = semester

    def present_id(self):
        print("my id number is {}".format(self.id_number))

    def my_name_is(self):
        print("hi, I am a student, my name is {}".format(self.name))