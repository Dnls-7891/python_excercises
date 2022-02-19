from person import person


class teacher(person):
    def __init__(self, specialization, name, lastname, age):
        super().__init__(name, lastname, age)
        self.specialization = specialization

    def tell_specialization(self):
        print(f"my specialization is {self.specialization}")

    def tell_your_age(self):
        print(f"I am a teacher and I am {self.age}")