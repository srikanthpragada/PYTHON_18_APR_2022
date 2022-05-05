def mathop(op, a, b):
    return op(a, b)


def add(n1, n2):
    return n1 + n2


print(mathop(add, 10, 20))
print(mathop(min, 10, 20))
# print(mathop(abs, 10, 20))
