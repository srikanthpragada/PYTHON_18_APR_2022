class Person:
    # Constructor
    def __init__(self, name, mobile=None):
        # Object attributes
        self.name = name
        self.__mobile = mobile   # private

    # Methods
    def show(self):
        print("Name   : ", self.name)
        print("Mobile : ", self.mobile)

    def set_mobile(self, newmobile):
        self.__mobile = newmobile

    def get_mobile(self):
        return self.__mobile


p1 = Person("Scott", "3939394433")  # __init__
print(p1.get_mobile())
print(p1.__dict__)
print(p1._Person__mobile)







