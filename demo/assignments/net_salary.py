# Take grade and salary and display net salary

grade = input("Enter grade [a/b] : ")
salary = int(input("Enter salary : "))

if grade == 'a':
    hra = salary * 30 // 100
    da = salary * 20 // 100
else:
    hra = salary * 25 // 100
    da = salary * 15 // 100

netsalary = salary + hra + da

print(netsalary)
