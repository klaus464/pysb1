class Duck:
    def disp(self):
        print("I am Duck")

class Hen:
    def show(self):
        print("I am Hen")
    
    def disp2(self, D):
        D.disp()

H = Hen()
D = Duck()
H.disp2(D)