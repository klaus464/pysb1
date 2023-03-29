class Student:
    def __init__(self, python):
        self.python = python
    
    def __add__(self, other):
        total = self.python + other.python

        return total
    
    def __gt__(self, other):
        return self.python > other.python



stu1 = Student(65)
stu2 = Student(87)

print(stu1 + stu2)
print(stu1 > stu2)
