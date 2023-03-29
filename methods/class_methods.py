class Food:
    Restraunt = "CMR Canteen"
    def __init__(self, starter, main_course, desert):
        self.starter = starter
        self.main_course = main_course
        self.desert = desert
    
    @classmethod
    def food_court(cls):
        print(cls.Restraunt)

Food.food_court()
