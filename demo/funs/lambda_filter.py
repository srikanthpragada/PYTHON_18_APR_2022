marks = [90, 88, 45, 65, 34]

# passed
for n in filter(lambda m: m >= 50, marks):
    print(n)

# Failed
for n in filter(lambda m: m < 50, marks):
    print(n)
