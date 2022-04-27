
l = []

while True:
    n = int(input("Enter number [ 0 to stop ] :"))
    if n == 0:
        break

    l.append(n)

for n in sorted(l):
    print(n)