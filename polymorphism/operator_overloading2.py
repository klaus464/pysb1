class Student:
    def __init__(self, java, python):
        self.java = java
        self.python = python
    
    def __add__(self, other):
        a = self.java + self.python
        b = other.java + other.python

        return a, b



stu1 = Student(65, 76)
stu2 = Student(87, 57)

print(stu1 + stu2)
