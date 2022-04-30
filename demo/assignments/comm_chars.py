
names = ['Java', 'JavaScript', 'Python', 'C#', 'C++']

chars = set()
for n in names:
    chars = chars | set(n)

print(chars)
