# Implementation of abstraction
from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def model(self):#abstract method
        pass
    
    def roof(self):
        print("I am the roof")

class Audi(Car):
    def model(self):
        print("I am Q8")
    
    def roof(self):
        print("I am having Moon Roof")

car1 = Audi()
car1.model()
car1.roof()