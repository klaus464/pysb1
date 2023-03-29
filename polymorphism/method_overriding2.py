class College:
    def show(self):
        print("I am CMR College")

class Student(College):
    pass

stu1 = Student()

stu1.show()