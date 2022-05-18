class FundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Available balance is {self.balance} but wanted to withdraw {self.amount}"


class Account:
    # static variables / class variable
    minbal = 10000

    @staticmethod
    def getminbal():
        return Account.minbal

    def __init__(self, acno, ahname, balance=0):
        # object attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    # Methods
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance - Account.minbal:
            self.balance -= amount
        else:
            raise FundsException(self.balance, amount)

    def getBalance(self):
        return self.balance

    def show(self):
        print(f"{self.acno}, {self.ahname}, {self.balance}")

    @property
    def availablebalance(self):
        return self.balance - Account.minbal


print(Account.getminbal())  # call static method
a1 = Account(1, "Scott", 10000)
print(a1.availablebalance)
a2 = Account(2, "Cathy")
a2.deposit(5000)
a2.withdraw(10000)
a2.show()
if a1.getBalance() == 0:
    print("Nil balance")
