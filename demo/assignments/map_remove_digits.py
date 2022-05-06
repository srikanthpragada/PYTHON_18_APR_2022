def remove_digits(s):
    st = ''
    for c in s:
        if not c.isdigit():
            st = st + c

    return st


items = ['Abc', 'A123B', 'Uef', 'A5D']
for s in map(remove_digits, items):
    print(s)
