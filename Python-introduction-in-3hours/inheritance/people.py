class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_first_name(self):
        print("My first name is: " + self.first_name)
    
    def print_last_name(self):
        print("My last name is: " + self.last_name)

    def print_info(self):
        print("I am a student. My full name is: " + self.first_name + " " + self.last_name)

class Teacher(Person):

    def print_info(self):
        print("I am a Teacher. My full name is: " + self.first_name + " " + self.last_name)

    def print_age(self):
        print("My age is: " + str(self.age))

class Student(Person):

    def print_info(self):
        print("I am a Student. My full name is: " + self.first_name + " " + self.last_name)