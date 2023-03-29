class Student:
    def show(self, a = None, b = None, c = None):
        if a  != None and b != None and c != None:
            print(a, b, c)
        elif a != None and b != None:
            print(a, b)
        elif a != None:
            print(a)
        else:
            print("No values to print")

s = Student()

s.show(1, 2, 3)
s.show(1, 2)
s.show(1)
s.show()