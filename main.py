from person import person
# call to static field
a = person.gender

def new_person():
    person1 = person('George', 'Washington', 45)
    person1.tell_your_name()
    person1.tell_your_age()
    person1.birthday()
    person1.tell_your_age()
    gender = person.gender
    print(gender)
    print(person1.g)

def main():
    print('hello')
    new_person()
    print(a)


if __name__ == '__main__':
    main()

