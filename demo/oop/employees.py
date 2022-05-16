from abc import ABC, abstractmethod


# Abstract class
class Employee(ABC):
    def __init__(self, name, desg):
        self.name = name
        self.desg = desg

    def __str__(self):
        return f"{self.name} - {self.desg}"

    @abstractmethod
    def get_salary(self):
        pass


class Salaried(Employee):
    def __init__(self, name, desg, salary):
        super().__init__(name, desg)
        self.salary = salary

    def get_salary(self):
        return self.salary

    def __str__(self):
        return f"{super().__str__()} - {self.salary}"

    def __eq__(self, other):
        return self.name == other.name and \
               self.desg == other.desg and \
               self.salary == other.salary


class Consultant(Employee):
    def __init__(self, name, desg, hours, rate):
        super().__init__(name, desg)
        self.hours = hours
        self.rate = rate

    def get_salary(self):
        return self.rate * self.hours

    def __str__(self):
        return f"{super().__str__()} - {self.hours} - {self.rate}"

    def __eq__(self, other):
        return self.name == other.name and \
               self.desg == other.desg and \
               self.hours == other.hours and \
               self.rate == other.rate


s = Salaried("Mike", "Prog", 500000)
print(s)
print(s.get_salary())

c = Consultant("Scott", "DBA", 10, 2000)
print(c)
print(c.get_salary())
