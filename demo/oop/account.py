class Account:
    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance
        self.minbal = 10000 

    # Methods
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError('Insufficient Balance')

    def getBalance(self):
        return self.balance

    def show(self):
        print(f"{self.acno}, {self.ahname}, {self.balance}")


a1 = Account(1, "Scott", 10000)
a2 = Account(2, "Cathy")
a2.deposit(5000)
a2.withdraw(10000)
a2.show()
if a1.getBalance() == 0:
    print("Nil balance")
