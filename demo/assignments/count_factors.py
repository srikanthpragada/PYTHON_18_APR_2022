# Take a number and display its factors
num = int(input("Enter number :"))
count = 0
for i in range(2, num // 2 + 1):
    if num % i == 0:
        count = count + 1

print(count)
