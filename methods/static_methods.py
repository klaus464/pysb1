class Food:
    Restraunt = "CMR Canteen"
    def __init__(self, starter, main_course, desert):
        self.starter = starter
        self.main_course = main_course
        self.desert = desert

    @staticmethod
    def info(x):
        print("we are in {}".format(x))

Food.info("CMRCET")