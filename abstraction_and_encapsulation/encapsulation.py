'''
Implementation of Encapsulation accessing protected members using getters
'''
class College:
    _exambranch= 102 #Protected Variable
    def _StaffRoom(self): #Protected Methhod
        print("You can't enter staff roo without valid reasonn")

    def get_exambranch(self):
        return self._exambranch
    def get_staffroom(self):
        self._StaffRoom()
    

stu1 = College()
print(stu1.get_exambranch())
stu1.get_staffroom()