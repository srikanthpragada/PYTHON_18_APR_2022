nums = [10, 25, 40, 44, -55, 33, -21]

for n in map(abs, nums):
    print(n)


def toggle(c):
    if c.isupper():
        return c.lower()
    else:
        return c.upper()


for c in map(toggle, 'Hello'):
    print(c)

st = "93,33,44,88,55"
nums = st.split(",")
print( sum(map(int, nums)))

