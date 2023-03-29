class College:
    def show(self):
        print("I am CMR College")

class Student(College):
    def show(self):#Overriding the show() function inherited from College
        print("I am Student")

stu1 = Student()

stu1.show()