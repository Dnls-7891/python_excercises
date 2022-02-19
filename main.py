from person import person
from student import student
from student_1st_semester import student_1st_semester

# call to static field
from teacher import teacher

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

def new_student():
    student1 = student(3423, 3, "John", "Smith", 21)
    student1.my_name_is()

def new_teacher():
    teacher1 = teacher("finances", "Bob", "Doe", 45)
    teacher1.tell_your_age()
    teacher1.introduce_yourself()

def new_1st_sem_student():
    student_1st_semester1 = student_1st_semester((2, 2, 3, 4), 4567, "Ian", "Locke", 19)
    student_1st_semester1.introduce_yourself()
    student_1st_semester1.tell_grades()

def main():
    # print('hello')
    # new_person()
    # print(a)
    # new_student()
    new_teacher()
    new_1st_sem_student()

if __name__ == '__main__':
    main()

