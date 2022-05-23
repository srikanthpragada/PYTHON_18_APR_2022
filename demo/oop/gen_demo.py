# Generator
def numbers():
    for n in range(1, 6):
        yield n


g = numbers()
print(g)
print(next(g))
print(next(g))