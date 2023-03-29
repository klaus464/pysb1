class Car:
    def show(self):
        print("I am Car")

class Bike:
    def show(self, x):
        x.show()

C = Car()
B = Bike()
B.show(C)
