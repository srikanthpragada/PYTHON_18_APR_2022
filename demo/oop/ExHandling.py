
try:
    num = int(input("Enter number :"))
    print(100 / num)
except ValueError:
    print("Sorry! Invalid number!")
except ZeroDivisionError:
    print("Sorry! Zero is not allowed!")

