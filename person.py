class person:
# static field
    gender = 'male'

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.g = person.gender

    def tell_your_name(self):
        print('my name is', self.name, self.lastname)

    def tell_your_age(self):
        print('I am ', self.age, 'years old.')

    def birthday(self):
        age_now = self.age
        self.age += 1
        return age_now
