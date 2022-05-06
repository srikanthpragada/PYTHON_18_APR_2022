def has_digit(s):
    for c in s:
        if c.isdigit():
            return True

    return False


items = ['Abc', 'A123', 'Uef', 'A5']

for s in filter(has_digit, items):
    print(s)

