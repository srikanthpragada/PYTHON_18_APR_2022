nums = [10, 25, 40, 44, 55, 33, 21]


def iseven(n):
    return n % 2 == 0


for n in filter(iseven, nums):
    print(n)

for c in filter(str.isupper, 'Hello How Are You'):
    print(c)