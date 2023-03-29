class Food:
    Restraunt = "CMR Canteen"
    def __init__(self, starter, main_course, desert):
        self.starter = starter
        self.main_course = main_course
        self.desert = desert

    

    def get_starter(self):
        return self.starter
    
    def set_starter(self, x):
        self.starter = x

    def display(self):
        print("Starte:- {}, Maincourse:- {}, Desert:- {}".format(self.starter, self.main_course, self.desert))

meal1 = Food("Manchurian", "Chicken Biryani", "Brownies")
meal2 = Food("Chilli Chicken", "PBM & Nan", "Gulab Jamoon")

print(meal1.get_starter())
meal1.set_starter("Kababs")
print(meal1.get_starter())

meal1.display()
