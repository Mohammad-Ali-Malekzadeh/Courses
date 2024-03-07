class Student:
    def __init__(self, first_name, last_name, math, phisic, chemistry):
        self.first_name = first_name
        self.last_name = last_name
        self.math = math
        self.phisic = phisic
        self.chemistry = chemistry
    
    def gpa(self):
        gpa = str((self.math + self.phisic + self.chemistry) / 3)
        print(f'Dear {self.first_name} {self.last_name}, Your GPA is: {gpa}')
    