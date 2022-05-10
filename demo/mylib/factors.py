import sys

if len(sys.argv) < 2:
    print("Number is missing!")
    exit(1)

for s in sys.argv[1:]:
    if not s.isdigit():
        continue

    num = int(s)
    print(f"{num:6} : ", end='')
    prime = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            print(i, end=' ')
            prime = False

    if prime:
        print('Prime Number')
    else:
        print()
