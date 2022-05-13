class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def totalseconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    def __eq__(self, other):
        return self.totalseconds() == other.totalseconds()

    def __gt__(self, other):
        return self.totalseconds() > other.totalseconds()


t1 = Time(m=5)
t2 = Time(10, 10, 10)
t3 = Time(10, 10, 10)
print(t1)  # str(t1)  -> t1.__str__()
print(t2 == t3)  # t2.__eq__(t3)
print(t2 > t1)   # t2.__gt__(t1)



