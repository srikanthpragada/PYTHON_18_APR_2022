class Person:
    # Constructor
    def __init__(self, name, mobile=None):
        self.name = name
        self.mobile = mobile

    # Methods
    def show(self):
        print("Name   : ", self.name)
        print("Mobile : ", self.mobile)

    def set_mobile(self, newmobile):
        self.mobile = newmobile


p1 = Person("Scott", "3939394433")  # __init__
print(p1.__dict__)  # Attributes

p1.set_mobile("393941111")
p1.show()
p2 = Person("Tom")
p2.show()
