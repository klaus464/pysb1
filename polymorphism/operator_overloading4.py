class Student:
    def __init__(self, java, python):
        self.java = java
        self.python = python

    def __str__(self):
        return "{} {}".format(self.java ,self. python)
    
    def __repr__(self):
        return "{} {}".format(self.java ,self. python)
    

stu1 = Student(65, 78)
stu2 = Student(87, 98)

print(stu1.__str__())
print(stu2.__repr__())
print(stu1.__repr__())
print(stu2.__str__())